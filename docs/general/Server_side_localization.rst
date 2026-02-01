Настройка бэкенд локализации
==============================

Добавлена возможность локализировать ошибки на стороне сервера.

В микросервисе или библиотеке необходимо добавить файл со списком локализаций сообщений в ``resources/ecos/messages`` в формате:

.. code-block::

    {
    "id": "test-messages",
    "locales": [
        "en",
        "ru"
    ],
    "messages": {
        "label.yes": [
        "Yes",
        "Да"
        ],
        "label.no": [
        "No",
        "Нет"
        ],
        "server-error-occurred-with-code": [
        "Server error occurred. Error code: {{code}}",
        "Произошла ошибка на сервере. Код ошибки: {{code}}"
        ]
    }
    }

Локализация сообщения должна располагаться в том же порядке, как указано в ``locales``.

В текст можно подставлять параметры в формате:

.. code-block::

 {{param}}

Для обработки локализованной ошибки добавлено исключение ``I18nRuntimeException``. Например:

.. code-block::

    throw I18nRuntimeException.create()
                    .messageKey("label.yes")
                    .build() 
                    
Пример с проставлением параметров:

.. code-block::

    throw I18nRuntimeException.create()
                    .messageKey("server-error-occurred-with-code")
                    .messageArgs(
                        mapOf(
                            "code" to 500
                        )
                    )
                    .build() 

При обработке такого исключения в логи всегда пишется с ENGLISH локализацией. Если локализация не найдена, будет использоваться ключ сообщения.
На клиент возвращается текст ошибки исходя из локализации в контексте запроса.