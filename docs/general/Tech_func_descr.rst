.. _tech-func-descr:

Техническое описание реализации функциональностей
=====================================================

Раздел описывает генерацию штрихкодов, рабочее расписание, предпросмотр и трансформацию документов, серверные групповые операции и выбор атрибута контента при подписании.

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: Штрих-код
      :link: barcode
      :link-type: ref

      Генерация изображения штрихкода, отображение и печать, наложение на PDF через ecos-transformations.

   .. grid-item-card:: Рабочее расписание и производственный календарь
      :link: working-schedule
      :link-type: ref

      Рабочие дни и часы, часовые пояса, праздники и сокращённые дни; условия лицензирования расчётов.

   .. grid-item-card:: Предпросмотр документов
      :link: doc_preview
      :link-type: ref

      Отображение файлов в браузере, генерация превью и thumbnail, конвертация контента и ограничения форматов.

   .. grid-item-card:: Групповые действия
      :link: group_actions
      :link-type: ref

      Серверная обработка наборов записей, выгрузка в Excel и ZIP; условия лицензирования.

   .. grid-item-card:: Подпись контента
      :link: content-sign
      :link-type: ref

      Выбор атрибута с подписываемым контентом при вызове Citeck.Esign.sign.

.. toctree::
    :maxdepth: 2
    :hidden:

    Tech_func_descr/barcode
    Tech_func_descr/business_calendar
    Tech_func_descr/Preview
    Tech_func_descr/Group_actions
    Tech_func_descr/content_sign
