Вебхуки
========

.. _webhooks:

.. contents::
   :depth: 3

В Citeck добавлен функционал входящих вебхуков.

**Вебхук** — автоматически сгенерированный HTTP-запрос, созданный на основе события (триггера), работающий быстро и в одну сторону.

Настройки доступны в журнале **«Входящие вебхуки» (Рабочее пространство "Раздел администратора" - Интеграция)**

 .. image:: _static/webhooks/webhook_01.png
       :width: 700
       :align: center

Журнал доступен по адресу: ``v2/admin?journalId=in-webhook-journal&type=JOURNAL`` 

Расположение артефактов с данным типом: **integration/in-webhook**

Форма создания
---------------

 .. image:: _static/webhooks/webhook_02.png
       :width: 600
       :align: center

Атрибуты (in-webhook):

.. list-table::
      :widths: 5 5 10
      :align: center
      :header-rows: 1
      :class: tight-table 
      
      * - Атрибут
        - Тип
        - Описание
      * - id
        - Текст
        - id используется для создания endpoint вебхука
      * - token
        - ASSOC (secret)
        - | :ref:`Секрет<ECOS_secrets>` с типом Токен. 
          | Необходим для проверки валидности запроса. 
      * - actionType
        - Текст
        - Тип действия при запросе
      * - authParameter
        - Текст
        - | Параметр запроса, в котором хранится Токен
          | Если не задано, используется дефолтное значение **token**


Пример конфигурации:

.. code-block::

    ---
    id: bitrix24-webhook
    token: emodel/secret@bitrix24-webhook-token
    actionType: toEvent
    authParameter: auth[application_token]

При создании входящего вебхука, становится доступным отправка POST запросов по адресу

.. code-block::

    http://host/gateway/integrations/pub/webhook/${id}

**id** – id, указанный при создании вебхука.

В запросе обязательно должно присутствовать **тело (body)**.

Токен для проверки запроса должен лежать в параметре, указанном при создании вебхука.

Например:

.. code-block::

    http://host/gateway/integrations/pub/webhook/bitrix24-webhook?token=testAuthToken 

На данный момент доступно только одно Действие для вебхука -  Трансформация в Events. При обработке вебхука проверяется Токен. 

Если проверка прошла успешно, то создается :ref:`ECOS Event<ecos_events>` в стандартную очередь **ecos-events** с типом **in-webhook-request**. Event содержит в себе данные запроса:

.. code-block::

    webhookId: String
    params: Map<String, String>
    body: String

Например:

.. code-block::

    {
      "params": {"event":"ONCRMDEALADD","auth[application_token]":"123","data[FIELDS][ID]":"9"}, 
      "body":"event=ONCRMDEALADD&auth%5Bapplication_token%5D=123&data%5BFIELDS%5D%5BID%5D=9",
      "webhookId":"bitrix24-webhook"
    }

Доступ на чтение и редактирование вебхуков есть только у Администратора и Системы.

Ошибки
-------

При отправке запроса на вебхук возможны следующие ошибки:

.. list-table::
      :widths: 5 10 10
      :align: center
      :header-rows: 1
      :class: tight-table 
      
      * - Код
        - Детали
        - Комментарий
      * - 500
        - Invalid webhook id={wh_id}
        - Если запрос выполнен на несуществующий вебхук
      * - 500
        - Secret ${webhook.token} not found
        - Если неверно задан секрет в вебхуке
      * - 500
        - Authentication token is not valid
        - Если отсутствует параметр с токеном в запросе или задан неверный токен
      * - 500
        - Not found action type ${webhook.actionType}
        - Если неверно задано действие в вебхуке

Вебхук используется, например, для :ref:`синхронизации с Bitrix24<bitrix24_crm>`