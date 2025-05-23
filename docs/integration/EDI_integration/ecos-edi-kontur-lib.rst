.. _ecos-edi-kontur-lib:

Описание ecos-edi-kontur-lib
=============================

Данная либа производит интеграцию с сервисами Контур.Диадок и Контур.EDI.

Документация сервисов:

`https://api-docs.diadoc.ru/ru/latest/  <https://api-docs.diadoc.ru/ru/latest/>`_

`API EDI.Контур documentation <https://edi-api-documentation.readthedocs.io/en/latest/>`_

Ссылки на веб-морды для работы сервисов:

`Вход в систему <https://diadoc.kontur.ru/>`_

`Тестовый Контур.EDI <https://test-edi.kontur.ru/SelectParty>`_

`Контур.EDI <https://edi.kontur.ru/SelectParty>`_

Интеграция с одним или с другим сервисов происходит раздельно. То есть, для интеграции с каждым сервисом необходимо создавать отдельные синхронизации. 

Пример настройки ящика с описанием можно найти на этой странице: :ref:`Настройка получения событий с ящиком Контур_Диадок<events_kontur>`

Разделение между синхронизацией с Диадоком или синхронизацией с EDI сервисом сейчас происходит засчет сравнения урлов из датасорса. Если содержится **"diadoc"** - синхронизироваться будем с диадоком. Если содержится **"edi"** - с Контур.EDI.

Отличие в конфигурации для Диадока и EDI - в том, что для EDI обязательно заполнение **GLN**

