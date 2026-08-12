Конфигурация AI инструментов
===============================

Раздел описывает AI-инструменты платформы Citeck: настраиваемых агентов на базе LLM, микросервис транскрипции и модуль записи совещаний.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Пользовательские AI-агенты
      :link: user-agents
      :link-type: ref

      Конфигурируемые сущности с системным промптом, набором инструментов и выбранным :ref:`LLM-провайдером <AI_assistant_config>`. Работают в двух режимах: stateless (однократный вызов из :ref:`BPMN-процессов <process_bpmn>`; вызов преднастроенного агента в текущем релизе отключён и будет доступен в следующих релизах — при этом :ref:`AI задача <ai_task>` с промптом в процессах полностью работает) и stateful (многоходовой диалог в :ref:`AI Assistant UI <AI_assistant>`). Администратор создаёт агентов через **Admin > AI Agents**, разработчик подключает собственные инструменты, реализуя интерфейс ``CiteckAiTool``.

   .. grid-item-card:: Архитектура выполнения AI-агентов
      :link: ai-architecture
      :link-type: ref

      Движки выполнения (``TOOL_LOOP`` и ``CONFIG``), маршрутизация запросов, конвейер планирования и исполнения многоартефактных запросов, сводный перечень точек участия человека (HITL), области публикации артефактов с локальными копиями и ограничения выполнения.

   .. grid-item-card:: Микросервис транскрипции аудио и диаризации
      :link: citeck-stt-sidecar
      :link-type: ref

      Работает как sidecar к сервису ``citeck-ai``. Принимает аудиофайл (WebM, WAV), конвертирует его в WAV 16 кГц через ``ffmpeg``, транскрибирует чанками по 25 секунд с помощью модели **GigaAM-v3** и при наличии токена HuggingFace определяет говорящих через **pyannote.audio**. Доступен по порту ``8090``.

   .. grid-item-card:: Модуль записи совещаний
      :link: call-recording-module
      :link-type: ref

      Захватывает аудио из браузерной вкладки и микрофона через :ref:`Chrome-расширение <citeck_browser_plugin>`, передаёт поток по WebSocket, транскрибирует его с помощью :ref:`citeck-stt-sidecar <citeck-stt-sidecar>` и автоматически формирует резюме через LLM. Результат сохраняется как ECOS-активность типа ``meeting-activity`` или ``call-activity``. Модуль доступен начиная с версии **1.11.0**.

.. toctree::
    :maxdepth: 2
    :hidden:

    AI_instruments/user_agents
    AI_instruments/ai_architecture
    AI_instruments/citeck-stt-sidecar
    AI_instruments/call-recording-module