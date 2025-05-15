.. _admin:

Раздел администратора 
======================

Перейдите в рабочее пространство **"Раздел администратора"**:

 .. image:: _static/admin/admin_2.png
       :width: 700
       :align: center 

В левой части представлено меню с разделами для конфигурации и настройки системы:

      * Управление системой;
      * Управление процессами;
      * Модель;
      * Конфигурация UI;
      * Конфигурация уведомлений
      * и т.д.

 .. image:: _static/admin/admin_1.png
       :width: 700
       :align: center 

Управление системой - Инструменты разработки
---------------------------------------------

Вкладка "Сборка"
~~~~~~~~~~~~~~~~~

Представлена актуальная информация о модулях Citeck:

 .. image:: _static/admin/admin_12.png
       :width: 600
       :align: center 

Вкладка "Коммиты"
~~~~~~~~~~~~~~~~~

По всем репозиториям указан список внесенных изменений:

 .. image:: _static/admin/admin_14.png
       :width: 600
       :align: center 

По ссылкам можно перейти в репозиторий, конкретный коммит, задачу.


Вкладка "Настройки"
~~~~~~~~~~~~~~~~~~~~

Представлены настройки:

 .. image:: _static/admin/admin_13.png
       :width: 600
       :align: center 

**Включить логгер для новых форм** - включает дебаг-логи для форм. Смотреть можно в консоли браузера.

**Включить дебаг для Records API** -  в ответе от :ref:`Records API<Records_API>` запросов возвращается дополнительная информация, которая помогает понять, что происходило на сервере во время запроса.

Интерфейс раздела администратора
--------------------------------

Данные в разделе представлены в виде журнала.

 .. image:: _static/admin/admin_3.png
       :width: 700
       :align: center 

Для каждой записи доступен стандартный набор действий.

.. note:: 

       Так же для разделов могут быть доступны иные специальные действия.

.. list-table::
      :widths: 5 10
      :align: center
      :class: tight-table 
      
      * - 

             .. image:: _static/admin/admin_4.png
                  :width: 25
                  :align: center 

        - Скачать в виде json-файла

      * - 

             .. image:: _static/admin/admin_5.png
                  :width: 25
                  :align: center 

        - Удалить

      * - 

             .. image:: _static/admin/admin_6.png
                  :width: 25
                  :align: center 

        - | Открыть карточку журнала в соседней вкладке.
          | Карточка представляет собой :ref:`дашборд<dashboard>`:

             .. image:: _static/admin/admin_7.png
                  :width: 500

      * - 

             .. image:: _static/admin/admin_8.png
                  :width: 25
                  :align: center 

        - Открыть на редактирование

      * - 

             .. image:: _static/admin/admin_9.png
                  :width: 25
                  :align: center 

        - Редактировать json-файл:

             .. image:: _static/admin/admin_11.png
                  :width: 500


      * - 

             .. image:: _static/admin/admin_10.png
                  :width: 25
                  :align: center 

        - Копировать

