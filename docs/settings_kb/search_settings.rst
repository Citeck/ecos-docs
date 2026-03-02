.. _search_settings:

Настройки поиска
==================

.. contents::
    :depth: 2

Поиск осуществляется по документам, людям (пользователям), рабочим пространствам.

.. image:: _static/search/search_01.png
       :width: 300
       :align: center

По нажатию на «Показать все результаты» открывается первая страница результатов поиска:

.. image:: _static/search/search_02.png
       :width: 700
       :align: center

Типы документов, по которым осуществлять поиск, настраиваются дополнительно.

Для настройки типов данных перейдите в журнал :ref:`«Конфигурация ECOS»<configuration_admin>`.

Журнал доступен по адресу: ``v2/journals?journalId=ecos-configs&viewMode=table&ws=admin$workspace``

В поисковой строке введите **global-search-config**:

.. image:: _static/search/setting_01.png
       :width: 700
       :align: center

откройте настройку:

.. image:: _static/search/setting_02.png
       :width: 500
       :align: center

На форме можно настроить:

    - Максимальное количество одновременных запросов на одно приложение (микросервис). Если будет много одновременных запросов в глобальный поиск, то это не должно положить сервер.
    - Список типов документов, по которым должен быть глобальный поиск и опционально возможность указать атрибуты, по которым его производить.

Если атрибуты для поиска не указывать, то поиск будет вестись по отображаемому имени. Список доступных типов атрибутов для выбора: ``TEXT``, ``MLTEXT``, ``OPTIONS``.

Добавление типа данных
------------------------------------------

Нажмите **«Добавить ещё»**. Выберите тип данных:

.. image:: _static/search/setting_03.png
       :width: 600
       :align: center

и атрибуты для поиска:

.. image:: _static/search/setting_04.png
       :width: 600
       :align: center

Сохраните - нажмите **«Создать»**.

Проверьте работу поиска:

.. list-table::
      :widths: 10 20
      :align: center

      * - |

            .. image:: _static/search/search_03.png
                  :width: 300
                  :align: center

        - |

            .. image:: _static/search/search_04.png
                  :width: 700
                  :align: center
