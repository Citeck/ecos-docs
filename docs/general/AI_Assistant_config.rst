Конфигурация AI ассистента
============================

.. _AI_assistant_config:

.. contents::
    :depth: 2

Микросервис ``ecos-ai`` обеспечивает работу :ref:`интеллектуального помощника<AI_assistant>` в платформе Citeck. Он интегрируется с внешними провайдерами больших языковых моделей (LLM) и предоставляет AI-функциональность остальным микросервисам через RESTful API.

Статья описывает технические детали микросервиса, порядок настройки провайдеров LLM, конфигурацию ассистентов и параметры подключения через прокси.

.. note::

   Для работы AI-ассистента необходима Enterprise-лицензия с флагом ``ai`` и наличие пользователя в группе ``GROUP_ai-feature-allowed``.

Архитектурные решения
------------------------

* **Spring Boot:** Основа микросервиса
* **Kotlin:** Основной язык разработки
* **Spring AI:** Интеграция с AI провайдерами
* **Ecos Records:** Интеграция с платформой Citeck
* **RESTful API:** Стандартные HTTP эндпоинты для интеграции

Базовая техническая платформа
-------------------------------

Инструменты
~~~~~~~~~~~~

Возможности ассистента реализованы инструментами, которые подключаются агентам белыми списками. Полный каталог с разделением на операционные и конфигурационные — в статье :ref:`Пользовательские AI-агенты <user-agents>`.

Безопасность, доступ, авторизация
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Лицензионный контроль (флаг ``ai``), группы доступа, три оси доступа к инструментам и работа под правами пользователя описаны в статье :ref:`Безопасность AI-функций <ai-security>`.

Конфигурация
~~~~~~~~~~~~~

* **Прокси поддержка:** HTTP и HTTPS протоколы
* **Гибкие настройки:** Конфигурация через переменные окружения и ``application.yml``
* **Мониторинг:** Логирование и отслеживание ошибок


Spring-профили
----------------

Для быстрого старта можно использовать готовые Spring-профили, которые содержат преднастроенную конфигурацию провайдеров и моделей.

.. list-table::
  :header-rows: 1
  :widths: 20 50 30
  :class: tight-table

  * - Профиль
    - Описание
    - Обязательные env
  * - ``ai-default``
    - **Рекомендуемый.** Yandex Cloud (``gpt-oss-120b``) как основной провайдер + Anthropic (``claude-sonnet-4-6``) для генерации BPMN. Для генерации BPMN используется более интеллектуальная модель, что обеспечивает лучшее качество процессов.
    - ``CTK_YANDEX_AI_API_KEY``, ``CTK_YANDEX_AI_FOLDER_ID``, ``CTK_ANTHROPIC_API_KEY``
  * - ``ai-yandex-gpt-oss``
    - Yandex Cloud (``gpt-oss-120b``) для всех ассистентов
    - ``CTK_YANDEX_AI_API_KEY``, ``CTK_YANDEX_AI_FOLDER_ID``

Подключение в Citeck Launcher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

На текущий момент, чтобы конфигурация настроек в лаунчере не перезаписывалась при обновлении версиий в ките, необходимо настраивать через кастомный application-launcher.yml.
В дальнейшем планируется добавить отдельный интерфейс для удобной настройки подключения AI ассистента.

