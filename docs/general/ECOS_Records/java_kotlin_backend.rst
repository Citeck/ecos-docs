Kotlin/Java Backend
====================

.. _java_kotlin_backend:

Для работы с RecordsAPI на kotlin/java бэкенде предусмотрена библиотека ecos-records - https://github.com/Citeck/ecos-records

Подключив библиотеку можно создать ``RecordsServiceFactory`` и получить оттуда все сервисы для работы с RecordsAPI.
Инициализация сервисов инкапсулирована в ``RecordsServiceFactory`` и не требует обязательного наличия DI механизмов.

Основной сервис для работы с RecordsAPI - это ``ru.citeck.ecos.records3.RecordsService``. Пример использования:

.. tabs::

   .. tab:: Kotlin

        .. code-block:: kotlin

            val serviceFactory = RecordsServiceFactory()
            val recordsService = serviceFactory.recordsServiceV1
        
            val value = HashMap<String, String>()
            value["someKey"] = "someValue"
        
            val attributeValue = recordsService.getAtt(value, "someKey").asText()
            println(attributeValue) // someValue
    
   .. tab:: Java

    .. code-block:: java
    
        RecordsServiceFactory serviceFactory = new RecordsServiceFactory();
        RecordsService recordsService = serviceFactory.getRecordsServiceV1();
        
        Map<String, String> value = new HashMap<>();
        value.put("someKey", "someValue");
    
        String attributeValue = recordsService.getAtt(value, "someKey").asText();
        System.out.println(attributeValue); // someValue

Здесь мы создаем новую мапу с одним значением и получаем из неё атрибут с именем someKey через ``RecordsService``.

Есть два основных сценария использования ``RecordsService``:

* Работа с уже готовыми данными как в примере выше. Нам не нужно никуда отправлять запросы и получение атрибутов проходит в пределах сервиса. В этом режиме доступно только получение атрибутов и Records DAO никак не задействуются.
   
* Работа с ссылками (``EntityRef``). В этом режиме сервис взаимодействует с источниками данных, функционал которых реализован через следующие интерфейсы:

  + ``RecordsDao`` базовый интерфейс для всех остальных ниже по списку. Содержит только один метод - ``String getId()``, который используется при регистрации ``RecordsDao`` в ``RecordsService``;

  + ``RecordsQueryDao`` для поиска записей;
  
  + ``RecordsAttsDao`` (``RecordAttsDao``) для получения атрибутов по заранее известным идентификаторам записей;
  
  + ``RecordMutateDao`` для создания или редактирования записей;
  
  + ``RecordsDeleteDao`` (``RecordDeleteDao``) для удаления записей;

*прим. - В скобках указаны варианты интерфейсов, где в метод приходит только один идентификатор записи. 
По своей сути эти интерфейсы отличаются от множественного варианта только отсутствием необходимости писать перебор идентификаторов вручную. Но
если есть какие-либо оптимизации, которые можно реализовать при пакетной обработке записей, то следует реализовывать интерфейсы, которые принимают коллекции записей*

*прим. - Records DAO - это реализация абстрактного понятия "Источник данных". Один Records DAO может представлять разные источники данных.*

