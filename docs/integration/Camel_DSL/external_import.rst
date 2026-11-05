.. _camel_dsl_external_import:

Импорт из Jira и GitLab
=======================

URI, параметры, входные и выходные данные и YAML-примеры каждого компонента приведены в :ref:`справочнике конечных точек <camel_external_endpoints>`.

GitLab
------

- :ref:`gitlab-commits-sync <GitLabCommitsSyncEndpoint>` выдаёт пачки коммитов.
- :ref:`gitlab-merge-requests-sync <GitLabMergeRequestsSyncEndpoint>` выдаёт пачки запросов на слияние.

Потребители сохраняют состояние синхронизации. Обработку полученных объектов и сохранение в целевые типы настраивает маршрут.

Jira
----

1. Настройте конечную точку ECOS для Jira и бин ``JiraApiClient``. В Citeck должны существовать проекты с импортируемыми ключами и связанными рабочими пространствами.
2. :ref:`jira-issues <JiraIssuesEndpoint>` читает задачи и задаёт контекст проекта. Разделите пачку шагом ``split`` и сохраните исходную задачу в переменной.
3. :ref:`transform-jira-issue <TransformJiraIssueEndpoint>` преобразует задачу по картам соответствия. Сохраните атрибуты через :ref:`ecos-records-mutate <EcosRecordsMutateEndpoint>` и передайте ссылку на целевую задачу заголовком ``eptIssueRef``.
4. Восстанавливайте исходный JSON перед каждым импортом связанных объектов: :ref:`import-jira-releases <ImportJiraReleasesEndpoint>`, :ref:`import-jira-attachment <ImportJiraAttachmentEndpoint>`, :ref:`import-jira-dev-info <ImportJiraDevInfoEndpoint>`, :ref:`import-jira-component <ImportJiraComponentEndpoint>`, :ref:`import-jira-sprint <ImportJiraSprintEndpoint>`, :ref:`import-jira-tags <ImportJiraTagsEndpoint>`.
5. :ref:`transform-jira-comment <TransformJiraCommentEndpoint>` и :ref:`transform-jira-worklog <TransformJiraWorkLogEndpoint>` возвращают атрибуты комментариев и трудозатрат; их также сохраняет маршрут. Заголовки целевых записей — ``commentLinkToRecord`` и ``worklogLinkToRecord``.

Полный маршрут ``ecos-camel-examples/jira/yaml/jira-import.yml`` и другие сценарии перечислены в :ref:`каталоге примеров <camel_dsl_repo_examples>`.
