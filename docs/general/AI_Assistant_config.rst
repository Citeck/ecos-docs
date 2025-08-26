Конфигурация AI ассистента
============================

.. _AI_assistant_config:

.. contents::
    :depth: 3

Архитектурные решения
------------------------

    * **Spring Boot:** Основа микросервиса
    * **Kotlin:** Основной язык разработки
    * **Spring AI:** Интеграция с AI провайдерами
    * **Ecos Records:** Интеграция с платформой Citeck
    * **RESTful API:** Стандартные HTTP эндпоинты для интеграции

Базовая техническая платформа
-------------------------------

Базовые инструменты
~~~~~~~~~~~~~~~~~~~~

    * **GetCurrentTimeTool:** Получение текущего времени
    * **GetRecordAttributesTool:** Извлечение атрибутов записей
    * **GetRecordContentTool:** Получение контента записей
    * **GetRecordDisplayNameTool:** Получение отображаемых имен
    * **GetRecordContactsTool:** Извлечение контактной информации
    * **GetRecordContentHistoryTools:** История изменений контента
    * **DocumentAnalysisTool:** Анализ документов
    * **DeployDataTypeTool:** Развертывание типов данных
    * **GetArtifactMetadataTool:** Метаданные артефактов
    * **GetActivitiesTool:** Работа с активностями

Безопасность, доступ, авторизация
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    * **Лицензионный контроль:** Проверка флага ``ai`` в лицензии
    * **Групповые права:** Контроль доступа через группу ``GROUP_ai-feature-allowed``
    * **Контроль доступа:** Расширенные проверки доступности AI функций
    * **BPMN авторизация:** Улучшенная обработка запросов BPMN с учетом прав пользователя

Конфигурация
~~~~~~~~~~~~~

    * **Прокси поддержка:** HTTP, HTTPS и SOCKS протоколы
    * **Гибкие настройки:** Конфигурация через переменные окружения и ``application.yml``
    * **Мониторинг:** Логирование и отслеживание ошибок


Провайдеры LLM
----------------

Citeck AI Assistant поддерживает работу с различными провайдерами больших языковых моделей (LLM).

Выбор провайдера
~~~~~~~~~~~~~~~~~~

Провайдер LLM выбирается один для всей системы и указывается в конфигурации ``spring.ai.model.chat``:

.. code-block:: yaml

    spring:
    ai:
        model:
        chat: openai  # Провайдер: anthropic, azure-openai, и т.д. (org.springframework.ai.observation.conventions.AiProvider)

Поддерживаемые провайдеры
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - **openai** - GPT-модели (gpt-4, gpt-4.1, gpt-4.1-mini и др.)
    - **azure-openai** - GPT-модели через Azure (gpt-4, gpt-35-turbo и др.)
    - **anthropic** - Claude модели (claude-3-opus, claude-3-sonnet, claude-3-haiku)
    - **ollama** - локальные модели (granite3.3, llama3, mistral и др.)
    - **deepseek** - модели DeepSeek (deepseek-chat, deepseek-coder и др.)
    - **vertex_ai** - Google Vertex AI модели (gemini-pro, gemini-pro-vision)
    - **google_genai** - Google GenAI модели
    - **bedrock_converse** - AWS Bedrock модели (claude, titan, jurassic и др.)
    - **mistral_ai** - модели Mistral AI (mistral-large, mistral-medium, mistral-small)
    - **minimax** - модели Minimax (abab6.5, abab5.5 и др.)
    - **zhipuai** - модели ZhipuAI (glm-4, glm-3-turbo)

Базовая конфигурация модели
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для работы системы необходимо указать базовую модель в ``citeck.ai.base.model``. Эта модель используется по умолчанию для всех ассистентов, если не указана специфичная модель:

.. code-block::

    citeck:
    ai:
        base:
        model: gpt-4.1-mini  # Базовая модель для всех ассистентов

Настройка моделей для разных ассистентов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В рамках выбранного провайдера каждый тип ассистента может использовать свою модель и температуру:

.. code-block:: yaml

    citeck:
    ai:
        assistants:
        bpmn:
            model: gpt-4.1          # Модель для BPMN-ассистента
            temperature: 0.7            # Температура для творческих задач
        universal:
            model: gpt-4-mini           # Модель для универсального ассистента
            temperature: 0.7
        intent-detection:
            model: gpt-3.5-turbo        # Быстрая модель для определения намерений
            temperature: 0.1            # Низкая температура для точности
        required-content-version-selection:
            model: gpt-4-mini           # Модель для выбора версий контента
            temperature: 0.1

.. note::

    Все указанные модели должны быть доступны в рамках выбранного провайдера.

Примеры конфигурации основных провайдеров
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenAI
""""""

.. code-block:: yaml

    spring:
    ai:
        model:
        chat: openai  # Выбор провайдера OpenAI
        openai:
        api-key: ${OPENAI_API_KEY}
        chat:
            options:
            model: gpt-4.1-mini  # Модель по умолчанию для Spring AI

    citeck:
    ai:
        base:
        model: gpt-4.1-mini  # Базовая модель системы
        assistants:
        bpmn:
            model: gpt-4.1      # Более мощная модель для BPMN
        universal:
            model: gpt-4.1-mini       # Стандартная модель
        intent-detection:
            model: gpt-3.5-turbo    # Быстрая модель для классификации

Ollama (локальные модели)
"""""""""""""""""""""""""""""

.. code-block:: yaml

    spring:
    ai:
        model:
        chat: ollama
        ollama:
        chat:
            options:
            model: granite3.3

    citeck:
    ai:
        base:
        model: granite3.3
        assistants:
        bpmn:
            model: llama3
        universal:
            model: granite3.3
        intent-detection:
            model: granite3.3

DeepSeek
"""""""""""

.. code-block:: yaml

    spring:
    ai:
        model:
        chat: deepseek
        deepseek:
        api-key: ${DEEPSEEK_API_KEY}
        chat:
            options:
            model: deepseek-chat

    citeck:
    ai:
        base:
        model: deepseek-chat
        assistants:
        bpmn:
            model: deepseek-coder
        universal:
            model: deepseek-chat
        intent-detection:
            model: deepseek-chat

Настройка прокси
----------------

Citeck AI Assistant поддерживает работу через прокси-сервер для доступа к внешним AI-сервисам.

Поддерживаемые протоколы прокси
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **HTTP** - стандартный HTTP прокси
- **HTTPS** - защищенный HTTPS прокси

Переменные окружения
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    # Включение прокси
    CITECK_AI_PROXY_ENABLED=true

    # Настройки подключения
    CITECK_AI_PROXY_HOST=your-proxy-host.com
    CITECK_AI_PROXY_PORT=8080
    CITECK_AI_PROXY_PROTOCOL=HTTP  # HTTP, HTTPS или SOCKS

    # Аутентификация (опционально)
    CITECK_AI_PROXY_USERNAME=your-username
    CITECK_AI_PROXY_PASSWORD=your-password


Пример конфигурации в application.yml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    citeck:
    ai:
        proxy:
        enabled: true
        host: proxy.company.com
        port: 8080
        protocol: HTTP
        username: proxy-user
        password: proxy-pass

