Пользователи и права доступа
==============================

Раздел описывает управление пользователями, группами доступа и синхронизацию учётных данных в Citeck.

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: Группы доступа
      :link: groups
      :link-type: ref

      Встроенные группы платформы (``ECOS_ADMINISTRATORS``, ``EVERYONE``, ``USERS_PROFILE_ADMIN`` и др.), определяющие роли и права пользователей в системе.

   .. grid-item-card:: Синхронизация Authorities
      :link: sync_authorities
      :link-type: ref

      Механизм синхронизации пользователей и групп с внешними источниками (LDAP и др.) через микросервис ecos-model.

.. toctree::
    :maxdepth: 2
    :hidden:

    authorities/groups
    authorities/sync_authorities
