.. _mango_reference:

Технические параметры
=====================

.. contents::
   :depth: 2
   :local:

Артефакты
~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 25 45
   :class: tight-table

   * - Артефакт
     - Расположение
     - Назначение
   * - ``mango-api``
     - ``model/secret``
     - Секрет ``BASIC``: «Имя пользователя» (``username``) — код ВАТС, «Пароль» (``password``) — соль; поставляется незаполненным
   * - ``mango-office``
     - ``model/endpoint``
     - API ВАТС MANGO OFFICE, ``https://app.mango-office.ru``
   * - ``stt-sidecar``
     - ``model/endpoint``
     - Сервис распознавания речи, ``http://citeck-stt-sidecar:8090``
   * - ``mango-webhook``
     - ``integration/in-webhook``
     - Входящий вебхук, аутентификация по подписи, действие «Трансформация в Events»
   * - ``mango-call-recordings-sync``
     - ``integration/camel-dsl``
     - Маршрут обработки, поставляется в состоянии ``STOPPED``

Адреса журналов, в которых настраиваются эти артефакты, приведены в шагах настройки (см. :ref:`mango_setup`).

.. _mango_webhook_codes:

Коды ответа вебхука
~~~~~~~~~~~~~~~~~~~

Принимаются POST-запросы на базовый адрес вебхука и на любые пути под ним.

.. list-table::
   :header-rows: 1
   :widths: 10 45 45
   :class: tight-table

   * - Код
     - Сообщение
     - Причина
   * - 200
     - Пустой ответ
     - Подпись верна, уведомление принято; этот же ответ возвращается при остановленном маршруте, и уведомление тогда теряется
   * - 401
     - ``Webhook signature is not valid``
     - Подписи нет или она неверна
   * - 401
     - ``Request parameter 'json' referenced by component 'param.json' is missing``
     - Подпись есть, но в запросе нет поля ``json``
   * - 500
     - ``Invalid webhook id=…``
     - Вебхук с таким идентификатором не найден
   * - 500
     - ``Secret … not found``
     - Секрет, указанный в вебхуке, не найден
   * - 500
     - ``Signature config is not defined…``
     - У вебхука не задана конфигурация подписи

После успешной проверки создаётся событие Citeck типа ``in-webhook-request`` с полями ``webhookId``, ``params`` и ``body``. В поле ``body`` передаётся значение поля ``json`` запроса.

.. _mango_ip_addresses:

IP-адреса MANGO OFFICE
~~~~~~~~~~~~~~~~~~~~~~

По документации MANGO OFFICE VPBX API версии 1.9 уведомления отправляются с адресов:

- ``81.88.80.132``
- ``81.88.80.133``
- ``81.88.82.36``
- ``81.88.82.44``
- ``81.88.82.45``

Актуальный список рекомендуется уточнить у MANGO OFFICE.

Очереди RabbitMQ
~~~~~~~~~~~~~~~~

Все очереди и exchange устойчивые (durable): они сохраняются при перезапуске брокера. Их объявляют обработчики маршрута при запуске, а очереди отложенных повторов объявляются при первом использовании.

.. list-table::
   :header-rows: 1
   :widths: 30 20 20 30
   :class: tight-table

   * - Объект
     - Тип
     - Routing key
     - Назначение
   * - ``mango-call-recordings``
     - Exchange (direct)
     - —
     - Общий exchange интеграции
   * - ``mango-events``
     - Очередь, 1 потребитель
     - ``mango-events``
     - Очередь уведомлений MANGO OFFICE
   * - ``mango-events-dlq``
     - Очередь
     - ``mango-events-dlq``
     - Недоставленные уведомления
   * - ``mango-recordings``
     - Очередь, 2 потребителя
     - ``mango-recordings``
     - Очередь аудиозаписей: звонки, ожидающие обработки аудиозаписи
   * - ``mango-recordings-dlq``
     - Очередь
     - ``mango-recordings-dlq``
     - Звонки, аудиозапись которых не удалось обработать
   * - ``mango-recordings-retry-<delayMillis>``
     - Quorum-очередь с TTL
     - —
     - Ожидание отложенного повтора; по истечении TTL сообщение возвращается в ``mango-recordings``

Номер попытки отложенного повтора хранится в заголовке сообщения ``mango-recording-retry-attempt``.

.. _mango_route_params:

