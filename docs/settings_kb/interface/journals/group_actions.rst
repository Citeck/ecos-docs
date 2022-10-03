Групповые действия 
==================

`См. Механизм групповых действий <https://www.youtube.com/watch?v=k6Qd9I4B4cs>`_

Для добавления групповых действий в новом конфиге журналов следует использовать поле **actions (List<RecordRef>)**. 

Действия из данного списка могут быть групповыми, для отфильтрованных элементов, для конкретных записей или любая комбинация данных возможностей. 

Возможность выполнения действия определяется реализацией ``ActionsExecutor`` на UI и флагами в конфиге действия. Пример действия на UI:

.. code-block::

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


Executor реализует 2 метода: ``execForRecords`` и ``execForRecord``. Это означает, что в конфиге действия мы можем управлять данными фичами отключая и включая их. 

Фича ``execForQuery`` будет всегда неактивна до реализации соответствующего метода.

По умолчанию все фичи по максимуму включены если соответствующий Executor переопределяет нужные методы.

Пример конфига действия:

.. code-block::

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
    

В DTO нового конфига журнала есть поле **groupActions**, но оно deprecated и будет удалено в дальнейшем.

Для воспроизведения такого же функционала как в groupActions следует настроить примерно следующий конфиг:

Было:

.. code-block::

    <group-actions>
    <action id="complete-document-task" title="journal.group-action.payments.approve">
        <param name="actionId">complete-document-task</param>
        <param name="tasks">[
            {"taskId": "confirm-task", "transition": "Confirmed"}
        ]</param>
    </action>
    </group-actions>



Стало:

.. code-block::

        {
        "id": "complete-confirm-task", <-- данный id не одно и то же что в старом конфиге. Следует его задавать по смыслу.
        "type": "server-group-action",
        "name": "journal.group-action.payments.approve",
        "config": {
            "id": "complete-document-task", <-- здесь уже id из группового действия
            "formKey": "...", <-- в примере выше формы нет, но её следует сюда помещать если хочется минимум действий при миграции. По хорошему функционал форм для действий следует использовать из статьи с действиями  
            "params": {
                "tasks": "[{ "taskId": "confirm-task", "transition": "Confirmed" }]" <-- здесь нужно проверить без кавычек. Если получится, то лучше использовать такой вариант.
                "actionId": "complete-document-task"
            }
        }   
    }

