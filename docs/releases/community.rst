Community
=============

4.9.0
-----

1. `Рабочее расписание <https://citeck-ecos.readthedocs.io/ru/latest/introduction/functions/work_calendar.html>`_ - функциональность для учета нерабочих дней.
    
2. В журналах :ref:`ширину колонки<column_width>` таблицы можно изменять и сохранять.

3. В журнале в столбце может отображаться общая сумма значений столбца. Включение или выключение отображения суммы для каждой колонки производится отдельно по каждому атрибуту в :ref:`настройках журнала<column_sum>`. 

4. Добавлен новый форматтер :ref:`Duration<DurationFormatter>`, при включении которого, продолжительность будет трансформироваться в часы, то есть 2d 3h 30m = 51h 30m

5. Добавлена возможность описывать `миксины <https://citeck-ecos.readthedocs.io/ru/latest/general/mixins.html#id2>`_ для любых ECOS типов в любом микросервисе.

6. Определены поддерживаемые форматы файлов для действия `Печатать <https://citeck-ecos.readthedocs.io/ru/latest/introduction/functions/actions.html#id2>`_

7. В форматтере :ref:`Color<ColoredFormatter>` добавлена возможность настройки условия отображения значения в определенном цвете в зависимости от значения данных в атрибуте.

8. К возможности выдавать ответ в виде ссылки на скачивания файла (использование config: implSourceId) только при выборе действия из журнала объектов, добавлена возможность аналогичного действия из :ref:`карточки объекта<mutate_action>`.

4.8.0
-----

1. BPMN редактор. Добавлен раздел :ref:`Администрирование БП<bpmn_admin>` позволяет наблюдать за состоянием опубликованных бизнес-процессов, получать подробную информацию о них и их запущенных экземплярах.

2. BPMN редактор. Добавлено :ref:`управление правами<bpmn_permissions>` в BPMN разделе.

3. BPMN редактор. Реализован запуск бизнес-процесса :ref:`у дочерних типов<inherit_bp_start>`.

4. BPMN редактор. Для информирования о наличии ошибок в схеме бизнес-процесса реализован :ref:`режим отображения ошибок<bpmn_linter>`. 

5. BPMN редактор. Добавлена возможность выгрузить модель :ref:`бизнес-процесса в Excel<bp_actions>` и загрузить :ref:`версию модели <widget_versions_journal>`.
   
6. В левое меню в раздел **Задачи** добавлен журнал :ref:`Задачи подчиненных<tasks>`, в котором отображаются задачи всех подчиненных пользователя.

7. Добавлена настройка :ref:`прав на конкретный тип данных<data_type_rights>`.

8. Добавлен OnlyOffice для правильной работы :ref:`предпросмотра документа<widget_doc_preview>`.

9. Добавлена возможность :ref:`отображать количество записей<journal_group>` в настройках группировки данных журнала.

4.7.0
-----

1.	Добавлен :ref:`модуль Корреспонденция. Входящие<ecos-indoc>`

2.	Добавлен :ref:`модуль Корреспонденция. Исходящие<ecos-outdoc>`

3.	Добавлен :ref:`модуль ОРД. Внутренние документы<ecos-order-ORD>`

4.  Добавлен :ref:`модуль Релизы<ecos-releases>`

5.  Реализована возможность сохранять бизнес-процесс как :ref:`черновик <save_bp>`


4.6.0
-----

1.	Расширены возможности поисковых запросов в источниках данных ECOS (ecos-data), реализовав `поддержку объединения таблиц <https://citeck-ecos.readthedocs.io/ru/latest/general/ecos_data.html#id1>`_

2.	Доступен иерархический интерфейс для работы с папками и документами `Doclib <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/journals/document_library.html>`_

3.	Реализованы  `динамические роли <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/%D0%A2%D0%B8%D0%BF%D1%8B_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.html#dmn>`_ на основе `DMN <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_dmn/editor/components/ecos_dmn_components_decision.html#dmn>`_, что дает возможность устанавливать гибкую логику, по которой будет произведено вычисление состава пользователей роли.

4.	Написан `гайд <https://citeck-ecos.readthedocs.io/ru/latest/case_sample/dmn_dynamic_role.html>`_ по использованию динамической роли DMN в бизнеc-процессе 

5.	Добавлена возможность проводить сортировку и группировку по полям из связанных таблиц.

