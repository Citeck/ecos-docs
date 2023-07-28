Компоненты Ecos BPMN 
=====================

.. _ecos_bpmn_components:

Для перехода к соответствующему разделу кликните картинку:

.. list-table::
      :widths: 10 30
      :class: tight-table 
      
      * - 
            .. image:: _static/components/user_task.png
                :width: 100
                :target: :ref:`Пользовательская задача<user_task>`

        - Пользовательская задача выполняется человеком. При выполнении таких задач обычно требуется ввод данных, манипуляции с объектами и т.д.
      * - 
            .. image:: _static/components/script_task.png
                :width: 100
                :target: :ref:`Скриптовая задача<script_task>`

        - Задача запускает скрипт (т.е. последовательность действий) или программный код, который выполняется автоматически.
      * - 

            .. image:: _static/components/notification_task.png
                :width: 100
                :target: :ref:`Уведомление<notification>` 

        - Задача используется для отправки уведомлений пользователям
      * - 
            .. image:: _static/components/service_task.png
                :width: 100
                :target: :ref:`Сервисная задача<service_task>`

        - Задача используется для обозначения подключения сторонних сервисов, не относящихся к среде выполнения бизнес-процесса. 
      * - 
            .. image:: _static/components/set_status_task.png
                :width: 100
                :target: :ref:`Установка статуса<set_status>`

        - Элемент позволяет производить смену статуса в создаваемом бизнес-процессе.
      * - 
            .. image:: _static/components/business_rule_task.png
                :width: 100
                :target: :ref:`Задача бизнес-правило<business_rule_task>`

        - Задача бизнес-правило служит для вызова :ref:`решения DMN<dmn_decision>` из процесса BPMN, используется для синхронного выполнения одного или нескольких правил.
      * - 
            .. image:: _static/components/gateway.png
                :width: 100
                :target: :ref:`Шлюзы<gateways>`
           
        - Шлюзы контролируют поток движения в процессе. 
      * - 
            .. image:: _static/components/seq_flow.png
                :width: 100
                :target: :ref:`Потоки управления<sequential flow>`

        - Поток управления используется для связи элементов потока BPMN (событий, процессов, шлюзов).
      * - 
            .. image:: _static/components/subprocess.png
                :width: 100
                :target: :ref:`Подпроцесс<sub_process>`

        - Действие, которое может включать в себя: другие действия, шлюзы, события и потоки операций.
      * - 
            .. image:: _static/components/events.png
                :width: 100
                :target: :ref:`События<bpmn_events>`

        - Элемент потока управления, который отражает состояние, влияющее на ход выполнения процесса. События могут инициировать действия процесса, либо являться их результатами.
      * - 
            .. image:: _static/components/multi_instance.png
                :width: 100
                :target: :ref:`Многоэкземплярная активность<multi_instance>`

        - Способ определения повторения определенного шага в бизнес-процессе.
      * - 
            .. image:: _static/components/pool_participant.png
                :width: 100
                :target: :ref:`Пул и дорожка<pool>`

        - Для отображения исполнителей процесса BPMN используются элементы: пул и дорожка. 

.. toctree::
    :hidden:
    :maxdepth: 3

    components/ecos_bpmn_components_user_task
    components/ecos_bpmn_components_script_task
    components/ecos_bpmn_components_notifications
    components/ecos_bpmn_components_service_task
    components/ecos_bpmn_components_set_status
    components/ecos_bpmn_components_business_rule_task
    components/ecos_bpmn_components_gateway
    components/ecos_bpmn_components_seq_flow
    components/ecos_bpmn_components_events
    components/ecos_bpmn_components_sub_process
    components/ecos_bpmn_components_multi_instance
    components/ecos_bpmn_components_pool