.. dropdown:: Как подключить AI-ассистента в Citeck Launcher
   :color: secondary

   1. Найдите микросервис **ai** в списке микросервисов.
   2. Нажмите **левой кнопкой мыши** на шестеренку настроек микросервиса и добавьте переменные окружения:

      - ``CTK_ANTHROPIC_API_KEY`` — для использования Anthropic
      - ``CTK_YANDEX_AI_FOLDER_ID``, ``CTK_YANDEX_AI_API_KEY`` — для Yandex AI Studio

      .. note::

         Для профиля ``ai-yandex-gpt-oss`` также добавьте его в строку ``SPRING_PROFILES_ACTIVE``.

   3. Нажмите **правой кнопкой мыши** на ту же шестеренку и выберите ``application-launcher.yml``.
   4. Вставьте содержимое нужного профиля:

      .. tab-set::

         .. tab-item:: ai-default

            .. code-block:: yaml

               citeck:
                 ai:
                   base:
                     model: 'gpt://${CTK_YANDEX_AI_FOLDER_ID}/gpt-oss-120b/latest'
                   assistants:
                     bpmn:
                       model: claude-sonnet-4-6
                       streaming: true
                       provider: anthropic
                       temperature: 0.0
                       reasoning-effort: none

               spring:
                 ai:
                   anthropic:
                     api-key: '${CTK_ANTHROPIC_API_KEY}'
                   openai:
                     api-key: '${CTK_YANDEX_AI_API_KEY}'
                     chat:
                       options:
                         model: 'gpt://${CTK_YANDEX_AI_FOLDER_ID}/gpt-oss-120b/latest'
                       base-url: https://llm.api.cloud.yandex.net

            .. tip::

               Вместо ``claude-sonnet-4-6`` можно указать ``claude-opus-4-6`` для более высокого качества генерации BPMN.

         .. tab-item:: ai-yandex-gpt-oss

            .. code-block:: yaml

               citeck:
                 ai:
                   base:
                     model: 'gpt://${CTK_YANDEX_AI_FOLDER_ID}/gpt-oss-120b/latest'
                   assistants:
                     bpmn:
                       streaming: false

               spring:
                 ai:
                   openai:
                     api-key: '${CTK_YANDEX_AI_API_KEY}'
                     chat:
                       options:
                         model: 'gpt://${CTK_YANDEX_AI_FOLDER_ID}/gpt-oss-120b/latest'
                       base-url: https://llm.api.cloud.yandex.net

      Если для доступа к AI API требуется прокси-сервер, добавьте блок ``proxy`` в конфигурацию — пример см. в разделе `Настройка прокси`_.

   5. Замените переменные ``${CTK_YANDEX_AI_API_KEY}``, ``${CTK_YANDEX_AI_FOLDER_ID}``, ``${CTK_ANTHROPIC_API_KEY}`` на реальные значения.
   6. Сохраните настройку, микросервис перезапустится автоматически.

.. tip::

  Профиль ``ai-default`` — рекомендуемый минимум для стабильной работы ассистента. Комбинация Yandex Cloud для основных задач и Anthropic Claude для генерации BPMN обеспечивает необходимое качество, так как для генерации BPMN-процессов требуется более интеллектуальная модель.

.. important::

  При использовании Anthropic в качестве провайдера (например, для генерации BPMN в профиле ``ai-default``) необходимо обеспечить сетевой доступ к API Anthropic. Для этого настройте HTTP-прокси (см. раздел `Настройка прокси`_) или используйте VPN.

Провайдеры LLM
----------------

Citeck AI Assistant поддерживает работу с различными провайдерами больших языковых моделей (LLM).

Поддерживаемые провайдеры
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **openai** - GPT-модели (gpt-5.1 и др.)
- **anthropic** - Claude модели (claude-opus-4-5 и др.)
- **deepseek** - модели DeepSeek (deepseek-chat, deepseek-coder)
- **ollama** - локальные модели (granite3.3, llama3, mistral)

Выбор провайдера по умолчанию
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Провайдер по умолчанию указывается в ``citeck.ai.default.provider``. Этот провайдер используется для всех ассистентов, если не указан специфичный:

.. code-block:: yaml

    citeck:
        ai:
            default:
                provider: openai  # openai, anthropic, deepseek, ollama

.. important::

    Для каждого типа ассистента можно указать своего провайдера через параметр ``provider``. Если не указан - используется ``citeck.ai.default.provider``.

Базовая конфигурация модели
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для работы системы необходимо указать базовую модель в ``citeck.ai.base.model``. Эта модель используется по умолчанию для всех ассистентов, если не указана специфичная модель:

.. code-block:: yaml

    citeck:
        ai:
            base:
                model: gpt-5.1  # Базовая модель для всех ассистентов

Настройка моделей для разных ассистентов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В рамках выбранного провайдера каждый тип ассистента может использовать свою модель и дополнительные параметры:

.. code-block:: yaml

    citeck:
        ai:
            assistants:
                bpmn:                            # Помощник BPMN в редакторе процессов
                    model: ${citeck.ai.base.model}
                    temperature: 0.0
                    reasoning-effort: none       # Уровень рассуждений: none, low, medium, high
                    streaming: true              # Потоковый вывод
                universal:                       # Универсальный ассистент (чат)
                    model: ${citeck.ai.base.model}
                    temperature: 0.7
                    reasoning-effort: medium
                script-writing:                  # Помощник написания скриптов
                    model: ${citeck.ai.base.model}
                    temperature: 0.2
                    reasoning-effort: medium
                    use-native-structured-output: true
                text-edit:                       # Редактирование текста в полях записей
                    model: ${citeck.ai.base.model}
                    temperature: 0.3
                    reasoning-effort: medium
                    use-native-structured-output: true
                intent-detection:                # Планирование и разбор ответов пользователя в агентном режиме
                    model: ${citeck.ai.base.model}
                    temperature: 0.1
                    reasoning-effort: low
                    use-native-structured-output: true

.. note::

   Название ``intent-detection`` историческое. Подсистемы определения намерения в платформе больше
   нет, но параметр остался и используется как слот модели для служебных вызовов агентного режима:
   построение и пересмотр плана, а также разбор ответа пользователя на вопрос агента (подтвердить,
   изменить, отклонить, пропустить). Удалять его не нужно — без него эти вызовы вернутся к базовой
   модели с параметрами по умолчанию.

Параметры ассистентов
~~~~~~~~~~~~~~~~~~~~~~

    * ``provider`` - провайдер для данного ассистента (если не указан - используется ``citeck.ai.default.provider``)
    * ``model`` - модель для использования (должна быть доступна у выбранного провайдера)
    * ``temperature`` - температура генерации (0.0-1.0)
    * ``reasoning-effort`` - уровень рассуждений: ``none``, ``low``, ``medium``, ``high``
    * ``streaming`` - включить потоковый вывод
    * ``use-native-structured-output`` - использовать нативный structured output провайдера

Помимо ``assistants``, свои блоки конфигурации имеют подсистемы:

    * ``citeck.ai.agents`` - агенты по умолчанию: ``default-operational`` (агент чата без явного выбора, по умолчанию ``tasks-documents-helper``) и ``default-config`` (агент правки скриптов, по умолчанию ``platform-config-agent``)
    * ``citeck.ai.multimodal`` - анализ загружаемых файлов: ``enabled``, ``limits.max-file-size-mb`` (по умолчанию 10)
    * ``citeck.ai.image`` - генерация изображений: провайдер, модель, лимиты (см. подраздел об изображениях в описании :ref:`AI ассистента <AI_assistant>`)
    * ``citeck.ai.model-capabilities`` - таблица возможностей моделей (какие модели мультимодальны и читают PDF нативно); дополняется шаблонами ``patterns`` и точечными ``overrides``
    * ``citeck.ai.rag`` - семантический поиск (:ref:`настройка RAG <rag-config>`)
    * ``citeck.ai.call-recording`` - :ref:`запись и резюме совещаний <call-recording-module>`

Модели AI-агентов
~~~~~~~~~~~~~~~~~~

У :ref:`пользовательских агентов <user-agents>` провайдер и модель — реквизиты записи агента (``aiProvider``, ``aiModel``, ``temperature``, ``reasoningEffort``); блок ``assistants`` на них не влияет. Модель агента протягивается и во внутренние генераторы артефактов: тип данных, форма или процесс, созданные по запросу через агента конфигурирования, генерируются моделью этого агента.

Поля ``aiProvider`` и ``aiModel`` обязательны. У преднастроенных агентов они заполнены при поставке; чтобы перевести агента на другую модель, измените их в карточке агента — платформенные значения ``citeck.ai.default.provider`` и ``citeck.ai.base.model`` на агентов не распространяются.

Пример раскладки моделей по агентам: мощная модель — агенту конфигурирования (генерация артефактов), экономичная — операционному агенту (массовые операции с записями), локальная — агенту, работающему с чувствительными данными. Исключение — помощник по изображениям: ему нужна мультимодальная модель для анализа картинок, поэтому экономичную или локальную модель ему назначать нельзя.

Телеметрия и расход токенов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

