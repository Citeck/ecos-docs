.. _camel_dsl_jira_import:

Настройка импорта проектов из Jira
==========================================

.. _ept_gitlab_sync:

Настройки синхронизации Commits и Мerge requests
--------------------------------------------------

Включение данной интеграции позволяет автоматически отображать информацию о коммитах и запросах на слияние из GitLab в карточках задач проекта.

Для запуска синхронизаций commits и merge request необходимо:

1.	Создать в GitLab **Access token**. В профиле GitLab перейти в **User settings -> Access tokens**

.. image:: /introduction/ecos_modules/_static/ept/git_01.png
       :width: 800
       :align: center
 
При создании токена обязательно необходимо указать **Select scopes -  read_api**

.. image:: /introduction/ecos_modules/_static/ept/git_02.png
       :width: 600
       :align: center
 
Далее скопировать созданный токен:

.. image:: /introduction/ecos_modules/_static/ept/git_03.png
       :width: 600
       :align: center

2.	Перейти в **Рабочее пространство «Раздел администратора» → Модель → Секреты** и указать его в Секрете **gitlab-access-token**

.. image:: /introduction/ecos_modules/_static/ept/git_04.png
       :width: 500
       :align: center
 
3.	Перейти в **Рабочее пространство «Раздел администратора» → Модель → Конечные точки** настроить конечную точку **gitlab-domain-url**:

-	указать **URL GitLab** – например, https://gitlab.yourcompany.ru
-	выбрать в Данных для аутентификации **Токен доступа Gitlab**

.. image:: /introduction/ecos_modules/_static/ept/git_05.png
       :width: 500
       :align: center
 
4.	Перейти в **Рабочее пространство «Раздел администратора» → Интеграция → Camel DSL**, запустить **gitlab-merge-requests-sync** и **gitlab-commits-sync**:

.. image:: /introduction/ecos_modules/_static/ept/git_06.png
       :width: 700
       :align: center
 

.. note::

      - Синхронизация будет происходить по всем проектам в GitLab, к которым созданный токен имеет доступ
      - Маппинг коммитов и MR к задачам происходит по ключу задачи Project tracker, указанному в комментарии к commit или названии MR в GitLab. То есть, если ключ задачи в Project Tracker равен **PT-1**, то в комментарии к commit или названии MR в GitLab должно быть указано **PT-1**

Подробнее о :ref:`действиях<camel_dsl_actions>`, доступных с Camel DSL.


.. _ept_jira_import:

Настройка импорта задач из Jira
--------------------------------

Введение
~~~~~~~~

Данный раздел описывает настройку синхронизации проектов из Jira в Citeck. Функциональность реализована с использованием Apache Camel DSL и позволяет настраивать гибкие сценарии импорта данных.

Основные возможности
~~~~~~~~~~~~~~~~~~~~

- Импорт задач (issues) из проекта Jira в Citeck;
- Импорт комментариев к задачам;
- Импорт затраченного времени (work logs);
- Импорт компонентов (components);
- Импорт тегов (tags/labels);
- Импорт релизов (releases);
- Импорт спринтов;
- Импорт вложений (attachments);
- Настраиваемое маппирование типов задач, статусов и приоритетов;
- Настраиваемое преобразование атрибутов;
- Импорт связей между задачами.

