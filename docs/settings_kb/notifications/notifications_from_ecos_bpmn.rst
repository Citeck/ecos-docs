Отправка уведомлений из BPMN (Send Task)
=========================================

.. _notification_from_bpmn:

.. contents::

Общее описание
--------------

Для отправки уведомлений из BPMN-процесса используется элемент **Send Task** — специальный
компонент платформы Citeck. Несмотря на название, Send Task в ECOS не является стандартным
BPMN Send Task: его поведение полностью определяется ECOS-расширениями и реализует отправку
уведомлений через микросервис ecos-notifications.

Уведомления отправляются через :ref:`ecos-notifications<notifications>`.
Не следует отправлять уведомления напрямую из кода микросервиса или из скриптов процесса,
минуя ecos-notifications.

.. important::

   На данный момент из BPMN Send Task поддерживается только тип уведомления **EMAIL_NOTIFICATION**.
   Указание любого другого типа вызовет ошибку при сохранении или публикации процесса.

Подробное описание компонента в редакторе BPMN — см. :ref:`Уведомление<notification>`.

XML-представление Send Task
----------------------------

В XML BPMN-файла Send Task описывается через элемент ``<bpmn:sendTask>`` с атрибутами
из пространства имён ``ecos:`` (``xmlns:ecos="http://www.citeck.ru/ecos/bpmn/1.0"``).

Пример — уведомление с получателями по ролям:

.. code-block:: xml

   <bpmn:sendTask
     id="Activity_notify_initiator"
     name="Уведомление инициатору"
     ecos:notificationType="EMAIL_NOTIFICATION"
     ecos:notificationTemplate="notifications/template@ecos-contract-approval-notification-template"
     ecos:notificationLang="ru"
     ecos:notificationTo="[&quot;initiator&quot;]"
     ecos:notificationToExpression="[]"
     ecos:notificationCc="[]"
     ecos:notificationCcExpression="[]"
     ecos:notificationBcc="[]"
     ecos:notificationBccExpression="[]"
     ecos:notificationSendCalendarEvent="false"
     ecos:notificationAdditionalMeta="{}">
   </bpmn:sendTask>

Пример — уведомление с динамическим получателем из переменной процесса:

.. code-block:: xml

   <bpmn:sendTask
     id="Activity_notify_confirmer"
     name="Уведомление согласующему"
     ecos:notificationType="EMAIL_NOTIFICATION"
     ecos:notificationTemplate="notifications/template@ecos-contract-approval-notification-template"
     ecos:notificationLang="ru"
     ecos:notificationTo="[]"
     ecos:notificationToExpression="[&quot;${confirmer}&quot;]"
     ecos:notificationCc="[]"
     ecos:notificationCcExpression="[]"
     ecos:notificationBcc="[]"
     ecos:notificationBccExpression="[]"
     ecos:notificationSendCalendarEvent="false"
     ecos:notificationAdditionalMeta="{}">
   </bpmn:sendTask>

Пример — уведомление с явным указанием отправителя из ecos-config:

.. code-block:: xml

   <bpmn:sendTask
     id="Activity_notify_with_from"
     name="Уведомление инициатору о создании заявки"
     ecos:notificationType="EMAIL_NOTIFICATION"
     ecos:notificationTemplate="notifications/template@sd-request-create"
     ecos:notificationLang="ru"
     ecos:notificationFrom="${Config.getNotNull(&quot;app/service-desk$send-sd-email-from&quot;).asText()}"
     ecos:notificationTo="[&quot;initiator-role&quot;]"
     ecos:notificationToExpression="[]"
     ecos:notificationCc="[]"
     ecos:notificationCcExpression="[]"
     ecos:notificationBcc="[]"
     ecos:notificationBccExpression="[]"
     ecos:notificationSendCalendarEvent="false"
     ecos:notificationAdditionalMeta="{}">
   </bpmn:sendTask>

Атрибуты Send Task
-------------------

