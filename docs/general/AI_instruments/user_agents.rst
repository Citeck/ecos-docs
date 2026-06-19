.. _user-agents:

Пользовательские AI-агенты
============================

.. contents::
    :depth: 3

**Агент** — конфигурируемая сущность в Citeck с системным промптом, LLM-провайдером и набором инструментов. Хранится как Citeck-запись типа ``emodel/ai-agent``.

Статья описывает модель данных агента, режимы выполнения, доступные инструменты и порядок создания агентов и пользовательских инструментов.

Модель данных
--------------

Модель данных определена в ``AgentDefinition.kt``:

.. list-table::
   :header-rows: 1
   :widths: 25 20 15 40

   * - Поле
     - Тип
     - Обязательное
     - Описание
   * - ``id``
     - TEXT
     - да
     - Идентификатор записи агента
   * - ``name``
     - TEXT
     - да
     - Отображаемое имя агента
   * - ``description``
     - TEXT
     - нет
     - Описание агента (отображается в журнале и в ответе ``/api/ai-agent/list``)
   * - ``instruction``
     - TEXT
     - да
     - Системный промпт
   * - ``aiProvider``
     - TEXT
     - да
     - Идентификатор LLM-провайдера
   * - ``aiModel``
     - TEXT
     - да
     - Идентификатор модели
   * - ``temperature``
     - NUMBER
     - нет
     - Степень случайности генерации: ``0.0`` — детерминированный вывод (модель всегда выбирает наиболее вероятный токен), ``1.0`` — высокая вариативность ответов. Значения выше ``1.0`` допускаются, но увеличивают риск несвязного текста. Рекомендуемый диапазон: ``0.0``–``0.3`` для фактических задач (резюме, извлечение данных), ``0.6``–``0.9`` для диалоговых агентов. По умолчанию ``0.7``.
   * - ``tools``
     - TEXT[]
     - нет
     - Список подключённых инструментов
   * - ``enabled``
     - BOOLEAN
     - нет
     - Включён ли агент (по умолчанию ``false``)


Режимы выполнения
------------------

Stateless
~~~~~~~~~~

Один запрос — один ответ, без памяти о предыдущих сообщениях. Предназначен для вызова из BPMN-процессов через ``POST /api/ai-agent/execute``.

Вызывается через ``AgentExecutionService.execute``.

.. note::

   Вызов AI-агентов из BPMN-процессов в текущем релизе отключён и будет доступен
   в следующих релизах.

.. warning::

   На stateless-пути нет HITL-подтверждения. Tool-вызовы выполняются под техническим пользователем Camunda, что фактически обходит Citeck record-level permissions. Не добавляйте деструктивные инструменты (``mutateRecord``, ``deleteRecords``) агентам без отдельного дизайна авторизации.

Stateful / Interactive
~~~~~~~~~~~~~~~~~~~~~~~

Многоходовой диалог с ``ChatMemory``, требует ``conversationId``. Используется в AI Assistant UI.

Вызывается через ``AgentExecutionService.executeInteractive``.

В интерактивном режиме оркестратор может дополнить системный промпт агента
контекстом пользователя, не меняя сохранённую инструкцию. Через
``AgentExecutionRequest.context`` передаётся ключ ``user_context``
(``USER_CONTEXT_KEY``) — блок записей, на которые сослался пользователь
(@-упоминания, выбор в UI, прикреплённые файлы). Это позволяет LLM
сопоставлять отображаемые имена с ``EntityRef`` при вызове инструментов.
Контекст добавляется в системный промпт под заголовком ``--- User Context ---``
(см. ``AgentExecutionService.buildSystemPrompt``).


REST API
---------

.. list-table::
   :header-rows: 1
   :widths: 10 45 45

   * - Метод
     - URL
     - Описание
   * - ``GET``
     - ``/api/ai-agent/available-providers``
     - Список подключённых LLM-провайдеров
   * - ``GET``
     - ``/api/ai-agent/available-tools``
     - Инструменты, доступные агентам
   * - ``POST``
     - ``/api/ai-agent/execute``
     - Stateless вызов: ``{agentId, message, context}`` → ``{response}``
   * - ``GET``
     - ``/api/ai-agent/list``
     - Список включённых агентов


Доступные инструменты
----------------------

