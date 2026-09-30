.. _s3_storage:

Настройка S3 хранилища через интерфейс
========================================

.. note::

    Доступно только в Enterprise версии.

.. seealso::

    Требования к объёму и ресурсам S3-совместимого хранилища — :ref:`sizing_s3`.

1. Откройте журнал **Хранилища контента**

Журнал - ``v2/journals?journalId=ecos-content-storages&viewMode=table&ws=admin$workspace``

2. Откройте на редактирование **content-storage-s3**

 .. image:: _static/s3_storage/01.png
       :width: 700
       :align: center

3. Откройте на редактирование **Адрес сервера S3 →S3 Хранилище контента**

 .. image:: _static/s3_storage/02.png
       :width: 500
       :align: center

4. Откройте на редактирование **Данные для аутентификации → Ключи доступа к API S3 хранилища**

 .. image:: _static/s3_storage/03.png
       :width: 500
       :align: center

5. Введите **Имя пользователя (Access key)** и **Пароль (Secret key)** для доступа к S3. Нажмите **Сохранить**

 .. image:: _static/s3_storage/04.png
       :width: 500
       :align: center

6. Введите **URL** для доступа к S3 серверу. Нажмите **Сохранить**

 .. image:: _static/s3_storage/05.png
       :width: 500
       :align: center

7. Введите **имя бакета**. Нажмите **Сохранить**

 .. image:: _static/s3_storage/06.png
       :width: 500
       :align: center

8. Перейдите в журнал **Конфигурация ECOS** и откройте на редактирование настройку **"default-content-storage"**

Прямая ссылка на настройку - ``v2/journals?journalId=ecos-configs&search=default-content-storage&viewMode=table&ws=admin$workspace``

 .. image:: _static/s3_storage/07.png
       :width: 700
       :align: center

9. Выберите **Хранилище контента для S3** и сохраните настройку. 

 .. image:: _static/s3_storage/08.png
       :width: 600
       :align: center

На этом настройка завершена. Контент для всех новых документов будут попадать в S3 бакет. Перезагрузка стенда не требуется.

Если возникнут проблемы и потребуется выключить S3 на время поиска причин, то можно повторить п.9, но выбрать **Локальное хранилище в БД**.
