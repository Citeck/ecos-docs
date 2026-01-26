Подписка на событие Citeck
===========================

.. code-block:: yaml
  
  - route:
      from:
        uri: 'ecos-event:record-created' # подписываемся на событие "Запись создана"
        parameters:
          attributes:
            recordId: 'record?id' # указываем какие атрибуты нам нужны из события
          filter: # устанавливаем фильтр 
            t: not-eq 
            a: conditionField
            v: true
        steps:
          - to: log:record-was-created


Пример: Выполнение действий при смене статуса
------------------------------------------------

Для выполнения действий при смене статуса можно использовать подписку на события Citeck:

.. code-block:: yaml

  from:
    uri: 'ecos-event:record-status-changed'
    parameters:
      attributes:
        recordId: 'record?id'
        documents: 'record.docs:documents[]{ref:?id,typeId:_type?localId,contentSize:_content.size?num}!'
      filter:
        t: and
        val:
          - t: 'eq'
            att: 'typeDef.id'
            # id типа основного документа, за статусом которого мы следим
            val: 'SED-agreement' 
          - t: 'eq'
            att: 'after?str'
            val: 'integration-trigger' # id ожидаемого статуса

Далее можно взять список документов, через **GetRecordAttsProcessor** получить их атрибуты (включая контент) и через http компонент отправить на внешний сервис.

Полная конфигурация с комментариями представлена во вложении. Для сценария прмиера нужно поменять:

  1. beans[0] -> properties -> FILE_TYPES_TO_PROCESS:     **['scan-document'] -> ['SED-main-document']**
  2. route -> from -> parameters -> filter -> val[0] -> val:     **contract -> SED-agreement**
  3. route -> from -> parameters -> filter -> val[1] -> val:     **integration-trigger -> ваш_статус**

А так же создать :ref:`секрет<ecos_secret>` с **username/password** в журнале ``/v2/journals?journalId=ecos-secrets&viewMode=table&ws=admin$workspace``

.. code-block:: yaml

  ---
  id: file-upload-endpoint-auth
  name:
    ru: File Upload Endpoint Auth
  type: BASIC
  data:
    username: admin
    password: admin

И :ref:`конечную точку<endpoints_dsl>` с URL для загрузки файлов в журнале ``/v2/journals?journalId=endpoints&viewMode=table&ws=admin$workspace``

.. code-block:: yaml

  ---
  id: file-upload-endpoint
  name:
    ru: File Upload Endpoint
  url: http://localhost/gateway/emodel/api/ecos/webapp/content
  credentials: emodel/secret@file-upload-endpoint-auth

Если конечная точка или секрет меняются, то необходимо перезапустить Camel DSL, чтобы изменения подхватились.

:download:`Полная конфигурация с комментариями <../files/send-files-to-ext-service-camel-yaml-dsl.yaml>`