Параметры маршрута
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 25 30 15
   :class: tight-table

   * - Параметр
     - По умолчанию
     - Назначение
     - Где задаётся
   * - ``mango.recording.retryDelaysMillis``
     - ``60000,120000,300000,600000,1800000``
     - Паузы между повторами обработки аудиозаписи, мс; число значений равно числу повторов
     - JVM или переменная окружения
   * - ``mango.queue.maximumRedeliveries``
     - ``3``
     - Повторы обработки уведомлений
     - JVM или переменная окружения
   * - ``mango.queue.redeliveryDelay``
     - ``30000``
     - Первая пауза перед повтором обработки уведомления, мс
     - JVM или переменная окружения
   * - ``mango.queue.useExponentialBackOff``
     - ``true``
     - Удвоение паузы между повторами обработки уведомления
     - JVM или переменная окружения
   * - ``mango.queue.maximumRedeliveryDelay``
     - ``120000``
     - Максимальная пауза между повторами обработки уведомления, мс
     - JVM или переменная окружения
   * - ``mango.queue.entryMaximumRedeliveries``
     - ``2``
     - Повторы первичной публикации
     - JVM или переменная окружения
   * - ``mango.queue.entryRedeliveryDelay``
     - ``500``
     - Пауза первичной публикации, мс
     - JVM или переменная окружения
   * - ``mango.queue.saveRetryDelay``
     - ``5000``
     - Пауза повтора сохранения, мс
     - JVM или переменная окружения
   * - ``recordingFailurePolicy.retryHttpStatuses``
     - ``401,403,408,425,429``
     - Коды HTTP-ответов, при которых загрузка и распознавание аудиозаписи повторяются
     - YAML маршрута
   * - ``mangoRecordingGuard.maxSize``
     - ``52428800``
     - Наибольший размер аудиозаписи, байт
     - YAML маршрута
   * - ``mangoResolvePolicy.inactiveStatuses``
     - См. :ref:`mango_search_order`
     - Статусы, исключаемые из поиска, по источникам (JSON-словарь)
     - YAML маршрута
   * - ``mangoResolvePolicy.candidatesPageSize``
     - ``100``
     - Число последних изменённых сделок или лидов, рассматриваемых в каждом источнике
     - YAML маршрута
   * - ``mangoResolvePolicy.ambiguousMarker``
     - ``[mango:ambiguous]``
     - Маркер пометки о неоднозначности
     - YAML маршрута
   * - ``mangoResolvePolicy.ambiguityNoteTemplate``
     - «Номер {number} совпал с несколькими активными записями ({names}). Звонок привязан к последней изменённой — {chosen}.»
     - Текст пометки для сделок и лидов
     - YAML маршрута
   * - ``mangoResolvePolicy.sourceNoteTemplates``
     - Шаблон для ``emodel/ecos-counterparty``
     - Тексты пометок по источникам (JSON-словарь)
     - YAML маршрута
   * - Рабочее пространство создаваемого лида
     - ``emodel/workspace@crm-workspace``
     - Размещение лидов, созданных по звонкам
     - YAML маршрута, константа ``LEAD_WORKSPACE`` в шаге ``mango-create-lead-for-call``
   * - Потребители очередей ``mango-events`` и ``mango-recordings``
     - ``1`` и ``2``, ``prefetchCount: 1``
     - Число одновременно обрабатываемых сообщений; число потребителей очереди уведомлений менять нельзя
     - YAML маршрута
   * - Запрос аудиозаписи
     - ``POST <mango-office>/vpbx/queries/recording/post``, ``action: download``
     - Загрузка mp3-файла
     - YAML маршрута
   * - Запрос распознавания
     - ``POST <stt-sidecar>/transcribe-diarize?language=ru``
     - Распознавание речи
     - YAML маршрута
   * - Тайм-аут распознавания
     - ``1800000`` мс
     - Наибольшее время ожидания ответа сервиса распознавания
     - YAML маршрута
   * - Провайдер, модель и температура резюме
     - ``citeck.ai.call-recording.summary.provider``, ``.model``, ``.temperature`` (по умолчанию ``0.3``)
     - Языковая модель для резюме
     - Свойства Citeck AI

