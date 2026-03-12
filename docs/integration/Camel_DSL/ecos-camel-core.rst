.. _ecos-camel-core:

Библиотека ecos-camel-core
========================================

Библиотека является надстройкой над Apache Camel, которая адаптирована для работы с платформой Citeck.

.. note::

   Для работы с библиотекой необходима enterprise лицензия.

Подключение
-----------------------

Добавьте зависимость в нужном микросервисе:

.. code-block:: xml

   <dependency>
       <groupId>ru.citeck.ecos.ent.camel</groupId>
       <artifactId>ecos-camel-core</artifactId>
   </dependency>

Подходящая версия будет загружена из родительского POM.

Пример использования
-----------------------------------------

Создайте компонент с настройками роутов. Он запустит новый контекст после старта приложения:

.. code-block:: java

   package ru.citeck.ecos.webapp.demo;

   import jakarta.annotation.PostConstruct;
   import kotlin.Unit;
   import lombok.RequiredArgsConstructor;
   import lombok.SneakyThrows;
   import org.apache.camel.Endpoint;
   import org.apache.camel.builder.RouteBuilder;
   import org.apache.groovy.util.Maps;
   import org.springframework.beans.factory.DisposableBean;
   import org.springframework.stereotype.Component;
   import ru.citeck.ecos.camel.context.EcosCamelContext;
   import ru.citeck.ecos.camel.context.EcosCamelContextFactory;
   import ru.citeck.ecos.commons.data.DataValue;
   import ru.citeck.ecos.records2.predicate.model.Predicates;
   import ru.citeck.ecos.webapp.api.EcosWebAppApi;

   @Component
   @RequiredArgsConstructor
   public class EcosCamelExample extends RouteBuilder implements DisposableBean {

       // для базовой работы нужны два бина:
       private final EcosWebAppApi ecosWebAppApi;           // запуск после инициализации приложения
       private final EcosCamelContextFactory contextFactory; // создание нового контекста

       // ссылку на контекст сохраняем в поле для последующей остановки
       private EcosCamelContext context = null;

       @SneakyThrows
       @PostConstruct
       public void init() {
           // создаём и запускаем контекст только после инициализации приложения
           ecosWebAppApi.doBeforeAppReady(0, () -> {
               createAndStartContext();
               return Unit.INSTANCE;
           });
       }

       @SneakyThrows
       private void createAndStartContext() {
           // создаём новый контекст и регистрируем роуты
           context = contextFactory.createContext().build();
           context.addRoutes(this);
           context.start();
       }

       @Override
       public void configure() {

           // endpoint для прослушивания событий ECOS с типом "record-created"
           // и фильтром по типу записей "demo-type"
           Endpoint endpoint = getContext().getEndpoint(
               "ecos-event:record-created",
               Maps.of(
                   "attributes", Maps.of(
                       "recordRef", "record?id",
                       "id",        "record?localId",
                       "name",      "record?disp",
                       "textField", "record.textField"
                   ),
                   "filter",        Predicates.eq("typeDef.id", "demo-type"),
                   "transactional", true
               )
           );

           from(endpoint)
               .to("log:after-event-received")
               .process(exchange -> {
                   DataValue body = exchange.getMessage().getBody(DataValue.class);

                   DataValue newBody = DataValue.createObj();
                   newBody.set("id",        body.get("id"));
                   newBody.set("name",      body.get("name"));
                   newBody.set("textField", body.get("textField"));

                   exchange.getMessage().setBody(newBody);
               })
               .to("log:after-processing")
               // создаём новую сущность в источнике данных emodel/demo-type-2
               .to("ecos-records-mutate:?sourceId=emodel/demo-type-2");
       }

       @Override
       public void destroy() throws Exception {
           if (context != null) {
               context.close();
           }
       }
   }

Пример демонстрирует следующий сценарий:

1. При старте приложения через ``@PostConstruct`` создаётся и запускается новый ``EcosCamelContext``.
2. Роут подписывается на событие ``record-created`` по типу ``demo-type``, извлекая нужные атрибуты записи.
3. В ``process``-шаге формируется новый объект с полями, необходимыми для создания записи в целевом источнике.
4. Результат передаётся в endpoint ``ecos-records-mutate``, который создаёт новую сущность в ``emodel/demo-type-2``.
5. При остановке приложения контекст корректно завершается в методе ``destroy()``.

.. seealso::

   :ref:`Endpoint ecos-records-mutate <EcosRecordsMutateEndpoint>`
