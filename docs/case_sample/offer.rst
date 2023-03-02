Процесс согласования оффера
=============================

.. contents::
		:depth: 6


Создание приложения включает в себя создание и настройку отдельных артефактов, таких как типы данных, журналы, формы, процессы и т.д.

Вы можете создать приложение самостоятельно, или загрузить по ссылке: https://gitlab.citeck.ru/ecos-community/ecos-offers 

В разделе приводятся рекомендации и пояснения по разработке приложения с нуля.

:ref:`Артефакты<ecos_artifacts>` взаимосвязаны между собой, поэтому рекомендуется придерживаться следующего порядка их создания:

    - :ref:`тип данных<data_types_main>`

    - :ref:`журнал<journals>`

    - :ref:`форма для типа<forms>` (если требуется);

    - :ref:`дашборд<dashboard>` (если требуется);

    - схема процесса;

    - формы задач процесса.

При создании собственных моделей рекомендуется предварительно составить схему взаимосвязей между создаваемыми типами, а далее производить процедуру внесения их в систему в порядке от более простых и независимых типов (справочников) к типам, включающим в себя уже ранее созданные. В таком случае не будет сведена к минимуму необходимость прерывания настройки одного типа для настройки другого. 

Последующие разделы будут содержать процесс пошагового создания приложения в соответствии с приведенными выше рекомендациями -  сначала будут созданы справочные типы:

    - Город,

    - Офис,

    - Тип должности;

    - Грейд,

    - Социальный пакет,

    - Должностные обязанности,

    - Кандидат

далее основной тип-кейс: 

     – Согласование оффера (тип данных, для которого будет реализована основная бизнес-логика приложения).

Структура создания каждого отдельного компонента будет обязательно начинаться с подготовки типа данных. При создании типа данных автоматически генерируеются форма и журнал.

.. _types_offer:

Типы данных
------------

Для просмотра существующих типов и их редактирования создан журнал Типы данных (**Раздел администратора - Модель - Журналы**):

 .. image:: _static/offer/type_new_1.png
       :width: 600
       :align: center

Для создания типа данных необходимо нажать **+ - Создать новый тип**:

 .. image:: _static/offer/type_new_2.png
       :width: 600
       :align: center

.. _dataset_sample:

Справочники
~~~~~~~~~~~~

Создание справочника "Город"
""""""""""""""""""""""""""""

**Тип Город** не зависит от других типов. Содержит информацию о городах.

Является справочником (о различиях справочников и кейсов :ref:`здесь<data_types_types>`)

Для создания справочника необходимо заполнить форму создания типа в соответствии со следующими таблицами.

Номер маркера в таблице соответствует номеру поля, отмеченного на рисунке, приведенном :ref:`здесь<data_types_main>`.

Таблица заполнения для вкладки **Основные**:

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table 

        1,id,city
        2,Имя,Город
        5,Родитель,Справочник
        11,Действия, Редактировать свойства; Удалить

Атрибуты, не указанные в таблице, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию)

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

 .. image:: _static/offer/type_1.png
       :width: 600
       :align: center

Таблица заполнения для вкладки **Атрибуты**:

.. csv-table::
   :header: "id (1)", "Имя (2)", "Тип (3)"
   :widths: 15, 10, 30
   :align: center
   :class: tight-table 

        cityCode,Код,Text
        cityName,Название,Text

Атрибуты, не указанные в таблицах, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию)

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

 .. image:: _static/offer/type_2.png
       :width: 600
       :align: center

Создание справочника "Офис"
""""""""""""""""""""""""""""

**Тип Офис** зависит от ранее созданного типа **Город** (обратить внимание на задание ассоциативного атрибута). Содержит информацию об офисах. Является справочником. 

Таблица заполнения для вкладки **Основные**:

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table    

        1,id,office
        2,Имя,Офис
        5,Родитель,Справочник
        11,Действия, Редактировать свойства; Удалить

Атрибуты, не указанные в таблице, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию).

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

 .. image:: _static/offer/type_3.png
       :width: 600
       :align: center

Таблица заполнения для вкладки **Атрибуты**:

.. csv-table::
   :header: "id (1)", "Имя (2)", "Тип (3)"
   :widths: 15, 10, 30
   :align: center
   :class: tight-table 

        officeCode,Код,Text
        officeCity,Город,Association По кнопке «Настроить» выбрать тип «Город»
        officeAddress,Адрес,Text

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

 .. image:: _static/offer/type_4.png
       :width: 600
       :align: center

Создание справочника "Тип должности"
""""""""""""""""""""""""""""""""""""""

**Тип Должности** не зависит от других типов. Содержит информацию о должностях.

Является справочником 

Таблица заполнения для вкладки **Основные**:

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table 

        1,id,orgstruct-simple-role
        2,Имя,Тип должности
        5,Родитель,Справочник
        11,Действия, Редактировать свойства; Удалить

Атрибуты, не указанные в таблице, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию)

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_5.png
       :width: 600
       :align: center

Таблица заполнения для вкладки **Атрибуты**:

.. csv-table::
   :header: "id (1)", "Имя (2)", "Тип (3)"
   :widths: 15, 10, 30
   :align: center
   :class: tight-table 

        name,Имя,Text
        title,Должность,Text
        rolesManager,Руководящая роль,Boolean

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_6.png
       :width: 600
       :align: center

Создание справочника "Грейд"
"""""""""""""""""""""""""""""

**Тип Грейд** зависит от ранее созданного типа **Тип должности** (обратить внимание на задание ассоциативного атрибута). Содержит информацию о грейдах.

Является справочником. 

Таблица заполнения для вкладки **Основные**:

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table 

   1,id,hr-grade
   2,Имя,Грейд
   5,Родитель,Справочник
   11,Действия, Редактировать свойства; Удалить

Атрибуты, не указанные в таблице, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию)

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_7.png
       :width: 600
       :align: center

Таблица заполнения для вкладки **Атрибуты**:

.. csv-table::
   :header: "id (1)", "Имя (2)", "Тип (3)"
   :widths: 15, 10, 30
   :align: center
   :class: tight-table 

    gradesSimpleRoleTypeAssoc,Должность,Association По кнопке «Настроить» выбрать тип «Тип должности»
    gradesNumber,Номер,Text
    gradesRequirements,Требования к сотруднику,Text
    gradesResponsibilities,Обязанности,Text
    gradesSalary,Вилка оклада,Text
    gradesPrize,Премия,Text

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_8.png
       :width: 600
       :align: center

Создание справочника "Социальный пакет"
""""""""""""""""""""""""""""""""""""""""

**Тип Социальный пакет** не зависит от других типов. Содержит информацию о социальном пакете. Является справочником. 