По умолчанию ``isAvailableForAgents() = true``. Недоступны для агентов (переопределяют в ``false``) внутренние служебные инструменты — ``SaveFormDraftTool``, ``SaveDataTypeDraftTool``, ``SaveEscalationTool`` и аналогичные.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Инструмент
     - Описание
   * - ``GetRecordAttributesTool``
     - Атрибуты записи
   * - ``GetRecordContentTool``
     - Содержимое документа
   * - ``GetRecordContentHistoryTools``
     - История версий
   * - ``GetRecordDisplayNameTool``
     - Отображаемое имя
   * - ``GetRecordTypeMetadataTool``
     - Метаданные типа
   * - ``GetRecordContactsTool``
     - Контакты записи
   * - ``QueryRecordsTool``
     - Поиск записей
   * - ``MutateRecordTool``
     - Изменение записи
   * - ``DeleteRecordsTool``
     - Удаление записей
   * - ``GetActivitiesTool``
     - Активности
   * - ``GetEcosAppContentTool``
     - Содержимое ECOS-приложения
   * - ``GetArtifactMetadataTool``
     - Метаданные артефакта
   * - ``SearchDocumentationTool``
     - Поиск в документации
   * - ``RagSearchTool`` / ``RagGetDocumentTool``
     - RAG-поиск (если включён)
   * - ``DocumentAnalysisTool``
     - Анализ документов
   * - ``GetCurrentTimeTool``
     - Текущее время


Создание агента
----------------

Через UI
~~~~~~~~~

В рабочем пространстве администратора в разделе **AI** перейдите в журнал **AI Агенты**:

1. Заполните **Название**, **Системный промпт**, выберите **Провайдер LLM** и **Модель**.
2. Опционально: добавьте инструменты, установите **Температуру**.
3. Установите чекбокс **Включён** и сохраните.

 .. image:: _static/ai_agent_setting.png
       :width: 650
       :align: center

Citeck-артефакты
~~~~~~~~~~~~~~~~~~

Артефакты агента расположены в следующих файлах:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Артефакт
     - Путь
   * - Тип
     - ``src/main/resources/eapps/artifacts/model/type/ai-agent.yml``
   * - Журнал
     - ``src/main/resources/eapps/artifacts/ui/journal/ai-agents-journal.yml``
   * - Форма
     - ``src/main/resources/eapps/artifacts/ui/form/ai-agent-form.json``


Создание собственного инструмента
-----------------------------------

Реализуйте интерфейс ``CiteckAiTool`` и пометьте класс как Spring-компонент:

.. code-block::

    @Component
    class MyCustomTool(
        private val someService: SomeService
    ) : CiteckAiTool {
        companion object {
            const val NAME = "my_custom_tool"
        }

        override fun getName(): String = NAME
        override fun getDescription(): String = "Описание для LLM"

        @Tool(name = NAME, description = "Описание для LLM")
        fun myAction(param: String): String {
            return someService.doSomething(param)
        }
    }

Spring DI автоматически обнаружит инструмент через ``List<CiteckAiTool>`` и добавит в список доступных.

Чтобы скрыть инструмент от агентов (только для внутреннего использования):

.. code-block:: kotlin

    override fun isAvailableForAgents(): Boolean = false


Маршрутизация в оркестраторе
------------------------------

``AgentOrchestratorService.processRequest()`` — первый приоритет маршрутизации: если к разговору привязан агент (``resolveAgentRef``), вся обработка делегируется ``AgentExecutionService.executeInteractive()``, минуя Intent Detection и Plan-and-Execute.


Ключевые файлы
---------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Компонент
     - Файл
   * - Модель данных
     - ``src/main/java/ru/citeck/ecos/ai/domain/agent/AgentDefinition.kt``
   * - Реестр агентов
     - ``src/main/java/ru/citeck/ecos/ai/domain/agent/AgentRegistry.kt``
   * - Сервис выполнения
     - ``src/main/java/ru/citeck/ecos/ai/domain/agent/AgentExecutionService.kt``
   * - REST-контроллер
     - ``src/main/java/ru/citeck/ecos/ai/domain/agent/AgentController.kt``
   * - Интерфейс инструментов
     - ``src/main/java/ru/citeck/ecos/ai/domain/assistant/tools/CiteckAiTool.kt``
   * - ECOS-тип
     - ``src/main/resources/eapps/artifacts/model/type/ai-agent.yml``
   * - ECOS-журнал
     - ``src/main/resources/eapps/artifacts/ui/journal/ai-agents-journal.yml``
   * - ECOS-форма
     - ``src/main/resources/eapps/artifacts/ui/form/ai-agent-form.json``
