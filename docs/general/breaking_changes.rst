Критические изменения
=====================

Релиз 2025.8
---------------

.. _breaking_changes_2025.8:

Изменена логика вычисления прав по умолчанию для системных артифактов ecos-data (ecos-webapp-common:3.18.23). Если артефакт системный, то права на чтение имеют все пользователи, права на запись - только администраторы.

Если в пользовательских типах данных есть указанные как **system**, то к ним будет применена новая логика. Если необходимо сделать доступ на редактирование, то выставить **system=false**, тогда редактировать смогут все, либо сделать матрицу прав.


Релиз 2024.8
---------------

.. _breaking_changes_2024.8:

В рамках релиза 2024.8 было выполнено обновление всех коробочных микросервисов и библиотек.

Обновления версий
~~~~~~~~~~~~~~~~~~

1. Обновление версии java до 21й версии (последняя LTS на момент миграции);
2. Обновление spring boot до 3.3.2 (последняя стабильная на момент миграции);
3. Обновление spring до 6.1.11 (подтянулся при обновлении spring boot);
4. Обновление версии kotlin до 2.0.0
5. Обновление camunda до 7.21.0
6. Обновление всех остальных зависимостей до последних стабильных версий

Обновление технологий
~~~~~~~~~~~~~~~~~~~~~~~

Движок для скриптов nashorn был заменен на GraalVM JS. GraalVM JS -  современный аналог устаревшему nashorn. Обновление позволяет использовать функционал новых версий JS. 

`Подробнее <https://www.graalvm.org/latest/reference-manual/js/NashornMigrationGuide/>`_ о миграции и совместимости движков.

Доработки
~~~~~~~~~~~

1. Полностью переписан **ecos-gateway** на основе **spring-cloud-gateway** на реактивных технологиях и виртуальных потоках. Это позволит обрабатывать большое количество одновременных запросов, не упираясь в лимит потоков.
2. Доработаны **контексты** вроде AuthContext, I18nContext и др. с тем, чтобы они не заполняли стектрейс запроса на уровне HTTP фильтров (на 4-5 строк все стектрейсы по входящим HTTP запросам сократились).
3. Микросервисы больше не регистрируются в ecos-registry. **Service Discovery** работает на базе реестра приложений в Zookeeper.
4. Исправлена проблема, которая не давала подняться приложению с новой версией hazelcast, если приложение со старой версией еще работает (rolling update при повышении версии - Enterprise фича hazelcast).
5. Добавлен spring профиль **json_logs**. Если его включить, то логи будут записываться в виде json объектов.

Удаление устаревшего кода
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Удален старый RecordsService и все старые RecordsDao интерфейсы. Метод RecordsServiceFactory.recordsServiceV1 переименован в RecordsServiceFactory.recordsService
2. Удален RecordRef.
3. **RecordEvaluatorService** и связанные с ним классы перенесены из ecos-records в ecos-uiserv, т.к. данный функционал используется только там.
4. Все микросервисы используют стандартные библиотеки **jackson/snakeyaml/guava**.
5. **REST контроллер для RecordsAPI** удален из ecos-webapp-commons и размещен только в ecos-gateway. Микросервисы между собой должны общаться по ECOS WebAPI, REST нужен только для запросов извне.
6. Удалена **логика фасадов** из ecos-history и убрана его зависимость от mongo.

Совместимость
~~~~~~~~~~~~~~~

По Records API совместимость любых новых и старых микросервисов полная. Микросервисы с обновленным parent'ом перестают регистрироваться в ecos-registry и как следствие - старая версия ecos-gateway не может прокидывать на них обычные REST запросы (например /gateway/uiserv/api/ui-cache?types=theme). Если сначала обновить gateway до 3.0.0+, то любые другие микросервисы можно уже обновлять по отдельности.

Возможные проблемы со скриптами
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Новый движок в противовес старому использует подход "безопасный по умолчанию". Это означает что многие функции, которые были доступны в nashorn "из коробки" отключены.

В нашем решении мы включили некоторые из **этих функций по умолчанию**:

.. code-block::

    val defaultHostAccess: HostAccess = HostAccess.newBuilder(HostAccess.SCOPED)
            .allowMapAccess(true)
            .allowListAccess(true)
            .allowArrayAccess(true)
            .allowBigIntegerNumberAccess(true)
            .allowIterableAccess(true)
            .allowIteratorAccess(true)
            .allowAccessInheritance(true)
            .build()

Но некоторые части все еще требуют миграции (флаг совместимости с nashorn лучше не включать по возможности из соображений безопасности):  

   1. Функционал доступа к геттерам через простое указание имени свойства (т.е. возможность вместо abc.getName() писать abc.name ) в новом движке "из коробки" отключен. 
   2. Функционал доступа к java классам "из коробки" отключен.
   3. Java классы, с которыми идет работа внутри js должны иметь аннотацию @Export на методах и полях к которым должен быть доступ из скрипта.

Если есть глобальные проблемы в скриптах BPMN процессов или вычисляемых атрибутах или вычисляемых ролях, то всегда можно включить режим совместимости со старым js движком через spring свойства:

.. code-block::

    ecos.webapp.scripts.graaljs.camunda.nashornCompat: true // задается в ecos-process для скриптов в процессах
    ecos.webapp.scripts.graaljs.records.nashornCompat: true // задается в любом микросервисе где хранятся данные (как правило ecos-model)

Этот режим желательно включать только как временное решение, в рамках которого начать миграцию скриптов в совместимый с graalvm вид.

`Подробнее <https://www.graalvm.org/latest/reference-manual/js/NashornMigrationGuide/>`_ о миграции и совместимости движков.

Изменения в библиотеках
~~~~~~~~~~~~~~~~~~~~~~~

Все библиотеки с версиями, которые собираются на java 8 и предназначены для старых версий микросервисов и alfresco помечены постфиксом _j8 в имени версии и мастер ветка для них именуется master-j8.

Эти версии в дальнейшем будут вестись независимо от основной нумерации.  Исключением в данном случае является ecos-commons, который для java 21 имеет версию 3.4+, а для java 8 версию 2.* и мастер ветку master-2

Изменение классов и методов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 20 20
      :header-rows: 1
      :align: center
      :class: tight-table  

      * - До
        - После
      * - mu.KotlinLogging
        - io.github.oshai.kotlinlogging.KotlinLogging
      * - ecos.guava30.com.google.*
        - com.google.*
      * - ru.citeck.ecos.records2.RecordRef
        - ru.citeck.ecos.webapp.api.entity.EntityRef
      * - org.apache.commons.collections.*
        - org.apache.commons.collections4.*
      * - ecos.com.fasterxml.jackson210.*
        - com.fasterxml.jackson.*
      * - javax.*
        - | jakarta.* 
          | (не для всех классов, но если javax.* недоступно после повышения версии, то следует использовать jakarta)
      * - ecos.org.snakeyaml.engine21.*
        - org.snakeyaml.engine.*
      * - ru.citeck.ecos.commons.utils.func.*
        - ru.citeck.ecos.webapp.api.func.*
      * - ru.citeck.ecos.commons.promise.Promises
        - ru.citeck.ecos.webapp.api.promise.Promises
      * - ru.citeck.ecos.records2.rest.RemoteRecordsUtils.runAsSystem
        - ru.citeck.ecos.context.lib.auth.AuthContext.runAsSystem(J)

Мигрированные микросервисы
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 20 20
      :align: center
      :class: tight-table  

      * - ecos-model
        - 2.28.0+
      * - ecos-notifications
        - 2.20.0+
      * - ecos-content
        - 1.2.0+
      * - ecos-uiserv
        - 2.26.0+
      * - ecos-edi
        - 1.2.0+
      * - ecos-service-desk
        - 1.11.0+
      * - ecos-gateway
        - 3.0.0+
      * - ecos-process
        - 2.21.0+
      * - ecos-integrations
        - 2.21.0+
      * - ecos-ecom
        - 1.8.0+
      * - ecos-transformations
        - 1.11.0+
      * - ecos-history
        - 2.20.0+
      * - ecos-apps
        - 2.20.0+


Мигрированная версия ecos-community-core - 4.25.0