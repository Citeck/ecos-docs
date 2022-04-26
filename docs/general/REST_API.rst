====================================================
**Управление маршрутами и группами через REST API**
====================================================

Для обеспечения корректной отправки http-запросов произведите настройки в соответствии со  `статьей  <https://citeck-ecos.readthedocs.io/ru/latest/admin/keycloack_postman.html>`_

Управление маршрутами 
----------------------


Получение списка маршрутов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**URL:** 

.. code-block::

    {{host}}/gateway/api/records/query

**TYPE:** POST 

**Запрос:** 

.. code-block::

    {"query":{
        "sourceId":"alfresco/",
        "query":{
            "att":"_type",
            "val":"emodel/type@ssgedidl-routeTemplateItem",
            "t":"eq"
            },
            "language":"predicate",
            "page":{"skipCount":0,"maxItems":10,"page":1},
            "consistency":"EVENTUAL",
            "sortBy":[{"attribute":"cm:created","ascending":false}]},
            "attributes":["ssgedidl:rtCode?disp"]
    }

Блок **“page”** и **“sortBy”** не обязательные параметры. 
Пагинация настраивается параметром **“page”**.
В **Attributes** указывают параметры, которые хотим получить на выходе. Можно не указывать параметры в **Attributes** или убрать данный блок, и на выходе получим список Id записей

**Ответ:** 

.. code-block::
    
    {
        "records": [
            {
                "id": "alfresco/@workspace://SpacesStore/820f88b5-e722-4bc0-933f-926d57e728aa",
                "attributes": {
                    "ssgedidl:rtCode?disp": "1"
                }
            }
        ],
        "errors": [],
        "hasMore": false,
        "totalCount": 1
    }


Получение иерархии по уровням 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**URL:** 

.. code-block::

 {{host}}/gateway/alfresco/alfresco/s/api/orgstruct/v2/group/_orgstruct_home_/children?addAdminGroup=true&branch=true&excludeAuthorities=&group=true&role=true&user=true

**TYPE:** GET

**Ответ:** 

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


**URL:** 

.. code-block::

    {{host}}/gateway/api/records/mutate

**TYPE:** POST 

**Запрос:** 

.. code-block::

    {"records":
    [{
        "id":"alfresco/@workspace://SpacesStore/820f88b5-e722-4bc0-933f-926d57e728aa", -- ID маршрута
        "attributes":{
            "ssgedidl:templateRouteSignerAssoc?str":"workspace://SpacesStore/15d05def-45fd-41cf-bf8d-96ecd422edea", - этап, на который необходимо добавить пользователя/группу (указать ID пользователя/группы), если необходимо удалить с этапа, то указать “”
            "_state?str":"submitted"}}
    ]}
 
**Ответ:** 

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
-------------------------------------


Просмотр списка пользователей
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**URL:** 

.. code-block::

    {{host}}/gateway/api/records/query

**TYPE:** POST 

**Запрос:** 

.. code-block::

    {"query":{
        "query":{
        "t":"and",
        "val":[{"t":"eq","att":"TYPE","val":"cm:person"}]},
        "language":"predicate",
        "consistency":"EVENTUAL",
        "page":{"maxItems":10,"skipCount":0}},
        "attributes":{"fullName":".disp","userName":"userName"}
    }

**Ответ:** 

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


Получения списка групп, в которой состоит пользователь
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**URL:** 

.. code-block::

    {{host}}/gateway/api/records/query

**TYPE:** POST 

**Запрос:** 

.. code-block::

    {"records":
        ["people@admin"],
        "attributes":
            ["groups[]"]
    }

**Ответ:** 

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
   

*Для старой версии оргструктуры и групп:*


**URL:** 

.. code-block::

    {{host}}/gateway/alfresco/alfresco/s/api/groups?sortBy=displayName&zone=APP.DEFAULT&shortNameFilter=*&maxItems=50&skipCount=0

**TYPE:** GET 

**Ответ:** 

.. code-block::

    {
        "data": [
            {
                "authorityType": "GROUP",
                "shortName": "_orgstruct_home_",
                "fullName": "GROUP__orgstruct_home_",
                "displayName": "_orgstruct_home_",
                "url": "/api/groups/_orgstruct_home_",
                "zones": [
                    "APP.DEFAULT",
                    "AUTH.ALF"
                ]
            }
        ],
        "paging": {
            "maxItems": 50,
            "skipCount": 0,
            "totalItems": 1,
            "totalItemsRangeEnd": null,
            "confidence": "exact"
        }
    }
   

Удаление/добавление пользователя в группу
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**URL:** 

.. code-block::

    {{host}}/gateway/api/records/mutate

**TYPE:** POST 

**Запрос:** 

.. code-block::

    {"records":[
        {
        "id":"emodel/person@admin",
        "attributes":{
            "att_add_authorityGroups":"emodel/authority-group@GROUP_company_accountancy"
    }}]} 

**att_add_authorityGroups** – добавление в группу

**att_rem_authorityGroups** – удаление из группы


*Для старой версии оргструктуры и групп:*

**Добавление**


**URL:** 

.. code-block::

    {{host}}/gateway/alfresco/alfresco/s/api/groups/{GROUP_NAME}/children/{USER_NAME}

**TYPE:** POST 

**Ответ:** 

.. code-block::

    {{host}}/gateway/alfresco/alfresco/s/api/groups/ssg-edi-ip-technologist/children/fet

**Удаление**

**URL:** 

.. code-block::

    {{host}}/gateway/alfresco/alfresco/s/api/groups/{GROUP_NAME}/children/{USER_NAME}

**TYPE:** DELETE


Просмотр содержимого группы
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Просмотр пользователей в группе
"""""""""""""""""""""""""""""""""


**URL:** 

.. code-block::

    {{host}}/gateway/api/records/query

**TYPE:** POST 

**Запрос:** 

.. code-block::

    {"query":{
        "sourceId": "emodel/person",
            "query": {"t": "contains", "a": "authorityGroups", "v": "emodel/authority-group@orders-technologist"},
        "language": "predicate"
    }}

**Ответ:** 

.. code-block::

    {
        "records": [
            "emodel/person@admin"
        ],
        "errors": [],
        "hasMore": false,
        "totalCount": 1
    }


Просмотр групп в группах
"""""""""""""""""""""""""""
Просмотр групп в группе аналогичен просмотру пользователей в группе, но **sourceId** равен **“emodel/authority-group“**.

Просмотр пользователей или групп с учетом иерархии вниз (т.е. указываем корень оргструктуры или любую другую группу, но так же ищем и во всех подгруппах) - то же что и просмотр пользователей в группе, но вместо **“authorityGroups”** использовать **“authorityGroupsFull“**

*Для старой версии оргструктуры и групп:*


**URL:** 

.. code-block::

    {{host}}/gateway/alfresco/alfresco/s//api/groups/{GROUP_NAME}/children?sortBy=displayName&maxItems=50&skipCount=0

**TYPE:** GET 

**Ответ:** 

.. code-block::

        {
        "data": [
            {
                "authorityType": "USER",
                "shortName": "admin",
                "fullName": "Administrator ",
                "displayName": "Administrator ",
                "url": "/api/people/admin"
            }
        ],
        "paging": {
            "maxItems": 50,
            "skipCount": 0,
            "totalItems": 1,
            "totalItemsRangeEnd": null,
            "confidence": "exact"
        }
    }