Основные атрибуты
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Атрибут
     - Описание
   * - ``ecos:notificationType``
     - Тип уведомления. Поддерживается только ``EMAIL_NOTIFICATION``.
   * - ``ecos:notificationTemplate``
     - Ссылка на шаблон уведомления в формате ``notifications/template@<id>``.
       Взаимоисключающий с ``ecos:notificationTitle`` / ``ecos:notificationBody``.
   * - ``ecos:notificationTitle``
     - Заголовок письма напрямую (без шаблона). Только статический текст, без динамических переменных.
   * - ``ecos:notificationBody``
     - Тело письма напрямую (без шаблона). Только статический текст.
   * - ``ecos:notificationLang``
     - Язык шаблона: ``ru``, ``en`` и т.д. Если не указан — берётся язык по умолчанию.
   * - ``ecos:notificationFrom``
     - Исходящий адрес отправителя. Можно указать напрямую или через expression.
       Если не указан — используется значение по умолчанию из настроек ecos-notifications.
       Поддерживает форматы:

       - ``someAddress@mail.com``
       - ``"Some Name" <someAddress@mail.com>``
       - ``${someExpressionToGetAddress}``
       - ``${Config.getNotNull("app/your-app$your-key").asText()}``
   * - ``ecos:notificationAdditionalMeta``
     - JSON-объект с дополнительными переменными, доступными в шаблоне.
       Значение, начинающееся с ``!str_``, передаётся как строка-константа.
       Пример: ``{"myKey": "!str_someConstant"}`` — в шаблоне доступно как ``${myKey}`` со значением ``someConstant``.

Получатели
~~~~~~~~~~

Получатели задаются JSON-массивами строк. Атрибуты ``*To``, ``*Cc``, ``*Bcc`` принимают
**имена ролей** документа; атрибуты ``*ToExpression``, ``*CcExpression``, ``*BccExpression`` —
**выражения** (имя пользователя, email, recordRef или ``${variable}``).

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Атрибут
     - Описание
   * - ``ecos:notificationTo``
     - JSON-массив ролей получателей. Платформа резолвит email всех пользователей роли.
       Пример: ``["initiator", "lead-tech-role"]``
   * - ``ecos:notificationToExpression``
     - JSON-массив выражений для получателей.
       Пример: ``["${confirmer}", "${assigneesOfCurrentLine}"]``
   * - ``ecos:notificationCc``
     - JSON-массив ролей для копии (CC).
   * - ``ecos:notificationCcExpression``
     - JSON-массив выражений для копии.
   * - ``ecos:notificationBcc``
     - JSON-массив ролей для скрытой копии (BCC).
   * - ``ecos:notificationBccExpression``
     - JSON-массив выражений для скрытой копии.

Роли и выражения можно комбинировать: статические роли — в ``*To``, динамические — в ``*ToExpression``.

Форматы получателей в ``*Expression``-атрибутах:

- ``ivan.petrov`` — имя пользователя
- ``ivan.petrov@company.com`` — email напрямую
- ``GROUP_company_accountant`` — группа (выбирается первый email)
- ``emodel/authority-group@company_accountant`` — recordRef группы
- ``emodel/person@ivan`` — recordRef пользователя
- ``${someVariable}`` — переменная процесса, содержащая любое из вышеперечисленных значений
- ``${someService.getEmails()},petya.voks`` — несколько через запятую

Приглашение в календарь (iCal)
--------------------------------

Send Task поддерживает отправку iCal-вложения (приглашения в календарь) вместе с письмом.