Таблица заполнения для вкладки **Основные**:

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table 

   1,id,social-package
   2,Имя,Социальный пакет
   5,Родитель,Справочник
   11,Действия, Редактировать свойства; Удалить

Атрибуты, не указанные в таблице, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию).

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_9.png
       :width: 600
       :align: center

Таблица заполнения для вкладки **Атрибуты**:

.. csv-table::
   :header: "id (1)", "Имя (2)", "Тип (3)"
   :widths: 15, 10, 30
   :align: center
   :class: tight-table 

    socialPackage,Соц.пакет,Text

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_10.png
       :width: 600
       :align: center

Создание справочника "Должностные обязанности"
""""""""""""""""""""""""""""""""""""""""""""""

**Тип Должностные обязанности** не зависит от других типов. Содержит информацию о должностных обязанностях.

Является справочником. 

Таблица заполнения для вкладки **Основные**:

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table 

        1,id,offer-responsibility
        2,Имя,Должностные обязанности
        5,Родитель,Справочник
        11,Действия, Редактировать свойства; Удалить

Атрибуты, не указанные в таблице, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию)

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_11.png
       :width: 600
       :align: center

Таблица заполнения для вкладки **Атрибуты**:

.. csv-table::
   :header: "id (1)", "Имя (2)", "Тип (3)"
   :widths: 15, 10, 30
   :align: center
   :class: tight-table 

        responsibilitiesSimpleRoleTypeAssoc,Должность,Association По кнопке «Настроить» выбрать тип «Тип должности»
        responsibilitiesSubordination,Подчинение, Person (для выбора сотрудника из оргструктуры)

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_12.png
       :width: 600
       :align: center

Создание справочника "Кандидат"
""""""""""""""""""""""""""""""""

**Тип Кандидаты** зависит от ранее созданного типа Города (обратить внимание на задание ассоциативного атрибута). Содержит информацию о кандидатах, рассматриваемых для выдачи оффера.

Является справочником.  

Таблица заполнения для вкладки **Основные**:

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table 

        1,id,offer-candidate
        2,Имя,Кандидат
        5,Родитель,Справочник
        11,Действия, Редактировать свойства; Удалить

Атрибуты, не указанные в таблице, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию).

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_13.png
       :width: 600
       :align: center

Таблица заполнения для вкладки **Атрибуты**:

.. csv-table::
   :header: "id (1)", "Имя (2)", "Тип (3)"
   :widths: 15, 10, 30
   :align: center
   :class: tight-table 

        candidateCode,Код,Text
        candidateLastName,Фамилия,Text
        candidateFirstName,Имя,Text
        candidateMiddleName,Отчество,Text
        candidateBirthDate,День рождения,Date
        candidateGender,Пол,Text
        candidateCityAssoc,Город,Association По кнопке «Настроить» выбрать тип «Город»

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_14.png
       :width: 600
       :align: center

Кейс
~~~~~

Создание типа данных "Согласование оффера"
"""""""""""""""""""""""""""""""""""""""""""

**Тип Согласование оффера** является типом-кейс и зависит от ранее созданных справочников (о различиях справочников и кейсов :ref:`здесь<data_types_types>`)

Таблица заполнения для вкладки **Основные**:

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table 

     1,id,offer
     2,Имя,Согласование оффера
     3,Шаблон отображения имени,Оффер №${_docNum|fmt("000000")} номер будет указан в виде 0000001
     5,Родитель,Кейс
     8,Шаблон нумерации, Создать hr-offer-number-template см. ниже
     11,Действия, Редактировать свойства; Удалить

Атрибуты, не указанные в таблице, не являются необходимыми при создании данного типа (поля могут быть оставлены пустыми или с неизменными значениями по умолчанию)

Номер маркера в таблице соответствует номеру поля, отмеченного на рисунке, приведенном :ref:`здесь<data_types_main>`.

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_15.png
       :width: 600
       :align: center

Пояснение к пп. 3 и 8. Номер можно присваивать автоматически. И номер можно отражать в шаблоне отображения имени. Для этого необходимо задать и настроить :ref:`Шаблон нумерации<number_template>`.

Нажать **"Выбрать"**:

  .. image:: _static/offer/counter/count_6.png
       :width: 400
       :align: center

Далее нажать **Создать  - Создать новый шаблон**:

  .. image:: _static/offer/counter/count_7.png
       :width: 600
       :align: center

Заполнить открывшуюся форму:

  .. image:: _static/offer/counter/count_3.png
       :width: 600
       :align: center

.. csv-table::
   :header: "Номер маркера", "Название поля", "Значение"
   :widths: 5, 10, 20
   :align: center
   :class: tight-table 

     1,id,hr-offer-number-template
     2,Name,Offer Number Template
     3,Counter key,hr-offer-counter

И выбрать созданный шаблон:

  .. image:: _static/offer/counter/count_8.png
       :width: 600
       :align: center


Таблица заполнения для вкладки **Атрибуты**:

.. csv-table::
   :header: "id (1)", "Имя (2)", "Тип (3)"
   :widths: 15, 10, 30
   :align: center
   :class: tight-table 

          registrationNumber,Регистрационный номер,Text
          offerIssueDate,Дата создания,Date
          initiator,Инициатор,Person
          offerCandidate,Кандидат,Association По кнопке «Настроить» выбрать тип «Кандидат»
          offerPosition,Должность,Association По кнопке «Настроить» выбрать тип «Тип должности»
          offerSubdivision,Подразделение,Group
          offerGrade,Грейд,Association По кнопке «Настроить» выбрать тип «Грейд»:
          offerOffice,Офис,Association По кнопке «Настроить» выбрать тип «Офис»:
          offerComment,Комментарий,Text
          offerChief,Руководитель,Person
          offerAdditionalChief,Доп. согласующий,Person
          offerFeedback,Фидбэк по собеседованиям,Text
          offerSalaryAndPrize,Зарплатная вилка и премия,Text
          offerSubordination,Подчинение,Person
          offerSalary,Оклад,Number
          offerPrize,Премия,Text
          offerSchedule,График работы,Text
          content,Содержимое,Content
          offerDateWork,Дата выхода на работу,Date
          offerApproveStage,Номер этапа согласования,Number
          offerTaskComment,Комментарий по офферу,Text

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_16.png
       :width: 600
       :align: center

.. _roles_offer:

Таблица заполнения для вкладки **Роли**:

.. csv-table::
   :header: "id (1)", "Название логики (2)", "Участники роли(3)", "Атрибуты(4)"
   :widths: 15, 10, 30, 30
   :align: center
   :class: tight-table 

          offer-initiator-role,Инициатор,Нет,Инициатор
          offer-chief-role,Руководитель,Нет,Руководитель
          offer-additional-chief-role,Доп. согласующий,Нет, Доп. согласующий
          offer-director-role,Директор, По кнопке «Выбрать» сотрудника из оргструктуры,
          offer-technologist-role,Технолог, По кнопке «Выбрать» сотрудника из оргструктуры,

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_17.png
       :width: 600
       :align: center

Таблица заполнения для вкладки **Статусы**:

.. csv-table::
   :header: "id (1)", "Название логики (2)"
   :widths: 15, 10
   :align: center
   :class: tight-table 

          draft,Черновик
          hr-offer-approve,Согласование руководителем
          hr-offer-director-approve,Согласование директором
          hr-offer-additionaly-approve,Согласование доп. согласующим
          hr-offer-rework,Доработка
          hr-offer-feedback,Формирование ответа кандидату
          hr-offer-feedback-from-candidate,Ожидание ответа от кандидата
          hr-offer-reject,Кандидату отказано
          hr-offer-accept-offer,Оффер принят
          hr-offer-reject-offer,Оффер не принят

Ниже приведено изображение конечной настройки типа (для визуальной сверки):

  .. image:: _static/offer/type_18.png
       :width: 600
       :align: center

При создании типа данных по умолчанию созда.тся :ref:`автоматически генерируемая форма и журнал<auto_journal_form>`

Формы
-------

При создании типа данных по умолчанию создается связанная :ref:`автоматически сгенерированная форма<auto_form>`.

Для просмотра существующих форм и их редактирования создан журнал **Формы** (**Раздел администратора - Конфигурация UI - Формы**):

 .. image:: _static/offer/forms_journal.png
       :width: 700
       :align: center

Автоматически сгенерированные формы используются в журналах как формы для :ref:`создания нового элемента<city_form>`.

Подробная информация о:

     - :ref:`формах<forms>`, 
     - :ref:`редакторе форм<form_builder>`, 
     - :ref:`компонентах формы<form_components>`,
     - :ref:`примерах компонент<form_examples>` 

Для справочников «Город», «Офис», «Тип должности», «Грейд», «Социальный пакет», «Должностные обязанности» оставим автоматически сгенерированные формы.

Ниже рассмотрим, как изменить  формы «Кандидаты» и «Офферы». Скопируйте форму из карточки типа данных:

 .. image:: _static/offer/form_edit_1.png
       :width: 600
       :align: center

Переименуйте идентификатор формы:

 .. image:: _static/offer/form_edit_2.png
       :width: 400
       :align: center

В типе данных проставляется данная форма и становятся доступны действия, включая редактирование:

 .. image:: _static/offer/form_edit_3.png
       :width: 600
       :align: center

Нажмите **«Редактировать»**:

 .. image:: _static/offer/form_edit_4.png
       :width: 600
       :align: center

И далее нажмите **«Редактировать форму»**.

Форма "Кандидаты"
~~~~~~~~~~~~~~~~~~~

Пример формы:

  .. image:: _static/offer/form_14.png
       :width: 600
       :align: center

Компоненты формы:

.. list-table::
      :widths: 5 10 20
      :header-rows: 1
      :align: center
      :class: tight-table 
      
      * - Название поля
        - Имя свойства
        - Наименование компонента
      * - |
        - Колонки формы
        - Columns Component
      * - Код
        - candidatesCode
        - Text Field Component
      * - Фамилия
        - candidatesLastName
        - Text Field Component
      * - Имя
        - candidatesFirstName
        - Text Field Component
      * - Отчество
        - candidatesMiddleName
        - Text Field Component
      * - Дата рождения
        - candidatesBirthDate
        - :ref:`Date / Time Component<sample_date_time_component>`
      * - Пол
        - candidatesGender
        - :ref:`ECOS Select Component<sample_ecos_select_component>` 

               .. image:: _static/offer/form_17.png
                    :width: 300
                    :align: center
      * - Город
        - candidatesCityAssoc
        - Select Journal Component

Кнопки для форм, созданных выше:

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - Отменить
        - |

               .. image:: _static/offer/form_18.png
                    :width: 400
                    :align: center

      * - Сохранить
        - |

               .. image:: _static/offer/form_19.png
                    :width: 400
                    :align: center

Для отображения кнопки на всю ширину ячейки необходимо на вкладке **"Вид"** выставить чекбокс **"Блокировать"**:

  .. image:: _static/offer/form_48.png
       :width: 600
       :align: center

Форма "Согласование оффера"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Пример формы:

  .. image:: _static/offer/form_16.png
       :width: 600
       :align: center

Компоненты формы:

.. csv-table::
   :header: "Название поля", "Имя свойства", "Наименование компонента"
   :widths: 15, 10, 10
   :align: center
   :class: tight-table 

     ,Заголовок,:ref:`Panel Component<sample_panel_component>`
     ,Колонки формы,Columns Component
     Регистрационный номер,registrationNumber,Text Field Component
     Присвоить номер,generateNumber,Checkbox Component
     Дата создания,_created (для автоматического ввода даты создания документа),Date / Time Component
     Комментарий по результатам,offerTaskComment,:ref:`Text Area Component<Text_Area>`
     initiator,initiator,Select Orgstruct Component
     Кандидат,offerCandidate,Select Journal Component
     Должность,offerPosition,Select Journal Component
     Подразделение,offerSubdivision,:ref:`Select Orgstruct Component<sample_select_orgstruct_component>`
     Грейд,offerGrade,Select Journal Component
     Руководитель,offerChief,Select Orgstruct Component
     Офис,offerOffice,Select Journal Component
     Доп.согласующий,offerAdditionalChief,Select Orgstruct Component
     Комментарий,offerComment,Text Area Component
     Зарплатная вилка и премия,offerSalaryForkAndPrize,Text Field Component
     Подчинение,offerSubordinationAtr,Text Field Component
     Фидбэк по собеседованиям,offerFeedback,Text Area Component
     Оклад,offerSalary,:ref:`Number Component<Number>`
     Премия,offerPrize,Text Field Component
     График работы,offerSchedule,Text Field Component
     Дата выхода на работу,offerDateWork,Date / Time Component
     Файлы,content,:ref:`File Component<File_>`

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - Отменить
        - |

               .. image:: _static/offer/form_20.png
                    :width: 400
                    :align: center

      * - Создать
        - |

               .. image:: _static/offer/form_21.png
                    :width: 400
                    :align: center

      * - Сохранить (как черновик)
        - |

               .. image:: _static/offer/form_22.png
                    :width: 400
                    :align: center

Журналы
--------

При создании типа данных по умолчанию создается связанный с ним :ref:`автоматически сгенерированный журнал<auto_journal>` журнал. Такой журнал получает идентификатор вида **type$idтипа**.

Созданные автоматически журналы доступны в разделе **Журналы** (**Раздел администратора - Конфигурация UI - Журналы**):

  .. image:: _static/offer/journal_auto_1.png
       :width: 700
       :align: center

Автосозданный журнал может полноценно использоваться в системе – и быть добавлен в :ref:`меню<menu>` - рассмотрим на примере справочника **«Города»**:

1. Перейдите в настройку меню, нажав на шестеренку справа сверху, далее выберите **«Настроить меню»**:

  .. image:: _static/offer/menu_1.png
       :width: 600
       :align: center

2. Перейдите во вкладку **«Настройки выбранной конфигурации»**, нажмите **«+ Добавить»**, выберите **«Раздел»**:

  .. image:: _static/offer/menu_2.png
       :width: 600
       :align: center

3. В поле **«Название»** введите название раздела. Например, «Офферы». Нажмите **«Сохранить»**.

  .. image:: _static/offer/menu_3.png
       :width: 400
       :align: center

4. Наведите курсор на добавленный раздел, нажмите **«+ Добавить»**, выберите **«Журнал»**:

  .. image:: _static/offer/menu_4.png
       :width: 600
       :align: center

Выберите журнал **«type$city»** и нажмите **ОК**:

  .. image:: _static/offer/menu_5.png
       :width: 600
       :align: center

  .. image:: _static/offer/menu_6.png
       :width: 600
       :align: center

.. _city_form:

В левом меню появился новый журнал **«Город»**, в котором по нажатию на **+** открывается форма создания нового элемента:

  .. image:: _static/offer/menu_7.png
       :width: 600
       :align: center


Создание бизнес-процесса
-------------------------

С использованием созданных ранее типов данных, форм настраиваем бизнес-процесс согласования оффера:

  .. image:: _static/offer/scheme/diagram_00.png
       :width: 800
       :align: center

Для наглядности описания разобьем процесс на **6 частей**. И рассмотрим каждую часть подробно.

На примере **1 части** рассмотрим подробное создание элементов, для частей **2-5** будт приведены изображения конечной настройки элементов.

Для просмотра существующих бизнес-процессов и их редактирования необходимо перейти в левом меню в пункт **«Редактор бизнес-процессов»**:

  .. image:: _static/offer/bp_new.png
       :width: 600
       :align: center

Для создания процесса необходимо нажать **«+ - Создать camunda процесс»**:

  .. image:: _static/offer/bp_new_1.png
       :width: 600
       :align: center

Подробно можно ознакомиться с:

     - :ref:`редактором бизнес-процесса<editor_bpmn>`, 
     - :ref:`созданием бизнес-процесса<new_bp>`, 
     - :ref:`компонентами конструктора<ecos_bpmn_components>`, 

Заполнение формы создания бизнес-процесса "Согласование оффера":

  .. image:: _static/offer/process_form.png
       :width: 600
       :align: center

где 

.. list-table:: 
      :widths: 10 20 30
      :header-rows: 1
      :align: center
      :class: tight-table 

      * - Номер маркера
        - Название поля
        - Значение
      * - 1
        - **Идентификатор**
        - hr-offer-process
      * - 2
        - **Имя**
        - hr-offer-process
      * - 3
        - **Ecos Type**
        - выбрать созданный ранее тип данных **"Согласование оффера (hr-offer-type)"** 
      * - 4
        - **Раздел**
        -  не заполнять, сохранение произойдет автоматически в раздел "По умолчанию".
      * - 5
        - **Форма**
        - не указывать
      * - 6
        - **Включен**
        - флаг выставлен
      * - 7
        - **Автоматический старт процесса**
        - флаг выставлен


Используемые в процессе элементы
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - 
               .. image:: _static/offer/bpform/bpform_1.png
                    :width: 50
                    :align: center
        - Начальное событие
  
      * - 
               .. image:: _static/offer/bpform/bpform_2.png
                    :width: 50
                    :align: center
        - :ref:`Шлюз<gateways>` и :ref:`поток управления<sequential flow>`
      * - 
               .. image:: _static/offer/bpform/bpform_3.png
                    :width: 50
                    :align: center
        - :ref:`Пользовательская задача<user_task>`
      * - 
               .. image:: _static/offer/bpform/bpform_4.png
                    :width: 50
                    :align: center
        - :ref:`Уведомление<notification>`
      * - 
               .. image:: _static/offer/bpform/bpform_5.png
                    :width: 50
                    :align: center
        - :ref:`Смена статуса<set_status>`
      * - 
               .. image:: _static/offer/bpform/bpform_6.png
                    :width: 50
                    :align: center
        - :ref:`Задача сценарий<script_task>`
      * - 
               .. image:: _static/offer/bpform/bpform_7.png
                    :width: 50
                    :align: center
        - Завершающее событие

Создание элементов для Части (1) схемы бизнес-процесса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Часть (1)** схемы бизнес-процесса:

 .. image:: _static/offer/scheme/scheme_1.png
       :width: 600
       :align: center


Начальное событие
"""""""""""""""""

