Примеры использования Records API для внешних систем
======================================================

.. _API_examples:

.. contents::
   :depth: 3

API-интерфейс позволяет работать с данными системы ECOS в привычном интерфейсе вашей информационной системы. 

С помощью Records API вы можете выполнять любые действия с данными, которые хранятся в любом из микросервисов ECOS. Подробнее про :ref:`Records API <Records_API>`

Примеры использования API:

* получение и изменение информации о маршрутах; 
* управление набором и составом групп пользователей.

.. important::
 
 Для обеспечения корректной отправки http-запросов произведите настройки аутентификации в соответствии со :ref:`статьей <keycloak_postman>`


Поиск и скачивание документа
-----------------------------

.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center
      
      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/api/records/query

      * - **Type**
        -  POST 
      * - **Запрос**
        -   
           .. code-block::

              {
                "query": {
                  "sourceId": "emodel/aro-internal-type",
                  "query": {
                    "att": "_status",
                    "t": "eq",
                    "val": "new"
                  },
                  "language": "predicate"
                },
                "attributes": [
                  "_content.url"
                ]
              }


      * - **Ответ**
        -  
           .. code-block::

              {
                "records": [
                  {
                    "id": "emodel/aro-internal-type@86edb336-7816-41fa-9809-680a077e0b5e",
                    "attributes": {
                      "_content.url": "/gateway/emodel/api/ecos/webapp/content?ref=aro-internal-type%4086edb336-7816-41fa-9809-680a077e0b5e&att=content"
                    }
                  },
                  {
                    "id": "emodel/aro-internal-type@dde85aac-e875-471c-a44d-a4135fc7c56a",
                    "attributes": {
                      "_content.url": "/gateway/emodel/api/ecos/webapp/content?ref=aro-internal-type%40dde85aac-e875-471c-a44d-a4135fc7c56a&att=content"
                    }
                  }
                ],
                "errors": [],
                "hasMore": false,
                "totalCount": 2
              }

Далее сделать GET запрос для скачивания контента:

.. code-block::

    GET {{host}}/gateway/emodel/api/ecos/webapp/content?ref=aro-internal-type%40dde85aac-e875-471c-a44d-a4135fc7c56a&att=content

Скачивание документа
---------------------

.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center
      
      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/api/records/query

      * - **Type**
        -  POST 
      * - **Запрос**
        -   
           .. code-block::

              {
                "records": [
                  "emodel/aro-internal-type@e3b81a2b-cdc9-42bc-abbc-a6a564aedbb8"
                ],
                "attributes": [
                  "_content.url"
                ]
              }

      * - **Ответ**
        -  
           .. code-block::

              {
                  "records": [
                      {
                          "id": "emodel/aro-internal-type@e3b81a2b-cdc9-42bc-abbc-a6a564aedbb8",
                          "attributes": {
                              "_content.url": "/gateway/emodel/api/ecos/webapp/content?ref=aro-internal-type%40e3b81a2b-cdc9-42bc-abbc-a6a564aedbb8&att=content"
                          }
                      }
                  ],
                  "errors": []
              }   

Далее сделать GET запрос для скачивания контента:

.. code-block::

    GET {{host}}/gateway/emodel/api/ecos/webapp/content?ref=aro-internal-type%40e3b81a2b-cdc9-42bc-abbc-a6a564aedbb8&att=content

Управление маршрутами
---------------------

Получение списка маршрутов
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center

      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/api/records/query

      * - **Type**
        -  POST 
      * - **Запрос**
        -   
           .. code-block::

            {"query":{
                "sourceId":"alfresco/",
                "query":{
                    "att":"_type",
                    "val":"emodel/type@testdl-routeTemplateItem",
                    "t":"eq"
                    },
                    "language":"predicate",
                    "page":{"skipCount":0,"maxItems":10,"page":1},
                    "consistency":"EVENTUAL",
                    "sortBy":[{"attribute":"cm:created","ascending":false}]},
                    "attributes":["testdl:rtCode?disp"]
            }

      * - **Ответ**
        -  
         .. code-block::
    
            {
                "records": [
                    {
                        "id": "alfresco/@workspace://SpacesStore/820f88b5-e722-4bc0-933f-926d57e728aa",
                        "attributes": {
                            "testdl:rtCode?disp": "1"
                        }
                    }
                ],
                "errors": [],
                "hasMore": false,
                "totalCount": 1
            }

Получение иерархии по уровням 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center

      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/alfresco/alfresco/s/api/orgstruct/v2/group/_orgstruct_home_/children?addAdminGroup=true&branch=true&excludeAuthorities=&group=true&role=true&user=true

      * - **Type**
        -  GET
      * - **Ответ**
        -  
         .. code-block::
            
            [
                {
                    "nodeRef": "workspace://SpacesStore/03094bf2-1395-4ded-98ff-3aba20698260",
                    "fullName": "GROUP_all",
                    "shortName": "all",
                    "displayName": "Все пользователи",
                    "authorityType": "GROUP",
                    "groupType": "branch",
                    "groupSubType": "company"
                },
                {
                    "nodeRef": "workspace://SpacesStore/6ac1289b-45c6-43b5-ad95-fdbbe1302d69",
                    "fullName": "GROUP_company",
                    "shortName": "company",
                    "displayName": "Организация",
                    "authorityType": "GROUP",
                    "groupType": "branch",
                    "groupSubType": "company"
                }
            ]

