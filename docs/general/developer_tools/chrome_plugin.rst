.. _citeck_browser_plugin:

Браузерное расширение Citeck
=============================

.. contents::
   :depth: 3

Браузерное расширение для платформы Citeck, предназначенное для разработчиков и администраторов. Реализовано как Chrome-расширение (Manifest V3) и добавляет три точки входа: всплывающую панель, контекстное меню и вкладку в DevTools.

Установка
----------

Установите расширение из Chrome Web Store или загрузите вручную через страницу управления расширениями Chrome:

1. Откройте ``chrome://extensions/``
2. Включите **Режим разработчика**.
3. Нажмите **Загрузить распакованное расширение** и укажите папку с расширением.

Умная строка поиска
--------------------

Открывается по **Ctrl+Shift+E** или кликом по иконке расширения.

- Поиск по всем доступным действиям с нечётким сопоставлением текста.
- Поддержка кириллицы: автоматическое переключение раскладки (й→q, ц→w, ...).
- Навигация стрелками ↑↓, выбор по **Enter**.
- Показывает до 10 элементов одновременно.
- Активируется только на страницах, где доступен объект ``Citeck``.

Действия
---------

Все действия реализуют единый интерфейс и доступны через строку поиска или контекстное меню.

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: BrowseRecord
      :class-header: sd-font-weight-bold

      Открывает диалог с полной информацией о записи:

      - Системные атрибуты: ``_id``, ``_created``, ``_modified``, ``_status``, ``_type``, ``_parent``.
      - Значения атрибутов модели.
      - Назначенные роли.
      - Для Alfresco workspace nodeRef — открывает Node Browser.

   .. grid-item-card:: SetStatus
      :class-header: sd-font-weight-bold

      Загружает список статусов из ``_type.model.statuses``, показывает текущий статус и позволяет выбрать новый.

   .. grid-item-card:: CopyRecordId
      :class-header: sd-font-weight-bold

      Копирует полный идентификатор записи в буфер обмена.

      Пример: ``emodel/person@admin``

   .. grid-item-card:: CopyLocalRecordId
      :class-header: sd-font-weight-bold

      Копирует только локальную часть идентификатора (подстрока после ``@``).

      Пример: ``admin``

   .. grid-item-card:: ClaimTask
      :class-header: sd-font-weight-bold

      - Запрашивает активные задачи workflow для текущей записи (sourceId: ``eproc/wftask``).
      - Показывает каждую задачу с кнопкой **Claim**.
      - Опция **Claim all** — назначить все задачи на текущего пользователя сразу.

   .. grid-item-card:: DeleteProcessInstance
      :class-header: sd-font-weight-bold

      .. note::

         Доступно только администраторам.

      - Находит активные экземпляры процессов для текущей записи.
      - Диалог подтверждения с обязательным полем комментария.
      - Опции: пропустить кастомные листенеры / IO mapping.
      - Опциональное изменение статуса записи (по умолчанию: ``rejected``).
      - Записывает событие в историю (``task.delete``).

   .. grid-item-card:: ShowFormComponentsKeys
      :class-header: sd-font-weight-bold

      Накладывает метки с именами атрибутов поверх полей формы в виде ``<sup>``-тегов. Берёт элементы с классом ``control-label``, извлекает имена из атрибутов ``name`` или ``for``. Полезно при разработке и отладке форм.

   .. grid-item-card:: HostOptions
      :class-header: sd-font-weight-bold

      Настройки на уровне домена, хранятся в ``chrome.storage.sync``.

      Позволяет задать цвет шапки сайта (``.ecos-header``) для визуального различия окружений. Предустановленная палитра: ``primary``, ``warning``, ``success``, ``danger``, ``purple``, ``pink``, ``teal`` и др. Применяется при каждой загрузке страницы через ``chrome.tabs.onUpdated``.

   .. grid-item-card:: AdminPageSection
      :class-header: sd-font-weight-bold

      .. note::

         Доступно только администраторам.

      - Запрашивает все разделы административной панели (sourceId: ``uiserv/admin-page-section``).
      - Двуязычный поиск (RU / EN).
      - Открывает ``/v2/admin`` с нужным типом и journalId.

   .. grid-item-card:: OpenCardInOldUi
      :class-header: sd-font-weight-bold

      Открывает карточку Alfresco workspace nodeRef в старом интерфейсе Share.

      URL: ``{origin}/share/page/card-details?forceOld=true&nodeRef={nodeRef}``

   .. grid-item-card:: InjectCiteckUtils
      :class-header: sd-font-weight-bold

      .. _InjectCiteckUtils:

      Автоматически внедряет объекты ``$`` и ``$$`` в контекст страницы при каждой загрузке. Не добавляет элемент в строку поиска — работает только как фоновый хук. Подробнее: :ref:`консольные хелперы <citeck_console_helpers>`.

   .. grid-item-card:: Impersonate
      :class-header: sd-font-weight-bold

      Имперсонация пользователя через Keycloak OAuth.

      - Сохраняет историю последних 10 пользователей (``chrome.storage.sync``).
      - Секреты (токены) хранятся в ``chrome.storage.session``.

      Keycloak endpoints:

      .. list-table::
         :widths: 50 50
         :class: tight-table

         * - ``/ecos-idp/auth/realms/master/protocol/openid-connect/token``
           - Получение токена.
         * - ``/ecos-idp/auth/admin/realms/ecos-app/users?username=...``
           - Поиск пользователя.

