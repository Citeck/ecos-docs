API запросы ecos-edi
======================

В ecos-edi микросервисе реализован функционал из enterprise-core cервиса **EcosEdiService**.

При отправке запроса на отправку пакета или документов или генерацию сервисных документов используется record dao c id - **edi-request**.

Для отправки запроса через рекорды необходимо использовать метод **mutate**.

DTO запроса и ответа:

.. code-block::

    public static class EdiRequest {
        private String requestType;
        private String providerType;
        private ObjectData requestData;
    }
    
    public static class EdiRequestResult {
        private boolean success;
        private ObjectData response;
        private String error;
    }

Где:

    **requestType** - тип запроса, например *“generatePrintForm“*
    **providerType **- тип провайдера, Контур, сбис и т.д. для диадока необходимо указывать *“kontur“*
    **requestData** - данные по запросу, например для генерации печатных форм это *documentRef документа*


Пример запроса:

.. code-block::

    RecordAtts requestAtts = new RecordAtts();
    requestAtts.setId("edi/edi-request");
    requestAtts.setAtt("requestType", "generatePrintForm");
    requestAtts.setAtt("providerType","kontur");
    requestAtts.setAtt("requestData", ObjectData.create().set("documentRef", RecordRef.valueOf("recordRef value")));
    recordsService.mutate(requestAtts);

Посмотреть различные типы запросов можно в классе **EdiRequestRecords** микросервиса ecos-edi

Пример запроса из консоли:

.. code-block::

    var rec = Records.get('edi/edi-request@'); // важно @ в конце
    rec.att("_self", {
                    "requestType":"generatePrintForm",
                    "providerType":"KONTUR",
        "requestData": {"documentRef":"emodel/edi-document@5d518efd-cef1-4ebf-b518-62ff9a620c9e"}
    
        });
    var resp = await rec.save("?json");

Список текущих поддерживаемых запросов:

.. list-table::
      :widths: 5 50 30
      :header-rows: 1
      :class: tight-table 
      
      * - Запрос
        - Описание
        - Пример
      * - **isCounterpartyExists**
        -  | Запрос на проверку существания связи с контрагентом у конткретной организации.
           | Параметры requestData:

               * *clientBoxId* - ид проверяемого ящика
               * *inn* - ИНН контрагента
               * *kpp* - КПП контрагента

        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"isCounterpartyExists",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "clientBoxId":"1312313-131331-1231",
                                    "inn":"12334561234",
                                    "kpp":"123652323"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **aquireCounterparty**
        -  | Запрос на создание связи с контрагентом.
           | Параметры:

               * *counterpartyRef* - recordRef контрагента в ecos
               * *clientBoxId* - ид ящика организации
               * *invitationDocRef* - recordRef пригласительного документа (опционально)
               * *comment* - Комментарий

        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"aquireCounterparty",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "counterpartyRef":"emodel/counterparty@12311241-123123",
                                    "clientBoxId":"123123-123123123-123213",
                                    "invitationDocRef ":"emodel/invitationDoc@12311241-123123",
                                    "comment": "commentText"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **breakWithCounterparty**
        -  | Запрос на разрыв связи с контрагентом
           | Параметры:

               * *counterpartyRef* - recordRef контрагента в ecos
               * *clientBoxId* - id ящика организации
               * *comment* - комментарий
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"breakWithCounterparty",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "counterpartyRef":"emodel/counterparty@12311241-123123",
                                    "clientBoxId":"123123-123123123-123213",
                                    "comment": "commentText"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **sendPackageToCounterparty**
        -  | Отправка исходящего пакета провайдеру.
           | Параметры:

              * *packageRef* - recordRef отправляемого пакета
              * *counterpartyRef* - recordRef контрагента в ecos
              * *counterpartyBoxId* - boxId контрагента (опционально, обязаетельно если не указан counterpartyRef )
              * *legalEntityRef* - recordRef юр. лица в ecos
              * *clientBoxId* - boxId юр. лица (опционально, обязательно если не указан *legalEntityRef*)
              * *fromDepartmentId* - Id департамента в провайдере от имени которого отправляется пакет (Опционально)
              * *toDepartmentId* - Id департамента в провайдере, которому отправляется пакет (Опционально)
              * *isInternal* - является ли пакет внутренним (оборот между департаменатами одной организации)
              * *needSentSignature* - Требуется ли подпись контрагента
              * *packageNumber* - Номер пакета (Опционально)
              * *packageDate* - Дата пакета (Опционлаьно)
              * *packageComment* - Комментарий к пакету (Опционально)
              * *signerRef* - recordRef пользователя подписавшего документы в пакете

        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"sendPackageToCounterparty",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "packageRef":"emodel/edi-package@12311241-123123",
                                    "counterpartyRef":"emodel/counterparty@12311241-123123",
                                    "counterpartyBoxId ":"234623478246824623442374",
                                    "legalEntityRef":"emodel/legal-entity@12311241-123123",
                                    "clientBoxId":"2342342342342342424324",
                                    "fromDepartmentId ":"3434444444444434343434",
                                    "toDepartmentId":"242423423424242424242",
                                    "isInternal":false,
                                    "needSentSignature":true,
                                    "packageNumber":"22551515252",             
                                    "packageDate":"2023/09/08",
                                    "packageComment":"Test comment",
                                    "signerRef": "emodel/person@12311241-123123"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **signPackage**
        -  | Отправка подписанных документов в пакете провайдеру.
           | Параметры:

              * *packageRef* – recordRef пакета с ЭДО документами
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"signPackage",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "packageRef ":"emodel/edi-package@12311241-123123"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **pointwiseSync**
        -  | Точечная синхронизация с провайдером по одному пакету.
           | Параметры:

              * *clientBoxId* - id ящика с которым настроена синхрнизация
              * *systemPackageId*- id пакета по которому требуется провести синхронизацию
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"pointwiseSync",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "clientBoxId":"12315116136163241231",
                                    "systemPackageId":"1321312312312321312312"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **signDocuments**
        -  | Отправка подписей по документам провайдеру.
           | Параметры:

              * *documentRefs* - список подписанных документов, для которых требуется отправить подписи
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"signDocuments",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **signDocumentsAndBuyerTitles**
        -  | Отправка подписей по формализованным документам провайдеру.
           | Параметры:

              * *documentRefs* - список подписанных неформализованных документов, для которых требуется отправить подписи.
              * *invoicesRefs* - список подписанных формализованных документов,  для которых требуется отправить подписи
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"signDocumentsAndBuyerTitles",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ],
                                    "invoicesRefs":[
                                                    "emodel/edi-document@ref3",
                                                    "emodel/edi-document@ref4"
                                                    ]     
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **sendReconciliationActSigns**
        -  | Отправка подписей для актов сверки.
           | Параметры:

              * *documentRefs* - список подписанных неформализованных документов, для которых требуется отправить подписи
              * *signerRef* - recordRef пользователя подписавшего документы
              * *signerJobTitle* - Должность пользователя подписавшего документы
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"sendReconciliationActSigns",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ],
                                    "signerRef":"emodel/person@ref-1",
                                    "signerJobTitle":"Директор тест"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **rejectPackage**
        -  | Отправка подписанного отказа в подписи документов в пакете.
           | Параметры:

              * *packageRef* - recordRef пакета с ЭДО документами
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"rejectPackage",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "packageRef ":"emodel/edi-package@12311241-123123"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **rejectDocuments**
        -  | Отправка подписанного отказа в подписи документов.
           | Параметры:

              * *documentRefs* - список документов, для которых требуется отправить отказ
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"rejectDocuments",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **sendReconciliationActRejects**
        -  | Отправка подписанных отказов в подписи для актов сверки.
           | Параметры:

              * *documentRefs* - список актов сверки для которых требуется отправить отказ
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"sendReconciliationActRejects",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **acceptRevocationRequests**
        -  | Отправка подписанных запросов на аннулирование по документам.
           | Параметры:

              * *documentRefs* - список документов по которым было подписано аннулирование
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"acceptRevocationRequests",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **declineRevocationRequests**
        -  | Отправка подписанных отказов по запросу на аннулирование по документам.
           | Параметры:

              * *documentRefs* - список документов по которым было подписан отказ аннулирования
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"declineRevocationRequests",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **sendRevocationRequests**
        -  | Отправка подписанных запросов на аннулирование по документам.
           | Параметры:

              * *documentRefs* - список документов по которым был подписан запрос на аннулирование
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"sendRevocationRequests",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **sendCorrectionRequests**
        -  | Отправка подписанных запросов на корректировку по документам.
           | Параметры:

              * *documentRefs* - список документов по которым был подписан запрос на корректировку
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"sendCorrectionRequests",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **sendBuyerTitles**
        -  | Отправка подписанных титулов покупателя по формализованным документам.
           | Параметры:

              * *documentRefs* - список документов по которым был подписан титул покупателя
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"sendBuyerTitles",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generatePrintForm**
        -  | Генерация печатной формы по документу, возвращается контент печатной формы
           | Параметры:

              * *documentRef* - recordRef документа по которому требуется сгенерировать печатную форму
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generatePrintForm",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generatePrintFormWithDetails**
        -  | Генерация печатной формы по документу, возвращается контент печатной формы + доп. параметры (id документа, статус генерации печатной формы у провайдера, возможные ошибки)
           | Параметры:

              * *documentRef* - recordRef документа по которому требуется сгенерировать печатную форму
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generatePrintFormWithDetails",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **needUpdateMainContentByPrintForm**
        -  | Требуется ли генерация печатной формы для документа
           | Параметры:

              * *documentRef* - recordRef документа по которому требуется уточнение по требованию генерации
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"needUpdateMainContentByPrintForm",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generateRejectionXml**
        -  | Генерация xml отказа в подписи для документа.
           | Параметры:

               * *documentRef* – recordRef документа по которому требуется генерация xml отказа в подписи
               * *signerRef* - recordRef пользователя, который будет подписывать отказ
               * *comment* - комментарий отказа
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generateRejectionXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1",
                                    "signerRef":"emodel/person@ref-1",
                                    "comment":"Test comment"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generateRejectionsXml**
        -  | Генерация xml отказа в подписи для документов
           | Параметры:

               * *documentRef* – recordRef документа по которому требуется генерация xml отказа в подписи
               * *signerRef* - recordRef пользователя, который будет подписывать отказ
               * *comment* - комментарий отказа
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generateRejectionsXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ], 
                                    "signerRef":"emodel/person@ref-1",   
                                    "comment":"Test comment"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generateRevocationXml**
        -  | Генерация xml запроса на аннулирование для документа
           | Параметры:

               * *documentRef* – recordRef документа по которому требуется генерация xml запроса на аннулирование
               * *signerRef* - имя пользователя, который будет подписывать запрос на аннулирование
               * *comment* - комментарий запроса на аннулирование
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generateRevocationXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1",
                                    "signerName":"admin",
                                    "comment":"Test comment"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generateRevocationsXml**
        -  | Генерация xml запроса на аннулирование для документов.
           | Параметры:

               * *documentRef* – recordRef документов по которым требуется генерация xml запроса на аннулирование
               * *signerRef* - имя пользователя, который будет подписывать запрос на аннулирование
               * *comment* - комментарий запроса на аннулирование
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generateRevocationsXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ], 
                                    "signerName":"admin",    
                                    "comment":"Test comment"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generateInvoiceCorrectionRequestXml**
        -  | Генерация xml корректировки для документа.
           | Параметры:

               * *documentRef* – recordRef документа по которому требуется генерация xml корректировки
               * *signerRef* - имя пользователя, который будет подписывать корректировку
               * *comment* - комментарий
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generateInvoiceCorrectionRequestXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1",
                                    "signerName":"admin",
                                    "comment":"Test comment"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **isNeedSignTitle**
        -  | Проверка на требование подписания титула покупателя у документа
           | Параметры:

              * *documentRef* - recordRef документа по которому требуется проверка
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"isNeedSignTitle",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generateBuyerTitle**
        -  | Генерация xml титула покупателя для документа
           | Параметры:

               * *documentRef* – recordRef документа по которому требуется генерация титула покупателя
               * *signerName* - имя пользователя, который будет подписывать титул покупателя
               * *factArrivalDate* - фактическая дата передачи товара
               * *comment* - комментарий 
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generateBuyerTitle",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1",
                                    "signerName":"admin",
                                    "factArrivalDate ":"2023/09/08",
                                    "comment":"Test comment"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generateReceiptXml**
        -  | Генерация xml извещения о получении для документа
           | Параметры:

               * *documentRef* – recordRef документа по которому требуется генерация извещения о получении
               * *signerName* - имя пользователя, который будет подписывать извещение о получении
               * *signerPosition* - должность пользователя

        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generateReceiptXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1",
                                    "signerName":"admin",
                                    "signerPosition":"DirectorTest"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **generateReceiptsXml**
        -  | Генерация xml извещения о получении для документов
           | Параметры:

               * *documentRefs* – recordRef документов по которым требуется генерация извещения о получении
               * *signerName* - имя пользователя, который будет подписывать извещение о получении
               * *signerPosition* - должность пользователя

        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"generateReceiptsXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ],  
                                    "signerName":"admin",
                                    "signerPosition":"DirectorTest"
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **sendReceiptsXml**
        -  | Отправка подписанного xml извещения о получении для документов.
           | Параметры:

              * *documentRefs* - recordRef документов по которым требуется отправка извещения о получении
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"sendReceiptsXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRefs":[
                                                    "emodel/edi-document@ref1",
                                                    "emodel/edi-document@ref2"
                                                    ]
                                }
                
                    });
                var resp = await rec.save("?json");

      * - **sendReceiptXml**
        -  | Отправка подписанного xml извещения о получении для документа (Оптимизируется в дальнейшем)
           | Параметры:

              * *documentRef* - recordRef документа по которому требуется отправка извещения о получении
        - 

            .. code-block::

                var rec = Records.get('edi/edi-request@');
                rec.att("_self", {
                                "requestType":"sendReceiptXml",
                                "providerType":"KONTUR",
                                "requestData": {
                                    "documentRef":"emodel/edi-document@ref1"
                                }
                
                    });
                var resp = await rec.save("?json");