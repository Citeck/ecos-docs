Unit тестирование BPMN процессов
=================================

1. Тестирование реализаций бизнес процессов BPMN
------------------------------------------------

С добавлением camunda как движка BPMN, в проекте появилась возможность писать unit тесты для процессов.

На текущий момент, есть возможность писать тесты только в микросервисе ecos-process, в дальнейшем планируется добавить возможность написания тестов для различных проектов.

Для написания unit тестов используются библиотеки облегчающие тестирование bpmn:

* https://github.com/camunda-community-hub/camunda-platform-scenario - написание unit тестов по стилю `GivenWhenThen <https://martinfowler.com/bliki/GivenWhenThen.html>`_
* https://github.com/camunda/camunda-bpm-platform/tree/master/test-utils/assert - удобные bpmn ассерты для тестов

2. Тестирование ecos компонентов BPMN
-------------------------------------

Тесты написанные для проверки ecos компонентов bpmn представляют собой небольшие процессы BPMN, которые реализуют варианты использования ecos компонентов, с дальнейшем запуском процесса и проверкой результатов. 

Тесты располагаются в микрсоервисе ecos-process по пути src/test/java/ru/citeck/ecos/process/domain/bpmn/elements и написаны в стиле `GivenWhenThen <https://martinfowler.com/bliki/GivenWhenThen.html>`_.

Предполгается покрытие тестами каждого компонента. На моммент написания статьи написано порядка 40 тестов.

2.1 Пример unit BPMN теста
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Проверка назначения userTask по роли.

Процесс:

 .. image:: _static/process_unit_example.png
       :width: 800
       :align: center

Unit test:

.. code-block:: kotlin
    :caption: Bpmn unit test

    @Test
    fun `task assignment by roles`() {
        val procId = "test-user-task-role"
        saveAndDeployBpmn(USER_TASK, procId)

        `when`(process.waitsAtUserTask("userTask")).thenReturn {
            assertThat(it).hasCandidateUser(USER_IVAN)
            assertThat(it).hasCandidateUser(USER_PETR)

            assertThat(it).hasCandidateGroup(GROUP_MANAGER)
            assertThat(it).hasCandidateGroup(GROUP_DEVELOPER)
            it.complete()
        }

        run(process).startByKey(procId, variables).execute()

        verify(process).hasFinished("endEvent")
    }

    
Таким образом, проверяется, что при выполнении компонента userTask, была назначена задача на корректных пользователей и группы исходя из указанных ролей.