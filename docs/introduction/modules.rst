Модули и микросервисы, доступные в ECOS
=======================================

Модули
-------

.. list-table::
      :widths: 10 20 10 10
      :header-rows: 1
      :class: tight-table 
      
      * - Название
        - Описание
        - Community
        - Enterprise
      * - :ref:`Пропуска<ecos-order-pass>`
        - Автоматизация процесса принятия решения по выдаче пропуска.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`Совещания<ecos-meetings>`
        - Автоматизация процесса планирования и проведения совещаний.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

Микросервисы
-------------

.. list-table::
      :widths: 10 20 10 10
      :header-rows: 1
      :class: tight-table 
      
      * - Название
        - Описание
        - Community
        - Enterprise
      * - ecos-gateway
        - Шлюз, через который мы попадаем от клиента к серверу.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - ecos-uiserv
        - | Микросервис UI конфигураций. 
          | Отвечает за формы, журналы, UI действия, темы, дашборды, локализацию, иконки, конфигурацию меню.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - ecos-model
        - | Микросервис моделей
          | Отвечает за информацию о типах, шаблонах нумерации и о матрицах прав.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - ecos-history
        - | Микросервис истории
          | Подписан на события в системе и сохраняет информацию о них в БД.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - ecos-apps
        - | Микросервис приложений ECOS
          | Отвечает за доставку приложений ECOS к целевым сервисам.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - ecos-notifications
        - | Микросервис нотификаций
          | Отвечает за отправку уведомлений (email, push-нотификации и др.).
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - ecos-process
        - | Микросервис процессов. 
          | Отвечает за процессы кейс-менеджмента и BPMN.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - :ref:`ecos-integrations<integration>`
        - | Микросервис для интеграции с внешними системами (SAP, 1C, Rabbit MQ и тд.).
        - |

           .. image:: _static/modules/red.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - :ref:`ecos-transformations<transformation>`
        - | Микросервис для генерации документов по шаблонам
        - |

           .. image:: _static/modules/red.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
      * - ecos-ecom
        - | Микросервис для парсинга данных из email, telegram бота.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
