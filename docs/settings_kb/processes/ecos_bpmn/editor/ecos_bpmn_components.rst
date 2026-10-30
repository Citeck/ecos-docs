.. _ecos_bpmn_components:

Компоненты Citeck BPMN
==================================

Компоненты — это строительные блоки, из которых собирается схема бизнес-процесса в редакторе Citeck BPMN. Каждый компонент соответствует определённому типу элемента стандарта BPMN 2.0 и обладает настройками, специфичными для платформы Citeck.

Компоненты делятся на несколько категорий:

- **Задачи** — выполняют действия в процессе: пользовательский ввод, запуск скриптов, отправка уведомлений, вызов сервисов, установка статуса, AI-обработка, применение бизнес-правил и вызов дочерних процессов.
- **Шлюзы** — управляют маршрутизацией потока в зависимости от условий.
- **События** — фиксируют наступление определённых состояний (старт, завершение, таймер, сигнал и др.).
- **Потоки управления** — связывают элементы процесса между собой.
- **Структурные элементы** — подпроцессы, пулы и дорожки для группировки и разграничения зон ответственности.

Ниже представлен обзор всех доступных компонентов с кратким описанием. Для перехода к подробной документации кликните на соответствующую карточку.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Пользовательская задача
      :link: user_task
      :link-type: ref

      .. image:: _static/components/user_task.png
         :width: 90
         :align: left

      Выполняется человеком. При выполнении таких задач обычно требуется ввод данных, манипуляции с объектами и т.д.

   .. grid-item-card:: Скриптовая задача
      :link: script_task
      :link-type: ref

      .. image:: _static/components/script_task.png
         :width: 90
         :align: left

      Запускает скрипт (т.е. последовательность действий) или программный код, который выполняется автоматически.

   .. grid-item-card:: Уведомление
      :link: notification
      :link-type: ref

      .. image:: _static/components/notification_task.png
         :width: 90
         :align: left

      Задача-уведомление используется для отправки уведомлений пользователям.

   .. grid-item-card:: Сервисная задача
      :link: service_task
      :link-type: ref

      .. image:: _static/components/service_task.png
         :width: 90
         :align: left

      Используется для обозначения подключения сторонних сервисов, не относящихся к среде выполнения бизнес-процесса.

   .. grid-item-card:: Установка статуса
      :link: set_status
      :link-type: ref

      .. image:: _static/components/set_status_task.png
         :width: 90
         :align: left

      Элемент позволяет производить смену статуса в создаваемом бизнес-процессе.

   .. grid-item-card:: AI задача
      :link: ai_task
      :link-type: ref

      .. image:: _static/components/ai_task.png
         :width: 90
         :align: left

      Отвечает за вызов AI по указанному промту. В зависимости от бизнес-требований можно делать всё, что позволяет BPMN: отправлять задачи, уведомления, генерировать документы и т.д.

   .. grid-item-card:: Задача бизнес-правило
      :link: business_rule_task
      :link-type: ref

      .. image:: _static/components/business_rule_task.png
         :width: 90
         :align: left

      Служит для вызова :ref:`решения DMN <dmn_decision>` из процесса BPMN, используется для синхронного выполнения одного или нескольких правил.

   .. grid-item-card:: Call activity
      :link: call_activity
      :link-type: ref

      .. image:: _static/components/call_activity.png
         :width: 90
         :align: left

      Элемент схемы процесса, который позволяет вызывать другой процесс в рамках уже выполняемого.

   .. grid-item-card:: Шлюзы
      :link: gateways
      :link-type: ref

      .. image:: _static/components/gateway.png
         :width: 80
         :align: left

      Контролируют поток движения в процессе.

   .. grid-item-card:: Потоки управления
      :link: seq_flow
      :link-type: ref

      .. image:: _static/components/seq_flow.png
         :width: 100
         :align: left

      Используются для связи элементов потока BPMN (событий, процессов, шлюзов).

   .. grid-item-card:: События
      :link: bpmn_events
      :link-type: ref

      .. image:: _static/components/events.png
         :width: 100
         :align: left

      Элемент потока управления, который отражает состояние, влияющее на ход выполнения процесса. События могут инициировать действия процесса, либо являться их результатами.

   .. grid-item-card:: Подпроцесс
      :link: sub_process
      :link-type: ref

      .. image:: _static/components/subprocess.png
         :width: 90
         :align: left

      Действие, которое может включать в себя другие действия, шлюзы, события и потоки операций.

   .. grid-item-card:: Multi Instance
      :link: multi_instance
      :link-type: ref

      .. image:: _static/components/multi_instance.png
         :width: 80
         :align: left

      Многоэкземплярная активность — способ определения повторения определенного шага в бизнес-процессе.

   .. grid-item-card:: Пул и Дорожка
      :link: pool
      :link-type: ref

      .. image:: _static/components/pool_participant.png
         :width: 100
         :align: left

      Используются для отображения исполнителей процесса BPMN.

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