6.	BPMN редактор. Добавлена поддержка `Error Events <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/events/ecos_bpmn_components_error.html>`_ , которое используется для обработки бизнес ошибок. 

7.	BPMN редактор. Добавлена поддержка `Terminate Event  <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/events/ecos_bpmn_components_termination.html>`_ , которое немедленное завершение выполнения процесса.

8.	BPMN редактор. Добавлена поддержка `Conditional Event <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/events/ecos_bpmn_components_conditional.html>`_ , которое используется для моделирования реакции бизнес-процесса на изменения условий.

9.	BPMN редактор. Добавлена поддержка `Service Task <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_service_task.html>`_ , которое используется для обозначения подключения сторонних сервисов, не относящихся к среде выполнения бизнес-процесса.

10.	Реализована возможность `настройки шаблонов <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/journals/kanban_board.html#id2>`_ для журналов в режиме для канбан доски. 

4.5.0
------

1.	Возможность `измененть исполнителя задачи <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/ecos_bpmn_tasks.html>`_ в бизнес-процессе при нажатии кнопки «Изменить исполнителя» в виджете «Все задачи».

2.	Микросервис нотификаций. Доработано `подключение к SMTP серверу <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/notifications/notifications_bulk_mail.html>`_ , чтобы его отсутствие не было блокером для работы микросервиса нотификаций. 

3.	BPMN редактор. Добавлена поддержка `Call activity <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_call_activity.html>`_ , который позволяет вызывать другой процесс в рамках уже выполняемого.

4.	BPMN редактор. Пользовательская задача. Приоритет не только выбирается из списка доступных, но и может быть добавлен `присвоением переменной <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_user_task.html>`_

5.	Добавлено отображение предыдущего комментария задачи в таблице виджета «Мои задачи».

6.	Реализована `защита от уязвимостей <https://citeck-ecos.readthedocs.io/ru/latest/introduction/ecos_modules/service_desk.html#id17>`_  при добавлении комментариев через email 

7.	Добавлен :ref:`модуль Офферы<ecos-offer>`


4.4.0
------

1.	Версионирование артефактов. В карточке артефакта в виджете «Журнал версий» представлены текущая и предыдущая версии артефакта с возможностью перехода между версиями и сравнения версий.

2.	Разработан гайд `по созданию простого бизнес-процесса <https://citeck-ecos.readthedocs.io/ru/latest/case_sample/equipment_request.html>`_

3.	Cоздать поручение можно из карточки документа, выбрав `действие «Создать поручение» <https://citeck-ecos.readthedocs.io/ru/latest/introduction/ecos_modules/tasks.html#ecos-tasks-action>`_ 

4.	Обеспечена синхронизация компонента формы `File Component с атрибутом documents и виджета «Документы» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/file.html#id6>`_, чтобы документы, загруженные через форму отображались в виджете и наоборот.

5.	Дочерние сущности удаляются `вместе с родителями <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/%D0%A2%D0%B8%D0%BF%D1%8B_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.html#ecos-model-types>`_

6.	Настройка связи `в обе стороны <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/%D0%A2%D0%B8%D0%BF%D1%8B_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.html#id29>`_

7.	BPMN. В Пользовательской задаче если форма задачи не указана, то `автоматически будут отображаться доступные вердикты задачи <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_user_task.html#id4>`_, заполненные в поле Результат задачи.

8.	Новый редактор `принятия решения DMN <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/DMN_ecos.html>`_  для более гибкой настройки процессов, которые помогают решать аналитические и автоматизационные задачи компаниям.

9.	В гайд по созданию простого бизнес-процесса добавлен `пример работы с редактором принятия решения DMN <https://citeck-ecos.readthedocs.io/ru/latest/case_sample/equipment_request_p2.html>`_

10.	BPMN. Добавлена поддержка `Business rule task <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_business_rule_task.html>`_ , который служит для вызова DMN Decision из процесса BPMN.

11.	Добавлена возможность `скрыть панель поиска по записям журнала <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/journals/new_journal.html#journal-settings>`_

12.	BPMN. В Скриптовую задачу добавлена возможность из BPMN вызывать `генерацию по указанному шаблону и запись в определенное свойство <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_script_task.html#templated-content>`_

13.	В тип данных добавлен `выбор статуса по умолчанию <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/%D0%A2%D0%B8%D0%BF%D1%8B_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.html#associations>`_. При сохранении кейса в состоянии «Черновик» автоматический старт бизнес- процесса не осуществляется. Автоматический старт произойдет только `при сабмите без состояния черновика. <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/ecos_bpmn_base_operations.html#submit>`_

