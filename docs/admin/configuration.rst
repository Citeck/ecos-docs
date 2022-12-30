Конфигурация
===================

Конфигурация в ECOS делится на два основных уровня:

1. Системный уровень
2. Уровень администратора

.. _configuration_system:

Системный уровень
------------------

Данный уровень конфигурации необходим для настройки низкоуровневых параметров, которые не предполагается изменять
в ходе работы приложеня (параметры подключение к БД, настройки для включения/отключения сервисов в приложении и др).

Конфигурация системного уровня настраивается средствами Spring Cloud - https://spring.io/projects/spring-cloud

Контейнер ecos-registry при старте загружает конфигурацию из указанных в настройках 
директорий и распространяет эту конфигурацию по всем приложениям.

Настройка ecos-registry через переменные среды::

  - SPRING_CLOUD_CONFIG_SERVER_COMPOSITE_0_TYPE=native
  - SPRING_CLOUD_CONFIG_SERVER_COMPOSITE_0_SEARCH_LOCATIONS=file:/central-config/

Путь во втором параметре указывает на место, откуда будет загружаться конфигурация

.. _configuration_admin:

Уровень администратора
-----------------------

**Конфигурация ECOS** - это артефакт, который позволяет описывать некоторые параметры системы с возможностью удобно использовать их значения как в коде так и в интерфейсе для изменения параметров без перезагрузки сервера.

Расположение артефактов: ``resources/eapps/artifacts/app/config``

Поддерживаемые форматы: **yml**, **yaml**, **json**

Ответственный за хранение и управление микросервис: **ecos-apps**

Можно использовать: в любом приложении

Доступ в интерфейсе есть у администраторов через инструменты: **Левое меню → Инструменты → Управление системой → Конфигурация ECOS**:

 .. image:: _static/configuration/config_journal.png
       :width: 600
       :align: center

Путь до страницы с конфигурацией: ``/v2/admin?journalId=ecos-configs&type=JOURNAL``

Примеры конфигураций:

.. code-block::

  ---
  id: active-theme
  name:
    ru: Активная тема
    en: Active theme
  value: ecos

.. code-block::

  ---
  id: custom-feedback-url
  name:
    ru: URL для обратной связи
    en: URL for feedback
  value: 'https://www.citeck.ru/feedback'

Чтобы воспользоваться этой конфигурацией в коде мы можем установить аннотацию ``@EcosConfig(“идентификатор_конфигурации”)`` на поле или метод, куда нужно поместить значение конфигурации. 

Любые изменения конфигурации в интерфейсе приведут к автоматическому обновлению значения поля или вызову метода, который был помечен аннотацией ``@EcosConfig``. 

Пример:

.. code-block::

  // kotlin
  @Component
  class CustomComponent {
      
      // Проставление через поле можно использовать
      // если нам не важно отлавливать событие изменения
      // Для полей можно использовать "var" и "lateinit var"
      @EcosConfig("some-config-id")
      private var configValue: String? = null

      // Проставление через метод можно использовать
      // если нам важно отлавливать событие изменения
      @EcosConfig("some-config-id")
      private fun setConfig(value: String) {
          println("New value: $value")
      }
  }

.. code-block::

  // java
  @Component
  public class CustomComponent {
      
      // Проставление через поле можно использовать
      // если нам не важно отлавливать событие изменения
      @EcosConfig("some-config-id")
      private String configValue;
      
      // Проставление через метод можно использовать
      // если нам важно отлавливать событие изменения
      @EcosConfig("some-config-id")
      private void setConfig(String value) {
          System.out.println("New value: " + value);
      }
  }

Если необходимо вручную применить конфигурацию на основе аннотаций к некоторому бину (может потребоваться там где нет spring контекста), то можно использовать сервис **BeanConsumerService**.

Пример теста:

