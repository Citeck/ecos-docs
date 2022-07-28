Миграция локализации из Share
------------------------------

Скрипт для формирования модуля локализации из alfresco-share (выполняется в консоли браузера). Работает с версии uiserv 1.14.0+
После выполнения можно зайти в системные журналы и скачать новый модуль, после чего залить его в репозиторий:

Скрипт::

  var getMessages = async (locale) => {
    var resProm = await fetch('/share/service/messages.js?locale=' + locale);
    if (resProm.status !== 200) {
        resProm = await fetch('/share/noauth/messages.js?locale=' + locale);
    }
    res = await resProm.text();
    var messagesRegexp = /global = (\{.+\})/;
    var messagesRes = res.match(messagesRegexp);
    return JSON.parse(messagesRes[1]);
  };

  var locales = ["en", "ru"];

  var module = {"moduleId": "alfresco-messages", locales, order: -1, messages: {} };

  var messagesByLocale = {};
  var keys = {};
  for (let locale of locales) {
      messagesByLocale[locale] = await getMessages(locale);
      for (let key in messagesByLocale[locale]) {
          keys[key] = true;
      }
  }

  for (let key of Object.keys(keys)) {
      module.messages[key] = locales.map(l => {
          let message = messagesByLocale[l][key];
          if (message == null) {
              for (let locale of locales) {
                  message = messagesByLocale[locale][key];
                  if (message != null) {
                      return message;
                  }
              }
              message = "";
          }
          return message;
      });
  }

  var record = Citeck.Records.get('uiserv/i18n@');
  for (let key in module) {
      record.att(key, module[key]);
  }
  record.save();
