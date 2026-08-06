.. _ecos_dmn_components:

Компоненты Citeck DMN
=========================================

Компоненты — это строительные блоки, из которых собирается диаграмма принятия решений в редакторе Citeck DMN. Каждый компонент соответствует определённому типу элемента стандарта DMN 1.3 и позволяет описать логику принятия решений в наглядной графической форме.

Компоненты делятся на несколько категорий:

- **Решение** — центральный элемент диаграммы, в котором задаётся логика принятия решения: условия, правила и результирующие значения.
- **Входные данные** — внешние данные, поступающие на вход в узел принятия решений или модель бизнес-знания.
- **Источник знания** — внешние сущности (документы, политики, комитеты), которые обосновывают или регулируют логику принятия решений.
- **Модель бизнес-знаний** — повторно используемая функция, инкапсулирующая один или несколько элементов принятия решений.
- **Соединители** — связи между элементами диаграммы, определяющие порядок передачи данных и зависимости между узлами.

Ниже представлен обзор всех доступных компонентов с кратким описанием. Для перехода к подробной документации кликните на соответствующую карточку.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Решение
      :link: dmn_decision
      :link-type: ref

      .. image:: _static/components/Decision.png
         :width: 100
         :align: left

      Узел, в котором один или несколько входных элементов определяют выход на основе бизнес-логики принятия решения, определённой в виде выражения или таблицы.

   .. grid-item-card:: Входные данные
      :link: dmn_input_data
      :link-type: ref

      .. image:: _static/components/Input_data.png
         :width: 100
         :align: left

      Информация, используемая в узле принятия решений или модели бизнес-знания.

   .. grid-item-card:: Источник знания
      :link: dmn_knowledge_data
      :link-type: ref

      .. image:: _static/components/Knowledge_source.png
         :width: 100
         :align: left

      Внешние сущности, документы, комитеты или политики, которые регулируют модель принятия решений или бизнес-знаний.

   .. grid-item-card:: Модель бизнес-знаний
      :link: dmn_knowledge_model
      :link-type: ref

      .. image:: _static/components/Business_knowledge_model.png
         :width: 100
         :align: left

      Повторно используемая функция с одним или несколькими элементами принятия решений.

   .. grid-item-card:: Соединители
      :link: dmn_connectors
      :link-type: ref

      .. image:: _static/components/Connectors.png
         :width: 50
         :align: left

      Правила соединения элементов.

.. toctree::
    :maxdepth: 1
    :hidden:

    components/ecos_dmn_components_decision
    components/ecos_dmn_components_input_data
    components/ecos_dmn_components_knowledge_data
    components/ecos_dmn_components_knowledge_model
    components/ecos_dmn_components_connectors
