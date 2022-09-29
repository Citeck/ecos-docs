rabbitmq-app
==============

Назначение:
--------------

Образ брокера сообщений Rabbitmq

Теги:
------

**rabbitmq:3.7.18-management-alpine** - используется официальный образ

Базовые образы:
----------------

* **rabbitmq:3.7.18-management-alpine** - образ версии 3.7.18 c интегрированным плагином managment на базе alpine linux

Шаблон сервиса docker-compose:
-------------------------------

.. code-block::

	rabbitmq:
		logging:
		options:
			max-size: "10m"
			max-file: "5"
		image: "rabbitmq:3.7.18-management-alpine"
		restart: unless-stopped
		stop_grace_period: 1m
		container_name: rabbitmq
		hostname: rabbitmq
		environment:
            - RABBITMQ_DEFAULT_USER=rabbitmqadmin
            - RABBITMQ_DEFAULT_PASS=LKSjdlkj847Klhfc
            - RABBITMQ_DEFAULT_VHOST=/
        expose:
            - 15672/tcp
        ports: 
            - 35672:5672
        volumes:
            - /opt/rabbitmqdata:/var/lib/rabbitmq
        networks:
            - app_network

Используемые переменные:
----------------------------

* **RABBITMQ_DEFAULT_USER** - логин создаваемого пользователя по умолчанию

* **RABBITMQ_DEFAULT_PASS** - пароль пользователя

* **RABBITMQ_DEFAULT_VHOST** - создаваемый виртуальный хост

Известные проблемы:
---------------------

* k8s после пересоздания пода при условии что приложение развернуто как statesful контейнер уходит в crash loopback

* Не реализовано конфигурирование дополнительных виртуальных хостов, пользователей, наделение правами пользователей

Типовой вывод успешного развертывания в лог контейнера:

