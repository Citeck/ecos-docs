.. _mcs_setup:

Создание нового микросервиса
============================

.. note::

    Для создания микросервиса используется `Spring Boot <https://docs.spring.io/spring-boot/documentation.html>`_

Результат описанных ниже инструкций можно посмотреть здесь: `Citeck/ecos-webapp-sample <https://github.com/Citeck/ecos-webapp-sample/tree/main/minimal-sample>`_ 

Создание микросервиса в интегрированной среде разработки
------------------------------------------------------------

1. Для создания нового микросервиса Citeck нужно создать новый **maven spring-boot проект** и в **pom.xml** добавить в качестве родителя один из следующих pom файлов:

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table 
      
      * - Артефакт
        - Описание
      * - ru.citeck.ecos.webapp:ecos-webapp-spring-base-parent
        - | Базовый родитель для spring-boot микросервисов, где требуется ручная настройка плагинов для сборки.
          | Этот проект является родительским для всех остальных в этой таблице.
      * - ru.citeck.ecos.webapp:ecos-webapp-spring-hibernate-parent
        - | Родитель для spring-boot микросервисов, в которых предполагается использование hibernate.
          | Настройка плагинов для сборки не требуется.
      * - ru.citeck.ecos.webapp:ecos-webapp-spring-simple-parent
        - Родитель для spring-boot микросервисов без состояния или микросервисов, которые работают с БД через jdbc или :ref:`ecos-data<ecos_data_main>`.

Актуальная версия родительских pom файлов: **3.3.3 (версия Java не ниже 21)**

Все родительские **pom файлы** импортируют spring-boot зависимости, общие библиотеки Citeck и дополнительные библиотеки для тестирования (rabbitmq mock, zookeeper mock и тд.)

Пример настроенного **pom файла**:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>ru.citeck.ecos.webapp.sample</groupId>
        <artifactId>minimal-sample</artifactId>
        <version>1.0.0-SNAPSHOT</version>

        <parent>
            <groupId>ru.citeck.ecos.webapp</groupId>
            <artifactId>ecos-webapp-spring-simple-parent</artifactId>
            <version>3.3.3</version>
        </parent>

        <repositories>
            <repository>
                <id>citeck-public</id>
                <url>https://nexus.citeck.ru/repository/maven-public</url>
            </repository>
        </repositories>

    </project>

2. Следующим шагом нужно создать **главный класс** для запуска spring-boot приложения по следующему пути:

.. code-block:: text

    src/main/java/ru/citeck/ecos/webapp/sample/minimal/MinimalWebAppSample.java

* ``ru/citeck/ecos/webapp/sample/minimal`` - java пакет для нашего приложения, который может быть произвольным;

* ``MinimalWebAppSample.java`` - файл с основным классом для запуска приложения. Может быть произвольным. Есть поддержка как Kotlin так и Java файлов.

Содержимое основного класса:

.. code-block:: java

    package ru.citeck.ecos.webapp.sample.minimal;

    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
    import ru.citeck.ecos.webapp.lib.spring.EcosSpringApplication;

    @SpringBootApplication
    @EnableDiscoveryClient
    public class MinimalWebAppSample {

        public static final String NAME = "minimal-webapp";

        public static void main(String[] args) {
            new EcosSpringApplication(MinimalWebAppSample.class).run(args);
        }
    }

где

* ``public static final String NAME = "minimal-webapp";`` - имя приложения (app name). Оно должно быть уникально в пределах всех остальных микросервисов. На этом имени основано много механизмов:

  - Распределенный кэш hazelcast формируется между микросервисами с одним именем;

  - Commands API работает на базе этого имени. При отправке команды мы указываем имя приложения и сообщение уходит в персональную очередь для этого приложения;

  - Records API работает на базе этого имени. Имя приложения используется при поиске и указывается в sourceId до символа “/" (напр. emodel/person). Ссылки на сущности формируются с учетом имени приложения (напр. emodel/person@someuser);

  - Service discovery механизм работает на основе имени приложения. 

