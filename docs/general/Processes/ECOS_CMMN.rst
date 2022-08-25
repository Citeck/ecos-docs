ECOS CMMN
=========

.. contents:: 
   :depth: 5

Общие сведения
---------------

CMMN + ecos process - движок бизнес процессов.

Движок создан для ускорения и сокращения объемов миграций - **definition** процесса не хранится в разрезе каждого кейса в Alfresco, а имеет свой **datasource** (ecos-process микросервис).

В общем виде последовательность шагов бизнес-движка при выполнении каких-либо действий с кейсом (создание/завершение задачи/выполнение пользовательского действия и тд):

1. В движок поступает событие (**Event**).

2. Начинается транзакция в Alfresco.

3. В процессе выполнения, запрашивается **state** и/или **definition** посредством команд (через RabbitMQ) из ecos-process микросервиса.

4. Выполняются действия по процессу (активация или завершение активностей и тд).

5. Перед коммитом транзакции, измененный **state** сохраняется в ecos-process посредством команд, новый **stateId** сохраняется в ноду.

6. Транзакция коммитится, фиксируется новый **stateId** для ноды, исходя из которого будут происходить дальнейшие действия.

Схематично это можно показать в следующем виде:

 .. image:: _static/cmmn/CMMN.png
       :width: 600
       :align: center
       :alt: Колонки

В случае проблем во время транзакции, в том числе после отправки нового **state** в микросервис - откат транзакции не меняет **stateId** в ноде кейса и мы не теряя данных, может продолжать работать с кейсом с последней зафиксированной общей в обоих инстансах точки.

Стоит отметить, состояния в микросервисе иммутабельны и хранятся в микросервисе вне зависимости от того, что на него уже не указывает ни один кейс. Это позволяет в будущем дополнить реализацию нового CMMN функционалом отката процесса.

Интеграция CMMN с ecos-process
-------------------------------

Интеграция осуществляется через библиотеку **ecos-commands**.

Микросервис **ecos-process** реализует на своей стороне несколько command executor'ов, которыми пользуется CMMN для получения/создания/обновления состояние или поиска конкретного описания процесса.

Команды и их роли, описаны в таблице:

.. list-table:: 
      :widths: 5 5 5 40
      :header-rows: 1
      :class: tight-table  

      * - Название команды
        - Структура запроса
        - Структура ответа
        - Описание
      * - **create-proc-instance**
        - | procType: String
          | ecosTypeRef: RecordRef
          | alfTypes: String[]
        - | procDefId: String
          | procDefRevId: String
        - | Создает новый пустой инстанс процесса (состояние) в микросервисе.
          | Возвращает идентификатор процесса и идентификатор состояния.
          | Идентификатор состояния обязателен для обновления состояния в будущем.
          | Вызывается при создании кейса единоразово.
      * - **get-proc-def-rev**
        - | procType: String
          | procDefRevId: String
        - | id: String
          | format: String
          | data: byte[]
          | procDefId: String
          | version: int
        - | Производит поиск по recisionId описания конкретного процесса.
          | В data - хранится описание процесса, которое парсится в удобный формат и позже кешируется.
      * - **create-proc-instance**
        - | procDefRevId: String
          | recordRef: RecordRef
        - | procId: String
          | procStateId: String
          | procStateData: byte[]
        - | Создает новый пустой инстанс процесса (состояние) в микросервисе.
          | Возвращает идентификатор процесса и идентификатор состояния.
          | Идентификатор состояния обязателен для обновления состояния в будущем.
          | Вызывается при создании кейса единоразово.
      * - **get-proc-state**
        - | procType: String
          | procStateId: String
        - | procDefRevId: String
          | stateData: byte[]
          | version: int
        - | Получение по stateId состояния процесса с данными.
          | Состояние хранится в том же виде, в котором происходило и сохранение (см. update-proc-state).
      * - **update-proc-state**
        - | prevProcStateId: String
          | stateData: byte[]
        - | procStateId: String
          | version: int
        - | Сохранение в микросервисе нового обновленного состояния.
          | Возвращает идентификатор новой версии состояния.

Примечание: procType для CMMN всегда имеет значение ``cmmn``.

Результат выполнения команд ``find-proc-def ``и ``get-proc-def-rev`` кешируется следующим образом:

Для команды ``find-proc-def`` кешируется идентификатор ревизии, который нужен для выполнения следующей команды. Ключом кеша является структура ``ecosTypeRef+alfTypes``. Используется Google Guava кеш.

Для команды ``get-proc-def-rev`` дела обстоят несколько сложнее. После выполнения команды, описание процесса парсится в удобный формат для процесса (см описание парсинга в соседней статье) и результат парсинга уже кешируется. Ключом кеша является идентификатор ревизии.  Используется Google Guava кеш.

Полностью работу с микросервисом ecos-process берет на себя сервис ``ru.citeck.ecos.icase.activity.service.eproc.EProcActivityServiceImpl``. Так же, он может предоставлять информацию по доп кешам конкретного дефинишена.

Интеграция CMMN с таймерами ecos-process
------------------------------------------

Микросервис **ecos-process** позволяет “зашедулить” некоторую команду на выполнение в будущем, в какой-то момент времени.

Последовательность следующая:

1. Срабатывает активность таймера в CMMN.

2. CMMN отправляет команду в ecos-process со временем, в которое эту команду нужно вернуть и описанием ответной команды.

3. Проходит отведенное время, ecos-process отправляет ответную команду в приложение, указанное для ответной команды (в данном случае, Alfresco).

4. Завершается активность таймера в CMMN.


Команды для управления таймерами со стороны ecos-process:

.. list-table:: 
      :widths: 5 5 5 40
      :header-rows: 1
      :class: tight-table  
      
      * - Название команды
        - Структура запроса
        - Структура ответа
        - Описание
      * - **create-timer**
        - | 
            
            .. code-block::

                     {   triggerTime: Instant,    
                            command: {        
                            id: String,        
                            targetApp: String,        
                            type: String,        
                            body: ObjectData    
                            }
                     }
        
        - | 
           
           .. code-block::

              {    
	              timerId: String
              }

        - | Создает таймер в ecos-process.
          | После прошествия времени, которое указано в **triggerTime**, ecos-process составит команду на основании структуры command и отправит ее в **targetApp** из структуры command.
          | Микросервис, если в body не было указано поле с названием **timerId**, то добавит туда настоящий из ecos-process **timerId**.
      * - **cancel-timer**
        - | 
           
           .. code-block::

              {    
	              timerId: String
              }

        - | 
           
           .. code-block::

               {    
	              wasCancelled: boolean
               }

        - | Отменяет таймер в ecos-process по идентификатору.

Новый CMMN реализует executor с типом **eproc-timer-occur** для реакции на таймеры.
Если ошибочно установленный (к примеру, оставшийся после отката транзакции) таймер вернет команду в CMMN, движок не отреагирует эту команду, так как, таймер с таким **id** не соответствует активности таймера.

Парсинг описания для нового CMMN
----------------------------------

Основную работу по парсингу выполняет класс ``ru.citeck.ecos.icase.activity.service.eproc.importer.parser.CmmnSchemaParser``.

Парсинг состоит из двух стадий:

С помощью JAXB, парсит **definition** в структуры старого CMMN.

Структуры старого CMMN парсит в единый объект **ProcessDefinition**'а с вложенными структурами активностей разных типов, с описаниями переходов и тд.

Вторая стадия особенна тем, что во время нее не только собирается **ProcessDefinition**, но и строятся кеши, которые будут возвращены с **ProcessDefinition** в виде структуры **OptimizedProcessDefinition**.
На данный момент, структура оптимизированного описания процесса следующая:

.. code-block::

       public class OptimizedProcessDefinition {
              private Definitions xmlProcessDefinition;
              private ProcessDefinition processDefinition;
              private Map<String, ActivityDefinition> idToActivityCache;
              private Map<String, SentryDefinition> idToSentryCache;
              private Map<SentrySearchKey, List<SentryDefinition>> sentrySearchCache;
              private Map<String, Set<ActivityDefinition>> roleVarNameToTaskDefinitionCache;
       }

где:

* **xmpProcessDefinition** - результат первой парсинга JAXB (первой стадии парсинга). Обязателен для импорта ролей и элементов кейса.

* **processDefinition** - неоптимизированное описание процесса, результат второй стадии парсинга.

* **idToActivityCache** - кеш ActivityDefinition’ов по идентификаторам.

* **idToSentryCache** - кеш SentryDefinition'ов по идентификаторам.