Начальное событие **(1) на схеме** задается по умолчанию элементом:

 .. image:: _static/offer/bmpn09.png
       :width: 600
       :align: center

**ID элемента** Система указывает автоматически для всех создаваемых элементов.

Шлюз и поток данных
"""""""""""""""""""

 .. image:: _static/offer/bmpn10.png
       :width: 400
       :align: center

Для шлюза **(2) на схеме** укажите **Имя**:

 .. image:: _static/offer/bmpn10_1.png
       :width: 500
       :align: center

Поток управления используется для связи элементов потока BPMN (событий, процессов, шлюзов).

Поток управления (стрелка) отображает ход выполнения процесса. 

 .. image:: _static/offer/bmpn10а.png
       :width: 300
       :align: center

Далее ведите стрелку к необходимому элементу. Для потока можно указать тип условия. 

Для шлюза, созданного выше:

**Поток «Нет»**:

               .. image:: _static/offer/bpflow/bpflow_1.png
                    :width: 400
                    :align: center
          
Текст скипта:
          
               .. code-block::

                    var offerChief = document.load('_roles.assigneesOf.offer-chief-role');
                    var director = document.load('_roles.assigneesOf.offer-director-role');

                    value= offerChief!=director;

**Поток «Да»**:

               .. image:: _static/offer/bpflow/bpflow_2.png
                    :width: 400
                    :align: center
          