.. code-block::

  import org.assertj.core.api.Assertions.assertThat
  import org.junit.jupiter.api.Test
  import ru.citeck.ecos.config.lib.consumer.bean.EcosConfig
  import ru.citeck.ecos.config.lib.service.EcosConfigServiceFactory

  class CustomComponentTest {

      @Test
      fun test() {

          val services = EcosConfigServiceFactory()
          val instance = CustomClass()

          // проверяем, что сейчас в field ничего нет
          assertThat(instance.field).isNull()
          
          // регистрируем все поля и методы с аннотацией @EcosConfig
          services.beanConsumersService.registerConsumers(instance)
          
          // т.к. значения для "some-config-id" мы не проставляли, то ожидаем, что значение все еще null
          assertThat(instance.field).isNull()

          // проставляем значение конфига в in-memory провайдере 
          services.inMemConfigProvider.setConfig("some-config-id", "123")
          
          // после проставления значения в одном из провайдеров ожидаем, что поле с аннотацией автоматически заполнилось
          assertThat(instance.field).isEqualTo("123")
          
          // получаем значение через EcosConfigService
          val value = services.ecosConfigService.getValue("some-config-id").asText()
          
          // проверяем, что значение, которое мы получили из EcosConfigService совпадает с тем, что мы проствляли в провайдере
          assertThat(value).isEqualTo("123")
      }

      class CustomClass {

          @EcosConfig("some-config-id")
          var field: String? = null
      }
  }

Создание нового конфига
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для создания нового конфига нужно создать **yaml файл** по пути ``src/main/resources/eapps/artifacts/app/config``

Например, **telegram-authtoken.yml**

С таким содержание:

.. code-block::

  id: telegram-authtoken
  name:
    ru: Авторизационный токен для Телеграм бота
    en: Telegram bot authorization token
  value: disabled

При старте конфиг будет создан и появится журнале **"Конфигурация ECOS"**.

Считать этот параметр можно:

1. Повесив аннотацию на поле: 

.. code-block::

  @EcosConfig("telegram-authtoken")
  private String telegramAuthorizationToken;

2.  Можно вместо поля сделать метод ``setAuthToken(String telegramAuthorizationToken)`` с той же аннотацией, и он будет вызываться при смене конфига (если нужно отслеживать изменение конфига без перезапуска).

Общая архитектура работы конфигураций
--------------------------------------

 .. image:: _static/configuration/ecos_config_1.png
       :width: 600
       :align: center

* **TargetBean** - это целевой бин с аннотациями ``@EcosConfig``;

* **resources** - это папка ресурсов в приложении;

* **some-config.yml** - некоторый конфиг в директории ``resources/eapps/artifacts/app/config``;

* **Artifacts Source** - источник артефактов, который загружает артефакты из папки ``resources/eapps/artifacts``;

* **EcosConfigService** - сервис конфигураций;

Получение конфигурации при старте системы:

1. Подключаемся к Zookeeper и проверяем актуальное значение конфигурации там.

  a. Если значение в Zookeeper отсутствует, то загружаем значение из **Artifacts Source** (т.е. напрямую из classpath);

  b. Если значение найдено, то загружаем его;

2. Все конфигурации, которое есть в app/config отправляются на микросервис ecos-apps через RabbitMQ (стандартный механизм деплоя артефактов);

3. Микросервис ecos-apps сохраняет конфигурации у себя в таблице, чтобы в дальнейшем можно было работать с ними через интерфейс (UI);

  a. При этом если в таблице уже есть конфигурация с таким же scope и id, то сравнивается версия конфига. Если новая версия совпадает или меньше текущей, то поле value в таблице не меняется;

4. После того как поле value у конфигурации в ecos-apps обновилось, микросервис отправляет новое значение в Zookeeper;

5. Наше приложение подписано на события изменения данных в Zookeeper и когда там меняется значение мы его тут же применяем ко всем слушателям конфигурации.

Когда пользователь в интерфейсе меняет значение конфигурации, то логика аналогична пунктам 3-5, но без проверки версии. 

Формы для конфигураций [rc5+]
------------------------------