Контекстное меню
-----------------

Действия доступны через правую кнопку мыши на ссылках, содержащих ``recordRef`` или ``nodeRef``:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Пункт меню
     - Действие
   * - Browse Record
     - Открыть атрибуты записи
   * - Copy Record Id
     - Скопировать полный ID
   * - Copy Local Record Id
     - Скопировать локальный ID
   * - Open Card in Old UI
     - Открыть в старом интерфейсе Alfresco

Панель DevTools
----------------

Вкладка **Citeck** в инструментах разработчика для мониторинга и отладки Records API.

Перехват запросов
~~~~~~~~~~~~~~~~~~

Перехватывает все запросы к ``/gateway/api/records/*`` через ``chrome.devtools.network.onRequestFinished``. Хранит до **300 записей** в памяти.

Цветовая маркировка по типу операции:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Тип
     - Цвет
   * - records
     - синий
   * - query
     - зелёный
   * - mutate
     - жёлтый
   * - delete
     - красный

Просмотр деталей
~~~~~~~~~~~~~~~~~

Четыре вкладки для каждого запроса:

.. list-table::
   :widths: 20 80
   :header-rows: 1
   :class: tight-table

   * - Вкладка
     - Содержимое
   * - Request
     - Отформатированный JSON тела запроса
   * - Response
     - Отформатированный JSON ответа
   * - Script
     - Автогенерированный исполняемый скрипт
   * - Raw
     - Сырые HTTP-данные (заголовки, тело, тайминги)

Генерация скрипта
~~~~~~~~~~~~~~~~~~

Автоматически создаёт готовый код для консоли браузера.

Для Records.get:

.. code-block:: javascript

   var result = await Records.get(['emodel/person@admin']).load({ name: 'cm:name' })
   result

Для Records.query:

.. code-block:: javascript

   var result = await Records.query(
       { sourceId: 'emodel/person', ... },
       { name: 'cm:name' }
   ).then(r => r.records)
   result

Обратное разворачивание атрибутов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Числовые ключи из оптимизированного ответа API преобразуются обратно в читаемые имена атрибутов.

Edit & Retry
~~~~~~~~~~~~~

- Редактирование JSON тела запроса прямо в панели.
- Повторная отправка через ``chrome.devtools.inspectedWindow.eval``.
- Dual-path: перехват через network listener (первичный) + eval callback (резервный).

Управление записью
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Кнопка
     - Действие
   * - **Pause** (⏸)
     - Приостановить запись новых запросов.
   * - **Clear** (🗑)
     - Очистить список.
   * - **Filter**
     - Фильтрация списка по тексту.
   * - **Find** (F3)
     - Поиск по тексту внутри детального просмотра.

Темы
~~~~~

Автоматически синхронизируется с темой DevTools (светлая / тёмная) через ``chrome.devtools.panels.themeName``.

.. _citeck_console_helpers:

Консольные хелперы ``$`` и ``$$``
-----------------------------------

Внедряются автоматически на каждой странице Citeck через :ref:`InjectCiteckUtils <InjectCiteckUtils>`.

Загрузка и сохранение атрибутов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   // Загрузка атрибутов произвольной записи
   await $.load('emodel/person@admin', { name: 'cm:name', email: 'email' })

   // Сохранение атрибутов
   await $.save('emodel/person@admin', { 'cm:name': 'New Name' })

   // Загрузка атрибутов текущей страницы
   await $$.load({ name: 'cm:name' })

   // Сохранение атрибутов текущей страницы
   await $$.save({ 'cm:name': 'New Name' })

Запросы с предикатами
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   // Простой запрос
   await $.query('emodel/person', $.eq('cm:name', 'admin'), { name: 'cm:name' })

   // Сложный предикат
   await $.query(
       'emodel/person',
       $.and($.contains('cm:name', 'admin'), $.not($.empty('email'))),
       { name: 'cm:name', email: 'email' }
   )

   // Запрос через sourceId
   await $.sourceId['emodel/person'].query($.eq('cm:name', 'admin'), { name: 'cm:name' })

Строители предикатов
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 35 65
   :header-rows: 1
   :class: tight-table

   * - Функция
     - Описание
   * - ``$.eq(att, val)``
     - Равенство
   * - ``$.contains(att, val)``
     - Содержит подстроку
   * - ``$.in(att, [...])``
     - Входит в список
   * - ``$.gt(att, val)``
     - Больше
   * - ``$.ge(att, val)``
     - Больше или равно
   * - ``$.lt(att, val)``
     - Меньше
   * - ``$.le(att, val)``
     - Меньше или равно
   * - ``$.empty(att)``
     - Пустое значение
   * - ``$.and(...predicates)``
     - Логическое И
   * - ``$.or(...predicates)``
     - Логическое ИЛИ
   * - ``$.not(predicate)``
     - Логическое НЕ

Разрешения расширения
----------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Разрешение
     - Назначение
   * - ``contextMenus``
     - Регистрация пунктов контекстного меню
   * - ``clipboardWrite``
     - Копирование в буфер обмена
   * - ``scripting``
     - Внедрение скриптов в контекст страницы (MAIN world)
   * - ``activeTab``
     - Доступ к текущей вкладке
   * - ``storage``
     - Хранилище Chrome (sync и session)

Host permissions: ``http://*`` и ``https://*`` (все хосты).
