Уведомления
============

Инициализация push-уведомлений
-------------------------------

При запуске приложения инициализируем пуш-уведомления **(src/helpers/notifications.helper.ts initNotifications)**

* запрашиваем у пользователя разрешение на прием пуш-уведомлений
* подписываемся на события открытия приложения по уведомлению: ``getInitialNotification``, ``onNotificationOpenedApp``
* в случае отсутствия разрешения на прием пуш уведомлений, отписываемся ``unsubscribeFromPushWorker``

Подписка на push-уведомлений
-----------------------------

**(src/store/actions/settings.actions.ts subscribeToPushWorker)**

* проверяем разрешение на прием уведомлений
* выполняем запрос ``/gateway/alfresco/alfresco/s/citeck/global-properties?name=ecos.server.tenant.id``
* получаем токен FCM
* полученный токен и Tenant ID передаем серверу в запросе ``/gateway/api/records/mutate``
* id подписки, полученный в ответе, сохраняется в локальном хранилище дл обновления токена, отписки от пуш-уведомлений

.. note::
 При подписке на пушуведомления дополнительно передается локаль приложения ``locale``
 
Обновление токена
------------------

**(src/store/actions/settings.actions.ts onTokenRefresh, sendLanguageSettings)**

* При обновлении токина FCM необходимо передать его в запросе ``/gateway/api/records/mutate`` с указание **id подписки**

.. note::
 При обновлении токена, и смене языка интерфейса приложения дополнительно передается локаль приложения ``locale``

Отписка от push-уведомлений
------------------------------

**(src/store/actions/settings.actions.ts unsubscribeFromPush)**

* выполняем запрос ``/gateway/api/records/delete``, указав **id подписки**, полученный на шаге подписки на уведомления

Открытие push-уведомлений
---------------------------

**(src/helpers/notifications.helper.ts getInitialNotification, onNotificationOpenedApp)**

При открытии задачи из уведомления важен ``taskId``, переданный в payload уведомления