Описание ecos-edi-sbis-lib
===========================

Данная либа производит интеграцию с Тензор.СБИС.

Ссылка на документацию:

`Порядок работы с API-интерфейсом  <https://sbis.ru/help/integration/api/sequence>`_

`список используемых в Тензор.СБИС форматов документов <https://sbis.ru/formats/edo/>`_

Ссылка на личный кабинет:

`Тест  <https://fix-online.sbis.ru/>`_

`Прод  <https://online.sbis.ru/>`_

Настройка ящика проще чем для других провайдеров, необходимо заполнить только **datasource**, **creds** и **boxId**:

 .. image:: _static/ecos-edi-sbis-lib/ecos-edi-sbis-lib_1.png
       :width: 600
       :align: center

На данный момент интеграция корректно работает только для ЮЗДО. EDI интеграция не реализована.