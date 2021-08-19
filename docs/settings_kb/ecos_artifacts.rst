========================
**ECOS Артефакты**
========================

Определения
~~~~~~~~~~~

**Артефакт** - единица расширения системы. Примеры артефактов: :guilabel:`Тип`, :guilabel:`Форма`, :guilabel:`Журнал`.

Тип артефакта как правило состоит из двух частей разделенных символом ``/``.
Первая часть - это область системы к которой относится артефакт. Обычно за одну область отвечает один микросервис.
Вторая часть - локальный идентификатор типа
Например в типе ``ui/form`` ui - это область, а form - локальный идентификатор.

**Расположение артефактов**

Все артефакты располагаются в директориях, которые соответствуют типу.
В приложении настраивается корневая папка с артефактами и в ней можно создавать подпапки ui/form, model/type и тд.
По умолчанию корневой папкой с артефактами является ``src/main/resources/eapps/artifacts``

Типы артефактов
~~~~~~~~~~~~~~~

.. list-table::
      :widths: 10 10 40
      :header-rows: 1

      * - Тип
        - Микросервис
        - Примечание
      * - ui/dashboard
        - ecos-uiserv
        - 
      * - ui/action
        - ecos-uiserv
        - 
      * - ui/admin-sections-group
        - ecos-uiserv
        - 
      * - ui/form
        - ecos-uiserv
        - 
      * - ui/i18n
        - ecos-uiserv
        - 
      * - ui/icon
        - ecos-uiserv
        - 
      * - ui/journal
        - ecos-uiserv
        - 
      * - ui/menu
        - ecos-uiserv
        -
      * - ui/theme
        - ecos-uiserv
        - 
      * - model/num-template
        - ecos-model
        - 
      * - model/permissions
        - ecos-model
        - 
      * - model/type
        - ecos-model
        - 
      * - app/ecosapp
        - ecos-apps
        - 
      * - app/artifact-patch
        - ecos-apps
        - 
      * - app/dev-module
        - ecos-apps
        - 
      * - integrations/credentials
        - ecos-integrations
        - 
      * - integrations/datasource
        - ecos-integrations
        - 
      * - integrations/file-import-config
        - ecos-integrations
        - 
      * - integrations/recsrc
        - ecos-integrations
        - 
      * - integrations/sync
        - ecos-integrations
        - 
      * - process/cmm
        - ecos-process
        - 
      * - notification/file
        - ecos-notifications
        - 
      * - notification/template
        - ecos-notifications
        - 

Переопределение артефактов
~~~~~~~~~~~~~~~~~~~~~~~~~~

Для переопределения артефактов можно создать папку с именем override в корне директории с артефактами.

Пример структуры папок::

  eapps:
    - artifacts:
        - ui:
            - form:
                - some-form.json
            - journal:
                - some-journal.yml
        - override:
            - ui:
                - form:
                    - some-form.json

Для формы some-form.json будет создан патч с типом override и порядком -100 (по умолчанию). Если требуется настроить порядок,
то следует в корне папки override создать файл ``meta.yml``. В нем возможны следующие настройки:

.. list-table:: Список возможных настроек в override/meta.yml
    :header-rows: 1

    *   - Название
        - Тип данных
        - Описание
    *   - order
        - float
        - Порядок патча для перезаписи артефакта. Сначала применяются патчи с меньшим порядком.
    *   - scope
        - string
        - | Параметр служит для исключения коллизий идентификаторов override патчей.
          | Идентификатор патча формируется по следующему шаблону: override[_{{scope}}]$ui/form$some-form

**Особенности**

1. Перезапись артефактов работает вне зависимости от того откуда деплоится основной артефакт
