Уведомления
======================

Инициализация push-уведомлений
--------------------------------------------------------------

При запуске приложения инициализируем push-уведомления ``src/helpers/notifications.helper.ts initNotifications``

* запрашиваем у пользователя разрешение на приём push-уведомлений
* подписываемся на события открытия приложения по уведомлению: ``getInitialNotification``, ``onNotificationOpenedApp``
* в случае отсутствия разрешения на приём push-уведомлений отписываемся ``unsubscribeFromPushWorker``

Подписка на push-уведомления
--------------------------------------------------------

``src/store/actions/settings.actions.ts subscribeToPushWorker``

* проверяем разрешение на приём уведомлений
* выполняем запрос ``/gateway/alfresco/alfresco/s/citeck/global-properties?name=ecos.server.tenant.id``
* получаем токен FCM
* полученный токен и Tenant ID передаём серверу в запросе ``/gateway/api/records/mutate``
* id подписки, полученный в ответе, сохраняется в локальном хранилище для обновления токена и отписки от push-уведомлений

.. note::

   При подписке на push-уведомления дополнительно передаётся локаль приложения ``locale``.

Обновление токена
----------------------------------

``src/store/actions/settings.actions.ts onTokenRefresh, sendLanguageSettings``

* при обновлении токена FCM необходимо передать его в запросе ``/gateway/api/records/mutate`` с указанием **id подписки**

.. note::

   При обновлении токена и смене языка интерфейса приложения дополнительно передаётся локаль приложения ``locale``.

Отписка от push-уведомлений
------------------------------------------------------

``src/store/actions/settings.actions.ts unsubscribeFromPush``

* выполняем запрос ``/gateway/api/records/delete``, указав **id подписки**, полученный на шаге подписки на уведомления

Открытие push-уведомлений
----------------------------------------------------

``src/helpers/notifications.helper.ts getInitialNotification, onNotificationOpenedApp``

При открытии задачи из уведомления важен ``taskId``, переданный в payload уведомления.
