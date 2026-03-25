Настройка S3 хранилища через интерфейс
========================================

.. _s3_storage:

.. note::

    Доступно только в Enterprise версии.

1. Открываем журнал **Хранилища контента**

Журнал - ``v2/journals?journalId=ecos-content-storages&viewMode=table&ws=admin$workspace``

2. Открываем на редактирование **content-storage-s3**

 .. image:: _static/s3_storage/01.png
       :width: 700
       :align: center

3. Открываем на редактирование **Адрес сервера S3 →S3 Хранилище контента**

 .. image:: _static/s3_storage/02.png
       :width: 500
       :align: center

4. Открываем на редактирование **Данные для аутентификации → Ключи доступа к API S3 хранилища**

 .. image:: _static/s3_storage/03.png
       :width: 500
       :align: center

5. Вводим **Имя пользователя (Access key)** и **Пароль (Secret key)** для доступа к S3. Нажимаем **Сохранить**

 .. image:: _static/s3_storage/04.png
       :width: 500
       :align: center

6. Вводим **URL** для доступа к S3 серверу. Нажимаем **Сохранить**

 .. image:: _static/s3_storage/05.png
       :width: 500
       :align: center

7. Вводим **имя бакета**. Нажимаем **Сохранить**

 .. image:: _static/s3_storage/06.png
       :width: 500
       :align: center

8. Переходим в журнал **Конфигурация ECOS** и открываем на редактирование настройку **"default-content-storage"**

Прямая ссылка на настройку - ``v2/journals?journalId=ecos-configs&search=default-content-storage&viewMode=table&ws=admin$workspace``

 .. image:: _static/s3_storage/07.png
       :width: 700
       :align: center

9. Выбираем **Хранилище контента для S3** и сохраняем настройку. 

 .. image:: _static/s3_storage/08.png
       :width: 600
       :align: center

На этом настройка завершена. Контент для всех новых документов будут попадать в S3 бакет. Перезагрузка стенда не требуется.

Если возникнут проблемы и потребуется выключить S3 на время поиска причин, то можно повторить п.9, но выбрать **Локальное хранилище в БД**.