По каждому обращению к LLM в журнал приложения ``citeck-ai`` записываются метрики: токены запроса, ответа и суммарные; расширенные метрики при их наличии у провайдера (токены рассуждений, кэшированные токены); длительность вызова и скорость генерации; время до первого токена (в потоковом режиме); причина завершения; остаток квоты провайдера. При использовании более 80 % квоты провайдера в журнал пишется предупреждение.

Пример использования разных провайдеров
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    citeck:
        ai:
            default:
                provider: openai           # Провайдер по умолчанию
            assistants:
                bpmn:
                    provider: anthropic      # Claude для генерации BPMN
                    model: claude-opus-4-5
                universal:
                    # provider не указан - используется openai
                    model: gpt-5.1
                intent-detection:
                    provider: deepseek       # DeepSeek для быстрой классификации
                    model: deepseek-chat

.. note::

    Все указанные модели должны быть доступны в рамках выбранного провайдера.

Настройка Structured Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Конфигурация retry-механизма для структурированного вывода:

.. code-block:: yaml

    citeck:
        ai:
            structured-output:
                max-attempts: 3              # Максимум попыток при ошибках парсинга
                delay-ms: 500                # Начальная задержка между попытками (мс)
                use-exponential-backoff: true # Экспоненциальное увеличение задержки
                backoff-multiplier: 2.0      # Множитель увеличения задержки
                max-delay-ms: 5000           # Максимальная задержка (мс)

Примеры конфигурации основных провайдеров
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: OpenAI

      .. code-block:: yaml

         spring:
             ai:
                 openai:
                     api-key: ${OPENAI_API_KEY}

         citeck:
             ai:
                 default:
                     provider: openai
                 base:
                     model: gpt-5.1
                 assistants:
                     bpmn:
                         reasoning-effort: medium
                         streaming: true
                     intent-detection:
                         use-native-structured-output: true

   .. tab-item:: Ollama (локальные модели)

      .. code-block:: yaml

         citeck:
             ai:
                 default:
                     provider: ollama
                 base:
                     model: granite3.3
                 assistants:
                     bpmn:
                         model: llama3

   .. tab-item:: DeepSeek

      .. code-block:: yaml

         spring:
             ai:
                 deepseek:
                     api-key: ${DEEPSEEK_API_KEY}

         citeck:
             ai:
                 default:
                     provider: deepseek
                 base:
                     model: deepseek-chat
                 assistants:
                     bpmn:
                         model: deepseek-coder

   .. tab-item:: Yandex Cloud (через OpenAI-совместимый API)

      .. tip::

         Для Yandex Cloud рекомендуется использовать готовые профили **``ai-default``** или **``ai-yandex-gpt-oss``** — см. раздел `Spring-профили`_ выше. Ниже приведена ручная конфигурация.

      .. code-block:: yaml

         spring:
             ai:
                 openai:
                     api-key: ${YANDEX_API_KEY}
                     chat:
                         base-url: https://llm.api.cloud.yandex.net

         citeck:
             ai:
                 default:
                     provider: openai  # Используем OpenAI-совместимый API
                 base:
                     model: 'gpt://{folder_id}/gpt-oss-120b/latest'

      .. important::

         * Замените ``{folder_id}`` на реальный идентификатор каталога Yandex Cloud
         * Поддержка Yandex Cloud через OpenAI-совместимый API является частичной
         * Формат модели: ``gpt://{folder_id}/model-name/latest``
         * Доступные модели: ``gpt-oss-120b``, и другие модели Yandex Cloud
         * Во всех настройках ``citeck.ai.*.model`` необходимо указать модель в формате Yandex Cloud

Настройка прокси
----------------

Citeck AI Assistant поддерживает работу через прокси-сервер для доступа к внешним AI-сервисам.

Поддерживаемые протоколы прокси
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **HTTP** - стандартный HTTP прокси
- **HTTPS** - защищенный HTTPS прокси

Переменные окружения
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Включение прокси
    CITECK_AI_PROXY_ENABLED=true

    # Настройки подключения
    CITECK_AI_PROXY_HOST=your-proxy-host.com
    CITECK_AI_PROXY_PORT=8080
    CITECK_AI_PROXY_PROTOCOL=HTTP  # HTTP или HTTPS

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