Текст скипта:
          
               .. code-block::

                    var offerChief = document.load('_roles.assigneesOf.offer-chief-role');
                    var director = document.load('_roles.assigneesOf.offer-director-role');


                    value = offerChief==director;

Для следующего шлюза **3 на схеме**:

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - 
               .. image:: _static/offer/bpform/bpform_13.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_14.png
                    :width: 400
                    :align: center

      * - **Поток "Начало процесса"**
        - 
               .. image:: _static/offer/bpflow/bpflow_3.png
                    :width: 400
                    :align: center

Смена статуса
"""""""""""""""

**4 на схеме**

 .. image:: _static/offer/bmpn35.png
       :width: 600
       :align: center

|

 .. image:: _static/offer/bmpn35_1.png
       :width: 600
       :align: center

.. list-table::
      :widths: 5 5
      :align: center
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/offer/bmpn36.png
                :width: 300
                :align: center

      * - Выбрать **статус**

        - 
               .. image:: _static/offer/bmpn37.png
                :width: 300
                :align: center

:ref:`Подробно об установке статуса<set_status>`

Уведомление
""""""""""""

**5 на схеме**

 .. image:: _static/offer/bmpn11.png
       :width: 600
       :align: center

|

 .. image:: _static/offer/bmpn11_1.png
       :width: 600
       :align: center

.. list-table::
      :widths: 5 5
      :align: center
      :class: tight-table 

      * - | Указать **Имя**, 
          | выбрать **Тип уведомления**

        - 
               .. image:: _static/offer/bmpn12.png
                :width: 300
                :align: center

      * - | Выбрать шаблон, 
          | или указать **Заголовок** и **тело сообщения**

        - 
               .. image:: _static/offer/bmpn13.png
                :width: 300
                :align: center

         |

               .. image:: _static/offer/bmpn14.png
                :width: 300
                :align: center
         
      * - Получатели выбираются из списка ролей, заполненных в :ref:`типе данных<roles_offer>`
        - 
               .. image:: _static/offer/bmpn15.png
                :width: 300
                :align: center

         |

               .. image:: _static/offer/bmpn16.png
                :width: 300
                :align: center   


Задача-сценарий
""""""""""""""""

