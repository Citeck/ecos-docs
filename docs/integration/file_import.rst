Файловый импорт в систему
==========================

.. contents::
		:depth: 4

Общая информация по функционалу
--------------------------------

В случае необходимости разобрать и импортировать данные из любого файла в систему - можно воспользоваться данным функционалом. 

Существует 3 системных справочника в микросервисе интеграций:

 .. image:: _static/file_import/file_import_1.png
       :width: 300
       :align: center

Кратко об использовании:

1. Создается конфигурация, где указывается информация о двух командах. Одна команда для парсинга, другая для обработки строк.

2. Загружается файл через справочник **“Файлы для импорта”**, указывается конфигурация в соответствии с которой этот файл должен обрабатываться.

3. Микросервис интеграции периодически ищет необработанные записи в справочнике **“Файлы для импорта”**. При их нахождении отправляет контент файла в виде команды в определенное приложение (данные для команды targetApp, type и тд берутся из конфигурации, это команда парсинга). В результате, ответом на команду вернется список строк для обработки, которые помещаются в журнал **“Элементы файлового импорта”**.

4. Микросервис интеграции периодически ищет необработанные записи в справочнике **“Элементы файлового импорта”**. При их нахождении отправляет payload найденных записей в виде команды в определенное приложение (данные для команды targetApp, type, maxBatch и тд берутся из конфигурации, это команда импорта). В результате, ответом на команду вернется информация об успешности завершения импорта строки или информация об ошибке.

Информация об использовании справочников
-----------------------------------------

Конфигурация импорта файлов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/file_import/file_import_2.png
       :width: 600
       :align: center

Содержит информацию о том, как именно файлы выбранного типа импорта должны быть обработаны в системе после загрузки.

Пример готовой конфигурации (основная информация о командах для обработки):

 .. image:: _static/file_import/file_import_3.png
       :width: 600
       :align: center

Файлы для импорта
~~~~~~~~~~~~~~~~~~~~

Журнал, в который загружаются файлы, которые необходимо обработать. Тут же пишется статус обработки файла.

 .. image:: _static/file_import/file_import_4.png
       :width: 600
       :align: center

Заведение записей в этот справочник состоит из выбора каким именно способом обрабатывать этот файл (выбор строки из журнала конфигурации импорта файлов), загрузки самого файла и выбора планируемой даты начала обработки. Если дата начала обработки не указана - файл начнет обрабатываться в ближайшее время.

 .. image:: _static/file_import/file_import_5.png
       :width: 600
       :align: center

Элементы файлового импорта
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Журнал, в которые попадают строки файла после его парсинга. Строки сюда попадают автоматически.

 .. image:: _static/file_import/file_import_6.png
       :width: 600
       :align: center

Каждая строка, после стадии парсинга, возвращается в виде payload. ``Payload`` содержит, обычно, json, который будет понимать команда импорта строк. Пример ``payload`` можно видеть на скриншоте ниже:

 .. image:: _static/file_import/file_import_7.png
       :width: 600
       :align: center

Если импорт строки завершился ошибкой - команда может вернуть информацию об ошибке и эта ошибка будет отображена в журнале.

Пример создания своих обработчиков
-----------------------------------

1. Создание конфигурации импорта
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Создать ее можно либо через журнал, либо подложив json по пути ``${module_path}/integration/file-import-config``

.. code-block::

    {
    "id": "edi-events-import-config-id",
    "title": "Загрузка события для документа по ID",
    "parseCommandConfig": {
        "targetApp": "alfresco",
        "type": "***-edi-events-by-document-id-parse",
        "ttl": "330000"
    },
    "importCommandConfig": {
        "targetApp": "alfresco",
        "type": "***-edi-get-events-by-document-id",
        "ttl": "120000",
        "maxBatch": "1"
    }
    }

2. Написание команды парсинга
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В качестве dto на вход всегда одна структура:

.. code-block::

    @data
    @CommandType ("***-edi ~events-by-document-id-parse")
    public class EdiGetEventsByDocumentIdParseConmand {
    private String filename;
    private byte[] content;

Выход должен быть следующим:

.. code-block::

    @Data

    @uloargsConstructor

    @aiiargsConstructor

    public class EdifventsByDocumentIdParseResult {
    private boolean success;
    private List<EdiEventsByDocumentIdItem> itemsResult;
    private String error;

    public static EdifventsByDocumentIdParseResult success (List<EdiEventsByDocumentIdItem> itemsResult) {
    return new EdiEventsByDocumentIdParseResult (true, itemsResult, null);

    public static EdigventsByDocumentIdParseResult fail (String error) {
    return new EdifventsByDocumentIdParseResult (false, null, error);

В качествен ``itemsResult`` может быть любая DTO, главное, чтобы она успешно могла преобразоваться в JSON.

Внутри команды файл надо распарсить и разбить на необходимые для будущей обработки DTOшки.

Если файл нельзя обрабатывать - возвращайте в виде результата ``success=false`` и в ``error`` информацию об ошибке.

3. Написание команды импорта элементов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В качестве dto на вход может быть следующая структура:

.. code-block::

    @Data

    GComnandType ("*#*-edi-get-events-by-document-id")

    public class EdiGetEventsByDocumentIdCommand {
    private List<FileImportItem> items;

.. code-block::

    @data
    public class FileImportitem {
    private String id;
    private ObjectData payload;

В качестве результата:

.. code-block::

    @Data
    public class FileInportResultList {
    private List<FileInportResultIvem> resultList = new ArrayList<>();

.. code-block::

    @Data
    public class FileInportResultItem {
    private String id:
    private boolean error;
    private String details;

Обратите внимание каждому ``id`` из ``FileImportItem`` должна соответствовать запись в результирующим листе с таким же ``id``.