Атрибуты активности «Звонок»
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Атрибут
     - Значение
   * - ``_type``
     - ``emodel/type@call-activity``
   * - ``_parent``
     - Сделка или лид
   * - ``_parentAtt``
     - ``has-ecos-activities:ecosActivities``
   * - ``_status``
     - ``completed``
   * - ``topic``
     - «Входящий звонок ``<номер>``»
   * - ``activityDate``
     - Время звонка (ISO 8601, UTC; см. :ref:`mango_call_time`)
   * - ``text``
     - Пометка о неоднозначности и ссылка на карточку звонка (HTML)
   * - ``recording-aspect:meetingUrl``
     - ``mango://entry/<entry_id>`` — идентификатор звонка
   * - ``recording-aspect:callPlatform``
     - ``mango``
   * - ``recording-aspect:recordingStatus``
     - Статус обработки аудиозаписи
   * - ``recording-aspect:recording``
     - mp3-файл ``mango-call-<entry_id>.mp3``
   * - ``recording-aspect:recordingDuration``
     - Длительность, с
   * - ``recording-aspect:transcription``
     - Полный текст
   * - ``recording-aspect:transcriptionDiarized``
     - Текст по репликам
   * - ``recording-aspect:summary``
     - Резюме

В имени файла аудиозаписи все символы, кроме латиницы, цифр, «.», «_» и «-», заменяются на «_», а идентификатор звонка обрезается до 80 символов. Поэтому имя файла может не совпадать с ``entry_id``: например, символы «=» и «+», обычные для ``entry_id``, заменяются.

Атрибуты создаваемого лида
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70
   :class: tight-table

   * - Атрибут
     - Значение
   * - ``_workspace``
     - ``emodel/workspace@crm-workspace``
   * - ``name``
     - Название найденного контрагента или «Входящий звонок ``<номер>``»
   * - ``contacts``
     - Номер звонящего как основной контакт (``contactPhone``, ``contactMain = true``)
   * - ``counterparty``
     - Найденный контрагент, если есть

Компоненты маршрута
~~~~~~~~~~~~~~~~~~~

Сведения для администратора, который читает YAML маршрута или лог.

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Компонент (бин) маршрута
     - Назначение
   * - ``mangoEventParser``
     - Разбор уведомления MANGO OFFICE и определение его типа
   * - ``phoneKeys``
     - Нормализация номера звонящего
   * - ``callTargetQuery``, ``callTargetPick``
     - Запрос кандидатов и выбор сделки или лида
   * - ``mangoResolvePolicy``
     - Правила выбора сделки или лида
   * - ``callActivityQuery``, ``callActivityDecision``, ``callActivityLink``
     - Поиск активности, решение о создании или обновлении, ссылка на карточку звонка
   * - ``mangoRecordingSign``
     - Подпись запроса к API MANGO OFFICE (sha256)
   * - ``mangoRecordingForm``
     - Формирование тела запроса
   * - ``mangoRecordingGuard``
     - Проверка размера и типа загруженного ответа
   * - ``mangoRecordingValidation``
     - Проверка mp3-файла в ответе без указания типа содержимого
   * - ``maskedErrorDescriber``
     - Описание ошибок с маскированием учётных данных
   * - ``recordingFailurePolicy``
     - Разделение ошибок на временные и постоянные
   * - ``recordingRetrySnapshot``, ``recordingRetry``
     - Отложенные повторы обработки аудиозаписи

.. _mango_known_issues:

Известные технические особенности
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Уникальность идентификатора звонка на уровне базы данных не гарантируется. В редких случаях одновременной обработки двух уведомлений одного звонка у звонка может появиться вторая активность; используется самая ранняя, в лог выводится предупреждение ``activities with the same key``.
- Два сообщения одного звонка могут одновременно обрабатываться двумя потребителями очереди аудиозаписей. Тогда аудиозапись загружается и распознаётся дважды, а в карточке остаётся результат обработки, закончившейся позже, в том числе статус ``transcription-failed`` поверх ``completed``.
- Очередь уведомлений обрабатывается в один поток: сбой одного уведомления задерживает уведомления других звонков на время повторов, до трёх с половиной минут.
- Когда повторы исчерпаны после успешной загрузки, записывается только статус ``transcription-failed``, без mp3-файла. Такой же статус устанавливается, если распознавание прошло, но не удалось сохранить результат.
- Если уведомление о записи уже перевело звонок в статус ``downloading``, а передать звонок в очередь аудиозаписей не удалось, статус остаётся ``downloading`` до повторной обработки сообщения из ``mango-events-dlq``.