.. code-block:: xml

   <bpmn:sendTask
     id="Activity_meeting_invite"
     name="Приглашение на встречу по согласованию"
     ecos:notificationType="EMAIL_NOTIFICATION"
     ecos:notificationTemplate="notifications/template@contract-meeting-notification"
     ecos:notificationTo="[&quot;initiator&quot;]"
     ecos:notificationToExpression="[]"
     ecos:notificationCc="[]"
     ecos:notificationCcExpression="[]"
     ecos:notificationBcc="[]"
     ecos:notificationBccExpression="[]"
     ecos:notificationLang="ru"
     ecos:notificationSendCalendarEvent="true"
     ecos:notificationCalendarEventSummary="Встреча по согласованию договора"
     ecos:notificationCalendarEventDescription="Необходимо согласовать договор №${docNum}"
     ecos:notificationCalendarEventOrganizer="{&quot;role&quot;:&quot;initiator&quot;}"
     ecos:notificationCalendarEventDate="${meetingDate}"
     ecos:notificationCalendarEventDuration="PT1H"
     ecos:notificationAdditionalMeta="{}">
   </bpmn:sendTask>

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Атрибут
     - Описание
   * - ``ecos:notificationSendCalendarEvent``
     - Включить отправку calendar invite: ``true`` / ``false``.
   * - ``ecos:notificationCalendarEventSummary``
     - Название события в календаре. Поддерживает expression: ``${someVar}``.
   * - ``ecos:notificationCalendarEventDescription``
     - Описание события. Поддерживает expression: ``${someVar}``.
   * - ``ecos:notificationCalendarEventOrganizer``
     - Организатор. JSON-объект с полем ``role`` или ``expression``.

       - По роли: ``{"role": "initiator"}``
       - По выражению: ``{"expression": "ivan.petrov@company.com"}``

       Если роль содержит несколько пользователей, берётся первый email.
   * - ``ecos:notificationCalendarEventDate``
     - Дата начала события. Переменная процесса типа ``Instant`` или ISO 8601-строка.
       Пример: ``${meetingDate}`` или ``2025-12-01T10:00:00Z``.
       При создании события используется часовой пояс организатора.
   * - ``ecos:notificationCalendarEventDateExpression``
     - Альтернатива ``ecos:notificationCalendarEventDate`` — expression для вычисления даты.
       Должно вернуть ``java.util.Date``, ``String (ISO 8601)`` или ``null``.
   * - ``ecos:notificationCalendarEventDuration``
     - Длительность события в формате `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.
       Примеры: ``PT15S``, ``PT1H30M``, ``P14D``.
   * - ``ecos:notificationCalendarEventDurationExpression``
     - Альтернатива ``ecos:notificationCalendarEventDuration`` — expression для длительности.

Шаблон уведомления
-------------------

Ссылка на шаблон задаётся в атрибуте ``ecos:notificationTemplate`` в формате:

.. code-block:: text

   notifications/template@<template-id>

Где ``<template-id>`` — идентификатор шаблона, совпадающий с именем директории артефакта.

Подробно о создании шаблонов — см. :ref:`Шаблоны уведомлений<notification_templates>`.

Переменные шаблона
------------------

В шаблоне доступны:

1. **Атрибуты документа** — резолвятся по полю ``model`` метафайла шаблона.
2. **Переменные процесса** — через ``$process.<имя переменной>`` в ``model``.
3. **Переменные события** (для event sub-process) — через ``$process.event.<атрибут>``.
4. **Контекстные переменные**:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Выражение в ``model``
     - Описание
   * - ``$now``
     - Текущая дата и время.
   * - ``$user``
     - Текущий пользователь системы.
   * - ``$process.webUrl``
     - URL процесса.
   * - ``$process.someVar``
     - Переменная процесса ``someVar``.
   * - ``$process.event.text``
     - Атрибут события, запустившего уведомление. Например, текст комментария.
   * - ``$process.event._meta.id``
     - ID события.
   * - ``$process.event._meta.type``
     - Тип события.
   * - ``$process.currentRunAsUser``
     - Пользователь, от имени которого выполняется процесс.
   * - ``$str.<КОНСТАНТА>``
     - Строковая константа без вычисления. Например: ``$str.APPROVED`` → ``"APPROVED"``.

Пример ``model`` для уведомления по событию добавления комментария:

.. code-block:: json

   {
     "documentDisp":    ".disp",
     "documentCreated": "_created",
     "now":             "$now",
     "user":            "$user",
     "commentText":     "$process.event.text",
     "eventType":       "$process.event._meta.type",
     "currentRunAsUser": "$process.currentRunAsUser"
   }

Для прикрепления вложений из события (например, файлов из комментария):

.. code-block:: json

   {
     "_attachments": "$process.event.attachments[]._as.ref._content{bytes,meta:?json}"
   }

Дополнительная модель (additional meta)
----------------------------------------

Через ``ecos:notificationAdditionalMeta`` можно передать дополнительные данные в шаблон,
не извлекая их из документа или процесса через ``model``.

- Ключ — имя переменной, доступной в шаблоне.
- Значение:

  - Если начинается с ``!str_`` — символы после префикса передаются как строка-константа.
  - Иначе — строка считается recordRef, и платформа пытается загрузить атрибуты по этому ref.

Пример:

.. code-block:: json

   {
     "myConstant": "!str_someValue",
     "relatedDoc":  "emodel/some-type@some-id"
   }

В шаблоне ``${myConstant}`` вернёт ``someValue``.

