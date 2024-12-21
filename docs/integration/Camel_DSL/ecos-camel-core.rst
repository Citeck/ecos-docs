Библиотека ecos-camel-core
============================

.. _ecos-camel-core:

Библиотека является надстройкой над Apache Camel, которая адаптирована для работы с платформой Citeck.

.. note::

    Для работы с библиотекой необходима enterprise лицензия.

Для начала работы нужно добавить зависимость в нужном микросервисе:

.. code-block::

    <dependency>
    <groupId>ru.citeck.ecos.ent.camel</groupId>
    <artifactId>ecos-camel-core</artifactId>
    </dependency>

Подходящая версия будет загружена из родительского POM.

Подробнее про :ref:`ecos-records-mutate<EcosRecordsMutateEndpoint>`

Далее создаем компонент с настройками роутов, который запустит новый контекст после старта приложения:

.. code-block::

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
    
        // для базовой работы нам нужны два бина
        private final EcosWebAppApi ecosWebAppApi; // для запуска после инициализации приложения
        private final EcosCamelContextFactory contextFactory; // для создания нового контекста
    
        // ссылку на созданный контекст сохраняем в поле, чтобы потом можно было выполнить остановку.
        private EcosCamelContext context = null;
    
        @SneakyThrows
        @PostConstruct
        public void init() {
            // создаем и запускаем контекст только после инициализации приложения
            ecosWebAppApi.doBeforeAppReady(0, () -> {
                createAndStartContext();
                return Unit.INSTANCE;
            });
        }
    
        @SneakyThrows
        private void createAndStartContext() {
            // создаем новый контекст и регистрируем наши роуты
            context = contextFactory.createContext().build();
            context.addRoutes(this);
            context.start();
        }
    
        @Override
        public void configure() {
            
            // создаем новый endpoint, который слушает события ECOS с типом "record-created" и типом записей "demo-type"
            Endpoint endpoint = getContext().getEndpoint(
                "ecos-event:record-created",
                Maps.of(
                    "attributes", Maps.of(
                        "recordRef", "record?id",
                        "id", "record?localId",
                        "name", "record?disp",
                        "textField", "record.textField"
                    ),
                    "filter", Predicates.eq("typeDef.id", "demo-type"),
                    "transactional", true
                )
            );
    
            from(endpoint)
                .to("log:after-event-received")
                .process(exchange -> {
    
                    DataValue body = exchange.getMessage().getBody(DataValue.class);
    
                    DataValue newBody = DataValue.createObj();
                    newBody.set("id", body.get("id"));
                    newBody.set("name", body.get("name"));
                    newBody.set("textField", body.get("textField"));
    
                    exchange.getMessage().setBody(newBody);
                })
                .to("log:after-processing")
                // создаем новую сущность в источнике данных emodel/demo-type-2
                .to("ecos-records-mutate:?sourceId=emodel/demo-type-2");
        }
    
        @Override
        public void destroy() throws Exception {
            if (context != null) {
                context.close();
            }
        }
    }