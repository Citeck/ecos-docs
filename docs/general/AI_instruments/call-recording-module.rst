.. _call-recording-module:

Модуль записи совещаний (callrecording)
=========================================

.. contents::
    :depth: 3

**Модуль callrecording** захватывает аудио из браузерной вкладки и микрофона через Chrome-расширение, передаёт его фрагментами через REST API, транскрибирует через GigaAM и генерирует резюме через LLM. Результат сохраняется как Citeck-активность типа ``meeting-activity`` или ``call-activity``.

Статья описывает архитектуру модуля, REST API, конфигурацию, артефакты и ключевые файлы. Функциональность доступна начиная с версии **1.11.0 (30 апреля 2026)**. Начиная с версии **1.12.0 (3 июня 2026)** аудио передаётся по REST вместо WebSocket — отдельная WebSocket-инфраструктура и аутентификация по ``wsToken`` больше не используются.

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
- **Кодирование** — ``MediaRecorder`` пишет сжатый поток в формат ``audio/webm;codecs=opus`` фрагментами по 30 секунд, что позволяет начинать передачу немедленно, не дожидаясь конца встречи.
- **Передача** — каждый фрагмент аудио отправляется POST-запросом на ``/api/call-recording/session/{id}/chunks`` с телом ``application/octet-stream`` и заголовками ``X-Upload-Token`` (токен сессии) и ``X-Chunk-Sequence`` (порядковый номер фрагмента). При сетевых ошибках и ответах 5xx расширение повторяет отправку с экспоненциально растущей задержкой (от 1 до 30 секунд) в пределах 5 минут; ответ 4xx считается неисправимой ошибкой, и запись останавливается.

Состояние записи зеркалируется в ``chrome.storage.session``, чтобы не потерять контекст при выгрузке MV3 Service Worker после ~30 сек неактивности.

Транскрипция и генерация резюме
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Фрагменты аудио поступают в бэкенд ``citeck-ai`` по REST через стандартный gateway (пути вида ``/gateway/ai/api/call-recording/…``) — отдельный WebSocket-прокси не требуется. Бэкенд запускает pipeline:

- **STT** — :ref:`citeck-stt-sidecar` транскрибирует аудио с помощью GigaAM (распознавание речи на русском языке).
- **LLM summary** — на основе транскрипта языковая модель формирует структурированное резюме встречи.

После выгрузки последнего фрагмента расширение завершает сессию запросом ``POST /session/{id}/end``, что запускает пост-обработку. Если расширение не смогло завершить сессию явно (окно рекордера закрыто, сбой браузера), бэкенд автоматически завершает сессию, не получавшую фрагментов дольше 5 минут. Пока идёт обработка, Service Worker каждые 3 секунды опрашивает ``/session/{id}/status`` (до 15 минут) и записывает результат в ``chrome.storage.local``.

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
        → POST /api/call-recording/session/start
        → POST /api/call-recording/session/{id}/chunks (фрагменты аудио)
        → POST /api/call-recording/session/{id}/end
            → CallRecordingController
                → CallRecordingService
                    → GigaAmSttProvider (транскрибация)
                    → CallSummaryService (LLM-резюме)
                    → CallActivityService (сохранение в Citeck)


Зависимости (внешние сервисы)
------------------------------------------------------

- **citeck-ai** — REST API + pipeline: STT → LLM summary → сохранение активности
- **citeck-stt-sidecar** — сервис транскрипции на базе GigaAM


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
     - Старт сессии — возвращает ``sessionId`` и ``uploadToken``
   * - ``POST``
     - ``/api/call-recording/session/{id}/chunks``
     - Загрузка фрагмента аудио (тело ``application/octet-stream``, заголовки ``X-Upload-Token`` и ``X-Chunk-Sequence``)
   * - ``POST``
     - ``/api/call-recording/session/{id}/end``
     - Завершение сессии и пост-обработка
   * - ``GET``
     - ``/api/call-recording/session/{id}/status``
     - Статус сессии

Загрузка фрагментов аудио
~~~~~~~~~~~~~~~~~~~~~~~~~~

Жизненный цикл сессии записи:

1. ``POST /session/start`` создаёт сессию и возвращает ``sessionId`` и ``uploadToken`` — токен, который выдаётся на одну сессию записи и авторизует загрузку аудио именно в эту сессию.
2. Каждый фрагмент аудио отправляется отдельным запросом ``POST /session/{id}/chunks`` с бинарным телом (``application/octet-stream``) и двумя заголовками: ``X-Upload-Token`` — токен, полученный при старте сессии, и ``X-Chunk-Sequence`` — порядковый номер фрагмента (целое число). Повторная загрузка фрагмента с тем же номером идемпотентна: дубликат подтверждается ответом 200, но не сохраняется второй раз, поэтому клиент может безопасно повторять запрос после потерянного ответа.
3. ``POST /session/{id}/end`` завершает сессию и запускает пост-обработку (транскрипция, резюме, сохранение активности), прогресс которой отслеживается через ``GET /session/{id}/status``.

Коды ответов ``/session/{id}/chunks``: ``400`` — некорректный заголовок ``X-Chunk-Sequence``; ``403`` — неверный ``X-Upload-Token``; ``404`` — сессия не существует или принадлежит другому пользователю; ``409`` — сессия уже не находится в состоянии записи; ``413`` — фрагмент превышает лимит размера (свойство ``citeck.ai.call-recording.session.max-chunk-size-bytes``, по умолчанию 5 МБ).


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


Безопасность и хранение сессий
-------------------------------

- Все эндпоинты ``/api/call-recording/*`` требуют доступности AI-функций: лицензия с признаком ``ai`` и членство в группе ``ai-feature-allowed`` (:ref:`подробнее <ai-security>`).
- Сессию записи можно запустить только от собственного имени; целевая запись (``targetRecordRef``) должна быть доступна пользователю на чтение — иначе запуск отклоняется.
- Завершённые сессии (успешные и ошибочные) хранятся в памяти сервиса 60 минут и затем удаляются. Срок настраивается свойством ``citeck.ai.call-recording.session.terminal-session-retention-minutes``.


Тесты
--------------

.. list-table::
   :header-rows: 1
   :widths: 100

   * - Файл
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/CallRecordingServiceTest.kt``
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/CallRecordingSessionStoreTest.kt``
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/CallSummaryServiceTest.kt``
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/api/CallRecordingControllerTest.kt``
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/platform/CallPlatformRegistryTest.kt``
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/platform/TelemostConnectorTest.kt``
   * - ``src/test/java/ru/citeck/ecos/ai/domain/callrecording/stt/SttProviderRegistryTest.kt``


Ключевые файлы
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Компонент
     - Файл
   * - Оркестрация сессий
     - ``domain/callrecording/CallRecordingService.kt``
   * - Хранилище сессий
     - ``domain/callrecording/CallRecordingSessionStore.kt``
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
     - ``config/CallRecordingProperties.kt``
   * - DTO и статусы
     - ``domain/callrecording/CallRecordingModels.kt``

Все пути относительно ``src/main/java/ru/citeck/ecos/ai/``.
