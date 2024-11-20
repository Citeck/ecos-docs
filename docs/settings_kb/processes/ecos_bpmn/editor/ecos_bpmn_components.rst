Компоненты Citeck BPMN 
=======================

.. toctree::
    :maxdepth: 1

    components/ecos_bpmn_components_user_task
    components/ecos_bpmn_components_script_task
    components/ecos_bpmn_components_notifications
    components/ecos_bpmn_components_service_task
    components/ecos_bpmn_components_set_status
    components/ecos_bpmn_components_business_rule_task
    components/ecos_bpmn_components_call_activity
    components/ecos_bpmn_components_gateway
    components/ecos_bpmn_components_seq_flow
    components/ecos_bpmn_components_events
    components/ecos_bpmn_components_sub_process
    components/ecos_bpmn_components_multi_instance
    components/ecos_bpmn_components_pool

.. _ecos_bpmn_components:

.. note:: 

  Для перехода к соответствующему разделу кликните картинку:

.. list-table::
      :widths: 10 30
      :class: tight-table 
      
      * - 
            .. image:: _static/components/user_task.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_user_task.html 

        - Пользовательская задача выполняется человеком. При выполнении таких задач обычно требуется ввод данных, манипуляции с объектами и т.д.
      * - 
            .. image:: _static/components/script_task.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_script_task.html

        - Скриптовая запускает скрипт (т.е. последовательность действий) или программный код, который выполняется автоматически.
      * - 

            .. image:: _static/components/notification_task.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_notifications.html

        - Задача-уведомление используется для отправки уведомлений пользователям
      * - 
            .. image:: _static/components/service_task.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_service_task.html

        - Сервисная задача используется для обозначения подключения сторонних сервисов, не относящихся к среде выполнения бизнес-процесса. 
      * - 
            .. image:: _static/components/set_status_task.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_set_status.html

        - Установка статуса. Элемент позволяет производить смену статуса в создаваемом бизнес-процессе.
      * - 
            .. image:: _static/components/business_rule_task.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_business_rule_task.html

        - Задача бизнес-правило служит для вызова :ref:`решения DMN<dmn_decision>` из процесса BPMN, используется для синхронного выполнения одного или нескольких правил.
      * - 
            .. image:: _static/components/call_activity.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_call_activity.html

        - Элемент схемы процесса, который позволяет вызывать другой процесс в рамках уже выполняемого.
      * - 
            .. image:: _static/components/gateway.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_gateway.html
           
        - Шлюзы контролируют поток движения в процессе. 
      
      * - 
            .. image:: _static/components/seq_flow.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_seq_flow.html

        - Поток управления используется для связи элементов потока BPMN (событий, процессов, шлюзов).
      * - 
            .. image:: _static/components/subprocess.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_sub_process.html

        - Подпроцесс. Действие, которое может включать в себя: другие действия, шлюзы, события и потоки операций.
      * - 
            .. image:: _static/components/events.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_events.html

        - Элемент потока управления, который отражает состояние, влияющее на ход выполнения процесса. События могут инициировать действия процесса, либо являться их результатами.
      * - 
            .. image:: _static/components/multi_instance.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_multi_instance.html

        - Multi Instance (многоэкземплярная активность). Способ определения повторения определенного шага в бизнес-процессе.
      * - 
            .. image:: _static/components/pool_participant.png
                :width: 100
                :target: https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_pool.html

        - Пул и дорожка используются для отображения исполнителей процесса BPMN. 