**6 на схеме**

 .. image:: _static/offer/bmpn17.png
       :width: 600
       :align: center

|

 .. image:: _static/offer/bmpn17_1.png
       :width: 600
       :align: center

.. list-table::
      :widths: 5 5
      :align: center
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/offer/bmpn18.png
                :width: 300
                :align: center

      * - Указать **скрипт**

        - 
               .. image:: _static/offer/bmpn19.png
                :width: 300
                :align: center
           
           | Текст скипта:
          
               .. code-block::

                    execution.removeVariable('chiefApproveComment'); 

:ref:`Подробно о скриптах<script_task>`

Пользовательская задача
"""""""""""""""""""""""

**7 на схеме**

 .. image:: _static/offer/bmpn20.png
       :width: 600
       :align: center

|

 .. image:: _static/offer/bmpn20_1.png
       :width: 600
       :align: center


.. list-table::
      :widths: 5 5
      :align: center
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/offer/bmpn21.png
                :width: 300
                :align: center

      * - Указать **Реципиентов** – исполнителей задачи, выбираются из списка ролей, заполненных :ref:`типе данных<roles_offer>`

        - 
               .. image:: _static/offer/bmpn22.png
                :width: 300
                :align: center
      * - | **Форма задачи** определяет то, что будет отображено при назначении задачи пользователю.
          | Если какие-то задачи могут совпадать, то можно использовать одинаковую форму, но если различаются, то, соответственно, формы разные.
          | Можно создать форму заранее и выбрать ее из списка или создать непосредственно из списка выбора (см. ниже)

        - 
               .. image:: _static/offer/bmpn23.png
                :width: 300
                :align: center

      * - | Выставить **приоритет задачи**, указать **результат задачи** – идентификатор и название.
          | Здесь и далее - исходящие варианты для потока управления доступны к выбору, если в пользовательской задаче добавлены результаты задачи.
          | См. ниже **(8)** в таблице.
        - 
               .. image:: _static/offer/bmpn24.png
                :width: 300
                :align: center

Создание формы:

Нажмите **"Выбрать"**:

 .. image:: _static/offer/bmpn25_1.png
       :width: 400
       :align: center

Далеее **"Создать - Создать форму"**:

 .. image:: _static/offer/bmpn25.png
       :width: 600
       :align: center

|

 .. image:: _static/offer/bmpn26.png
       :width: 600
       :align: center

.. csv-table::
   :header: "Название поля", "Значение"
   :widths: 10, 10
   :align: center
   :class: tight-table 

      Идентификатор формы,offer-form-approve
      Название формы,Offer Form Approve
      Редактируемый тип данных,Нет

Ниже приведено изображение конечной настройки (для визуальной сверки):

  .. image:: _static/offer/form_26.png
       :width: 600
       :align: center

Пример формы:

  .. image:: _static/offer/form_27.png
       :width: 600
       :align: center


Компоненты формы:

.. csv-table::
   :header: "Название поля", "Имя свойства", "Наименование компонента"
   :widths: 15, 10, 10
   :align: center
   :class: tight-table 

      ,Колонки формы,Columns Component
      Комментарий доп. согласующего,addApproveComment,Text Area Component
      Комментарий после доработки,reworkComment,Text Area Component
      Комментарий,chiefApproveComment,Text Area Component

Кнопки формы:

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - Reject
        - |

               .. image:: _static/offer/form_28.png
                    :width: 400
                    :align: center

      * - Rework
        - |

               .. image:: _static/offer/form_29.png
                    :width: 400
                    :align: center

      * - Submit
        - |

               .. image:: _static/offer/form_30.png
                    :width: 400
                    :align: center


Для последующих элементов:

.. list-table::
      :widths: 5 10 50
      :align: center
      :class: tight-table 

      * - 8
        - 
               .. image:: _static/offer/bpform/bpform_31.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_32.png
                    :width: 400
                    :align: center
          
          | Здесь и далее -  исходящие варианты для потока управления доступны к выбору, если в пользовательской задаче добавлены результаты задачи. См. выше описание элемента **(7)**.
      * - 
        - **Поток «Вернуть на доработку»**
        - 
               .. image:: _static/offer/bpflow/bpflow_4.png
                    :width: 400
                    :align: center

      * - 
        - **Поток «Отказ»**
        - 
               .. image:: _static/offer/bpflow/bpflow_5.png
                    :width: 400
                    :align: center

      * -
        - **Поток «Доп согласование»**
        - 
               .. image:: _static/offer/bpflow/bpflow_6.png
                    :width: 400
                    :align: center

      * - 9
        - 
               .. image:: _static/offer/bpform/bpform_33.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_34.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    var offerAdditionalChief = document.load('offerAdditionalChief'); 


                    if(offerAdditionalChief) { 
                    execution.setVariable('additional', true); 
                    } else { 
                    execution.setVariable('additional', false); 
                    }

:ref:`Подробно о формах для бизнес-процессов<user_task>`

Создание элементов для Части (2) схемы бизнес-процесса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/offer/scheme/scheme_2.png
       :width: 600
       :align: center

И таблица, в которой отражены конечные настройки компонент бизнес-процесса (для визуальной сверки):

.. list-table::
      :widths: 5 10 50
      :align: center
      :class: tight-table 

      * - 1
        - 
               .. image:: _static/offer/bpform/bpform_21.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_22.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

	               execution.removeVariable('reworkComment');
      * - 2
        - 
               .. image:: _static/offer/bpform/bpform_19.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_20.png
                    :width: 400
                    :align: center
      
      * - 3
        -
               .. image:: _static/offer/bpform/bpform_17.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_18.png
                    :width: 400
                    :align: center
      * - 4
        - 
               .. image:: _static/offer/bpform/bpform_15.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_16.png
                    :width: 400
                    :align: center

           | **Для всех подобных задач в «Форма задачи» выбрать ранее созданную форму задачи**   

Информация по форме **Доработка (Offer Form Rework)**:

.. csv-table::
   :header: "Название поля", "Значение"
   :widths: 10, 10
   :align: center
   :class: tight-table 

      Идентификатор формы,offer-form-rework
      Название формы,Offer Form Rework
      Редактируемый тип данных,Нет

Ниже приведено изображение конечной настройки (для визуальной сверки):

  .. image:: _static/offer/form_23.png
       :width: 600
       :align: center

Пример формы:

  .. image:: _static/offer/form_24.png
       :width: 600
       :align: center


Компоненты формы:

.. csv-table::
   :header: "Название поля", "Имя свойства", "Наименование компонента"
   :widths: 15, 10, 10
   :align: center
   :class: tight-table 

      ,Колонки формы,Columns Component
      Комментарий руководителя,chiefApproveComment,Text Area Component
      Комментарий Директора,dirApproveComment,Text Area Component
      Комментарий,reworkComment,Text Area Component

Кнопка Done:

  .. image:: _static/offer/form_25.png
       :width: 400
       :align: center

Создание элементов для Части (3) схемы бизнес-процесса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/offer/scheme/scheme_3.png
       :width: 600
       :align: center

И таблица, в которой отражены конечные настройки компонент бизнес-процесса (для визуальной сверки):

.. list-table::
      :widths: 5 10 50
      :align: center
      :class: tight-table 

      * - 1
        - 
               .. image:: _static/offer/bpform/bpform_103.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_104.png
                    :width: 400
                    :align: center

      * - 
        - **Поток "Да"**
        - 
               .. image:: _static/offer/bpflow/bpflow_7.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    var offerAdditionalChief = execution.getVariable('additional');
                    value= offerAdditionalChief===true;

      * -
        - **Поток "Нет"**
        - 
               .. image:: _static/offer/bpflow/bpflow_8.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    var offerAdditionalChief = execution.getVariable('additional');
                    value= offerAdditionalChief===false;
      * - 2
        - 
               .. image:: _static/offer/bpform/bpform_43.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_44.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    execution.removeVariable(‘addApproveComment’);
                    execution.removeVariable('reworkComment');

      * - 3
        - 
               .. image:: _static/offer/bpform/bpform_41.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_42.png
                    :width: 400
                    :align: center
      * - 4
        - 
               .. image:: _static/offer/bpform/bpform_39.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_40.png
                    :width: 400
                    :align: center
      * - 5
        - 
               .. image:: _static/offer/bpform/bpform_37.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_38.png
                    :width: 400
                    :align: center

Информация по форме **Согласование доп. согласующими (Offer Form Add Approve)**:      

.. csv-table::
   :header: "Название поля", "Значение"
   :widths: 10, 10
   :align: center
   :class: tight-table 

        Идентификатор формы,offer-form-add-approve
        Название формы,Offer Form Add Approve
        Редактируемый тип данных,Нет

Ниже приведено изображение конечной настройки (для визуальной сверки):

  .. image:: _static/offer/form_31.png
       :width: 600
       :align: center

Пример формы:

  .. image:: _static/offer/form_32.png
       :width: 600
       :align: center


Компоненты формы:

.. csv-table::
   :header: "Название поля", "Имя свойства", "Наименование компонента"
   :widths: 15, 10, 10
   :align: center
   :class: tight-table 

      ,Колонки формы,Columns Component
      Комментарий руководителя,chiefApproveComment,Text Area Component
      Комментарий,addApproveComment,Text Area Component

Кнопки формы:

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - Reject
        - |

               .. image:: _static/offer/form_33.png
                    :width: 400
                    :align: center

      * - Submit
        - |

               .. image:: _static/offer/form_34.png
                    :width: 400
                    :align: center


.. list-table::
      :widths: 5 10 50
      :align: center
      :class: tight-table 

      * - 6
        - 
               .. image:: _static/offer/bpform/bpform_35.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_36.png
                    :width: 400
                    :align: center

      * -
        - **Поток «Отказано»**
        - 
               .. image:: _static/offer/bpflow/bpflow_9.png
                    :width: 400
                    :align: center

      * -
        - **Поток «Согласовано»**
        - 
               .. image:: _static/offer/bpflow/bpflow_10.png
                    :width: 400
                    :align: center
      * - 7
        - 
               .. image:: _static/offer/bpform/bpform_27.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_28.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    execution.removeVariable('chiefApproveComment');


Создание элементов для Части (4) схемы бизнес-процесса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/offer/scheme/scheme_4.png
       :width: 600
       :align: center

И таблица, в которой отражены конечные настройки компонент бизнес-процесса (для визуальной сверки):

.. list-table::
      :widths: 5 15 50
      :align: center
      :class: tight-table 

      * - 1
        - 
               .. image:: _static/offer/bpform/bpform_46.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_47.png
                    :width: 400
                    :align: center
      * -
        - **Поток "Согласование директором"**
        - 
               .. image:: _static/offer/bpflow/bpflow_11.png
                    :width: 400
                    :align: center
      * - 2
        - 
               .. image:: _static/offer/bpform/bpform_48.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_49.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    execution.removeVariable('dirApproveComment');

      * - 3
        - 
               .. image:: _static/offer/bpform/bpform_50.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_51.png
                    :width: 400
                    :align: center
      * - 4
        - 
               .. image:: _static/offer/bpform/bpform_52.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_53.png
                    :width: 400
                    :align: center
      * - 5
        - 
               .. image:: _static/offer/bpform/bpform_54.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_55.png
                    :width: 400
                    :align: center

Информация по форме **Согласование директором (Offer Director Form Approve)**:   

.. csv-table::
   :header: "Название поля", "Значение"
   :widths: 10, 10
   :align: center
   :class: tight-table 

      Идентификатор формы,offer-director-form-approve
      Название формы,Offer Director Form Approve
      Редактируемый тип данных,Нет

Ниже приведено изображение конечной настройки (для визуальной сверки):

  .. image:: _static/offer/form_35.png
       :width: 600
       :align: center

Пример формы:

  .. image:: _static/offer/form_36.png
       :width: 600
       :align: center


Компоненты формы:

.. csv-table::
   :header: "Название поля", "Имя свойства", "Наименование компонента"
   :widths: 15, 10, 10
   :align: center
   :class: tight-table 

      ,Колонки формы,Columns Component
      Комментарий руководителя,chiefApproveComment,Text Area Component
      Комментарий доп. согласующего,addApproveComment,Text Area Component
      Комментарий после доработки,reworkComment,Text Area Component
      Комментарий,addApproveComment,Text Area Component

Кнопки формы:

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - Reject
        - |

               .. image:: _static/offer/form_37.png
                    :width: 400
                    :align: center

      * - Rework
        - |

               .. image:: _static/offer/form_38.png
                    :width: 400
                    :align: center
      
      * - Submit
        - |

               .. image:: _static/offer/form_39.png
                    :width: 400
                    :align: center

.. list-table::
      :widths: 5 15 50
      :align: center
      :class: tight-table 

      * - 6
        - 
               .. image:: _static/offer/bpform/bpform_56.png
                    :width: 200
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_57.png
                    :width: 400
                    :align: center
      * -
        - **Поток «Вернуть на доработку»**
        - 
               .. image:: _static/offer/bpflow/bpflow_12.png
                    :width: 400
                    :align: center
      * -
        - **Поток «Отказ»**
        - 
               .. image:: _static/offer/bpflow/bpflow_13.png
                    :width: 400
                    :align: center
      * -
        - **Поток «Согласовано»**
        - 
               .. image:: _static/offer/bpflow/bpflow_14.png
                    :width: 400
                    :align: center

      * - 7
        - 
               .. image:: _static/offer/bpform/bpform_64.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_65.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    execution.removeVariable('reworkComment');
                    execution.removeVariable('addApproveComment');
                    execution.removeVariable('chiefApproveComment');

      * - 8
        - 
               .. image:: _static/offer/bpform/bpform_62.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_63.png
                    :width: 400
                    :align: center
      * - 9
        -
               .. image:: _static/offer/bpform/bpform_60.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_61.png
                    :width: 400
                    :align: center

      * - 10
        - 
               .. image:: _static/offer/bpform/bpform_58.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_59.png
                    :width: 400
                    :align: center

          Для всех подобных задач в **«Форма задачи»** выбрать ранее созданную форму задачи. 


Создание элементов для Части (5) схемы бизнес-процесса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/offer/scheme/scheme_5.png
       :width: 600
       :align: center

И таблица, в которой отражены конечные настройки компонент бизнес-процесса (для визуальной сверки):

.. list-table::
      :widths: 5 15 50
      :align: center
      :class: tight-table 

      * - 1
        - 
               .. image:: _static/offer/bpform/bpform_105.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_106.png
                    :width: 400
                    :align: center
      * -
        - **Поток «Отказ»**
        - 
               .. image:: _static/offer/bpform/bpform_107.png
                    :width: 400
                    :align: center
      * - 2
        - 
               .. image:: _static/offer/bpform/bpform_67.png
                    :width: 100
                    :align: center

        - 
               .. image:: _static/offer/bpform/bpform_68.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    execution.setVariable('isRejected', true);
      * - 3
        -  
               .. image:: _static/offer/bpform/bpform_69.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_70.png
                    :width: 400
                    :align: center
      * - 
        - **Поток «Отказ 1»**
        - 
               .. image:: _static/offer/bpflow/bpflow_15.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    value =execution.getVariable('isRejected')!=true;

      * - 
        - **Поток «Отказ 2»**
        - 
               .. image:: _static/offer/bpflow/bpflow_16.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    value =execution.getVariable('isRejected')==true;
      * - 4, 5
        - 
               .. image:: _static/offer/bpform/bpform_71.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_72.png
                    :width: 400
                    :align: center
      * - 6, 7 
        - 
               .. image:: _static/offer/bpform/bpform_73.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_74.png
                    :width: 400
                    :align: center
      * - 8
        -
               .. image:: _static/offer/bpform/bpform_75.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_76.png
                    :width: 400
                    :align: center

      * - 
        - **Поток "Формирование ответа"**
        - 
               .. image:: _static/offer/bpflow/bpflow_17.png
                    :width: 400
                    :align: center

      * - 9
        - 
               .. image:: _static/offer/bpform/bpform_77.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_78.png
                    :width: 400
                    :align: center

Информация по форме **Формирование ответа кандидату (Offer Form Feedback)**:   

.. csv-table::
   :header: "Название поля", "Значение"
   :widths: 10, 10
   :align: center
   :class: tight-table 

      Идентификатор формы,offer-form-feedback
      Название формы,Offer Form Feedback
      Редактируемый тип данных,нет

Ниже приведено изображение конечной настройки (для визуальной сверки):

  .. image:: _static/offer/form_40.png
       :width: 600
       :align: center

Пример формы:

  .. image:: _static/offer/form_41.png
       :width: 600
       :align: center

Компоненты формы:

.. csv-table::
   :header: "Название поля", "Имя свойства", "Наименование компонента"
   :widths: 15, 10, 10
   :align: center
   :class: tight-table 

      ,Колонки формы,Columns Component
      Комментарий директора,dirApproveComment,Text Area Component
      Comment,offerTaskComment,Text Area Component

Кнопки формы:

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - Send Reject
        - |

               .. image:: _static/offer/form_42.png
                    :width: 400
                    :align: center

      * - Send Offer
        - |

               .. image:: _static/offer/form_43.png
                    :width: 400
                    :align: center


.. list-table::
      :widths: 5 15 50
      :align: center
      :class: tight-table 

      * - 10
        - 
               .. image:: _static/offer/bpform/bpform_79.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_80.png
                    :width: 400
                    :align: center

Создание элементов для Части (6) схемы бизнес-процесса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/offer/scheme/scheme_6.png
       :width: 600
       :align: center

И таблица, в которой отражены конечные настройки компонент бизнес-процесса (для визуальной сверки):

.. list-table::
      :widths: 5 15 50
      :align: center
      :class: tight-table 

      * - 1
        - 
               .. image:: _static/offer/bpform/bpform_82.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_83.png
                    :width: 400
                    :align: center

      * -
        - **Поток «Отправлен оффер»**
        - 
               .. image:: _static/offer/bpflow/bpflow_18.png
                    :width: 400
                    :align: center

      * -
        - **Поток «Отправлен отказ»**
        - 
               .. image:: _static/offer/bpflow/bpflow_19.png
                    :width: 400
                    :align: center

      * - 2
        - 
               .. image:: _static/offer/bpform/bpform_99.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_100.png
                    :width: 400
                    :align: center
      * - 3
        -
               .. image:: _static/offer/bpform/bpform_84.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_85.png
                    :width: 400
                    :align: center
      * - 4
        - 
               .. image:: _static/offer/bpform/bpform_88.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_89.png
                    :width: 400
                    :align: center

           | Текст скрипта:

               .. code-block::

                    execution.removeVariable('offerTaskComment');
                    execution.removeVariable('dirApproveComment');
      * - 5
        - 
               .. image:: _static/offer/bpform/bpform_86.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_87.png
                    :width: 400
                    :align: center

Информация по форме **Ожидание ответа кандидата (Offer Form Feedback From Candidate)**:   

.. csv-table::
   :header: "Название поля", "Значение"
   :widths: 10, 10
   :align: center
   :class: tight-table 

      Идентификатор формы,offer-form-feedback-from-candidate
      Название формы,Offer Form Feedback From Candidate
      Редактируемый тип данных,нет

Ниже приведено изображение конечной настройки (для визуальной сверки):

  .. image:: _static/offer/form_44.png
       :width: 600
       :align: center

Пример формы:

  .. image:: _static/offer/form_45.png
       :width: 600
       :align: center


Компоненты формы:

.. csv-table::
   :header: "Название поля", "Имя свойства", "Наименование компонента"
   :widths: 15, 10, 10
   :align: center
   :class: tight-table 

      ,Колонки формы,Columns Component
      Комментарий,offerTaskComment,Text Area Component
      Комментарий по результатам,_ECM_offerTaskComment,Text Area Component

Кнопки формы:

.. list-table::
      :widths: 10 50
      :align: center
      :class: tight-table 

      * - Reject Offer
        - |

               .. image:: _static/offer/form_46.png
                    :width: 400
                    :align: center

      * - Accept Offer
        - |

               .. image:: _static/offer/form_47.png
                    :width: 400
                    :align: center      

.. list-table::
      :widths: 5 15 50
      :align: center
      :class: tight-table 


      * - 6
        - 
               .. image:: _static/offer/bpform/bpform_90.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_91.png
                    :width: 400
                    :align: center

      * - 
        - **Поток «Оффер принят»**
        - 
               .. image:: _static/offer/bpflow/bpflow_20.png
                    :width: 400
                    :align: center

      * - 
        - **Поток «Оффер не принят»**
        - 
               .. image:: _static/offer/bpflow/bpflow_21.png
                    :width: 400
                    :align: center 
      * - 7
        -
               .. image:: _static/offer/bpform/bpform_92.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_93.png
                    :width: 400
                    :align: center
      * - 8
        - 
               .. image:: _static/offer/bpform/bpform_97.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_98.png
                    :width: 400
                    :align: center 
      * - 9
        -
               .. image:: _static/offer/bpform/bpform_94.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_96.png
                    :width: 400
                    :align: center
      * - 10
        - 
               .. image:: _static/offer/bpform/bpform_95.png
                    :width: 100
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_108.png
                    :width: 400
                    :align: center

      * - 11, 12, 13
        -
               .. image:: _static/offer/bpform/bpform_101.png
                    :width: 70
                    :align: center
        - 
               .. image:: _static/offer/bpform/bpform_102.png
                    :width: 400
                    :align: center

Сохранение и публикация
~~~~~~~~~~~~~~~~~~~~~~~~

Созданный процесс сохраняем и публикуем:

 .. image:: _static/offer/bmpn27.png
       :width: 600
       :align: center

.. _menu_add:

Добавление журнала в главное меню
-----------------------------------

Для наполнения созданных журналов данными необходимо добавить их в главное меню:

1.	Перейти в настройку меню, нажав на шестеренку, потом кнопку **«Настроить меню»** справа сверху.

 .. image:: _static/offer/bmpn28.png
       :width: 600
       :align: center

2.	Выбрать вкладку **"Настройки выбранной конфигурации"**, выбрать раздел , в котором будет находиться журнал. Навести на раздел и нажать кнопку **«Добавить»**, выбрать **«Журнал»**:

 .. image:: _static/offer/journal_9.png
       :width: 600
       :align: center

 Поместим созданные справочники в раздел "Справочники", а кейс "Согласование оффера" в отдельный раздел.

1. Выбрать журнал:

 .. image:: _static/offer/journal_10.png
       :width: 600
       :align: center

Выбранный журнал будет отражен в настройках меню:

 .. image:: _static/offer/journal_11.png
       :width: 600
       :align: center

Аналогично добавим кейс:

 .. image:: _static/offer/journal_12.png
       :width: 600
       :align: center

4. Добавленный пункт меню:

 .. image:: _static/offer/journal_13.png
       :width: 250
       :align: center

Просмотр журнала и создание в нем элемента 
---------------------------------------------

В главном меню выбрать журнал. В журнале нажать **+**, откроется форма для заполнения:

 .. image:: _static/offer/journal_14.png
       :width: 800
       :align: center


Настройка меню "Создать"
-------------------------

Для добавления процесса в меню **«Создать»**:

1.	Перейти в настройку меню, нажав на шестеренку, потом кнопку **«Настроить меню»** справа сверху.

 .. image:: _static/offer/bmpn28.png
       :width: 600
       :align: center

2.	Выбрать вкладку **"Меню "Создать"**, выбрать элемент меню, в котором будет находиться процесс. Навести на элемент и нажать кнопку **«Добавить»**, выбрать **«Добавить ссылку на создание кейса»**:

     .. image:: _static/offer/bmpn29.png
          :width: 600
          :align: center

     |

     .. image:: _static/offer/bmpn30.png
          :width: 400
          :align: center

3. Выбрать тип данных:

     .. image:: _static/offer/bmpn31.png
          :width: 600
          :align: center

**Название** будет указано по умолчанию из типа данных, и может быть изменено. Нажать **"Сохранить"**

     .. image:: _static/offer/bmpn32.png
          :width: 400
          :align: center

4. Добавленный пункт меню:

     .. image:: _static/offer/bmpn33.png
          :width: 250
          :align: center

Запуск кейса
--------------

В меню **"Создать"** выбрать **"Согласование оффера"**, откроется форма для заполнения:

 .. image:: _static/offer/bmpn34.png
       :width: 500
       :align: center