Изменение маршрута (Добавление/удаление пользователей/группы в маршрут)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center

      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/api/records/mutate

      * - **Type**
        -  POST 
      * - **Запрос**
        -   
           .. code-block::

                {
                    "records": [
                        {
                            "id":"alfresco/@workspace://SpacesStore/820f88b5-e722-4bc0-933f-926d57e728aa", // ID маршрута
                            "attributes":{
                                "testdl:templateRouteSignerAssoc?str":"workspace://SpacesStore/15d05def-45fd-41cf-bf8d-96ecd422edea", // этап, на который необходимо добавить пользователя/группу (указать ID пользователя/группы), если необходимо удалить с этапа, то указать “”
                                "_state?str":"submitted"
                                         }
                        }
                               ]
                }
 
      * - **Ответ**
        -  
         .. code-block::
    
            {
                "records": [
                    {
                        "id": "alfresco/@workspace://SpacesStore/820f88b5-e722-4bc0-933f-926d57e728aa",
                        "attributes": {}
                    }
                ],
                "errors": []
            }

Управление набором и составом групп 
------------------------------------

Просмотр списка пользователей
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center

      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/api/records/query

      * - **Type**
        -  POST 
      * - **Запрос**
        -   
           .. code-block::

            {
                "query":{
                    "query":{
                    "t":"and",
                    "val":[{"t":"eq","att":"TYPE","val":"cm:person"}]},
                    "language":"predicate",
                    "consistency":"EVENTUAL",
                    "page":{"maxItems":10,"skipCount":0}},
                    "attributes":{"fullName":".disp","userName":"userName"}
                }
 
      * - **Ответ**
        -  
         .. code-block::
    
            {
            "records": [
                {
                    "id": "alfresco/@workspace://SpacesStore/e0d4333e-97e1-4d42-a4d0-83e4259ed936",
                    "attributes": {
                        "fullName": "Guest",
                        "userName": "guest"
                    }
                },
                {
                    "id": "alfresco/@workspace://SpacesStore/6985ba61-155a-4ae8-aeb3-28acbc59f5f4",
                    "attributes": {
                        "fullName": "system",
                        "userName": "system"
                    }
                },
                {
                    "id": "alfresco/@workspace://SpacesStore/15d05def-45fd-41cf-bf8d-96ecd422edea",
                    "attributes": {
                        "fullName": "Administrator",
                        "userName": "admin"
                    }
                }
            ],
            "errors": [],
            "hasMore": false,
            "totalCount": 3
                }

Получение списка групп, в которой состоит пользователь
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center
      
      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/api/records/query

      * - **Type**
        -  POST 
      * - **Запрос**
        -   
           .. code-block::

            {"records":
                ["people@admin"],
                "attributes":
                    ["groups[]"]
            }

      * - **Ответ**
        -  
           .. code-block::
    
            {
            "records": [
                {
                    "id": "people@admin",
                    "attributes": {
                        "groups[]": [
                            "ALFRESCO_ADMINISTRATORS",
                            "ALFRESCO_MODEL_ADMINISTRATORS" 
                        ]
                    }
                }
            ],
            "errors": []
            }


Удаление/добавление пользователя в группу
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center
      
      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/api/records/mutate

      * - **Type**
        -  POST 
      * - **Запрос**
        -   
           .. code-block::

                {"records":[
                    {
                    "id":"emodel/person@someuser",
                    "attributes":{
                        "att_add_authorityGroups":"emodel/authority-group@GROUP_company_accountancy"
                }}]} 


* **att_add_authorityGroups** – добавление в группу
* **att_rem_authorityGroups** – удаление из группы


Просмотр содержимого группы
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Просмотр пользователей в группе
""""""""""""""""""""""""""""""""
.. list-table:: 
      :widths: 5 40 
      :class: tight-table
      :align: center
      
      * - **URL**
        - 
         .. code-block::

            {{host}}/gateway/api/records/query

      * - **Type**
        -  POST 
      * - **Запрос**
        -   
           .. code-block::

                {"query":{
                    "sourceId": "emodel/person",
                        "query": {"t": "contains", "a": "authorityGroups", "v": "emodel/authority-group@orders-technologist"},
                    "language": "predicate"
                }}

      * - **Ответ**
        -  
           .. code-block::
    
                {
                    "records": [
                        "emodel/person@someuser"
                    ],
                    "errors": [],
                    "hasMore": false,
                    "totalCount": 1
                }


Просмотр групп в группах
"""""""""""""""""""""""""
Просмотр групп в группе аналогичен просмотру пользователей в группе, но **sourceId** равен **“emodel/authority-group“**.

