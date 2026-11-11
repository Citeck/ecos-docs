.. _mixins:

Миксины
===================

.. contents::
   :depth: 3

Внешние миксины атрибутов
--------------------------------------------------

Внешние миксины позволяют добавлять вычисляемые атрибуты к записям выбранного ECOS типа. Обработчик атрибута может находиться в другом приложении при настроенной межсервисной интеграции.

Требования
~~~~~~~~~~~~~~~~~~~~~~

Приложению с источником данных и приложению с обработчиком нужны совместимые версии ``ecos-records`` и ``ecos-webapp-commons`` с поддержкой пакета ``ru.citeck.ecos.records3.record.mixin.external``. Базовый интерфейс ``AttMixin`` и локальные миксины DAO сами по себе не обеспечивают внешнее межсервисное вычисление.

Spring-интеграция должна предоставлять ``ExtAttMixinService``, регистрировать бины конфигураторов и подключать удалённые обработчики. В ``ecos-webapp-commons`` реестр внешних атрибутов использует ZooKeeper (namespace ``ecos/records/extmixin``), а вычисление выполняется через web executor. Для межсервисной работы должны быть доступны реестр и web-вызовы между приложениями.

Описание
~~~~~~~~~~~~~~~~~~

В приложении с поддержкой внешних миксинов необходимо создать Spring-бин, реализующий интерфейс:

.. code-block:: text

    ru.citeck.ecos.records3.record.mixin.external.ExtAttMixinConfigurer

``RecordsExtMixinsRegistrar`` собирает такие бины и передаёт каждый в ``ExtAttMixinService.register``. Регистрация бина и настройка атрибутов — разные шаги: в примерах ниже настройки задаются методом ``configure`` конфигуратора.

Приведены фрагменты конфигураторов. Импорты ``ExtAttMixinConfigurer`` и ``ExtMixinConfig``, сигнатуры и доступные методы настроек необходимо согласовать с используемой версией ``ecos-records``. Обработчик в примере возвращает константную ссылку на пользователя и не требует атрибутов исходной записи, поэтому карта ``requiredAtts`` пуста.

.. tab-set::

   .. tab-item:: Kotlin

      .. code-block:: kotlin

         import org.springframework.stereotype.Component
         import ru.citeck.ecos.webapp.api.entity.EntityRef

         @Component
         class CustomExtMixinConfigurer : ExtAttMixinConfigurer {

             override fun configure(settings: ExtMixinConfig) {
                 settings.setEcosType("contract") // тип ECOS, к которому добавляется атрибут
                     .addProvidedAtt("newExtAtt") // имя добавляемого атрибута
                     .addRequiredAtts(emptyMap()) // обработчику не нужны атрибуты исходной записи
                     .withHandler { // код по вычислению атрибута
                         EntityRef.create("emodel","person", "admin") // возвращаем просто ссылку на другую сущность
                     }
             }
         }

   .. tab-item:: Java

      .. code-block:: java

         import java.util.HashMap;
         import java.util.Map;
         import org.jetbrains.annotations.NotNull;
         import org.springframework.stereotype.Component;
         import ru.citeck.ecos.webapp.api.entity.EntityRef;

         @Component
         public class CustomExtMixinConfigurer implements ExtAttMixinConfigurer {

             @Override
             public void configure(@NotNull ExtMixinConfig config) throws Exception {

                 Map<String, String> requiredAtts = new HashMap<>();

                 config.setEcosType("contract") // тип ECOS, к которому добавляется атрибут
                     .addProvidedAtt("newExtAtt") // имя добавляемого атрибута
                     .addRequiredAtts(requiredAtts) // атрибуты, которые нужны для вычисления значения нашего атрибута
                     .withHandler(data -> { // код по вычислению атрибута
                         return EntityRef.create("emodel", "person", "admin"); // возвращаем просто ссылку на другую сущность
                     });
             }
         }

Класс с ``@Component`` должен входить в область сканирования Spring. Вместо аннотации можно зарегистрировать конфигуратор явно через ``@Bean``.

После регистрации конфигуратора и доступности обработчика значение атрибута можно запрашивать через стандартный :ref:`Records API <Records_API>`.

Например, для загрузки нового атрибута в браузере можно выполнить следующий скрипт:

.. code-block:: javascript

    var rec = Records.get("emodel/contract@295ea260-df3e-493e-b27c-34b6c27e7fea"); // берем сущность с типом, на который мы добавили новый атрибут.
    await rec.load("newExtAtt", true); // загружаем значение нового атрибута
