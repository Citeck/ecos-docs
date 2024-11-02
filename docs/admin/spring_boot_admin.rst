Spring Boot Admin
==================

.. _spring_boot_admin:

Добавлен новый системный административный интерфейс для веб-приложений Spring Boot по адресу  https://host/gateway/eapps/admin/wallboard 

Spring Boot Admin представляет собой удобную прослойку пользовательского интерфейса поверх конечных точек Spring Boot Actuator. Конечные точки предлагают проверку работоспособности, мониторинг метрик, доступ к журналам, информации об окружающей среде и многое другое. 

.. list-table::
      :widths: 20 20
      :align: center

      * - |

            .. image:: _static/spring_boot_admin/01.png
                  :width: 600
                  :align: center

        - |

            .. image:: _static/spring_boot_admin/02.png
                  :width: 600
                  :align: center

В интерфейсе есть возможность снимать thread dump и управлять уровнями логирования.

.. list-table::
      :widths: 20 20
      :align: center

      * - |

            .. image:: _static/spring_boot_admin/03.png
                  :width: 600
                  :align: center

        - |

            .. image:: _static/spring_boot_admin/04.png
                  :width: 600
                  :align: center

Подробнее см. `официальную информацию проекта Spring Boot Admin <https://github.com/codecentric/spring-boot-admin>`_ 
