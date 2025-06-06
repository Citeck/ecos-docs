Citeck WebAPI
==============

.. contents::
   :depth: 3

**Citeck WebAPI** - основной низкоуровневый способ общения микросервисов между собой в пределах Citeck. Общение происходит по схеме **Запрос → Ответ** синхронно.

API для работы с WebAPI описано в **ecos-webapp-api** (репозиторий ecos-webapp-api).

Реализация API находится в **ecos-webapp-lib** (репозиторий ecos-webapp-commons).

Что обеспечивает Citeck WebAPI
--------------------------------

1. Единообразная обработка ошибок. WebAPI берет на себя сбор информации о возникнувшей ошибке и отправку этой информации вызывающей стороне. Пользователь WebAPI клиента получит исключение EcosWebException и либо его обработает, либо оно отправится следующему приложению в иерархии вызовов;

2. Возможность единообразно отправлять запросы любых размеров (от байтов до гигабайтов) без опасений, что на какой-либо из сторон закончится оперативная память. Потоковая обработка позволяет пропускать через WebAPI запросы любых размеров;

3. WebAPI позволяет не ломать голову над отправкой структурированных данных вместе с бинарными. В одном запросе предусмотрены обе части;

4. WebAPI абстрагирует отправителя и получателя от способа доставки сообщений. Это позволяет независимо дорабатывать возможности транспорта не изменяя прикладной код. Например, к вопросам транспорта относятся следующие аспекты системы:

    a) Шифрование. Настройка TLS не должна никак влиять на работу прикладного кода;

    b) Транзакционность. Идентификатор транзакции и "прилипание" к определенным инстансам микросервисов происходит на этом уровне;

    c) Локали из текущего контекста прокидывается на принимающую сторону;

    d) Таймзона из текущего контекста прокидывается на принимающую сторону;

    e) Информация о клиенте (IP адрес) прокидывается из контекста на принимающую сторону;

    f) Подготовка и отправка JWT токена для аутентификации происходит на этом уровне;

    g) Информация о тенанте из текущего контекста прокидывается на принимающую сторону;

5. WebAPI позволяет сжимать сообщения, что при сетевых задержках позволяет увеличить скорость передачи данных;

6. WebAPI позволяет в библиотеках реализовывать клиент-серверное общение между приложениями без добавления тяжелых зависимостей вроде Spring MVC или различных HTTP клиентов;

7. Версионирование API позволяет еще до выполнения запроса узнать поддерживается или нет запрос на принимающей стороне. При этом информация о поддерживаемости так же включает в себя диапазон поддерживаемых версий. Если клиент умеет общаться с эндпоинтом /content/upload используя версии 0-3, а сервер поддерживает версии 0-2, то клиент отправит запрос в формате максимально поддерживаемой версии (2). Этот механизм позволяет развивать продукт не ломая совместимость по API.

8. Для некоторых запросов (коммит транзакции) нужна максимальная скорость и малейшая задержка может нарушить целостность данных в системе. В этом случае использование высокоуровневых API - не лучший вариант. 

9. Асинхронность на уровне API. Все запросы через Citeck WebAPI возвращают Promise, возможности которого можно использовать для асинхронных оптимизаций со стороны клиента. 

**Пример использования со стороны клиента:**

Java:

.. code-block::

    EcosWebClientApi webClient;
    int apiVersion = webClient.getApiVersion("emodel", "/custom/request", 2); // 2 - максимально поддерживаемая версия. В ответе вернется версия <= 2
    // Здесь должен быть код, который в зависимости от apiVersion подготовит тело запроса
    // Если на данный момент предполагается, что есть только нулевая версия эндпоинта, то ничего делать не нужно. Сервер всегда будет получать версию 0 и будет работать с ней.  
    String result = webClient.newRequest()
        .targetApp("emodel") // целевое приложение
        .path("/custom/request") // целевой путь (эндпоинт) запроса
        .version(apiVersion) // если предполагается поддержка только нулевой версии, то эту строчку можно опустить
        .header("custom-1", "value-1") // произвольные структурированные данные, которые можно 
        .header("custom-2", "value-2") // прочитать на принимающей стороне
        .bodyJ((writer) -> { writer.writeText("request-text"); })
        .executeJ((resp) -> { return resp.getBodyReader().readAsText(); })
        .get();

**Пример использования со стороны сервера:**

Java:

.. code-block::

    class CustomExecutor implements EcosWebExecutor {

        @Override
        public void execute(@NotNull EcosWebExecutorReq req, @NotNull EcosWebExecutorResp resp) {
            int apiVer = req.getApiVersion();
            // тут может быть логика для обработки разных версий API
            String requestText = req.getBodyReader().readAsText();
            resp.setHeader("custom-header", "custom-value"); // хидеры можно использовать для любых данных
            resp.getBodyWriter().writeText(requestText + "-response");
        }
        @NotNull
        @Override
        public Pair<Integer, Integer> getApiVersion() {
            return new Pair<>(0, 2); // поддерживаются версии от 0 до 2
        }
        @NotNull
        @Override
        public String getPath() {
            return "/custom/request";
        }
        @Override
        public boolean isReadOnly() {
            return false;
        }
    }
    ...
    EcosWebExecutorsApi executorsApi;
    executorsApi.register(new CustomExecutor());

