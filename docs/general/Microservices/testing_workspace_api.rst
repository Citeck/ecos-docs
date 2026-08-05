.. _testing_workspace_api:

Тестирование с WorkspaceApiMock
===============================

.. contents::
   :depth: 4

Обзор
--------

Сервисы, использующие сущности с привязкой к рабочему пространству (workspace) —
например, ``ecos-uiserv`` — зависят от ``WorkspaceWebApi``, который обращается к
``ecos-model`` по HTTP для определения принадлежности к рабочему пространству. Во
время ``@SpringBootTest`` тестов ``ecos-model`` не запущен, поэтому
``WorkspaceWebApi.waitUntilEmodelApiIsAvailable()`` уходит в бесконечный цикл
ожидания, и тесты зависают навсегда.

Класс ``WorkspaceApiMock``, предоставляемый ``ecos-webapp-lib-spring-test``,
решает эту проблему. Он полностью реализует ``WorkspaceApi`` в памяти, не
выполняет HTTP-вызовов и автоматически обнаруживается Spring Boot в тестовой
области видимости.

Проблема: зависающие тесты
----------------------------

Цепочка вызовов, приводящая к зависанию:

.. code-block:: text

    BoardRecord.getRef()
      → WorkspaceServiceImpl.addWsPrefixToId()
        → WorkspaceWebApi.mapIdentifiers()
          → WorkspaceWebApi.waitUntilEmodelApiIsAvailable()
            → бесконечный цикл ожидания

Если тест затрагивает любой участок кода, который определяет идентификатор с
префиксом рабочего пространства, весь набор тестов зависнет, если не
предоставлена тест-совместимая реализация ``WorkspaceApi``.

Решение: WorkspaceApiMock
--------------------------

``WorkspaceApiMock`` поставляется в модуле ``ecos-webapp-lib-spring-test``
(в ``src/main``, поэтому он экспортируется как часть артефакта модуля). Он
аннотирован ``@Component``, поэтому компонентное сканирование Spring Boot
автоматически подхватывает его, когда модуль присутствует в тестовом classpath.

``ModelServiceFactoryInitializer`` был расширен для опциональной инъекции
любого бина ``WorkspaceApi``:

.. code-block:: kotlin

    @Autowired(required = false)
    var workspaceApi: WorkspaceApi? = null

    @PostConstruct
    fun init() {
        // ... другие инъекции ...
        workspaceApi?.let { modelServices.setWorkspaceApi(it) }
    }

Когда ``WorkspaceApiMock`` присутствует (тестовая область видимости), он
инъецируется и переопределяет ``WorkspaceWebApi``. В продуктивных развёртываниях
(где тестового модуля нет в classpath) ``ModelServiceFactory`` использует
``WorkspaceWebApi`` по умолчанию. Продуктивный код никак не затрагивается.

Настройка
---------

Добавьте ``ecos-webapp-lib-spring-test`` как тестовую зависимость в
``pom.xml`` вашего сервиса:

.. code-block:: xml

    <dependency>
        <groupId>ru.citeck.ecos.webapp</groupId>
        <artifactId>ecos-webapp-lib-spring-test</artifactId>
        <scope>test</scope>
    </dependency>

Это всё, что требуется. В любом ``@SpringBootTest`` бин ``WorkspaceApiMock``
автоматически обнаруживается и инъецируется в ``ModelServiceFactory``. Явный
``@Import`` или дополнительная конфигурация не нужны.

Настройка тестовых данных
--------------------------

Инъецируйте ``WorkspaceApiMock`` напрямую в тестовый класс, чтобы настроить
участников (members) и менеджеров рабочего пространства:

.. code-block:: kotlin

    @ExtendWith(EcosSpringExtension::class)
    @SpringBootTest(classes = [TestApp::class])
    class MyWorkspaceTest {

        @Autowired
        lateinit var workspaceApiMock: WorkspaceApiMock

        @Autowired
        lateinit var workspaceService: WorkspaceService

        @BeforeEach
        fun setUp() {
            workspaceApiMock.clear()  // всегда сбрасывайте состояние между тестами
        }

        @Test
        fun someWorkspaceScopedTest() {
            workspaceApiMock.addMember("my-workspace", "john.doe")
            workspaceApiMock.addManager("my-workspace", "admin")

            val workspaces = workspaceService.getUserWorkspaces("john.doe")
            assertThat(workspaces).contains("my-workspace")
        }
    }

Доступные методы ``WorkspaceApiMock``:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Метод
     - Описание
   * - ``addMember(workspace, user)``
     - Регистрирует ``user`` как участника ``workspace``.
   * - ``addManager(workspace, user)``
     - Регистрирует ``user`` как менеджера ``workspace``.
   * - ``clear()``
     - Удаляет всех добавленных ранее участников и менеджеров.

Поведение по умолчанию
------------------------

Пока данные не настроены через ``addMember()`` / ``addManager()``:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Метод
     - Поведение по умолчанию
   * - ``getUserWorkspaces(user)``
     - Возвращает ``setOf("user$<username>")`` — персональное рабочее
       пространство, что соответствует реальному поведению
       ``WorkspaceService``.
   * - ``getNestedWorkspaces(workspaces)``
     - Возвращает пустые множества для всех переданных рабочих пространств.
   * - ``mapIdentifiers(ids, type)``
     - Возвращает идентификаторы без изменений (тождественное отображение).
   * - ``isUserManagerOf(user, workspace)``
     - Возвращает ``false``.

.. important::

    ``WorkspaceApiMock`` — это Spring-бин с единственным экземпляром (singleton),
    общий для всех тестов в рамках одного тестового прогона. Состояние,
    настроенное в одном тесте, сохраняется и в следующем. **Всегда вызывайте**
    ``workspaceApiMock.clear()`` в ``@BeforeEach``, чтобы обеспечить изоляцию
    тестов.

Защита от регрессий
----------------------

Чтобы явно защититься от возможной будущей регрессии, из-за которой зависание
вернётся, помечайте чувствительные ко времени тесты аннотацией ``@Timeout``:

.. code-block:: kotlin

    @Test
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    fun workspacePrefixShouldNotHang() {
        val result = workspaceService.addWsPrefixToId("local-id", "ws1")
        assertThat(result).isNotNull()
    }

Если базовый код снова начнёт блокироваться, тест завершится с ошибкой
таймаута, а не зависнет вместе со всем CI-пайплайном.

Примечание о структуре модуля
--------------------------------

``WorkspaceApiMock`` находится в ``src/main`` модуля
``ecos-webapp-lib-spring-test``, а не в ``src/test``. Это разделение сделано
намеренно:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Каталог
     - Назначение
   * - ``src/main``
     - Код, который компилируется в артефакт модуля и экспортируется в
       тестовый classpath потребителей.
   * - ``src/test``
     - Внутренние тесты самого модуля (например, ``WorkspaceApiMockTest``).

Любой класс ``@Component`` или ``@Configuration``, который должен
автоматически обнаруживаться Spring Boot тестами сервисов-потребителей,
должен находиться в ``src/main`` тестового модуля.

См. также
---------

* :ref:`Создание нового микросервиса <mcs_setup>` — общее руководство по
  настройке Spring Boot микросервиса в Citeck.
* :ref:`Демо-микросервис <demo_microservice>` — рабочий пример микросервиса
  Citeck с тестами.
