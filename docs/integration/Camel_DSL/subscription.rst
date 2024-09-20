Подписка на событие ECOS
=========================

.. code-block:: yaml
  
  - route:
      from:
        uri: 'ecos-event:record-created' # подписываемся на событие "Запись создана"
        parameters:
          attributes:
            recordId: 'record?id' # указываем какие атрибуты нам нужны из события
          filter: # устанавливаем фильтр 
            t: not-eq 
            a: conditionField
            v: true
        steps:
          - to: log:record-was-created