Версионирование API
--------------------

Микросервис при инициализации собирает информацию обо всех зарегистрированных executor'ах и записывает эту информацию в Zookeeper.

Микросервис, который хочет отправить запрос достает информацию из Zookeeper и предоставляет возможность отправителю скорректировать свое поведение на основе поддерживаемости определенного эндпоинта.

Описание запроса и ответа
--------------------------

Запрос формируется по следующему паттерну:

1. Версия Citeck WebAPI (целое число);

2. Тип сжатия всего последующего содержимого (целое число);

3. Размер сжатых метаданных в байтах включая тип метаданных и тип сжатия (целое число);

4. Тип метаданных (целое число);

5. Тип сжатия метаданных (целое число);

6. Метаданные (зависит от типа метаданных (4))

7. Тип тела запроса (целое число)

8. Тип сжатия тела запроса (целое число)

9. Тело запроса (зависит от типа тела запроса (7))

Ответ формируется по тем же принципам, что и запрос, но без указания версии Citeck WebAPI (1)

Структура метаданных запроса:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

 Имена полей не играют роли? если тип метаданных - массив.

.. code-block::

    jwt: String // JWT токен с информацией о текущей аутентификации
    path: String // Путь для обращения к нужному executor'у
    version: Int // Версия запроса для executor'а
    headers: DataValue // Заголовки запроса (произвольные структурированные данные)
    routes: Map<String, String> // Роуты, которые следует использовать для внешних запросов. Ключ - имя приложения, Значение - идентификатор инстанса приложения
    tenant: String // Тенант, в рамках которого выполняется запрос
    tzUtcOffset: Duration // Часовое смещение относительно UTC
    clientData: ClientData // Информация о клиенте (ip адрес)
    txnId: TxnId // Идентификатор транзакции
    locales: List<Locale> // Список локалей

Структура метаданных ответа:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    Имена полей не играют роли если тип метаданных - массив.

.. code-block::

    headers: DataValue // Заголовки запроса (произвольные структурированные данные)
    status: EcosWebRespStatus // Статус выполнения запроса. Поддерживается SUCCESS и ERROR
    routes: Map<String, String> // Роуты, которые следует использовать для внешних запросов. Ключ - имя приложения, Значение - идентификатор инстанса приложения
    txnData: TxnRespData // Транзакционные данные. Описание ниже

.. code-block::

    TxnRespData
    actions: Map<TxnActionType, List<TxnActionRef>> // Транзакционные действия, которые нужно выполнить перед или после завершения транзакции;
    remoteTxnApps: List<String> // Приложения, которые нужно включить в качестве ресурсов в транзакцию. Другими словами - это приложения, которые ожидают коммита или ролбэка в рамках текущей транзакции.

Поддерживаемые типы сжатия:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 10
      :header-rows: 1

      * - ID типа сжатия
        - Тип сжатия
      * - **0**
        - Без сжатия
      * - **1**
        - ZSTD (Zstandard)

Поддерживаемые типы метаданных:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 10
      :header-rows: 1

      * - ID типа метаданных
        - Тип метаданных
      * - **0**
        - CBOR массив с данными, где имя поля определяется по порядковому индексу.

Поддерживаемые типы тела:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
      :widths: 5 10
      :header-rows: 1

      * - ID типа метаданных
        - Тип метаданных
      * - **0**
        - NONE - тело отсутствует
      * - **1**
        - BINARY - бинарные данные
      * - **2**
        - CBOR - структурированные данные в формате CBOR
      * - **3**
        - JSON - структурированные данные в формате JSON
      * - **4**
        - TEXT_UTF8 - текстовые данные

Бинарное представление целого числа в Citeck WebAPI:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Если число в диапазоне от 0 до 127 включительно, то мы его записываем как есть в виде одного байта.

Если число не в диапазоне от 0 до 127, то мы первый байт формируем следующим образом (по битам):

   - **0-2** - в этих битах кодируется количество байт, в которых закодировано число. Для кодирования мы берем количество байт (например 2) и вычитаем один (получаем 1). Таким образом, 001 означает, что число закодировано двумя байтами. 

   - **3-5** - не используются

   - **6** - бит определяет знак "минус". Если он равен 1, то число отрицательное.

   - **7** - бит определяет, что число не входит в диапазон от 0 до 127

Далее на основе битов 0-2 мы получаем число байт, которые нужно прочитать, читаем их и преобразуем в исходное число. Если бит 6 выставлен в 1, то домножаем результат на -1.  

Транспорт
----------

В качестве транспорта для Citeck WebAPI на данный момент используется HTTP, но в будущем возможны и другие протоколы.

FAQ
----

    Как связан Records API и Citeck WebAPI?

        RecordsAPI использует Citeck WebAPI в качестве транспорта для общения между микросервисами. 