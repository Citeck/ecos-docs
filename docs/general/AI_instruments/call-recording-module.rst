.. _call-recording-module:

Модуль записи совещаний (callrecording)
=========================================

.. contents::
    :depth: 3

**Модуль callrecording** захватывает аудио из браузерной вкладки и микрофона через Chrome-расширение, передаёт потоком по WebSocket, транскрибирует через GigaAM и генерирует резюме через LLM. Результат сохраняется как Citeck-активность типа ``meeting-activity`` или ``call-activity``.

Статья описывает архитектуру модуля, REST API, конфигурацию, артефакты и ключевые файлы. Функциональность доступна начиная с версии **1.11.0 (30 апреля 2026)**.

Принцип работы
--------------

Расширение решает сквозную задачу: от момента обнаружения активного звонка до появления структурированной записи встречи в CRM/проекте — без ручного участия пользователя в процессе обработки.

Обнаружение звонка
~~~~~~~~~~~~~~~~~~

``content/call-detector.js`` следит за открытыми вкладками Chrome. Как только пользователь переходит на страницу Yandex Telemost, скрипт отправляет событие ``call-detected`` в Service Worker. Пользователю достаточно открыть вкладку встречи — ничего запускать вручную не нужно.

Захват и передача аудио
~~~~~~~~~~~~~~~~~~~~~~~

Service Worker создаёт скрытое окно-рекордер (``recorder/recorder.js``), которое работает параллельно со встречей:

- **Захват голосов участников** — через ``tabCapture.getMediaStreamId`` получает аудиопоток вкладки Telemost (то, что слышит пользователь).
- **Захват микрофона** — через ``getUserMedia({audio: true})`` захватывает локальный микрофон пользователя. ``tabCapture`` сам по себе микрофон не включает, поэтому используется отдельный поток.
- **Микширование** — оба потока объединяются в ``AudioContext`` через ``GainNode``, образуя единый аудиовыход.
- **Кодирование** — ``MediaRecorder`` пишет сжатый поток в формат ``audio/webm;codecs=opus`` чанками по 5 секунд, что позволяет начинать передачу немедленно, не дожидаясь конца встречи.
- **Стриминг** — каждый чанк отправляется по WebSocket с бинарным протоколом: 4 байта sequence number (big-endian) + аудиоданные. При разрыве соединения ``lib/ws-client.js`` автоматически переподключается с экспоненциальной задержкой (до 5 попыток, максимум 30 сек).

Состояние записи зеркалируется в ``chrome.storage.session``, чтобы не потерять контекст при выгрузке MV3 Service Worker после ~30 сек неактивности.

Транскрипция и генерация резюме
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Аудиопоток поступает в бэкенд ``citeck-ai`` через WebSocket-эндпоинт ``/gateway/ai/ws/`` (проксируется через nginx в обход основного gateway, который WebSocket не поддерживает). Бэкенд запускает pipeline:

- **STT** — :ref:`citeck-stt-sidecar` транскрибирует аудио с помощью GigaAM (распознавание речи на русском языке).
- **LLM summary** — на основе транскрипта языковая модель формирует структурированное резюме встречи.

Сессия завершается текстовым WebSocket-сообщением ``{ type: "end" }``. Пока идёт обработка, Service Worker каждые 3 секунды опрашивает ``/session/{id}/status`` (до 15 минут) и записывает результат в ``chrome.storage.local``.

Сохранение в Citeck
~~~~~~~~~~~~~~~~~~~~~~~~~

Результат — транскрипт и резюме — сохраняется как объект ``meeting-activity`` в платформе Citeck и автоматически привязывается к нужной сущности (сделке или проекту). Пользователь выбирает сущность в popup-интерфейсе расширения через combobox с поиском ещё до начала записи.

Уведомление пользователя
~~~~~~~~~~~~~~~~~~~~~~~~~

Когда обработка завершена, Service Worker отправляет Chrome Notification. Popup расширения может быть закрыт к этому моменту — уведомление гарантирует, что пользователь узнает о готовности результата вне зависимости от состояния UI.


Архитектура
------------------------

.. code-block:: text

    Chrome Extension (захват аудио)
        → WebSocket /ws/call-recording
            → CallRecordingWebSocketHandler
                → CallRecordingService
                    → GigaAmSttProvider (транскрибация)
                    → CallSummaryService (LLM-резюме)
                    → CallActivityService (сохранение в Citeck)


Зависимости (внешние сервисы)
------------------------------------------------------

- **citeck-ai** — WebSocket-хэндлер + pipeline: STT → LLM summary → сохранение активности
- **citeck-stt-sidecar** — сервис транскрипции на базе GigaAM
- **nginx** — WebSocket proxy (``/gateway/ai/ws/``) в обход основного gateway, который WS не проксирует


REST API
---------