Для конфигураций есть автогенерация форм на основе значения valueDef:

1. Сущность конфигурации имеет атрибут ``_formRef``, который возвращает ссылку на форму следующего вида - ``“uiserv/form@config${{config-scope}}${{config-id}}“``, где

  a. {{config-scope}} - область конфигурации

  b. {{config-id}} - идентификатор конфигурации

2. С этой ссылкой на форму UI отправляет запрос формы на **ecos-uiserv** и он в свою очередь по префиксу ``“config$“`` понимает, что форму необходимо вычислить. Вычисление происходит в **ConfigFormsProvider**

Если же для конфигурации нужна форма со своим набором полей и логикой, то можно использовать поле **valueDef.formRef** для указания ссылки на любую реальную форму.

Область (scope) 
-----------------

Вся конфигурация имеет scope, который описывает разные области для исключения влияния конфигурации в разных микросервисах друг на друга.

По умолчанию scope равен **“app/{{webapp_name}}“**, где **{{webapp_name}}** - это системное имя приложения.

Таким образом уникальным идентификатором конфигурации в системе можно считать только связку scope + config_id (т.е. один и тот же config_id может использоваться в разных областях).

Модель
--------

.. code-block::

  id: String // идентификатор конфигурации
  name: MLText // имя конфигурации
  scope: String // область действия конфигурации. По умолчанию "app/{{appName_приложения_в_котором_находится_артефакт}}" 
  value: Any // значение конфигурации
  version: Integer // версия конфигурации. Подробнее ниже.
  valueDef: // описание значения в поле value
    type: ConfigValueType // тип конфигурации. Если не задан, то будет вычислен автоматически [rc5+] на основе значения в value
    multiple: Boolean // флаг "множественное значение"
    formRef: RecordRef // форма для редактирования значения

* **ConfigValueType**  - одно из следующих значений:

.. code-block::

  ASSOC,
  PERSON,
  AUTHORITY_GROUP,
  AUTHORITY,
  TEXT,
  MLTEXT,
  NUMBER,
  BOOLEAN,
  DATE,
  DATETIME,
  JSON

Версия конфигурации
---------------------

В конфигурации ECOS есть поле версии, которое нужно для:

1. Защиты от случайного затирания значения, которое настроено в системе вручную;

2. Для возможности поменять значение по умолчанию для новых разворачиваемых систем;

3. Для возможности принудительно поменять значение, которое изменили в системе вручную.

Обновление поля value в уже задеплоеной конфигурации при загрузке новой версии артефакта происходит только если поле **version** у нового конфига больше чем то что сохранено в БД. 

При использовании патчей для артефакта конфигурации следует так же учитывать влияние поля **version** (т.е. если мы поменяем только value, но version оставим старым, то в системе значение конфига останется прежним).

Config Provider
----------------

Вся конфигурация в сервисе EcosConfigService получается из провайдеров, которые имеют следующий интерфейс:

.. code-block::

  interface EcosConfigProvider {
      fun getConfig(key: String): ConfigValue?
      fun getConfig(key: ConfigKey): ConfigValue?
      fun watch(action: (ConfigEvent) -> Unit)
      fun getOrder(): Float
  }

Все провайдеры сортируются по значению **getOrder()** и в итоге **EcosConfigService** отдает не-null значение из провайдера с наименьшим значением **getOrder()**

Стандартные провайдеры:

* **ArtifactsConfigProvider** - конфигурация загружается из classpath;

* **InMemConfigProvider** - in-memory провайдер. В основном используется для тестов; 

* **ZkConfigProvider** - провайдер на основе Zookeeper.

Обновление значения через патч ECOS
------------------------------------

Нужно разместить подобный some-patch.yml в директории ``resources/eapps/artifacts/app/patch``:

.. code-block::

  ---
    id: some-patch
    date: '2022-01-01T00:00:00Z'
    targetApp: uiserv
    type: mutate
    config:
      record:
        id: cfg@active-theme
        attributes:
          value: customTheme

