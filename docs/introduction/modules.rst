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

      * - :ref:`Поручения<ecos-assignments>`
        - Постановка поручений на исполнение, и проверки результатов их исполнения при необходимости. 
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`Договоры<ecos-contract>`
        - Автоматизация процеса учета и согласования бумажных договоров, и документов, связанных с договорами.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`Корреспонденция. Входящие документы <ecos-indoc>`
        - Автоматизация процесса работы с входящими документами: регистрация, отправка на рассмотрение и исполнение. 
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`ОРД <ecos-order-ORD>`
        - автоматизации процесса работы с организационно-распорядительными документами: приказами, распоряжениями, нормативными актами, служебными записками и т.д.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`Офферы<ecos-offer>`
        - Автоматизация процесса подбора персонала по заявкам подразделений.
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`Service desk<ecos-service-desk>`
        - Автоматизация работы техподдержки с клиентскими обращениями (заявками).
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`CRM<ecos-crm>`
        - Поддержка процесса маркетинга, продаж и обслуживания клиентов компании
        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - |

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

Функциональность, доступная только в enterprise версии
--------------------------------------------------------

.. list-table:: 
      :widths: 20 40
      :header-rows: 1
      :class: tight-table 

      * - Функциональность
        - Описание
      * - :ref:`Виджет «Статистика процесса»<widget_process_statistics>`
        - Виджет визуализирует статистику по бизнес-процессу с отображением тепловой карты (heatmap). 
      * - :ref:`Виджет «Стадии»<widget_stages>`
        - Виджет визуализирует прохождение :ref:`ECOS стадий<stages>` документа.
      * - :ref:`Виджет «Канбан»<widget_kanban>`
        - Виджет добавляет в карточку :ref:`канбан доску<kanban_board>` с настраиваемым журналом, связанным атрибутам и шаблонами для удобства пользователя и быстрым взаимодействием со статусами через карточку.
      * - :ref:`Виджет «Графическая статистика»<widget_graphic_statistics>`
        - Виджет позволяет пользователям наглядно представлять и анализировать данные. Виджет поддерживает различные типы графиков: линейные, столбчатые, круговые.
      * - :ref:`Делегирование<delegation>`
        - Настройка передача своих задач или функций другим сотрудникам.
      * - :ref:`Редактирование матрицы прав<permissions>`
        - Настройка прав для типа данных.
      * - :ref:`Микросервис интеграции<integration>`
        - Интеграции с внешними системами (SAP, 1C, Rabbit MQ и тд.).
      * - :ref:`Микросервис трансформации<transformation>`
        - Микросервис для генерации документов по шаблонам, которые можно подгрузить с проектом или добавить через инструменты администратора, :ref:`формирования PDF-файла со штрихкодом<barcode_pdf>`, конвертации всех офисных форматов в PDF.
      * - :ref:`Синхронизация пользователей из LDAP<LDAP_sync>`
        - Можно создать несколько конфигураций синхронизации из LDAP, указав различные настройки - например, сервера, домены, фильтры и т.д.
      * - :ref:`ECOS KeyCloak Extension<keycloak_extension>`
        - Возможность создания или формирование событий ECOS при возникновении пользовательских и админских событий Keycloak 
