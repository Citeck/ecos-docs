rabbitmq-app
==============

Назначение:
--------------

Образ брокера сообщений Rabbitmq

Теги:
------

**rabbitmq:3.12.12-management** - используется официальный образ

Базовые образы:
----------------

* **rabbitmq:3.12.12-management** - образ версии 3.12.12 c интегрированным плагином managment

Шаблон сервиса docker-compose:
-------------------------------

.. code-block::

	rabbitmq:
		logging:
		options:
			max-size: "10m"
			max-file: "5"
		image: "rabbitmq:3.12.12-management"
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

Типовой вывод успешного развертывания в лог контейнера:

.. code-block::

    [notice] <0.44.0> Application syslog exited with reason: stopped
    [notice] <0.230.0> Logging: switching to configured handler(s); following messages may not be visible in this log output
    [notice] <0.230.0> Logging: configured log handlers are now ACTIVE
    [info] <0.230.0> ra: starting system quorum_queues
    [info] <0.230.0> starting Ra system: quorum_queues in directory: /var/lib/rabbitmq/mnesia/rabbit@rabbitmq-dev/quorum/rabbit@rabbitmq-dev
    [info] <0.316.0> ra system 'quorum_queues' running pre init for 0 registered servers
    [info] <0.317.0> ra: meta data store initialised for system quorum_queues. 0 record(s) recovered
    [notice] <0.322.0> WAL: ra_log_wal init, open tbls: ra_log_open_mem_tables, closed tbls: ra_log_closed_mem_tables
    [info] <0.230.0> ra: starting system coordination
    [info] <0.230.0> starting Ra system: coordination in directory: /var/lib/rabbitmq/mnesia/rabbit@rabbitmq-dev/coordination/rabbit@rabbitmq-dev
    [info] <0.329.0> ra system 'coordination' running pre init for 0 registered servers
    [info] <0.330.0> ra: meta data store initialised for system coordination. 0 record(s) recovered
    [notice] <0.335.0> WAL: ra_coordination_log_wal init, open tbls: ra_coordination_log_open_mem_tables, closed tbls: ra_coordination_log_closed_mem_tables
    [info] <0.230.0> 
    [info] <0.230.0>  Starting RabbitMQ 3.12.12 on Erlang 25.3.2.9 [jit]
    [info] <0.230.0>  Copyright (c) 2007-2023 Broadcom Inc and/or its subsidiaries
    [info] <0.230.0>  Licensed under the MPL 2.0. Website: https://rabbitmq.com
    
      ##  ##      RabbitMQ 3.12.12
      ##  ##
      ##########  Copyright (c) 2007-2023 Broadcom Inc and/or its subsidiaries
      ######  ##
      ##########  Licensed under the MPL 2.0. Website: https://rabbitmq.com
    
      Erlang:      25.3.2.9 [jit]
      TLS Library: OpenSSL - OpenSSL 3.1.5 30 Jan 2024
      Release series support status: supported
    
      Doc guides:  https://rabbitmq.com/documentation.html
      Support:     https://rabbitmq.com/contact.html
      Tutorials:   https://rabbitmq.com/getstarted.html
      Monitoring:  https://rabbitmq.com/monitoring.html
    
      Logs: <stdout>
    
      Config file(s): /etc/rabbitmq/conf.d/10-defaults.conf
    
      Starting broker...2024-02-19 07:39:39.882850+00:00 [info] <0.230.0> 
    [info] <0.230.0>  node           : rabbit@rabbitmq-dev
    [info] <0.230.0>  home dir       : /var/lib/rabbitmq
    [info] <0.230.0>  config file(s) : /etc/rabbitmq/conf.d/10-defaults.conf
    [info] <0.230.0>  cookie hash    : I5O997hmvOcshbu1gB6G/Q==
    [info] <0.230.0>  log(s)         : <stdout>
    [info] <0.230.0>  data dir       : /var/lib/rabbitmq/mnesia/rabbit@rabbitmq-dev
    [info] <0.230.0> Running boot step pre_boot defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_global_counters defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_osiris_metrics defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_core_metrics defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_alarm defined by app rabbit
    [info] <0.354.0> Memory high watermark set to 25657 MiB (26903694540 bytes) of 64143 MiB (67259236352 bytes) total
    [info] <0.356.0> Enabling free disk space monitoring (disk free space: 481622982656, total memory: 67259236352)
    [info] <0.356.0> Disk free limit set to 50MB
    [info] <0.230.0> Running boot step code_server_cache defined by app rabbit
    [info] <0.230.0> Running boot step file_handle_cache defined by app rabbit
    [info] <0.359.0> Limiting to approx 1048479 file handles (943629 sockets)
    [info] <0.360.0> FHC read buffering: OFF
    [info] <0.360.0> FHC write buffering: ON
    [info] <0.230.0> Running boot step worker_pool defined by app rabbit
    [info] <0.337.0> Will use 12 processes for default worker pool
    [info] <0.337.0> Starting worker pool 'worker_pool' with 12 processes in it
    [info] <0.230.0> Running boot step database defined by app rabbit
    [info] <0.230.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
    [info] <0.230.0> Successfully synced tables from a peer
    [info] <0.230.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
    [info] <0.230.0> Successfully synced tables from a peer
    [info] <0.230.0> Peer discovery backend rabbit_peer_discovery_classic_config does not support registration, skipping registration.
    [info] <0.230.0> Running boot step tracking_metadata_store defined by app rabbit
    [info] <0.382.0> Setting up a table for connection tracking on this node: tracked_connection
    [info] <0.382.0> Setting up a table for per-vhost connection counting on this node: tracked_connection_per_vhost
    [info] <0.382.0> Setting up a table for per-user connection counting on this node: tracked_connection_per_user
    [info] <0.382.0> Setting up a table for channel tracking on this node: tracked_channel
    [info] <0.382.0> Setting up a table for channel tracking on this node: tracked_channel_per_user
    [info] <0.230.0> Running boot step networking_metadata_store defined by app rabbit
    [info] <0.230.0> Running boot step feature_flags defined by app rabbit
    [info] <0.230.0> Running boot step codec_correctness_check defined by app rabbit
    [info] <0.230.0> Running boot step external_infrastructure defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_event defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_registry defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_auth_mechanism_amqplain defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_auth_mechanism_cr_demo defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_auth_mechanism_plain defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_exchange_type_direct defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_exchange_type_fanout defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_exchange_type_headers defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_exchange_type_topic defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_mirror_queue_mode_all defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_mirror_queue_mode_exactly defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_mirror_queue_mode_nodes defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_priority_queue defined by app rabbit
    [info] <0.230.0> Priority queues enabled, real BQ is rabbit_variable_queue
    [info] <0.230.0> Running boot step rabbit_queue_location_client_local defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_queue_location_min_masters defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_queue_location_random defined by app rabbit
    [info] <0.230.0> Running boot step kernel_ready defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_sysmon_minder defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_epmd_monitor defined by app rabbit
    [info] <0.390.0> epmd monitor knows us, inter-node communication (distribution) port: 25672
    [info] <0.230.0> Running boot step guid_generator defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_node_monitor defined by app rabbit
    [info] <0.394.0> Starting rabbit_node_monitor (in ignore mode)
    [info] <0.230.0> Running boot step delegate_sup defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_memory_monitor defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_fifo_dlx_sup defined by app rabbit
    [info] <0.230.0> Running boot step core_initialized defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_channel_tracking_handler defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_connection_tracking_handler defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_definitions_hashing defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_exchange_parameters defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_mirror_queue_misc defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_policies defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_policy defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_queue_location_validator defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_quorum_memory_manager defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_stream_coordinator defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_vhost_limit defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_mgmt_reset_handler defined by app rabbitmq_management
    [info] <0.230.0> Running boot step rabbit_mgmt_db_handler defined by app rabbitmq_management_agent
    [info] <0.230.0> Management plugin: using rates mode 'basic'
    [info] <0.230.0> Running boot step recovery defined by app rabbit
    [info] <0.430.0> Making sure data directory '/var/lib/rabbitmq/mnesia/rabbit@rabbitmq-dev/msg_stores/vhosts/628WB79CIFDYO9LJI6DKMI09L' for vhost '/' exists
    [info] <0.430.0> Starting message stores for vhost '/'
    [info] <0.440.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_transient": using rabbit_msg_store_ets_index to provide index
    [info] <0.430.0> Started message store of type transient for vhost '/'
    [info] <0.444.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_persistent": using rabbit_msg_store_ets_index to provide index
    [info] <0.430.0> Started message store of type persistent for vhost '/'
    [info] <0.430.0> Recovering 35 queues of type rabbit_classic_queue took 53ms
    [info] <0.430.0> Recovering 0 queues of type rabbit_quorum_queue took 0ms
    [info] <0.430.0> Recovering 0 queues of type rabbit_stream_queue took 0ms
    [info] <0.230.0> Running boot step empty_db_check defined by app rabbit
    [info] <0.230.0> Will not seed default virtual host and user: have definitions to load...
    [info] <0.230.0> Running boot step rabbit_observer_cli defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_looking_glass defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_core_metrics_gc defined by app rabbit
    [info] <0.230.0> Running boot step background_gc defined by app rabbit
    [info] <0.230.0> Running boot step routing_ready defined by app rabbit
    [info] <0.230.0> Running boot step pre_flight defined by app rabbit
    [info] <0.230.0> Running boot step notify_cluster defined by app rabbit
    [info] <0.230.0> Running boot step networking defined by app rabbit
    [info] <0.230.0> Running boot step definition_import_worker_pool defined by app rabbit
    [info] <0.337.0> Starting worker pool 'definition_import_pool' with 12 processes in it
    [info] <0.230.0> Running boot step cluster_name defined by app rabbit
    [info] <0.230.0> Running boot step direct_client defined by app rabbit
    [info] <0.230.0> Running boot step rabbit_maintenance_mode_state defined by app rabbit
    [info] <0.230.0> Creating table rabbit_node_maintenance_states for maintenance mode status
    [info] <0.230.0> Running boot step rabbit_management_load_definitions defined by app rabbitmq_management
    [info] <0.669.0> Resetting node maintenance status
    [info] <0.728.0> Management plugin: HTTP (non-TLS) listener started on port 15672
    [info] <0.756.0> Statistics database started.
    [info] <0.755.0> Starting worker pool 'management_worker_pool' with 3 processes in it
    [info] <0.770.0> Prometheus metrics: HTTP (non-TLS) listener started on port 15692
    [info] <0.669.0> Ready to start client connection listeners
    [info] <0.814.0> started TCP listener on [::]:5672 completed with 4 plugins.
    [info] <0.669.0> Server startup complete; 4 plugins started.
    [info] <0.669.0>  * rabbitmq_prometheus
    [info] <0.669.0>  * rabbitmq_management
    [info] <0.669.0>  * rabbitmq_management_agent
    [info] <0.669.0>  * rabbitmq_web_dispatch
    [info] <0.9.0> Time to start RabbitMQ: 9404729 us
