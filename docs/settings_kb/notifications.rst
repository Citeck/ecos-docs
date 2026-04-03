.. _notifications:

Уведомления
===========

Раздел описывает настройку и использование уведомлений в Citeck.

Подразделы охватывают следующие темы:

- :ref:`Настройка подключения микросервиса ecos-notifications <ecos-notifications-settings>` — конфигурация SMTP-параметров через application.yml или переменные окружения.
- :ref:`Уведомления <notifications-label>` — общий обзор механизма уведомлений: типы, каналы доставки и базовая конфигурация.
- :ref:`Шаблоны уведомлений <notification_templates>` — создание и управление шаблонами для автоматической генерации текста писем и сообщений.
- :ref:`Массовая рассылка <bulk_mail>` — отправка уведомлений сразу нескольким получателям по заданным критериям.
- :ref:`Функционал Lazy approval для задачи <lazy_approval_settings>` — согласование задач непосредственно через ответ на письмо, без входа в систему.
- :ref:`Отправка уведомлений из BPMN (Send Task) <notification_from_bpmn>` — интеграция уведомлений в бизнес-процессы с помощью элемента Send Task.
- :ref:`Отправители <senders>` — настройка почтовых отправителей и параметров SMTP-подключения.
- :ref:`Отправка электронных писем, подтверждённых ЭЦП <mail_eds>` — подписание исходящих писем электронной цифровой подписью.
- :ref:`Отправка тестового сообщения при запуске микросервиса <test_mail>` — проверка работоспособности почтового канала при старте сервиса.


.. toctree::
    :maxdepth: 2

    notifications/notifications
    notifications/notifications_template
    notifications/notifications_bulk_mail
    notifications/notification_lazy_approval
    notifications/notifications_from_ecos_bpmn
    notifications/senders
    notifications/mail_eds
    notifications/test_mail
    notifications/settings
