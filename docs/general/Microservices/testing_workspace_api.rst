.. _testing_workspace_api:

Testing with WorkspaceApiMock
==============================

.. contents::
   :depth: 4

Overview
--------

Services that use workspace-scoped entities — such as ``ecos-uiserv`` — depend on
``WorkspaceWebApi``, which calls ``ecos-model`` over HTTP to resolve workspace
membership. During ``@SpringBootTest`` tests ``ecos-model`` is not running, so
``WorkspaceWebApi.waitUntilEmodelApiIsAvailable()`` loops forever and tests hang
indefinitely.

The ``WorkspaceApiMock`` class, provided by ``ecos-webapp-lib-spring-test``, solves
this problem. It implements ``WorkspaceApi`` entirely in-memory, performs no HTTP
calls, and is auto-discovered by Spring Boot in test scope.

Problem: Hanging Tests
----------------------

The call chain that triggers the hang:

.. code-block:: text

    BoardRecord.getRef()
      → WorkspaceServiceImpl.addWsPrefixToId()
        → WorkspaceWebApi.mapIdentifiers()
          → WorkspaceWebApi.waitUntilEmodelApiIsAvailable()
            → infinite sleep loop

Whenever a test exercises any code path that resolves a workspace-prefixed
identifier, the whole test suite will stall unless a test-safe ``WorkspaceApi``
implementation is present.

Solution: WorkspaceApiMock
--------------------------

``WorkspaceApiMock`` is shipped in the ``ecos-webapp-lib-spring-test`` module
(in ``src/main``, so it is exported as part of the module artifact). It is
annotated with ``@Component``, so Spring Boot's component scan picks it up
automatically when the module is on the test classpath.

``ModelServiceFactoryInitializer`` was extended to optionally inject any
``WorkspaceApi`` bean:

.. code-block:: kotlin

    @Autowired(required = false)
    var workspaceApi: WorkspaceApi? = null

    @PostConstruct
    fun init() {
        // ... other injections ...
        workspaceApi?.let { modelServices.setWorkspaceApi(it) }
    }

When ``WorkspaceApiMock`` is present (test scope), it is injected and overrides
``WorkspaceWebApi``. In production deployments — where the test module is not on
the classpath — ``ModelServiceFactory`` falls back to the default
``WorkspaceWebApi``. No production code is affected.

Setup
-----

Add ``ecos-webapp-lib-spring-test`` as a test-scoped dependency in your service's
``pom.xml``:

.. code-block:: xml

    <dependency>
        <groupId>ru.citeck.ecos.webapp</groupId>
        <artifactId>ecos-webapp-lib-spring-test</artifactId>
        <scope>test</scope>
    </dependency>

That is all. In any ``@SpringBootTest``, the ``WorkspaceApiMock`` bean is
automatically discovered and injected into ``ModelServiceFactory``. No explicit
``@Import`` or additional configuration is required.

Configuring Test Data
---------------------

Inject ``WorkspaceApiMock`` directly into your test class to set up workspace
members and managers:

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
            workspaceApiMock.clear()  // always reset between tests
        }

        @Test
        fun someWorkspaceScopedTest() {
            workspaceApiMock.addMember("my-workspace", "john.doe")
            workspaceApiMock.addManager("my-workspace", "admin")

            val workspaces = workspaceService.getUserWorkspaces("john.doe")
            assertThat(workspaces).contains("my-workspace")
        }
    }

Available methods on ``WorkspaceApiMock``:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Method
     - Description
   * - ``addMember(workspace, user)``
     - Registers ``user`` as a member of ``workspace``.
   * - ``addManager(workspace, user)``
     - Registers ``user`` as a manager of ``workspace``.
   * - ``clear()``
     - Removes all members and managers added so far.

Default Behavior
----------------

When no data has been configured via ``addMember()`` / ``addManager()``:

* ``getUserWorkspaces(user)`` returns ``setOf("user$<username>")`` — the
  personal workspace, matching real ``WorkspaceService`` behavior.
* ``getNestedWorkspaces(workspaces)`` returns empty sets for all input workspaces.
* ``mapIdentifiers(ids, type)`` returns identifiers unchanged (identity mapping).
* ``isUserManagerOf(user, workspace)`` returns ``false``.

.. important::

    ``WorkspaceApiMock`` is a singleton Spring bean shared across all tests in a
    test run. State configured in one test persists into the next. **Always call**
    ``workspaceApiMock.clear()`` in ``@BeforeEach`` to ensure test isolation.

Guarding Against Regressions
-----------------------------

To explicitly protect against any future regression that re-introduces a hang,
annotate time-sensitive tests with ``@Timeout``:

.. code-block:: kotlin

    @Test
    @Timeout(value = 10, unit = TimeUnit.SECONDS)
    fun workspacePrefixShouldNotHang() {
        val result = workspaceService.addWsPrefixToId("local-id", "ws1")
        assertThat(result).isNotNull()
    }

If the underlying code ever starts blocking again, the test will fail with a
timeout error rather than hanging the entire CI pipeline.

Module Structure Note
---------------------

``WorkspaceApiMock`` lives in ``src/main`` of the ``ecos-webapp-lib-spring-test``
module — not in ``src/test``. This distinction is intentional:

* **``src/main``** — code that is compiled into the module artifact and exported
  to consumers' test classpaths.
* **``src/test``** — internal tests of the module itself (e.g.,
  ``WorkspaceApiMockTest``).

Any ``@Component`` or ``@Configuration`` class that must be auto-discovered by
consuming services' Spring Boot tests must reside in ``src/main`` of the test
module.

See Also
--------

* :ref:`Creating a new microservice <mcs_setup>` — general guide on setting up
  a Spring Boot microservice with Citeck.
* :ref:`Demo microservice <demo_microservice>` — a working example of a
  Citeck microservice with tests.
