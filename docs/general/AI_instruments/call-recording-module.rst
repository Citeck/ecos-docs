.. _call-recording-module:

Модуль записи совещаний (callrecording)
=========================================

.. contents::
    :depth: 3

**Модуль callrecording** захватывает аудио из браузерной вкладки и микрофона через Chrome-расширение, передаёт потоком по WebSocket, транскрибирует через GigaAM и генерирует резюме через LLM. Результат сохраняется как Citeck-активность типа ``meeting-activity`` или ``call-activity``.

Статья описывает архитектуру модуля, REST API, конфигурацию, артефакты и ключевые файлы. Функциональность доступна начиная с версии **1.11.0 (30 апреля 2026)**.

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


REST API
---------

.. list-table::
   :header-rows: 1
   :widths: 10 45 45

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
   * - Загрузка в ECOS
     - ``domain/callrecording/ecos/CallActivityService.kt``
   * - Перехват Telemost-URL
     - ``domain/callrecording/platform/TelemostConnector.kt``
   * - Конфигурационные свойства
     - ``ai/config/CallRecordingProperties.kt``
   * - DTO и статусы
     - ``domain/callrecording/CallRecordingModels.kt``

Все пути относительно ``src/main/java/ru/citeck/ecos/ai/``.
