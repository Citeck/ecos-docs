Формирование PDF-файла со штрихкодом
=====================================

.. _barcode_pdf:

Функционал реализован с использованием микросервиса :ref:`ecos-transformations<transformation>` и PDFStamp.

Citeck формирует PDF-файл со штрихкодом:

    1) Конвертация в PDF происходит из **doc** и **docx** файлов в контенте карточки. 
    2) Контент заполняется либо путем вложения пользователем документа, либо генерируется из хранимого в системе :ref:`шаблона (FreeMarkerTemplate)<doc_template>`. 
    3) После генерации pdf-файл прикрепляется в виджет документов карточки, либо в контент дочерней сущности.
    4) Штрихкод размещается внизу документа:
 
 .. image:: _static/barcode/barcode_1.png 
       :width: 400
       :align: center

Конфигурация действия:

.. code-block::

    ---
    # This is temporary action to test transformations
    # If you want to use it, then rename extension from yml-sample to yml
    id: download-transformation-test
    type: transform
    name:
    ru: Тестовое скачивание
    config:

    #### прочитать содержимое из шаблона и заполнить его данными из текущего документа ####
    #  input:
    #    type: 'template'
    #    config:
    #      entityRef: '${?id}'
    #      templateRef: 'transformations/template@test-docx-template'

    transformations:
        - { type: 'convert', config: { toMimeType: 'application/pdf' } }
        - { type: 'barcode' }

    #### сохранить результат в документы ####
    #  output:
    #    type: "mutate"
    #    config:
    #      entityRef: 'emodel/document@'
    #      additionalAttributes:
    #        "_parent": '${?id}'
    #        "_parentAtt": "docs:documents"
    #        "_type": 'emodel/type@document'

Для скачивания документа с размещенным штрихкодом используйте в карточке документа действие **Скачать PDF (со штрихкодом)**:

 .. image:: _static/barcode/barcode_2.png 
       :width: 300
       :align: center