Пример конфигурации
~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

  - route:
      # Пример импорта задач из Jira
      # Проект должен быть создан в Citeck
      id: jira-crm-import
      from:
        uri: "jira-issues:crm-import"
        # Проверьте доступ к jira пользователя, под которым запускается импорт
        parameters:
          delay: 5000
          jiraHost: '{{ecos-endpoint:jira-host/url}}'
          jiraUser: '{{ecos-endpoint:jira-host/credentials/username}}'
          jiraToken: '{{ecos-endpoint:jira-host/credentials/password}}'
          projectKey: "ECOSCRM"
        steps:
          #- to: log:raw-jira-issues?level=INFO&showBody=true
          # Указание workspace и проекта обязательно
          - set-property:
              name: jiraImportedRecordIdPrefix
              constant: "imported-jira"
          - set-property:
              name: _workspace
              constant: "ECOSCRM"
          - set-property:
              name: link-project:project
              constant: "emodel/ept-project@eadfe69d-676a-42a5-b21f-2db7d5fc18bf"
          - set-property:
              name: "valuesMapping"
              constant: >
                {
                  "_type": {
                    "10000": "emodel/type@ept-issue-epic",
                    "10001": "emodel/type@ept-issue-story",
                    "10002": "emodel/type@ept-issue-task",
                    "10003": "emodel/type@ept-issue-subtask",
                    "10004": "emodel/type@ept-issue-bug",
                    "10501": "emodel/type@ept-issue-task",
                    "10500": "emodel/type@ept-issue-story",
                    "10503": "emodel/type@ept-issue-bug"
                  },
                  "priority": {
                    "1": "100_urgent",
                    "2": "200_high",
                    "3": "300_medium",
                    "4": "400_low"
                  },
                  "_status": {
                    "1": "backlog",
                    "10010": "backlog",
                    "3": "in-progress",
                    "10000": "to-do",
                    "10561": "to-do",
                    "10011": "to-do",
                    "10510": "review",
                    "10101": "waiting-for-qa",
                    "10100": "in-qa-review",
                    "10537": "in-qa-review",
                    "10565": "in-qa-review",
                    "10001": "done",
                    "10541": "done",
                    "10530": "on-hold",
                    "10006": "on-hold",
                    "10531": "on-hold"
                  },
                  "resolution": {
                    "10000": "emodel/ept-issue-resolution@done",
                    "10001": "emodel/ept-issue-resolution@wont-do",
                    "10002": "emodel/ept-issue-resolution@duplicate",
                    "10003": "emodel/ept-issue-resolution@cannot-reproduce",
                    "10400": "emodel/ept-issue-resolution@cannot-reproduce"
                  }
                }
          - set-property:
              name: "valuesConverter"
              constant: >
                {
                  "description": "jiraRenderedFieldToTextArea",
                  "_created": "jiraDateToInstant",
                  "_modified": "jiraDateToInstant",
                  "endDate": "jiraDateToInstant",
                  "reporter": "emailToPersonRef",
                  "implementer": "emailToPersonRef",
                  "epicLink": "issueKeyToRef",
                  "remainingEstimateMills": "secondsToMills"
                }
          - set-property:
              name: "attributesMapping"
              # Json path to EPT field
              constant: >
                {
                  "fields.issuetype.id": "_type",
                  "fields.priority.id": "priority",
                  "fields.summary": "summary",
                  "fields.description": "description",
                  "fields.resolution.id": "resolution",
                  "fields.labels": "tags",
                  "fields.resolutiondate": "endDate",
                  "fields.status.id": "_status",
                  "fields.reporter.emailAddress": "reporter",
                  "fields.assignee.emailAddress": "implementer",
                  "fields.timetracking.originalEstimate": "estimatedWorks",
                  "fields.timetracking.remainingEstimateSeconds": "remainingEstimateMills",
                  "fields.created": "_created",
                  "fields.updated": "_modified",
                  "fields.customfield_10002": "epicLink"
                }
          - set-property:
              name: "staticAttributes"
              constant: >
                {
                  "__disableAudit": true
                }
          - set-property:
              name: "linksMapping"
              constant: >
                {
                  "10000": "issue-links:blocker",
                  "10001": "issue-links:clone",
                  "10002": "issue-links:duplicate",
                  "10300": "issue-links:problem",
                  "10003": "issue-links:relates"
                }
          - split:
              expression:
                simple: "${body}"
              steps:
                - set-property:
                    name: "originalIssue"
                    simple: "${body}"
                # Трансформация метаданных jira в поля ept
                - to:
                    uri: "transform-jira-issue:crm-import"
                    parameters:
                      jiraHost: '{{ecos-endpoint:jira-host/url}}'
                      jiraUser: '{{ecos-endpoint:jira-host/credentials/username}}'
                      jiraToken: '{{ecos-endpoint:jira-host/credentials/password}}'
                - to: log:transformed-issue?level=INFO&showBody=true
                # Создание ept задачи через records
                - to: "ecos-records-mutate:?sourceId=emodel/ept-issue"
                #- to: log:created-record?level=INFO&showHeaders=true

                - set-header:
                    name: eptIssueRef
                    simple: "${header.recordsMutated[0]}"

                - step:
                    id: import-comments
                    steps:
                      - set-body:
                          simple: "${exchangeProperty.originalIssue}"
                      - set-header:
                          name: commentLinkToRecord
                          simple: "${header.eptIssueRef}"
                      - to: "transform-jira-comment:crm-import"
                      - to: "ecos-records-mutate:?sourceId=emodel/comment"
                      #- to: log:importcomments?level=INFO&showBody=true

                - step:
                    id: import-components
                    steps:
                      - set-body:
                          simple: "${exchangeProperty.originalIssue}"
                      - set-header:
                          name: eptIssueRef
                          simple: "${header.eptIssueRef}"
                      - to: "import-jira-component:crm-import"
                      #- to: log:importcomponents?level=INFO&showBody=true

                - step:
                    id: import-jira-tags
                    steps:
                        - set-body:
                            simple: "${exchangeProperty.originalIssue}"
                        - set-header:
                            name: eptIssueRef
                            simple: "${header.eptIssueRef}"
                        - to: "import-jira-tags:crm-import"
                        #- to: log:importtags?level=INFO&showBody=true

                - step:
                    id: import-releases
                    steps:
                      - set-body:
                          simple: "${exchangeProperty.originalIssue}"
                      - set-header:
                          name: eptIssueRef
                          simple: "${header.eptIssueRef}"
                      - to:
                          uri: "import-jira-releases:crm-import"
                          parameters:
                            jiraHost: "{{ecos-endpoint:jira-host/url}}"
                            jiraUser: "{{ecos-endpoint:jira-host/credentials/username}}"
                            jiraToken: "{{ecos-endpoint:jira-host/credentials/password}}"
                      #- to: log:importreleases?level=INFO&showBody=true

                - step:
                    # Если настроен плагин 2FA для Jira, то в нем нужно отключить принудительный
                    # 2FA для url /secure/attachment
                    id: import-attachments
                    steps:
                      - set-body:
                          simple: "${exchangeProperty.originalIssue}"
                      - set-header:
                          name: eptIssueRef
                          simple: "${header.eptIssueRef}"
                      - to:
                          uri: "import-jira-attachment:crm-import"
                          parameters:
                            jiraHost: "{{ecos-endpoint:jira-host/url}}"
                            jiraUser: "{{ecos-endpoint:jira-host/credentials/username}}"
                            jiraToken: "{{ecos-endpoint:jira-host/credentials/password}}"
                      #- to: log:importattachments?level=INFO&showBody=true

                - step:
                    id: import-sprint
                    steps:
                      - set-body:
                          simple: "${exchangeProperty.originalIssue}"
                      - set-header:
                          name: eptIssueRef
                          simple: "${header.eptIssueRef}"
                      - to:
                          uri: "import-jira-sprint:crm-import"
                          parameters:
                            # Поле в jira, в котором хранится спринт
                            sprintFieldId: "customfield_10006"
                      #- to: log:importsprint?level=INFO&showBody=true

                - step:
                    id: import-work-logs
                    steps:
                      - set-body:
                          simple: "${exchangeProperty.originalIssue}"
                      - set-header:
                          name: worklogLinkToRecord
                          simple: "${header.eptIssueRef}"
                      - to: "transform-jira-worklog:crm-import"
                      #- to: log:transformworklog?level=INFO&showBody=true
                      - to: "ecos-records-mutate:?sourceId=emodel/ecos-time-tracking-type"
                      #- to: log:importworklogs?level=INFO&showBody=true



