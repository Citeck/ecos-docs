.. _spring_boot_admin:

Spring Boot Admin
==================

**Spring Boot Admin** — системный административный интерфейс для веб-приложений Spring Boot.

Доступен по адресу: ``https://host/gateway/eapps/admin/wallboard``

Интерфейс представляет собой удобный UI поверх конечных точек Spring Boot Actuator и предоставляет:

* проверку работоспособности сервисов (health checks);
* мониторинг метрик;
* доступ к журналам (logs);
* информацию об окружении (environment);
* управление уровнями логирования;
* снятие thread dump.

.. list-table::
   :widths: 50 50
   :align: center

   * - .. image:: _static/spring_boot_admin/01.png
          :width: 600
          :align: center

     - .. image:: _static/spring_boot_admin/02.png
          :width: 600
          :align: center

.. list-table::
   :widths: 50 50
   :align: center

   * - .. image:: _static/spring_boot_admin/03.png
          :width: 600
          :align: center

     - .. image:: _static/spring_boot_admin/04.png
          :width: 600
          :align: center

Просмотр логов
--------------

Для оперативного просмотра логов микросервиса непосредственно в интерфейсе Spring Boot Admin необходимо активировать Spring Boot profile ``admin_logs`` у соответствующего микросервиса.

Это может быть полезно при траблшутинге, когда нет доступа к основному сборщику логов.

.. note::

   Доступно начиная с версии **ecos-webapp-commons 3.21.4**.

Документация
------------

Подробнее см. `официальную документацию проекта Spring Boot Admin <https://github.com/codecentric/spring-boot-admin>`_.