* **sentrySearchCache** - кеш для поиска SentryDefinition'ов, которые могут сработать при прошествии события, описанного в SentrySearchKey. Смысл этого кеша в том, чтоб без перебора всего процесса найти те sentry, которые могут произойти при событии какого-то типа для определенного SourceRef. В дальнейшем, будут выполнены для этих sentry их evaluator'ы и только те что вернули true - сработают sentry. Активности, привязанные к этим sentry триггерами - перейдут в новое состояние согласно описанным переходам. SentrySearchKey состоит из SourceRef+EventType.

* **roleVarNameToTaskDefinitionCache** - кеш названий ролей к ActivityDefinition с типом “пользовательская задача”. Используется для синхронизации изменившихся ролей с запущенными задачами.

Импорт кейса
-------------

Для импорта кейсов - давно существует бихейвиор ``ru.citeck.ecos.behavior.CaseTemplateBehavior``.

Процесс импорта новой реализации CMMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Процесс импорта можно расписать по следующим шагам:

1. Определение в бихейвиоре, импортировать ли CMMN кейс? Если да, то продолжаем.

2. Парсинг **ProcessDefinition**, расписанного в соседней статье.

3. Импорт ролей.

4. Импорт элементов кейса.

5. Создание нового состояния в микросервисе (с помощью команды **create-proc-instance**, описанной в соседней статье).

6. Сохранение **stateId** и **processId** в ноду кейса.

7. Создание **ProcessInstance** исходя из **ProcessDefinition** перебором активностей. **ProcessInstance** сохраняется в транзакции.

8. Отправка события **case-created** по процессу.

Как включить новую реализацию CMMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Первое на что смотрится, какая реализация вообще включена в системном журнале конфигурации по ключу ``ecos-case-process-type``. Может быть 2 значения:

- **alf** - Всегда выбирать alfresco реализацию CMMN.

- **eproc** - Выбирать ecos-process реализацию CMMN при условии, что для этого типа включена новая реализация. Иначе - выбирать alfresco реализацию CMMN.

Как включить eproc реализацию для конкретного типа при условии, что eproc реализация включена в системном журнале
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Класс ``ru.citeck.ecos.icase.activity.service.eproc.importer.EProcCaseImporter`` имеет список типов, доступных для новой реализации CMMN.

Чтобы зарегистрировать новый тип - можно создать бин класса ``ru.citeck.ecos.icase.activity.service.eproc.importer.EProcTypeRegistrar``.

Пример для коробочных договоров:

.. code-block::
       
       <bean id="contracts.eproc.registrarForEnabled" class="ru.citeck.ecos.icase.activity.service.eproc.importer.EProcTypeRegistrar">
              <property name="alfTypes">
                     <list>
                            <value>{http://www.citeck.ru/model/contracts/1.0}agreement</value>
                     </list>
              </property>
       </bean>

Поддерживает наследование типов alfresco, то есть, если указать ``sys:base`` тип - то eproc реализация будет доступна для всех типов (при условии, что в журнале eproc реализация включена).

Поддерживает указание не только alfresco типов, но и **ecosType (RecordRef)**.

Как работает движок
--------------------

Триггером для начала обработки внутри процесса всегда является событие (**Event**).

Чтобы началась обработка конкретного Event, нужно, чтобы произошла какая-либо из активностей следующих возможных типов (**eventType**):

* ``activity-started`` - срабатывает при запуске активности (внутреннее событие процесса).

* ``activity-stopped`` - срабатывает при завершении активности (внутреннее событие процесса).

* ``stage-children-stopped`` - срабатывает при завершении дочерней активности, при условии, что все дочерние элементы не активны (внутреннее событие).

* ``case-created`` - срабатывает единоразово при создании кейса (внешнее событие).

* ``case-properties-changed`` - срабатывает при изменении свойств процесса (внешнее событие, инициатор - бихейвиор).

* ``user-action`` - срабатывает при выполнении действия пользователем из виджета действий (внешнее событие).

После срабатывания, например, **“activity-started” eventType** для активности с id=”id-2” - начнется поиск из кешей Sentry с подходящими параметрами.

Найденные Sentry будут проверены evaluator'ами и уже для тех, что были пропущены evaluator'ами - будет запущена обработка события.

Сработавшее событие смотрит из своей Sentry, к чему она привязана по следующей схеме (некоторые переходы по сущностям опущены для поддержания простоты усвоения последовательности шагов):

 .. image:: _static/cmmn/CMMN_1.png
       :width: 600
       :align: center
       :alt: Колонки

где процесс из ``ActivityTransitionDefinition(1)`` смотрит **toState**. В зависимости от его значения:

* ``toState=Started (fromState=Not started)`` - В данном случае будет запущена активность процесса с привязанной definition(2) текущего процесса. Если активность уже была запущена и она перезапускаема - будет произведен reset перед запуском активности.

* ``toState=Completed (fromState=Started)`` - В данном случае будет остановлена активность процесса с привязанной definition(2) текущего процесса.

 

В итоге, запускаемые или останавливаемые активности триггируют события, которые могут влиять на состояния других активностей. Такая рекурсивная цепочка действий и является сутью работы движка.

Цепочка действий прекратится, когда последние отработавшие активности не найдут sentry, которые бы могли отработать.

 

Основные классы для управления активностями и триггирования событий:

* ``ru.citeck.ecos.icase.activity.service.eproc.EProcCaseActivityDelegate``

* ``ru.citeck.ecos.icase.activity.service.eproc.EProcCaseActivityEventDelegate``

Как работают таймеры
----------------------
При запуске активности с типом **“Таймер”** - происходит отправка команды в микросервис ecos-process на создание таймера.

После того, как таймер дотикает - происходит обратная команда из ecos-process в альфреско, которая останавливает активность таймера. Остановка активности таймера начинает триггерить смену состояний других активностей, завязанных на него и процесс идет дальше.

Evaluator'ы для событий
------------------------

После того, как sentry был найден, нужно определить, нужно ли триггировать данное событие.

За это ответственны evaluator'ы, описание которых можно найти в **SentryDefinition** сущности. 

В новой реализации CMMN, при триггировании события, конвертируются **EvaluatorDefinition** в понятные для **RecordEvaluatorService** структуры вида **RecordEvaluatorDto** и скармливаются, непосредственно, сервису **RecordEvaluatorService**.

Если сервис вернул true - значит, событие происходит. Иначе - игнорируется.

Конвертация **EvaluatorDefinition** в **RecordEvaluatorDto** происходит в классе ``ru.citeck.ecos.icase.activity.service.eproc.EProcCaseEvaluatorConverter``. Маппинг доступных эвалюаторов можно посмотреть там же.

Command'ы для действий
-----------------------

Команды происходят синхронно и на локальном инстансе (Alfresco).

Всю работу делает класс ``ru.citeck.ecos.icase.commands.CaseCommandsServiceImpl``.

Алгоритм примерно следующий:

1. В старой или новой реализации CMMN запускается активность с типом Action. Каждый движок своими средствами обращается к CaseCommandsService с идентификатором активности.

2. CaseCommandsService вытягивает из активности тип события.

3. По типу события ищет зарегистрированный Provider команд.

4. Собирает с помощью провайдера команду.

5. Отправляет команду на выполнение.


Список существующих команд:

* Выполнить скрипт (``ru.citeck.ecos.icase.commands.executors.ExecuteScriptCommandExecutor``);

* Fail, просто выбрасывает ошибку. Используется с каким-нибудь Evaluator'ом (``ru.citeck.ecos.icase.commands.executors.FailCommandExecutor``);

* Сигнал БП (``ru.citeck.ecos.icase.commands.executors.SendWorkflowSignalCommandExecutor``);

* Установить статус кейса (``ru.citeck.ecos.icase.commands.executors.SetCaseStatusCommandExecutor``);

* Установить переменную процесса (``ru.citeck.ecos.icase.commands.executors.SetProcessVariableCommandExecutor``);

* Установить переменную кейса (``ru.citeck.ecos.icase.commands.executors.SetPropertyValueCommandExecutor``).


Полезные JS-скрипты при работе с CMMN + ecos-process
------------------------------------------------------

Получение дерева активностей с состояниями и датами старта (выводимые данные можно расширить, указано в комментарии в коде). Актуально, пока конструктор кейса не разработан.

.. code-block::

       var document = search.findNode('workspace://SpacesStore/2523f47a-f9aa-4320-81d7-6551c2e42fcc');
	getActivities(document, 0);

	function getActivities(parent, level) {
		var activities = CaseActivityService.getActivities(parent);
		for (var i in activities) {
			var activity = activities[i];
			printActivity(activity, level);
			var childActivities = CaseActivityService.getActivities(activity);
			getActivities(activity, level + 1);
		}
	}

	function printActivity(activity, level) {
		var spaces = '';
		for (var i = 0; i < level; i++) {
			spaces = spaces + '    ';
		}
		print(spaces + activity.title + " : " + activity.state); // Тут можно расширить вывод другими данными из сущности CaseActivity.
	}

Сброс кэша шаблонов кейсов (актуально если шаблоны меняются через журнал описаний процессов).

.. code-block::

       var srv = services.get('eprocActivityService');

	var cache1 = Packages.org.apache.commons.lang.reflect.FieldUtils.readField(srv, 'typesToRevisionIdCache', true);
	cache1.invalidateAll();

	var cache2 = Packages.org.apache.commons.lang.reflect.FieldUtils.readField(srv, 'revisionIdToProcessDefinitionCache', true);
	cache2.invalidateAll();

Проверка наличия шаблона для типа в обход кэшей:

.. code-block::

       var srv = services.get('eprocActivityService');
       var commandsService = Packages.org.apache.commons.lang.reflect.FieldUtils.readField(srv, 'commandsService', true);
       var findProcDefCommand = new Packages.ru.citeck.ecos.icase.activity.service.eproc.commands.dto.request.FindProcDef();
       findProcDefCommand.setProcType("cmmn");
       findProcDefCommand.setEcosTypeRef(Packages.ru.citeck.ecos.records2.RecordRef.valueOf("emodel/type@supplementary-agreement/6ce21c23-d1e7-43b3-994b-2c3c305d320d"));
       print(commandsService.executeSync(findProcDefCommand, "eproc"));


Проверка наличия шаблона для заявки с учетом кэшей:

.. code-block::

       var srv = services.get('eprocActivityService');
       print(srv.getFullDefinition(Packages.ru.citeck.ecos.records2.RecordRef.valueOf("workspace://SpacesStore/45a5d9cf-502f-4622-bf41-040df6d599e5")));

Повторное применение шаблона кейса к документу без статуса или в статусе “Error while starting the process/ОШИБКА ПРИ СТАРТЕ ПРОЦЕССА“ (ecos-process-start-error): 

.. code-block::

       var document = search.findNode("workspace://SpacesStore/***");
       if (document.hasAspect("req:hasCompletenessLevels")) {
	       document.removeAspect("req:hasCompletenessLevels");
       }
       services.get('caseTemplateBehavior').onAddAspect(document.nodeRef, citeckUtils.createQName('icase:case'));

Сброс и перезапуск EPROC процесса кейса

.. code-block::

       var document = search.findNode('workspace://SpacesStore/6bb46ade-b5d0-4c0b-bca6-71298e6979a7');
       CaseActivityService.reset(document);
       caseActivityEventService.fireEvent(document, 'case-created');

Переприменение шаблона кейса (запустить процесс заново с последней версией шаблона)

.. code-block::

       Выполнение в 2 этапа
       >>>>> 1. Сбрасываем состояние кейса и кэш шаблонов

       var document = search.findNode('workspace://SpacesStore/6558016c-e787-4f24-9d43-34d2739f01a2');

       var srv = services.get('eprocActivityService');
       var cache1 = Packages.org.apache.commons.lang.reflect.FieldUtils.readField(srv, 'typesToRevisionIdCache', true);
       cache1.invalidateAll();
       var cache2 = Packages.org.apache.commons.lang.reflect.FieldUtils.readField(srv, 'revisionIdToProcessDefinitionCache', true);
       cache2.invalidateAll();

       CaseActivityService.reset(document);

       >>>>> 2. Сбрасываем для кейса шаблон и состояние, запускаем импорт и стартуем новый процесс:

       document.properties['icaseEproc:stateId'] = null;
       document.properties['icaseEproc:definitionRevisionId'] = null;

       document.save();

       var roles = document.childAssocs['icaseRole:roles'];
       for each(var role in roles) {
	       role.remove();
       }
       services.get('EProcCaseImporter').importCase(Packages.ru.citeck.ecos.records2.RecordRef.valueOf("" + document.nodeRef))
       caseActivityEventService.fireEvent(document, 'case-created');