Быстрая настройка
~~~~~~~~~~~~~~~~~~

1. :ref:`Создайте проект<ept_new_project>` в Citeck. После этого должно создаться рабочее пространство проекта.
2. В jira создайте пользователя для импорта задач, получите его токен или пароль.
3. В журнале **Конечные точки** (Рабочее пространство «Раздел администратора» → Модель) создайте конечную точку, заполните URL, данные для аутентификации с типом Basic.
4. В журнале **Camel DSL** (Рабочее пространство «Раздел администратора» → Интеграция ) создайте маршрут с контекстом на основе примера выше. Обязательно укажите параметры подключения к Jira, ``_workspace`` и ``link-project:project``.
5. Логи импорта доступны в журнале **Журнал синхронизаций** (Рабочее пространство «Раздел администратора» → Интеграция).
6. Посмотреть состояние импорта, сбросить его можно в журнале **Состояние синхронизации** (Рабочее пространство «Раздел администратора» → Интеграция).
7. После того, как задачи импортированы, выключите маршрут.
8. Скорректируйте генератор счетчика задач. Для этого необходимо выполнить скрипт в консоли браузера:

.. code-block:: javascript

      const record = Records.get("emodel/num-template-action@");
      record.att("type", "set-next-number");
      record.att("args",
      {
            "templateRef": "emodel/num-template@ept-issue-num-template",
            "counterKey": "emodel/ept-project@767a669f-8455-4cf3-b43f-75b66c6eeb8f",
            "nextNumber": 39
      })
      record.save();

