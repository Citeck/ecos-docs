.. _notifications:

Уведомления
===========

Раздел описывает настройку и использование уведомлений в Citeck.

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: Настройка подключения микросервиса ecos-notifications
      :link: ecos-notifications-settings
      :link-type: ref

      Конфигурация SMTP-параметров через application.yml или переменные окружения.

   .. grid-item-card:: Уведомления
      :link: notifications-label
      :link-type: ref

      Общий обзор механизма уведомлений: типы, каналы доставки и базовая конфигурация.

   .. grid-item-card:: Шаблоны уведомлений
      :link: notification_templates
      :link-type: ref

      Создание и управление шаблонами для автоматической генерации текста писем и сообщений.

   .. grid-item-card:: Массовая рассылка
      :link: bulk_mail
      :link-type: ref

      Отправка уведомлений сразу нескольким получателям по заданным критериям.

   .. grid-item-card:: Функционал Lazy approval для задачи
      :link: lazy_approval_settings
      :link-type: ref

      Согласование задач непосредственно через ответ на письмо, без входа в систему.

   .. grid-item-card:: Отправка уведомлений из BPMN (Send Task)
      :link: notification_from_bpmn
      :link-type: ref

      Интеграция уведомлений в бизнес-процессы с помощью элемента Send Task.

   .. grid-item-card:: Отправители
      :link: senders
      :link-type: ref

      Настройка почтовых отправителей и параметров SMTP-подключения.

   .. grid-item-card:: Отправка электронных писем, подтверждённых ЭЦП
      :link: mail_eds
      :link-type: ref

      Подписание исходящих писем электронной цифровой подписью.

   .. grid-item-card:: Отправка тестового сообщения при запуске микросервиса
      :link: test_mail
      :link-type: ref

      Проверка работоспособности почтового канала при старте сервиса.

.. toctree::
    :maxdepth: 2
    :hidden:

    notifications/settings
    notifications/notifications
    notifications/notifications_template
    notifications/notifications_bulk_mail
    notifications/notification_lazy_approval
    notifications/notifications_from_ecos_bpmn
    notifications/senders
    notifications/mail_eds
    notifications/test_mail
