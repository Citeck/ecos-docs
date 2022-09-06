Apps microservice
==================

Платформа Citeck ECOS строится на базе артефактов, позволяя расширять функционал написанием новых артефактов, не затрагивая уже существующий функционал.

Артефакт означает единицу конфигурации системы ECOS. Примером артефактов  являются: форма, журнал, тип, раздел, матрица прав, действие и др.

Уровень модулей Alfresco в новой архитектуре называется Application. Микросервис, который управляет деплоем приложений и артефактов ECOS называется ECOS Applications или сокращенно ecos-apps.

Цели микросервиса ECOS Apps:

1. Версионирование артефактов . Все меняющиеся артефакты сохраняются как отдельные ревизии без возможности изменения.

2. Доставка артефактов  от всех микросервисов к целевому (например, доставка форм из ecos-integrations, ecos-model, alfresco в ecos-uiserv).

3. Отслеживание зависимостей. Если артефакт зависит от другого артефакта, то ECOS Apps соблюдает порядок деплоя.

4. Управление патчами для артефактов.

Процесс деплоя артефактов выглядит примерно следующим образом:

Простое описание:
------------------

 .. image:: _static/apps_1.png
       :width: 400
       :align: center

После появления в сети нового приложения (на схеме это alfresco) происходит 3 этапа:

1. Запрос типов.

2. Получение артефактов.

3. Деплой артефактов.

Подробное описание:
--------------------

Микросервис периодически опрашивает всех кто подключен к Rabbit MQ

 .. image:: _static/apps_2.png
       :width: 400
       :align: center

1. Пока к Rabbit'у никто не подключился ничего не происходит

2. Когда появляется первый микросервис он возвращает ответ в ECOS Apps о своем присутствии
   
 .. image:: _static/apps_3.png
       :width: 400
       :align: center

3. После этого ECOS Apps отправляет запрос на типы, в которых заинтересован микросервис. 

Получив список типов ECOS Apps отправляет всем зарегистрировавшимся микросервисам запрос на получение артефактов.

 .. image:: _static/apps_4.png
       :width: 400
       :align: center

4. Получив необходимые артефакты ECOS Apps проверяет поменялись или они с прошлой загрузки и если нет, то ничего не делает. 

Если выясняется, что артефакты поменялись, то они отправляются в целевой микросервис на деплой.

Все взаимодействие происходит посредством Rabbit MQ и библиотеки ecos-commands.

Лог ECOS Apps при обнаружении трех микросервисов (включая себя): 

.. code-block::

    Detected new application 'eapps' with EcosApps: [EcosAppInfo(id=eapps, lastChanged=1584425736433)]
    // Обнаржено новое приложение (микросервис). eapps не содержит типов артефактов. Поэтому грузить нечего
    Detected new application 'uiserv' with EcosApps: [EcosAppInfo(id=uiserv, lastChanged=1584425751061)]
    // В uiserv уже есть 4 типа (форма, дашборд, действие и меню). Мы должны пройтись по всем зарегистрированным микросервисам и опросить есть ли у них модули с такими типами:
    Loaded 1 modules from 'eapps' EcosApp: 'eapps' type: 'ui/form'
    // нашли одну форму в eapps 
    Loaded 1 modules from 'eapps' EcosApp: 'eapps' type: 'ui/action'
    // нашли одно действие в eapps
    Loaded 0 modules from 'eapps' EcosApp: 'eapps' type: 'ui/menu'
    Loaded 0 modules from 'eapps' EcosApp: 'eapps' type: 'ui/dashboard'
    Loaded 3 modules from 'uiserv' EcosApp: 'uiserv' type: 'ui/form'
    // нашли 3 формы в uiserv (локальные артефакты тоже деплоятся через ECOS Apps)
    Loaded 7 modules from 'uiserv' EcosApp: 'uiserv' type: 'ui/action'
    Loaded 0 modules from 'uiserv' EcosApp: 'uiserv' type: 'ui/menu'
    Loaded 4 modules from 'uiserv' EcosApp: 'uiserv' type: 'ui/dashboard'
    Modules count was changed by target app. Before: 4 After: 1
    // мы отправили в uiserv изменившиеся артефакты, но он отказался принимать 3 из них (защита от перезатирания конфигурации, которую настроили на стенде)
    Detected new application 'emodel' with EcosApps: [EcosAppInfo(id=emodel, lastChanged=1584425829184)]
    Loaded 0 modules from 'eapps' EcosApp: 'eapps' type: 'model/section'
    Loaded 0 modules from 'eapps' EcosApp: 'eapps' type: 'model/type'
    Loaded 0 modules from 'uiserv' EcosApp: 'uiserv' type: 'model/section'
    Loaded 1 modules from 'uiserv' EcosApp: 'uiserv' type: 'model/type'
    Loaded 0 modules from 'emodel' EcosApp: 'emodel' type: 'model/section'
    Loaded 3 modules from 'emodel' EcosApp: 'emodel' type: 'model/type'
    Loaded 3 modules from 'emodel' EcosApp: 'emodel' type: 'ui/form'
    Loaded 0 modules from 'emodel' EcosApp: 'emodel' type: 'ui/action'
    Loaded 0 modules from 'emodel' EcosApp: 'emodel' type: 'ui/menu'
    Loaded 0 modules from 'emodel' EcosApp: 'emodel' type: 'ui/dashboard'


Полезные скрипты (EApps)
------------------------

Для получения всех артефактов по типу можно выполнить следующий скрипт:

.. code-block::

      Citeck.Records.query({
      sourceId: 'eapps/module',
            query: {
                  type: 'form'
            },
            page: {maxItems: 100} 
      }).then(console.log);

В результате выполнения в консоль выведется список id артефактов.

Имея id артефакта, его можно удалить следующим скриптом:

.. code-block::

      Citeck.Records.remove(["eapps/module@form$3784f71c-5557-4123-b751-84e38c6157a1"]);

Получение содержимого модулей из базы eapps
--------------------------------------------

Получаем список ревизий по ext_id и типу артефакта:

.. code-block::

      select module.ext_id,rev.created_date,rev.created_by,rev.content_id
      from ecos_module module 
      join ecos_module_rev rev on module.id=rev.module_id 
      where module.ext_id='ECOS_FORM' and module.type='ui/form';

Смотрим на поле **content_id** нужных модулей и делаем следующий запрос:

.. code-block::

      select id,encode(data, 'base64') from ecos_content where id=14809;

Получаем:

.. code-block::

       id   |                                    encode                                    
      -------+------------------------------------------------------------------------------
      11448 | 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
            | AQBFAAAAmQgAAAAA

Убираем шапку, отступы ``|``, переносы строк, знаки + в конце строк и получаем строку:

.. code-block::

      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

Загружаем полученную строку в любой сервис по декодированию base64 в файл. Например:

`https://base64.guru/converter/decode/file <https://base64.guru/converter/decode/file>`_

Скачиваем итоговый файл:

 .. image:: _static/app_download.png
       :width: 400
       :align: center

В результате получаем архив с нашим модулем.

Полезные скрипты в базе ECOS Apps
----------------------------------

Получение ревизий модуля:

.. code-block::

      select module.ext_id,rev.created_date,rev.created_by,rev.is_user_rev,rev.content_id 
      from ecos_module module 
      join ecos_module_rev rev on module.id=rev.module_id 
      where module.ext_id='ECOS_FORM' order by rev.created_date desc;

**is_user_rev** флаг определяет, что модуль менялся пользователем.