.. list-table::
   :header-rows: 1
   :widths: 10 45 45
   :class: tight-table 

   * - Метод
     - URL
     - Описание
   * - ``GET``
     - ``/api/call-recording/config``
     - Платформы, типы записей, STT-провайдер (Speech-to-Text — сервис распознавания речи, преобразующий аудио в текст)
   * - ``GET``
     - ``/api/call-recording/records``
     - Поиск записей по типу
   * - ``POST``
     - ``/api/call-recording/session/start``
     - Старт сессии — возвращает ``sessionId`` и ``wsToken``
   * - ``POST``
     - ``/api/call-recording/session/{id}/end``
     - Завершение сессии и пост-обработка
   * - ``GET``
     - ``/api/call-recording/session/{id}/status``
     - Статус сессии
   * - ``WS``
     - ``/ws/call-recording``
     - Потоковая передача аудио (4 байта sequence + аудиоданные)


Конфигурация
--------------------------

Настройки задаются в ``application.yml``:

.. code-block:: yaml

    citeck.ai.call-recording:
      enabled: true
      stt:
        provider: gigaam
        sidecar-url: http://localhost:8090
        language: ru
        enable-diarization: false
      session:
        max-duration-minutes: 180
        chunk-size-seconds: 30
      summary:
        model: ${citeck.ai.base.model}
        temperature: 0.3


Через UI
~~~~~~~~~

В рабочем пространстве администратора в разделе **AI** перейдите в журнал **Запись звонков**:

1. Заполните **Название**.
2. Выберите **Типы данных для привязки**.
3. Укажите **STT-провайдер по умолчанию** для платформы (например, GigaAM для Telemost).
4. Сохраните.

 .. image:: _static/meeting_setting.png
       :width: 650
       :align: center


Citeck-артефакты
-----------------

Модуль добавляет аспект ``recording-aspect`` с атрибутами ``recording`` (аудиофайл), ``transcription``, ``transcriptionDiarized``, ``summary``, ``recordingDuration``, ``recordingStatus``, ``callPlatform``, ``meetingUrl``. Аспект подключается к типам ``meeting-activity`` и ``call-activity`` через artifact-patch.

.. list-table::
   :header-rows: 1
   :widths: 55 45

   * - Путь
     - Назначение
   * - ``eapps/artifacts/model/aspect/recording-aspect.yml``
     - Аспект с атрибутами записи
   * - ``eapps/artifacts/app/artifact-patch/meeting-activity-recording-aspect.yml``
     - Подключение аспекта к ``meeting-activity``
   * - ``eapps/artifacts/app/artifact-patch/call-activity-recording-aspect.yml``
     - Подключение аспекта к ``call-activity``
   * - ``eapps/artifacts/ui/form/meeting-activity-form.json``
     - Форма с полями аудио, резюме, расшифровки
   * - ``eapps/artifacts/ui/action/meeting-activity-bind-record.yml``
     - Действие привязки встречи к сделке или проекту
   * - ``eapps/artifacts/model/type/call-recording-config.yml``
     - Тип конфигурации записи (типы, платформы, STT-провайдер)
   * - ``eapps/artifacts/ui/form/call-recording-config-form.json``
     - Форма администрирования конфигурации
   * - ``eapps/artifacts/ui/journal/call-recording-config-journal.yml``
     - Журнал конфигураций
   * - ``eapps/artifacts/ui/dashboard/meeting-activity-dashboard.json``
     - Дашборд встречи


LLM-промпт
--------------------

``src/main/resources/prompts/call_summary_prompt.xml`` — инструкция для генерации резюме на русском языке. Промпт формирует адаптивный по длине текст с разделами: ключевые темы, решения, задачи, открытые вопросы, участники.


Тесты
--------------

.. list-table::
   :header-rows: 1
   :widths: 100

   * - Файл
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/CallRecordingServiceTest.kt``
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/CallRecordingSessionStoreTest.kt``
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/api/CallRecordingWebSocketHandlerTest.kt``


Ключевые файлы
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Компонент
     - Файл
   * - Оркестрация сессий
     - ``domain/callrecording/CallRecordingService.kt``
   * - WebSocket-обработчик
     - ``domain/callrecording/api/CallRecordingWebSocketHandler.kt``
   * - REST-контроллер
     - ``domain/callrecording/api/CallRecordingController.kt``
   * - STT через GigaAM
     - ``domain/callrecording/stt/GigaAmSttProvider.kt``
   * - LLM-резюме
     - ``domain/callrecording/summary/CallSummaryService.kt``
   * - Загрузка в Citeck
     - ``domain/callrecording/ecos/CallActivityService.kt``
   * - Перехват Telemost-URL
     - ``domain/callrecording/platform/TelemostConnector.kt``
   * - Конфигурационные свойства
     - ``ai/config/CallRecordingProperties.kt``
   * - DTO и статусы
     - ``domain/callrecording/CallRecordingModels.kt``

Все пути относительно ``src/main/java/ru/citeck/ecos/ai/``.