При работе с Records DAO в зависимости от типа действия происходит следующее:

  + **Query**. Мы передаем в ``RecordsQueryDao`` поисковый запрос и ждем на выходе следующие типы значений (поддерживаются как коллекции этих значений так и значения в одном экземпляре):

    - ``EntityRef`` - ссылки на сущности. Если мы получаем ссылки, то сервис обращается к соответствующему ``RecordsAttsDao`` для получения атрибутов;

    - ``String`` - текстовый результат означает что мы вернули идентификаторы записей, по которым нам нужно получить атрибуты через RecordsAttsDao. Если в строке не указан другой Records DAO, то используется тот же, у которого мы вызывали query;
    
    - ``RecsQueryRes`` - список записей вместе с данными об их общем количестве;

    - ``Any`` - любое другое значение, которое обрабатывается с использованием реализаций интерфейса ``AttValueFactory``;

  + **Get attributes**. Получение атрибутов по идентификаторам записей. Этот метод используется либо с результатом Query из предыдущего пункта либо посредством прямого вызова ``recordsService.getAtts(...)``
    Метод возвращает любое значение, которое обрабатывается с использованием реализаций интерфейса ``AttValueFactory``;
    
  + **Mutate**. Изменение или создание записей через ``RecordMutateDao``


    В Records API создание записи происходит при мутации записи с пустым локальным идентификатором. Т.е. если мы хотим создать сущность в микросервисе emodel в источнике данных types-repo то делаем следующее:

    .. code-block::

      // здесь следует обратить внимание на строку 'emodel/types-repo@'. 
      // Согласно структуре RecordRef'а (ссылка внизу) здесь 
      // (AppName - "emodel", SourceId - "types-repo", LocalId - "" (пустая строка)) 
      let newRecord = Citeck.Records.get('emodel/types-repo@');

      newRecord.att("id", "id-value");
      newRecord.att("name", "Custom name");
      // В resultRecord будет созданная запись. 
      // Если мы задаем id вручную (как двумя строчками выше), 
      // то в resultRecord будет лежать то же самое что мы получим при выполнении
      // Citeck.Records.get('emodel/types-repo@id-value');
      // Если мы не указали вручную ID, то он сгенерируется в виде UUID.
      let resultRecord = await newRecord.save();
  
  + **Delete**. Удаление записей через ``RecordsDeleteDao``

**AttValue** - это интерфейс, который представляет собой значение, с которым умеет работать ``RecordsService`` при получении атрибутов. Методы интерфейса:

.. code-block:: java

    Promise<?> init() // инициализация значения перед тем как начать вычисление атрибутов
    Object getId() // идентификатор значения. Может быть как строкой, так и EntityRef  
    Object getDisplayName() // значение для скаляра "?disp"
    String asText() // значение для скаляра "?str"
    Object getAs(String type) // значение для спец. атрибута "_as"
    Double asDouble() // значение для скаляра "?num"
    Boolean asBoolean() // значение для скаляра "?bool"
    Object asJson() // значение для скаляра "?json"
    Object asRaw() // значение для скаляра "?raw"
    Object asBin() // значение для скаляра "?bin"
    has(String name) // значение для спец. атрибута "_has"
    Object getAtt(String name) // получить значение атрибута по его имени
    AttEdge getEdge(String name) // получить мета-информацию об атрибуте по его имени
    Object getType() // получить ECOS тип значения

**AttValueFactory** - это интерфейс для преобразования произвольных типов данных в имплементацию **AttValue**

.. code-block:: java
  
  // Проинициализировать фабрику. В основном используется для получения конвертеров для других типов. 
  // Например: attValuesConverter.getFactory(DataValueAttFactory.class)
  void init(attValuesConverter: AttValuesConverter)
  
  // Получить реализацию AttValue для значения
  AttValue getValue(T value)
  
  // Получить список доступных типов значений, которые может обрабатывать данная фабрика
  List<Class<*>> getValueTypes()
  
  // Получить приоритет фабрики. Чем выше приоритет, тем важнее фабрика в случае если для одного и того же типа нашлось две фабрики.
  int getPriority()

Для регистрации произвольных AttValueFactory нужно в библиотеке или микросервисе создать следующий файл::
  
  resources/META-INF/services/ru.citeck.ecos.records3.record.atts.value.factory.AttValueFactory

Внутри этого файла должно быть полное имя класса (вместе с пакетом) с вашей реализацией интерфейса **AttValueFactory**

Пример: https://github.com/Citeck/ecos-records/blob/master/ecos-records/src/test/resources/META-INF/services/ru.citeck.ecos.records3.record.atts.value.factory.AttValueFactory

Если для значения не нашлось подходящего ``AttValueFactory``, то используется стандартная фабрика ``BeanValueFactory``.
Эта фабрика работает со значением как с бином, у которого ищутся геттеры для атрибутов.