.. code-block::

	rabbitmq                    | 2020-05-12 20:35:36.412 [info] <0.8.0> Feature flags: list of feature flags found:
	rabbitmq                    | 2020-05-12 20:35:36.413 [info] <0.8.0> Feature flags: feature flag states written to disk: yes
	rabbitmq                    | 2020-05-12 20:35:36.754 [info] <0.264.0> 
	rabbitmq                    |  Starting RabbitMQ 3.7.18 on Erlang 22.1.1
	rabbitmq                    |  Copyright (C) 2007-2019 Pivotal Software, Inc.
	rabbitmq                    |  Licensed under the MPL.  See https://www.rabbitmq.com/
	rabbitmq                    | 
	rabbitmq                    |   ##  ##
	rabbitmq                    |   ##  ##      RabbitMQ 3.7.18. Copyright (C) 2007-2019 Pivotal Software, Inc.
	rabbitmq                    |   ##########  Licensed under the MPL.  See https://www.rabbitmq.com/
	rabbitmq                    |   ######  ##
	rabbitmq                    |   ##########  Logs: <stdout>
	rabbitmq                    | 
	rabbitmq                    |               Starting broker...
	rabbitmq                    | 2020-05-12 20:35:36.756 [info] <0.264.0> 
	rabbitmq                    |  node           : rabbit@rabbitmq
	rabbitmq                    |  home dir       : /var/lib/rabbitmq
	rabbitmq                    |  config file(s) : /etc/rabbitmq/rabbitmq.conf
	rabbitmq                    |  cookie hash    : 69+WXGG5CrjDEU7Bmh7IbA==
	rabbitmq                    |  log(s)         : <stdout>
	rabbitmq                    |  database dir   : /var/lib/rabbitmq/mnesia/rabbit@rabbitmq
	rabbitmq                    | 2020-05-12 20:35:36.807 [info] <0.264.0> Running boot step pre_boot defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.807 [info] <0.264.0> Running boot step rabbit_core_metrics defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.808 [info] <0.264.0> Running boot step rabbit_alarm defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.843 [info] <0.284.0> Memory high watermark set to 6202 MiB (6504172748 bytes) of 15507 MiB (16260431872 bytes) total
	rabbitmq                    | 2020-05-12 20:35:36.900 [info] <0.301.0> Enabling free disk space monitoring
	rabbitmq                    | 2020-05-12 20:35:36.900 [info] <0.301.0> Disk free limit set to 50MB
	rabbitmq                    | 2020-05-12 20:35:36.924 [info] <0.264.0> Running boot step code_server_cache defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.924 [info] <0.264.0> Running boot step file_handle_cache defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.925 [info] <0.316.0> FHC read buffering:  OFF
	rabbitmq                    | 2020-05-12 20:35:36.925 [info] <0.316.0> FHC write buffering: ON
	rabbitmq                    | 2020-05-12 20:35:36.924 [info] <0.315.0> Limiting to approx 1048476 file handles (943626 sockets)
	rabbitmq                    | 2020-05-12 20:35:36.929 [info] <0.264.0> Running boot step worker_pool defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.929 [info] <0.265.0> Will use 4 processes for default worker pool
	rabbitmq                    | 2020-05-12 20:35:36.929 [info] <0.265.0> Starting worker pool 'worker_pool' with 4 processes in it
	rabbitmq                    | 2020-05-12 20:35:36.930 [info] <0.264.0> Running boot step database defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.955 [info] <0.264.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
	rabbitmq                    | 2020-05-12 20:35:37.025 [info] <0.264.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
	rabbitmq                    | 2020-05-12 20:35:37.025 [info] <0.264.0> Peer discovery backend rabbit_peer_discovery_classic_config does not support registration, skipping registration.
	rabbitmq                    | 2020-05-12 20:35:37.025 [info] <0.264.0> Running boot step database_sync defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.025 [info] <0.264.0> Running boot step feature_flags defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step codec_correctness_check defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step external_infrastructure defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step rabbit_registry defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step rabbit_auth_mechanism_cr_demo defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step rabbit_queue_location_random defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step rabbit_event defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_auth_mechanism_amqplain defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_auth_mechanism_plain defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_exchange_type_direct defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_exchange_type_fanout defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_exchange_type_headers defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_exchange_type_topic defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_mirror_queue_mode_all defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_mirror_queue_mode_exactly defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_mirror_queue_mode_nodes defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_priority_queue defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Priority queues enabled, real BQ is rabbit_variable_queue
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_queue_location_client_local defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_queue_location_min_masters defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step kernel_ready defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_sysmon_minder defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.033 [info] <0.264.0> Running boot step rabbit_epmd_monitor defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.067 [info] <0.264.0> Running boot step guid_generator defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.069 [info] <0.264.0> Running boot step rabbit_node_monitor defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.070 [info] <0.343.0> Starting rabbit_node_monitor
	rabbitmq                    | 2020-05-12 20:35:37.070 [info] <0.264.0> Running boot step delegate_sup defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.070 [info] <0.264.0> Running boot step rabbit_memory_monitor defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.071 [info] <0.264.0> Running boot step core_initialized defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.071 [info] <0.264.0> Running boot step upgrade_queues defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_connection_tracking defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_connection_tracking_handler defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_exchange_parameters defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_mirror_queue_misc defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_policies defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.101 [info] <0.264.0> Running boot step rabbit_policy defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.101 [info] <0.264.0> Running boot step rabbit_queue_location_validator defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.101 [info] <0.264.0> Running boot step rabbit_vhost_limit defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.101 [info] <0.264.0> Running boot step rabbit_mgmt_reset_handler defined by app rabbitmq_management
	rabbitmq                    | 2020-05-12 20:35:37.102 [info] <0.264.0> Running boot step rabbit_mgmt_db_handler defined by app rabbitmq_management_agent
	rabbitmq                    | 2020-05-12 20:35:37.102 [info] <0.264.0> Management plugin: using rates mode 'basic'
	rabbitmq                    | 2020-05-12 20:35:37.102 [info] <0.264.0> Running boot step recovery defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.113 [info] <0.446.0> Making sure data directory '/var/lib/rabbitmq/mnesia/rabbit@rabbitmq/msg_stores/vhosts/628WB79CIFDYO9LJI6DKMI09L' for vhost '/' exists
	rabbitmq                    | 2020-05-12 20:35:37.117 [info] <0.446.0> Starting message stores for vhost '/'
	rabbitmq                    | 2020-05-12 20:35:37.117 [info] <0.450.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_transient": using rabbit_msg_store_ets_index to provide index
	rabbitmq                    | 2020-05-12 20:35:37.119 [info] <0.446.0> Started message store of type transient for vhost '/'
	rabbitmq                    | 2020-05-12 20:35:37.119 [info] <0.453.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_persistent": using rabbit_msg_store_ets_index to provide index
	rabbitmq                    | 2020-05-12 20:35:37.124 [info] <0.446.0> Started message store of type persistent for vhost '/'
	rabbitmq                    | 2020-05-12 20:35:37.352 [info] <0.264.0> Running boot step load_definitions defined by app rabbitmq_management
	rabbitmq                    | 2020-05-12 20:35:37.352 [info] <0.264.0> Running boot step empty_db_check defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.352 [info] <0.264.0> Running boot step rabbit_looking_glass defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.352 [info] <0.264.0> Running boot step rabbit_core_metrics_gc defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.353 [info] <0.264.0> Running boot step background_gc defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.353 [info] <0.264.0> Running boot step connection_tracking defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.353 [info] <0.264.0> Setting up a table for connection tracking on this node: tracked_connection_on_node_rabbit@rabbitmq
	rabbitmq                    | 2020-05-12 20:35:37.353 [info] <0.264.0> Setting up a table for per-vhost connection counting on this node: tracked_connection_per_vhost_on_node_rabbit@rabbitmq
	rabbitmq                    | 2020-05-12 20:35:37.354 [info] <0.264.0> Running boot step routing_ready defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.354 [info] <0.264.0> Running boot step pre_flight defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.354 [info] <0.264.0> Running boot step notify_cluster defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.354 [info] <0.264.0> Running boot step networking defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.362 [info] <0.704.0> started TCP listener on [::]:5672
	rabbitmq                    | 2020-05-12 20:35:37.362 [info] <0.264.0> Running boot step direct_client defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.430 [info] <0.754.0> Management plugin: HTTP (non-TLS) listener started on port 15672
	rabbitmq                    | 2020-05-12 20:35:37.430 [info] <0.860.0> Statistics database started.
	rabbitmq                    | 2020-05-12 20:35:37.431 [info] <0.859.0> Starting worker pool 'management_worker_pool' with 3 processes in it
	rabbitmq                    |  completed with 3 plugins.
	rabbitmq                    | 2020-05-12 20:35:37.739 [info] <0.8.0> Server startup complete; 3 plugins started.
	rabbitmq                    |  * rabbitmq_management
	rabbitmq                    |  * rabbitmq_management_agent
	rabbitmq                    |  * rabbitmq_web_dispatch