Просмотр пользователей или групп с учетом иерархии вниз (т.е. указать корень оргструктуры или любую другую группу, но так же ищется и во всех подгруппах) - то же что и просмотр пользователей в группе, но вместо ``authorityGroups`` использовать ``authorityGroupsFull``

.. list-table:: Таблица 1 Описание полей
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Поле
        - Наименование
      * - **fullName**
        - Полное наименование 
      * - **shortName**
        - Сокращенное наименование
      * - **id**
        - ID записи
      * - **nodeRef**
        - Ссылка на запись в системе Citeck
      * - **displayName**
        - Отображаемое наименование
      * - **authorityType**
        - Тип полномочий User/Group
      * - **groupType**
        - Тип группы 
      * - **groupSubType**
        - Тип подгруппы
      * - **userName**
        - Логин
      * - **templateRouteSignerAssoc**
        - Этап, на который необходимо добавить пользователя/группу (указать ID пользователя/группы), если необходимо удалить с этапа указать “”
      * - **att_add_authorityGroups**
        - | att_add_authorityGroups – добавление в группу
          | att_rem_authorityGroups – удаление из группы
      * - **rtCode**
        - Код шаблона
      * - **_state**
        - Тип состояния
      * - **errors**
        - Значение ошибки, если при запросе она произошла
      * - **hasMore**
        - Есть ли дальше рекорды (записи)
      * - **totalCount**
        - Общее количество найденных записей
      * - **disp**
        - Значение для вывода 
      * - **value**
        - Значение

.. list-table:: Таблица 2 Описание параметров
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Параметр
        - Значение
      * - **Блок “page”**
        - | Параметр для настройки пагинации. 
          | Необязательный параметр.
      * - **Блок “sortBy”**
        - | Параметр для сортировки.
          | Необязательный параметр.
      * - **Блок “attributes“**
        - | Параметры (см. Таблица 1), которые необходимо получить на выходе. 
          | Необязательный параметр.
          | Можно не указывать параметры в “attributes“ или убрать данный блок и на выходе получить список Id записей.
      * - **sourceId**
        - | Источник данных для поиска. В данном случае alfresco. 
          | Возможные варианты: 
          | •	reports-data 
          | •	alfresco
      * - **query**
        - Необходимый predicate query для поиска записей
      * - **att**
        - Название аттрибута
      * - **val**
        - Значение
      * - **t**
        - | Типы предикатов.
          | Возможные варианты: 
          | •	starts
          | •	ends
          | •	or
          | •	and
          | •	empty	
          | •	not
          | •	eq
          | •	gt
          | •	ge
          | •	lt
          | •	le
          | •	like
          | •	in
          | •	contains
      * - **language**
        - Язык запроса. На текущий момент поддерживается только predicate
      * - **consistency**
        - | Консистенция (Согласованность)
          | Возможные варианты: 
          | •	EVENTUAL
          | •	TRANSACTIONAL
          | •	DEFAULT
          | •	TRANSACTIONAL_IF_POSSIBLE

Внесение изменений в запись
-----------------------------

.. code-block::

  {
    "records": [
      {
        "id":  "alfresco/@workspace://SpacesStore/10a8c2e8-2c14-4c64-83b3-06b8bfc45006", //id workspace, в который данные необходимо добавить
        "attributes": {
          "testpkg: poAssoc?assoc": [ 
            "dict@testpkg:po-alias-4" // alias должен быть уникальным в пределах запроса, можно задать константой
          ]
        }
      },	
      {
        "id": "dict@testpkg: po",
        "attributes": {
          "_alias?str": "dict@testpkg:po-alias-4",
          "testpkg:poValue?str": "1234567890",
          "testpkg: poPpsDate?str":"2023-05-19T00:00:00Z",
          "_state?str": "submitted",
          "_formInfo?json": {
            "submitName": {
              "en": "Cохранить"
            }
            "formId": "testpkg-po-form"		
          }
        }
      }
    ]
  }

Добавление данных
------------------

.. code-block::

  {
    "records": [
      {
        "id":  "alfresco/@workspace://SpacesStore/10a8c2e8-2c14-4c64-83b3-06b8bfc45006", 
        "attributes": {
          "att_add_testpkg: poAssoc?assoc": [
            "dict@testpkg:po-alias-4"
          ]
        }
      },	
      {
        "id": "dict@testpkg: po",
        "attributes": {
          "_alias?str": "dict@testpkg:po-alias-4",
          "testpkg:poValue?str": "1234567890",
          "testpkg: poPpsDate?str":"2023-05-19T00:00:00Z",
          "_state?str": "submitted",
          "_formInfo?json": {
            "submitName": {
              "en": "Cохранить"
            }
            "formId": "testpkg-po-form"		
          }
        }
      }
    ]
  }

Отправка запроса в Alfresco-FTS
------------------------------------

Для отправки запроса в Alfresco (Alfresco-FTS) через Records в URL указывать:

**URL** -  https://{{host}}/gateway/api/records/query 

**body**

.. code-block::

  {
    "query": {
          "sourceId": "alfresco/",
          "language": "fts-alfresco",
          "query": "{{fts-query}}"
      },
      "version": 1
  }