Например, если у нас есть следующий бин:

.. code-block:: java
   
    static class TestDto {
      private String field;    
      void setField(String value) {
        this.field = value;
      }
      String getField() {
        return field;
      }
    } 

То с точки зрения ``BeanValueFactory`` у этого бина есть значение с одним атрибутом "field". Пример работы:

.. code-block:: java

    RecordsServiceFactory serviceFactory = new RecordsServiceFactory();
    RecordsService recordsService = serviceFactory.getRecordsServiceV1();
    
    TestDto value = new TestDto();
    value.setField("field-value");
  
    String attributeValue = recordsService.getAtt(value, "someKey").asText();
    System.out.println(attributeValue); // field-value

Если же мы хотим изменить имя атрибута не меняя названия методов, то можно воспользоваться аннотацией ``AttName``:

.. code-block:: java

    static class TestDto {
      private String field;    
      void setField(String value) {
        this.field = value;
      }
      @AttName("otherName")
      String getField() {
        return field;
      }
    }
    ...
    TestDto value = new TestDto();
    value.setField("field-value-2");
  
    String attributeValue = recordsService.getAtt(value, "otherName").asText();
    System.out.println(attributeValue); // field-value-2

Аннотация ``@AttName`` помогает задать произвольное имя атрибута. Её можно использовать:

* На геттере, чтобы дать произвольное название атрибуту;
* На сеттере для конвертации DTO -> Схема атрибутов для запроса; (см. методы ``recordsService.getAtts(Any record, Class<?> atts)``)
* Аннотация на поле работает как для сеттера так и для геттера если они есть;

Аннотация ``@AttName`` может в качестве аргумента принимать значение ``"..."``. 
Такая запись означает, что все атрибуты из поля с этой аннотацией будут доступны так же и в нашем значении. Пример:

.. code-block:: java

   static class ParentDto {
     @AttName("...")
     private ChildDto child = new ChildDto(); // опустим сеттер, чтобы не усложнять пример
     public ChildDto getChild() {
       return child;
     }
   }
   static class ChildDto {
      public String getValue(): String {
        return "abc"; // геттер не обязательно должен отдавать значение поля. Его поведение может быть произвольным
      }
   }
   ...
   ParentDto value = new ParentDto();
   
   // Если бы аннотация AttName отсутствовала, то до значения 'abc' мы бы могли добраться так:
   // recordsService.getAtt(value, "child.value").asText();
   // Но с аннотацией @AttValue("...") можно обращаться к вложенному атрибуту так:
   
   String attributeValue = recordsService.getAtt(value, "value").asText();
   System.out.println(attributeValue); // abc

Так же особое значение имеют аннотации ``AttName`` где в качестве аргумента указан один из скаляров с вопросительным знаком. 
Например: ``@AttName("?str")``. Такие геттеры вызываются при загрузке скаляров.

``BeanValueFactory`` так же ищет в бине ряд специальных методов по их имени и аргументам (тип возвращаемого значения не важен):

.. code-block:: java
  
  Object getId() // значение для скаляра ?id
  Object getAsStr() // значение для скаляра "?str"
  Object getAsNum() // значение для скаляра "?num"
  Object getAsBool() // значение для скаляра "?bool"
  Object getAsJson() // значение для скаляра "?json"
  Object getAsRaw() // значение для скаляра "?raw"
  Object getAsBin() // значение для скаляра "?bin"
  Object getEcosType() // значение для атрибута "_type"
  Object getAs(String name) // значение для спец. атрибута "_as"
  Object has(String name) // значение для спец. атрибута "_has"
  Object getEdge(String name) // значение для спец. атрибута "_edge"
  Object getAtt(String name) // Значение атрибута по имени если не получилось найти геттер для него

Для отображаемого имени нашего бина ``BeanValueFactory`` ищет следующие методы в порядке убывания приоритета (используется первый найденный):

.. code-block:: java
  
  Object getDisplayName()
  Object getLabel()
  Object getTitle()
  Object getName()