* ``EcosSpringApplication`` - наше расширение штатного SpringApplication. Для корректной работы микросервиса нужно использовать EcosSpringApplication.

3. Создать **файл с настройками** по пути (опционально):

.. code-block:: text

    src/main/resources/config/application.yml
    
Содержимое файла:

.. code-block:: yaml

    ---
    server:
      port: 8686 # указываем порт, на котором будет развернут микросервис 

В этом файле можно разместить настройки приложения.

4. Добавить **файл для настройки логирования**:

.. code-block:: text

    src/main/resources/logback-spring.xml

со следующим содержимым:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE configuration>
    <configuration>
        <include resource="ecos/logback-base.xml" />
    </configuration>

Для запуска микросервиса локально использовать команду:

.. code-block:: bash

    mvn spring-boot:run

Или стандартные механизмы IDE для запуска spring-boot приложений 

*Далее описаны шаги для тестирования микросервиса*

5. Создать файл с **настройками логирования для тестов** (опционально):

.. code-block:: text

    src/test/resources/logback-test.xml

с содержимым:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE configuration>
    <configuration>
        <include resource="ecos/logback-base.xml" />
    </configuration>

6. Создать файл с **настройками для автотестов** (опционально):

.. code-block:: text

    src/main/resources/config/application-test.yml

В этом файле можно разместить настройки, которые будут использованы только во время авто-тестов.

7. Создать **файл для тестирования микросервиса**:

.. code-block:: text

    src/test/java/ru/citeck/ecos/webapp/sample/minimal/MinimalWebAppSampleTest.java

где

* ``ru/citeck/ecos/webapp/sample/minimal``- java пакет с тестами. Может быть любым, но крайне желательно размещать тесты в том же пакете или подпакетах, что и основной класс из п.2;

* ``MinimalWebAppSampleTest.java`` - имя файла с тестами. Может быть любым. 

Содержимое файла:

.. code-block:: java

    package ru.citeck.ecos.webapp.sample.minimal;

    import org.junit.jupiter.api.Test;
    import org.junit.jupiter.api.extension.ExtendWith;
    import org.springframework.boot.test.context.SpringBootTest;
    import ru.citeck.ecos.webapp.lib.spring.test.extension.EcosSpringExtension;

    import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

    @ExtendWith(EcosSpringExtension.class)
    @SpringBootTest(classes = { MinimalWebAppSample.class })
    public class MinimalWebAppSampleTest {

        @Test
        public void test() {
            assertThat(1 + 1).isEqualTo(2);
        }
    }

где

* ``EcosSpringExtension`` - расширения Citeck для SpringExtension, которое позволяет запускать в автотестах полноценный spring-context с in-memory БД (если для неё заданы настройки подключения в application.yml);

* ``MinimalWebAppSample.class`` - класс из п.2

Для запуска автотестов нужно выполнить следующую команду:

.. code-block:: bash

    mvn clean test
    
Для сборки docker образа с микросервисом выполнить следующую команду:

.. code-block:: bash
  
    mvn clean package jib:dockerBuild -Djib.docker.image.tag=1.0.0-snapshot

.. note::

    При сборке внутри контейнера обязательно должны быть файлы для запуска:

    * /entrypoint.sh 
    * /app/jib-classpath-file
    * /app/jib-main-class-file

В списке модулей системы в ID: 

.. image:: _static/system_modules.png
       :width: 600
       :align: center

выводится имя репозитория (свойство repo), который загружается из файла: 

  * в проекте ``target/classes/ecos/build-info.json`` 
  * в контейнере ``/app/resources/ecos/build-info.json``

Создание микросервиса с использованием плагин для IntelliJ IDEA 
-----------------------------------------------------------------

Быстрее и удобнее создавать микросервис с использованием плагина для IntelliJ IDEA см. :ref:`как<plugin_app_mks>`.