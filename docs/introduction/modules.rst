Модули и микросервисы, доступные в ECOS
=======================================

.. contents::
   :depth: 2

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

      * - :ref:`Корреспонденция. Исходящие документы <ecos-outdoc>`
        - Автоматизация процесса работы с исходящими документами: согласование, подписание, регистрация, отправка. 
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
        - 
             .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - 

             .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - ecos-uiserv
        - | Микросервис UI конфигураций, 
          | Предоставляет элементы UI и хранящий их настройки (меню, журналы, UI конфиги, формы, настройки журналов, дашборды).
        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - ecos-model
        - | Микросервис моделей
          | Отвечает за информацию о типах, шаблонах нумерации и о матрицах прав.
        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 
        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - ecos-history
        - | Микросервис истории
          | Подписан на события в системе и сохраняет информацию о них в БД.
        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`ecos-apps<apps_service>`
        - | Микросервис приложений ECOS
          | Отвечает за доставку приложений ECOS к целевым сервисам.
        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`ecos-notifications<notifications>`
        - | Микросервис нотификаций
          | Отвечает за отправку уведомлений (email, push-нотификации и др.).
        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`ecos-process<process>`
        - | Микросервис процессов. 
          | Отвечает за процессы кейс-менеджмента и BPMN.
        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`ecos-integrations<integration>`
        - | Микросервис для интеграции с внешними системами (SAP, 1C, Rabbit MQ и тд.).
        - 

           .. image:: _static/modules/red.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`ecos-transformations<transformation>`
        - | Микросервис для преобразования (трансформации) контента, генерации документов по шаблонам, которые можно подгрузить с проектом или добавить через инструменты администратора, :ref:`формирования PDF-файла со штрихкодом<barcode_pdf>`, конвертации всех офисных форматов в PDF.
        - 

           .. image:: _static/modules/red.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`ecos-content<content_service>`
        - | Микросервис для обеспечения хранения файлов в системе в определенное файловое хранилище.
        - 

           .. image:: _static/modules/red.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - :ref:`ecos-edi <ecos-edi>`
        - | Микросервис с вынесенной логикой ЭДО из микросервиса :ref:`интеграции<integration>`.
        - 

           .. image:: _static/modules/red.png
              :width: 30
              :align: center 

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

      * - ecos-ecom
        - | Микросервис для парсинга данных из email, telegram бота.

        - 

           .. image:: _static/modules/green.png
              :width: 30
              :align: center 

        - 

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
      * - :ref:`Синхронизация пользователей из LDAP<LDAP_sync>`
        - Можно создать несколько конфигураций синхронизации из LDAP, указав различные настройки - например, сервера, домены, фильтры и т.д.
      * - :ref:`ECOS KeyCloak Extension<keycloak_extension>`
        - Возможность создания или формирование событий ECOS при возникновении пользовательских и админских событий Keycloak 
