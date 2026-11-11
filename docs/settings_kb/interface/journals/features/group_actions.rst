.. _group_actions_journal:

Групповые действия
==================

.. contents::
   :depth: 3

Групповые действия позволяют применять действие одновременно к нескольким записям журнала: к выбранным, к результатам фильтрации или к конкретным записям. Они задаются в конфигурации журнала в поле **actions** и управляются через реализацию ``ActionsExecutor`` на стороне UI.

`См. Механизм групповых действий <https://www.youtube.com/watch?v=k6Qd9I4B4cs>`_

Для добавления групповых действий в новом конфиге журналов следует использовать поле **actions (List<RecordRef>)**.

Действия из данного списка могут быть групповыми, для отфильтрованных элементов, для конкретных записей или любая комбинация данных возможностей.

Реализация ActionsExecutor
---------------------------

Возможность выполнения действия определяется реализацией ``ActionsExecutor`` на UI и флагами в конфиге действия. Пример действия на UI:

``execForRecord`` выполняет действие для одной записи, ``execForRecords`` — для набора записей, ``execForQuery`` — для запроса. Флаг применимости может отключить возможность, но не добавляет отсутствующий метод исполнителя. Например, ``server-group-action`` поддерживает ``execForRecords`` и ``execForQuery``.

При ``execForQuery`` исполнитель определяет, как обработать запрос. При выполнении запроса как набора записей UI перебирает страницы и вызывает поддерживаемые методы для записей. Обработка на сервере зависит от конкретного действия.

.. code-block:: javascript

  export default class DeleteAction extends ActionsExecutor {
    static ACTION_ID = 'delete';

    async execForRecord(record, action, context) {
      return this.execForRecords([record], action, context);
    }

    async execForRecords(records, action, context) {
      let dialogTitle, dialogText;
      if (records.length === 1) {
        dialogTitle = 'record-action.delete.dialog.title.remove-one';
        dialogText = 'record-action.delete.dialog.title.remove-one';
      } else {
        dialogTitle = 'record-action.delete.dialog.title.remove-many';
        dialogText = 'record-action.delete.dialog.msg.remove-many';
      }

      return new Promise(resolve => {
        dialogManager.showRemoveDialog({
          title: dialogTitle,
          text: dialogText,
          onDelete: () => {
            Records.remove(records)
              .then(() => {
                resolve(true);
              })
              .catch(e => {
                dialogManager.showInfoDialog({
                  title: 'record-action.delete.dialog.title.error',
                  text: e.message || 'record-action.delete.dialog.msg.error',
                  onClose: () => {
                    resolve(false);
                  }
                });
                console.error(e);
              });
          },
          onCancel: () => {
            resolve(false);
          }
        });
      });
    }

    getDefaultActionModel() {
      return {
        name: 'record-action.name.delete',
        icon: 'icon-delete',
        theme: 'danger'
      };
    }
  }


Executor реализует два метода: ``execForRecords`` и ``execForRecord``. Это означает, что в конфиге действия мы можем управлять данными фичами, отключая и включая их.

Фича ``execForQuery`` будет всегда неактивна до реализации соответствующего метода.

По умолчанию все фичи по максимуму включены, если соответствующий Executor переопределяет нужные методы.

Конфигурация действия
-----------------------

Пример конфига действия:

.. code-block:: json

  {
    "id": "download-zip",
    "type": "download-zip",
    "evaluator": {
      "type": "has-attribute",
      "config": {
        "attribute": "_content"
      }
    },
    "features": {
      "execForQuery": false,
      "execForRecord": false,
      "execForRecords": true
    }
  }

Миграция со старого формата groupActions
-------------------------------------------

В DTO нового конфига журнала есть поле **groupActions**, но оно deprecated и будет удалено в дальнейшем.

Для воспроизведения такого же функционала как в groupActions следует настроить примерно следующий конфиг:

Было:

.. code-block:: xml

  <group-actions>
    <action id="complete-document-task" title="journal.group-action.payments.approve">
      <param name="actionId">complete-document-task</param>
      <param name="tasks">[
        {"taskId": "confirm-task", "transition": "Confirmed"}
      ]</param>
    </action>
  </group-actions>


Стало:

.. code-block:: json

  {
    "id": "complete-confirm-task",
    "type": "server-group-action",
    "name": "journal.group-action.payments.approve",
    "config": {
      "id": "complete-document-task",
      "params": {
        "tasks": "[{ \"taskId\": \"confirm-task\", \"transition\": \"Confirmed\" }]",
        "actionId": "complete-document-task"
      }
    }
  }

Внешний ``id`` идентифицирует UI-действие; ``config.id`` сохраняет идентификатор прежнего группового действия. В примере ``tasks`` остаётся строкой JSON, как в исходной конфигурации; формат параметров определяет серверный обработчик.

Если старому действию нужна форма, её ключ можно перенести в ``config.formKey``. Для новых действий используйте общую :ref:`настройку форм и подтверждения <ui_actions>`.