4.3.0
------

1.	Кастомизирована страница авторизации keycloak.

2. Добавлен `модуль CRM <https://citeck-ecos.readthedocs.io/ru/latest/introduction/ecos_modules/crm.html>`_

3. Добавлен `модуль «Поручения» <https://citeck-ecos.readthedocs.io/ru/latest/introduction/ecos_modules/tasks.html>`_

4.	Добавлена возможность редактировать документ с помощью onlyoffice - реализовано `действие «Редактировать документ» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/onlyoffice_edit.html>`_ , которое открывает отдельную страницу с onlyoffice.

5.	В конфигурацию журналов для столбцов добавлен `«Атрибут для поиска» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/journals/new_journal.html#additional-column-settings>`_. Параметр будет использоваться на UI при построении запроса с фильтром по столбцу.

6.	Добавлена возможность `прикреплять вложения (attachments) <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/notifications/notifications_template.html#attachments-email>`_ к email уведомлению

7.	BPMN. Для полной работы с отправкой уведомлений добавлено `поле «Исходящий адрес» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_notifications.html>`_  в компоненте Уведомление, чтобы можно было показывать от кого отправляется письмо.

4.2.0
-------

1.	Добавлен `модуль Service Desk <https://citeck-ecos.readthedocs.io/ru/latest/introduction/ecos_modules/service_desk.html>`_

2.	BPMN. Добавлена возможность `логирования из ScriptTask <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_script_task.html#logger>`_ 

3.	BPMN. В Уведомлении добавлена возможность указывать `реципиентов (пользователи, группы, точные адреса) <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_notifications.html#id4>`_ напрямую и с использованием expressions.

4.	BPMN. В Пользовательской задаче добавлен срок выполнения . У каждой задачи может быть добавлено поле `«due date» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_user_task.html#id3>`_ , указывающее дату выполнения задачи (должна быть выполнена до или после определенной даты).

4.1.0
------

1.	BPMN. Добавлена поддержка следующих типов шлюза:

    -	`Инклюзивный (inclusive gateway) <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_gateway.html#id4>`_   
    -	`Шлюз на основе события (event based gateway) <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_gateway.html#id5>`_    

2.	BPMN. В шаблоне уведомления доступны к использованию следующие переменные:

    1.	Переменные из базового record. 
    2.	Переменные процесса. 
    3.	Переменные событий Ecos. 
    4.	Контекстные переменные Records API

 `Подробно о переменных <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_notifications.html#id6>`_

3.	BPMN. В событиях ECOS добавлена поддержка `событий о Records <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/components/events/ecos_bpmn_components_signal.html#id7>`_

4.0.0
------

1.	Новый BPMN редактор, разработанный на основе библиотеки редактора `bpmn-js <https://bpmn.io/>`_ и движка `camunda <https://camunda.com/>`_. Со следующими элементами процесса, адаптированными под ECOS:

    -	Пользовательская задача,
    -	Скриптовая задача,
    -	Уведомления,
    -	Установка статуса,
    -	Шлюзы,
    -	Потоки управления,
    -	Подпроцесс, 
    -	Multi Instance (многоэкземплярная активность),
    -	Пулы и дорожки.

 `Подробно о редакторе <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/BPMN_ecos.html>`_

2.	Осуществленаа миграция бизнес-процессов модулей «Пропуска» и «Совещания» на новый BPMN редактор. Работа в модулях описана в следующих разделах:

    - `Пропуска <https://citeck-ecos.readthedocs.io/ru/latest/introduction/ecos_modules/order_pass.html>`_
    - `Совещания <https://citeck-ecos.readthedocs.io/ru/latest/introduction/ecos_modules/meeting.html>`_

3.	Библиотека для быстрой `разработки новых микросервисов <https://citeck-ecos.readthedocs.io/ru/latest/general/Microservices/new_microservice.html#ecos>`_ 

4.	Обновлен виджет «Журнал версий». В виджете реализованы:

    -	отображение списка версий,
    -	сравнение версий,
    -	скачивание версии.

 `О виджете «Журнал версий» подробно <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#widget-versions-journal>`_

5.	Обновление виджета «История событий». В виджете фиксируются следующих события работы с задачами:

    -	Задача создана,
    -	Задача назначена,
    -	Задача завершена.

 `О виджете «История событий» подробно <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#widget-events-history>`_


