Список микросервисов, доступных в Community/Enterprise
========================================================

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
        - Микросервис реализует API шлюз взаимодействия с остальными микросервисами

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - ecos-uiserv
        - | Микросервис, предоставляющий элементы ui и хранящий их настройки (меню, журналы, UI конфиги, формы, настройки журналов, дашборды).
        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - ecos-model
        - | Микросервис моделей 
          | Отвечает за информацию о типах, шаблонах нумерации и о матрицах прав.
        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - ecos-history
        - | Микросервис истории
          | Подписан на события в системе и сохраняет информацию о них в БД.
        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - :ref:`ecos-apps<apps_service>`
        - | Микросервис приложений ECOS
          | Отвечает за доставку приложений ECOS к целевым сервисам.
        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - :ref:`ecos-notifications<notifications>`
        - | Микросервис нотификаций
          | Отвечает за отправку уведомлений (email, push-нотификации и др.).
        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - :ref:`ecos-process<process>`
        - | Микросервис процессов. 
          | Отвечает за процессы кейс-менеджмента и BPMN.
        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - :ref:`ecos-integrations<integration>`
        - | Микросервис для интеграции с внешними системами (SAP, 1C, Rabbit MQ и тд.).
        - |

           .. image:: _static/list/red.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - :ref:`ecos-transformations<transformation>`
        - | Микросервис для преобразования (трансформации) контента. На данный момент обеспечивает:
          | - Конвертацию из doc/docx в pdf
          | - Накладывание баркода на pdf файлы

        - |

           .. image:: _static/list/red.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - ecos-ecom
        - | Микросервис для парсинга данных из email, telegram бота.
        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 
      * - :ref:`ecos-content<content_service>`
        - | Микросервис для обеспечения хранения файлов в системе в определенное файловое хранилище.
        - |

           .. image:: _static/list/red.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/list/green.png
              :width: 30
              :align: center 