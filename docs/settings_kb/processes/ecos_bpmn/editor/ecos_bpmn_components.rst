.. _ecos_bpmn_components:

Компоненты Citeck BPMN
==================================

Компоненты — это строительные блоки, из которых собирается схема бизнес-процесса в редакторе Citeck BPMN. Редактор поддерживает стандартные элементы BPMN 2.0 и расширения Citeck, такие как установка статуса и AI задача. Компоненты обладают настройками, специфичными для платформы Citeck.

Компоненты делятся на несколько категорий:

- **Задачи и вызываемые активности** — выполняют действия в процессе: работу пользователя, запуск скриптов, отправку уведомлений, вызов сервисов, установку статуса, AI-обработку, применение бизнес-правил и вызов дочерних процессов.
- **Шлюзы** — выбирают маршруты, запускают параллельные ветви и синхронизируют их.
- **События** — запускают процесс, ожидают таймер, условие или сигнал, передают и обрабатывают ошибки, завершают ветвь или область выполнения.
- **Потоки управления** — связывают элементы процесса между собой.
- **Структурные элементы** — подпроцессы, пулы и дорожки для группировки и разграничения зон ответственности.
- **Multi Instance** — настройка многократного выполнения активности последовательно или параллельно.

Ниже представлен обзор компонентов и настроек их выполнения. Для перехода к подробной документации выберите соответствующую карточку. Доступность отдельных настроек зависит от типа элемента и версии редактора.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Пользовательская задача
      :link: user_task
      :link-type: ref

      .. image:: _static/components/user_task.png
         :width: 90
         :align: left

      Создаёт задачу для пользователя или группы исполнителей и ожидает её завершения. Форма, исполнители и варианты завершения задаются в настройках задачи.

   .. grid-item-card:: Скриптовая задача
      :link: script_task
      :link-type: ref

      .. image:: _static/components/script_task.png
         :width: 90
         :align: left

      Автоматически выполняет скрипт для работы с переменными процесса, документами и доступными сервисами.

   .. grid-item-card:: Уведомление
      :link: notification
      :link-type: ref

      .. image:: _static/components/notification_task.png
         :width: 90
         :align: left

      Отправляет уведомления настроенным получателям с использованием шаблона и выбранного способа доставки.

   .. grid-item-card:: Сервисная задача
      :link: service_task
      :link-type: ref

      .. image:: _static/components/service_task.png
         :width: 90
         :align: left

      Передаёт работу внешнему обработчику по топику либо выполняет выражение. Внешняя задача ожидает завершения обработчиком независимо от флагов асинхронности.

   .. grid-item-card:: Установка статуса
      :link: set_status
      :link-type: ref

      .. image:: _static/components/set_status_task.png
         :width: 90
         :align: left

      Изменяет статус документа, связанного с бизнес-процессом.

   .. grid-item-card:: AI задача
      :link: ai_task
      :link-type: ref

      .. image:: _static/components/ai_task.png
         :width: 90
         :align: left

      Вызывает AI по промпту: выполняет обычный запрос со штатными инструментами чтения либо запускает выбранного AI-агента. Оба режима работают без истории диалога. Ответ доступен в переменной процесса и может быть сохранён в документ или обработан скриптом.

   .. grid-item-card:: Задача бизнес-правило
      :link: business_rule_task
      :link-type: ref

      .. image:: _static/components/business_rule_task.png
         :width: 90
         :align: left

      Вызывает :ref:`решение DMN <dmn_decision>` и передаёт результат вычисления правил в процесс.

   .. grid-item-card:: Call activity
      :link: call_activity
      :link-type: ref

      .. image:: _static/components/call_activity.png
         :width: 90
         :align: left

      Запускает отдельный экземпляр вызываемого процесса и ожидает его завершения. Настройки определяют выбор процесса и передачу переменных между родительским и дочерним экземплярами.

   .. grid-item-card:: Шлюзы
      :link: gateways
      :link-type: ref

      .. image:: _static/components/gateway.png
         :width: 80
         :align: left

      Управляют выбором и объединением ветвей: позволяют выбрать один или несколько маршрутов, выполнить ветви параллельно либо продолжить процесс по наступившему событию.

   .. grid-item-card:: Потоки управления
      :link: seq_flow
      :link-type: ref

      .. image:: _static/components/seq_flow.png
         :width: 100
         :align: left

      Задают порядок переходов между задачами, событиями, шлюзами и подпроцессами внутри процесса. Условия переходов определяют выбор маршрута там, где поддерживается условная маршрутизация.

   .. grid-item-card:: События
      :link: bpmn_events
      :link-type: ref

      .. image:: _static/components/events.png
         :width: 100
         :align: left

      Запускают процесс, ожидают или генерируют события, обрабатывают ошибки и завершают выполнение. Обычное конечное событие завершает ветвь, а Terminate — текущую область выполнения со всеми активными потоками внутри неё.

   .. grid-item-card:: Подпроцесс
      :link: sub_process
      :link-type: ref

      .. image:: _static/components/subprocess.png
         :width: 90
         :align: left

      Объединяет задачи, шлюзы, события и потоки управления внутри текущего процесса. Для запуска по событию используется :ref:`событийный подпроцесс <event_subprocess>` с собственным стартовым событием.

   .. grid-item-card:: Multi Instance
      :link: multi_instance
      :link-type: ref

      .. image:: _static/components/multi_instance.png
         :width: 80
         :align: left

      Настройка активности для выполнения нескольких экземпляров последовательно или параллельно, например для каждого элемента коллекции. Это свойство задачи или подпроцесса.

   .. grid-item-card:: Пул и дорожка
      :link: pool
      :link-type: ref

      .. image:: _static/components/pool_participant.png
         :width: 100
         :align: left

      Пул представляет участника взаимодействия и связан с процессом. Дорожки визуально группируют элементы, например по подразделениям или ролям; исполнители задач задаются в настройках самих задач.

.. toctree::
    :maxdepth: 1
    :hidden:

    components/ecos_bpmn_components_user_task
    components/ecos_bpmn_components_script_task
    components/ecos_bpmn_components_notifications
    components/ecos_bpmn_components_service_task
    components/ecos_bpmn_components_set_status
    components/ecos_bpmn_components_ai_task
    components/ecos_bpmn_components_business_rule_task
    components/ecos_bpmn_components_call_activity
    components/ecos_bpmn_components_gateway
    components/ecos_bpmn_components_seq_flow
    components/ecos_bpmn_components_events
    components/ecos_bpmn_components_sub_process
    components/ecos_bpmn_components_multi_instance
    components/ecos_bpmn_components_pool
