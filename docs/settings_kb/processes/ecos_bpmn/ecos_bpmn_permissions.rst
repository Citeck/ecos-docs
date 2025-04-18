Управление правами в BPMN разделе
=================================

.. _bpmn_permissions:

.. contents:: 

Настройка прав
------------------

.. note:: 

      Настраивать права для разделов могут только системные администраторы (пользователи из группы **ECOS_ADMINISTRATORS**).

Права можно настраивать для каждого раздела отдельно. Для этого необходимо открыть страницу редактора бизнес-процессов:

.. code-block::

      https://{host}/admin?type=BPM

И напротив необходимого раздела нажать кнопку действий и выбрать **Редактировать права**:

 .. image:: _static/permissions_1.png
       :width: 400
       :align: center

выводится окно настройки:

 .. image:: _static/permissions_2.png
       :width: 600
       :align: center

в котором можно настроить права для группы и людей, включить или выключить наследование следующих прав:

 .. image:: _static/permissions_3.png
       :width: 400
       :align: center

Права на типы
--------------

При создании и редактировании процессов часто требуется вносить изменения в конфигурацию типов. Чтобы разрешить редактирование и создание для пользователей без прав системного администратора следует настроить права на родительских типах как описано в статье :ref:`Настройка прав для описания типов<data_type_rights>`

Пример вариантов настроек:

      1. Настроить права на тип **"base"** и дать пользователям доступ на создание и редактирование любых типов.
      2. Настроть права на тип **"user-base"** и дать пользователям доступ на создание и редактирование только бизнес-типов.
      3. Создать отдельный прокси-тип унаследованный от одного из стандартных (case/data-list/document/doclib-file и т.д.) и выдать права только на него.

Общие правила распределения прав по разделам
---------------------------------------------

Все разделы принадлежат к дереву с одним корнем - корневым разделом. Права наследуются от родителя к дочерним разделам и от разделов к вложенным процессам.

Если при настройке прав у раздела убрать флаг **"Наследовать права"**, то права не будут наследоваться.

Права на дочерних сущностях плюсуются к правам родительских, если включено наследование прав.

Корневой раздел
----------------

Корневой раздел имеет идентификатор **ROOT** и служит для настройки прав по умолчанию для всех остальных разделов.

Корневой раздел виден только администраторам системы (пользователям в группе **ECOS_ADMINISTRATORS**).

В корневом разделе нельзя создавать подразделы через действия напротив этого раздела. Для создания новых разделов в корне следует использовать кнопку **"+"** над всеми разделами:

Права по умолчанию для корневого раздела BPMN
----------------------------------------------

 .. image:: _static/permissions_4.png
       :width: 600
       :align: center

.. list-table::
      :widths: 3 5
      :header-rows: 1
      :align: center
      :class: tight-table 
      
      * - Группа
        - Права
      * - **bp-administrator**
        - | read
          | write
          | bpmn-process-def-deploy
          | bpmn-process-def-report-view
          | bpmn-process-instance-run
          | bpmn-process-instance-edit
          | bpmn-process-instance-read
          | bpmn-process-instance-migrate
          | bpmn-section-edit-process-def
      * - **bp-manager**
        - | read
          | bpmn-process-def-report-view
      * - **bp-developer**
        - | read
          | bpmn-process-def-deploy
          | bpmn-process-instance-run
          | bpmn-process-def-report-view
          | bpmn-process-instance-migrate
      * - **bp-viewer**
        - | read

Описание BPMN прав
-------------------

.. list-table::
      :widths: 5 5 10
      :header-rows: 1
      :align: center
      :class: tight-table 

      * - Идентификатор
        - Название
        - Описание
      * - **read**
        - Право на чтение (read)
        - Будет ли виден пользователю раздел и все процессы в нем.
      * - **write**
        - Право на изменение (write)
        - Можно ли редактировать раздел и процессы в нем 
      * - **bpmn-section-create-process-def**
        - Создание процессов в разделе
        - Можно ли создавать новые процессы в разделе
      * - **bpmn-section-create-subsection**
        - Создание подразделов
        - Можно ли создавать подразделы внутри раздела
      * - **bpmn-section-edit-process-def**
        - Редактирование процессов в разделе
        - Можно ли редактировать процессы в разделе
      * - **bpmn-process-def-deploy**
        - Деплой процесса
        - Можно ли публиковать описание процеса в BPMN движок
      * - **bpmn-process-def-report-view**
        - Просмотр отчета
        - Можно ли просматривать статистику по процессу
      * - **bpmn-process-instance-read**
        - Просмотр экземпляра процесса
        - Можно ли просматривать экземпляры процесса
      * - **bpmn-process-instance-edit**
        - Редактирование экземпляра процесса
        - Можно ли редактировать экземпляры процесса
      * - **bpmn-process-instance-migrate**
        - Миграция экземпляра процесса
        - Можно ли мигрировать экземпляры процесса
      * - **bpmn-process-instance-run**
        - Ручной запуск экземпляра бизнес-процесса
        - Можно ли запускать вручную новые экземпляры процесса