- ``"nextNumber": 39`` - следующий номер задачи, который будет присвоен при создании новой задачи.
- ``"counterKey": "emodel/ept-project@767a669f-8455-4cf3-b43f-75b66c6eeb8f"`` - recordRef проекта, аналогичный полю ``link-project:project`` в маршруте импорта.

Параметры настройки
~~~~~~~~~~~~~~~~~~~~~~

Основные параметры
"""""""""""""""""""

- **jiraHost** - URL сервера Jira
- **jiraUser** - Имя пользователя для подключения к Jira
- **jiraToken** - Токен или пароль пользователя для подключения к Jira
- **projectKey** - Ключ проекта в Jira для импорта
- **delay** - Интервал проверки новых задач в миллисекундах


Указание рабочего пространства и проекта
"""""""""""""""""""""""""""""""""""""""""

Для корректной работы импорта обязательно необходимо указать рабочее пространство и проект в Citeck:

.. code-block:: yaml

    - set-property:
        name: _workspace
        constant: "ECOSCRM" # id рабочего пространства
    - set-property:
        name: link-project:project
        constant: "emodel/ept-project@eadfe69d-676a-42a5-b21f-2db7d5fc18bf" # recordRef проекта, должен быть связан с рабочим пространством


Настройка маппинга значений
""""""""""""""""""""""""""""

``valuesMapping`` позволяет указать соответствие значений из Jira значениям в Citeck:

.. code-block:: json

    {
      "_type": {
        "10000": "emodel/type@ept-issue-epic",
        "10001": "emodel/type@ept-issue-story",
        "10002": "emodel/type@ept-issue-task",
        "10003": "emodel/type@ept-issue-subtask",
        "10004": "emodel/type@ept-issue-bug"
      },
      "priority": {
        "1": "100_urgent",
        "2": "200_high",
        "3": "300_medium",
        "4": "400_low"
      },
      "_status": {
        "1": "backlog",
        "10010": "backlog",
        "3": "in-progress"
      }
    }

Конвертеры значений
"""""""""""""""""""

``valuesConverter`` определяет преобразование значений полей из формата Jira в формат Citeck:

.. code-block:: json

    {
      "description": "jiraRenderedFieldToTextArea",
      "_created": "jiraDateToInstant",
      "_modified": "jiraDateToInstant",
      "endDate": "jiraDateToInstant",
      "reporter": "emailToPersonRef",
      "implementer": "emailToPersonRef",
      "epicLink": "issueKeyToRef",
      "remainingEstimateMills": "secondsToMills"
    }

Доступные конвертеры:

- **jiraRenderedFieldToTextArea** - преобразует отрендеренное HTML-содержимое поля Jira в формат TextArea для Citeck, сохраняя форматирование и ссылки
- **jiraDateToInstant** - преобразует дату из формата Jira в формат Instant для Citeck
- **emailToPersonRef** - преобразует email-адрес пользователя Jira в ссылку на пользователя в Citeck
- **issueKeyToRef** - преобразует ключ задачи Jira (например, ECOSCRM-123) в ссылку на соответствующую задачу в Citeck
- **secondsToMills** - преобразует время в секундах в миллисекунды для корректного отображения в Citeck

Маппинг атрибутов
"""""""""""""""""

``attributesMapping`` определяет соответствие полей Jira атрибутам сущностей в Citeck:

.. code-block:: json

    {
      "fields.issuetype.id": "_type",
      "fields.priority.id": "priority",
      "fields.summary": "summary",
      "fields.description": "description",
      "fields.resolution.id": "resolution",
      "fields.labels": "tags",
      "fields.resolutiondate": "endDate",
      "fields.status.id": "_status",
      "fields.reporter.emailAddress": "reporter",
      "fields.assignee.emailAddress": "implementer",
      "fields.timetracking.originalEstimate": "estimatedWorks",
      "fields.timetracking.remainingEstimateSeconds": "remainingEstimateMills",
      "fields.created": "_created",
      "fields.updated": "_modified",
      "fields.customfield_10002": "epicLink"
    }

Маппинг связей между задачами
"""""""""""""""""""""""""""""

``linksMapping`` определяет соответствие типов связей между задачами в Jira типам связей в Citeck:

.. code-block:: json

    {
      "10000": "issue-links:blocker",
      "10001": "issue-links:clone",
      "10002": "issue-links:duplicate",
      "10300": "issue-links:problem",
      "10003": "issue-links:relates"
    }

Статические атрибуты
"""""""""""""""""""""

``staticAttributes`` позволяет указать атрибуты, которые будут добавлены ко всем импортируемым сущностям:

.. code-block:: json

    {
      "__disableAudit": true
    }

Для корректного установления атрибутов ``_created``, ``_modified`` и т.д. необходимо указать ``__disableAudit: true``

Компоненты и этапы синхронизации
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Импорт задач (Issues)
"""""""""""""""""""""

Основной компонент синхронизации, выполняет загрузку задач из Jira и их преобразование в сущности Citeck. Для работы использует **JiraIssuesComponent** и **TransformJiraIssueComponent**.

Импорт комментариев
"""""""""""""""""""

Компонент **TransformJiraCommentComponent** импортирует комментарии к задачам из Jira в Citeck, сохраняя их как связанные записи с типом ``"emodel/type@ecos-comment"``.

Импорт затраченного времени
"""""""""""""""""""""""""""

Компонент **TransformJiraWorkLogComponent** импортирует записи о затраченном времени (work logs) из Jira в Citeck, сохраняя их как сущности с типом ``"emodel/type@ecos-time-tracking-type"``.

Импорт компонентов
"""""""""""""""""""

Компонент **ImportJiraComponentComponent** импортирует компоненты, присвоенные задачам в Jira.

Импорт тегов
"""""""""""""

Компонент **ImportJiraTagsComponent** импортирует метки (labels) из Jira, преобразуя их в теги Citeck.

Импорт релизов
"""""""""""""""

Компонент **ImportJiraReleasesComponent** импортирует информацию о релизах (fixVersions и affectedVersions) из Jira в Citeck.

Импорт спринтов
"""""""""""""""

Компонент **ImportJiraSprintComponent** импортирует информацию о спринтах, к которым отнесены задачи в Jira.

Импорт вложений
"""""""""""""""

Компонент **ImportJiraAttachmentComponent** загружает вложения задач из Jira и импортирует их в Citeck.

Дополнительные возможности
~~~~~~~~~~~~~~~~~~~~~~~~~~

Префикс идентификаторов
"""""""""""""""""""""""

Для уникальной идентификации импортированных записей можно задать префикс через свойство ``jiraImportedRecordIdPrefix``:

.. code-block:: yaml

    - set-property:
        name: jiraImportedRecordIdPrefix
        constant: "imported-jira"

Все созданные записи в рамках импорта будут использовать данные префикс, обратите внимание, если импорт будет выполняться несколько раз, то существующие записи будут обновлены, а новые созданы.

Если необходимо запустить импорт заново, то можно сбросить состояние импорта в журнале **Состояние синхронизации** (Рабочее пространство «Раздел администратора» → Интеграция).

Ограничения и рекомендации
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Перед настройкой импорта убедитесь, что пользователь Jira имеет необходимые права доступа к проекту.
2. При использовании двухфакторной аутентификации в Jira необходимо использовать API-токен вместо пароля.
3. Для импорта вложений может потребоваться отключение принудительной 2FA для URL ``/secure/attachment`` в настройках Jira.
4. Рекомендуется начинать с небольшого набора задач для проверки корректности импорта.
5. При импорте большого количества задач рекомендуется увеличить значение параметра ``delay``.
6. Убедитесь, что корректно указаны ``_workspace`` и ``link-project:project``.

Устранение неполадок
~~~~~~~~~~~~~~~~~~~~

1. **Проблема**: Задачи не импортируются.
   
   **Решение**: Проверьте правильность указания ``jiraHost``, ``jiraUser``, ``jiraToken`` и ``projectKey``.

2. **Проблема**: Не импортируются вложения.
   
   **Решение**: Проверьте настройки двухфакторной аутентификации в Jira для URL ``/secure/attachment``.

3. **Проблема**: Неверное маппирование типов/статусов.
   
   **Решение**: Проверьте значения **ID** в Jira и обновите соответствующую секцию ``valuesMapping``.

4. **Проблема**: Ошибка "Value mapping for field does not contain value".
   
   **Решение**: Добавьте отсутствующее значение в соответствующую секцию ``valuesMapping``.

