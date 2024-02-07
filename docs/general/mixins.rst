Миксины
==========

.. contents::
   :depth: 3

Внешние миксины атрибутов
--------------------------

Внешние миксины позволяют расширять атрибутивный состав записей в любой части системы указывая только их ECOS тип.

Требования
~~~~~~~~~~~

Версия родительского проекта 2.21.0+ (для java 17) 1.49.0+ (для java 8) должна быть у приложения с источником данных и у приложения с описанием внешних миксинов.

Описание 
~~~~~~~~~

Для описания новых атрибутов необходимо создать в любом микросервисе новый бин, который реализует интерфейс: 

.. code-block::

    ru.citeck.ecos.records3.record.mixin.external.ExtAttMixinConfigurer

В этом интерфейсе 1 метод **register**, который принимает настройки, которые позволяют добавлять любое количество вычисляемых атрибутов. 

Пример на Kotlin:

.. code-block::

    @Component
    class CustomExtMixinConfigurer : ExtAttMixinConfigurer {
    
        override fun configure(settings: ExtMixinConfig) {
            settings.setEcosType("contract") // тип ECOS к которому добавляется новый атрибут. Атрибут добавляется к указанному типу и к его наследникам.
                .addProvidedAtt("newExtAtt") // имя добавляемого атрибута
                .addRequiredAtts(mapOf("ref" to "?id")) // атрибуты, которые нужны для вычисления значения нашего атрибута
                .withHandler { // код по вычислению атрибута
                    EntityRef.create("emodel","person", "admin") // возвращаем просто ссылку на другую сущность
                }
        }
    }

Пример на java:

.. code-block::

    public class CustomExtMixinConfigurer implements ExtAttMixinConfigurer {
    
        @Override
        public void configure(@NotNull ExtMixinConfig config) throws Exception {
    
            Map<String, String> requiredAtts = new HashMap<>();
    
            config.setEcosType("contract") // тип ECOS к которому добавляется новый атрибут. Атрибут добавляется к указанному типу и к его наследникам.
                .addProvidedAtt("newExtAtt") // имя добавляемого атрибута
                .addRequiredAtts(requiredAtts) // атрибуты, которые нужны для вычисления значения нашего атрибута
                .withHandler(data -> { // код по вычислению атрибута
                    return EntityRef.create("emodel", "person", "admin"); // возвращаем просто ссылку на другую сущность
                });
        }
    }

После описания новых атрибутов для типов ECOS можно пользоваться стандартным :ref:`Records API<Records_API>` для получения значения этих атрибутов. 

Например, для загрузки нового атрибута в браузере можно выполнить следующий скрипт:

.. code-block::

    var rec = Records.get("emodel/contract@295ea260-df3e-493e-b27c-34b6c27e7fea"); // берем сущность с типом, на который мы добавили новый атрибут.
    await rec.load("newExtMixin", true); // загружаем значение нового атрибута