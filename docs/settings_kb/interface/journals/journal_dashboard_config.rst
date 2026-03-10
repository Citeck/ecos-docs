.. _journal_dashboard_config:

Journal Dashboard Configuration
================================

.. contents::
   :depth: 3

Overview
--------

Each record type in Citeck can have its own :ref:`dashboard <dashboard>` that controls how the record's detail page looks when opened from a journal. This dashboard defines the layout, tabs, and widgets shown to the user.

This article describes how dashboards are associated with journals (via record types), how they are saved and loaded, how workspace and user-level overrides work, and how to export and import dashboard configurations.

.. note::

   Dashboards are managed in the **Admin section → UI Configuration → Dashboards** journal
   (``/v2/journals?journalId=ecos-dashboards``).

How a Dashboard Is Linked to a Journal
---------------------------------------

Citeck journals are always associated with a **record type** (``typeRef`` in the journal configuration). When a user opens a record from a journal, the platform resolves which dashboard to display using the following data:

- The ``typeRef`` of the opened record (determined from ``_type`` attribute or from ``recordRef`` in the URL).
- The dashboard type (``case-details``, ``user-dashboard``, etc.) determined from the ``_dashboardType`` attribute of the record.
- The current user's authority (username or group membership).
- The current workspace context.

To set up a dashboard for a specific journal's records, you create (or upload) a dashboard artifact with ``typeRef`` pointing to the ECOS type used by that journal.

Dashboard Resolution Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a record page is opened, the platform selects the dashboard in the following order (highest to lowest priority):

1. Dashboard with ``appliedToRef`` matching the exact record **and** the current user's authority.
2. Dashboard with ``appliedToRef`` matching the exact record **for all users** (authority is empty).
3. Dashboard with ``typeRef`` matching the record's type **and** the current user's authority.
4. Dashboard with ``typeRef`` matching the record's type **for all users** (authority is empty).
5. If no match found and ``expandType`` is enabled — repeat steps 3–4 for each parent type in the type hierarchy (stops when the ``inhDashboardType`` attribute changes).
6. If still no match — fall back to the default dashboard for the resolved dashboard type (e.g., ``user-dashboard``).

.. note::

   For workspace-scoped requests the platform first searches dashboards within the current workspace,
   then falls back to dashboards with no workspace restriction.

Data Model
----------

A dashboard is represented by the ``DashboardDto`` data class. Each dashboard record has the following fields:

.. list-table::
   :widths: 20 15 65
   :header-rows: 1
   :class: tight-table

   * - Field
     - Type
     - Description
   * - ``id``
     - String
     - Unique external identifier of the dashboard (UUID or human-readable string).
   * - ``name``
     - MLText
     - Multilingual display name (used in the Dashboards journal).
   * - ``typeRef``
     - EntityRef
     - Reference to the ECOS type this dashboard is configured for (e.g., ``emodel/type@contract``).
   * - ``appliedToRef``
     - EntityRef
     - Reference to a specific record this dashboard applies to. When set, the dashboard overrides the type-level dashboard for that one record only.
   * - ``authority``
     - String
     - Username or group for whom this dashboard is personalised. Empty means the dashboard applies to all users.
   * - ``scope``
     - String
     - Contextual scope string. Usually empty; can be used to distinguish dashboards opened in different UI contexts.
   * - ``priority``
     - Float
     - Priority used when multiple dashboards match; higher value = higher priority.
   * - ``workspace``
     - String
     - Workspace ID this dashboard belongs to. Empty means the dashboard is available in all workspaces.
   * - ``config``
     - JSON object
     - The full layout configuration: tabs, columns, and widgets. See `Dashboard Config Structure`_ below.
   * - ``attributes``
     - JSON object
     - Additional metadata. Rarely used; can hold arbitrary key-value pairs.

Dashboard Config Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``config`` field contains the visual layout of the dashboard. The format supports two versions:

**Legacy format (v1):**

.. code-block:: json

   {
     "layouts": [
       {
         "id": "layout_<uuid>",
         "tab": { "label": "Tab name", "idLayout": "layout_<uuid>" },
         "type": "1-column",
         "columns": [
           {
             "widgets": [
               {
                 "id": "<widget-uuid>",
                 "dndId": "<dnd-uuid>",
                 "name": "journal",
                 "label": "dashboard-settings.widget.journal",
                 "props": {
                   "id": "<widget-uuid>",
                   "config": {
                     "version": "v2",
                     "v2": {
                       "journalId": "my-journal",
                       "customJournalMode": false
                     }
                   }
                 }
               }
             ]
           }
         ]
       }
     ],
     "mobile": [ ... ]
   }

**v2 format** (current, recommended):

.. code-block:: json

   {
     "version": "v2",
     "v2": {
       "widgets": [
         {
           "id": "<widget-uuid>",
           "dndId": "<dnd-uuid>",
           "name": "properties",
           "label": "dashboard-settings.widget.properties",
           "props": { "id": "<widget-uuid>", "config": {} }
         }
       ],
       "desktop": [
         {
           "id": "layout_<uuid>",
           "tab": { "label": { "ru": "Основное", "en": "General" }, "idLayout": "layout_<uuid>" },
           "type": "2-columns-big-small",
           "columns": [
             { "widgets": ["<widget-uuid>"] },
             { "widgets": ["<widget-uuid>"], "width": "25%" }
           ]
         }
       ],
       "mobile": [
         {
           "id": "layout_<uuid>",
           "tab": { "label": { "ru": "Вкладка", "en": "Tab" }, "idLayout": "layout_<uuid>" },
           "type": "mobile",
           "columns": [ { "widgets": ["<widget-uuid>"] } ]
         }
       ]
     }
   }

Available layout types:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Layout type
     - Description
   * - ``1-column``
     - Single full-width column.
   * - ``2-columns``
     - Two equal columns.
   * - ``2-columns-big-small``
     - Two columns, main (wide) + sidebar (narrow, e.g., 25%).
   * - ``mobile``
     - Single column optimised for mobile screens.

Configuring a Dashboard for a Journal via the UI
-------------------------------------------------

The dashboard for a journal's record type is configured directly on the record's detail page or in the Dashboards journal.

**From the record's detail page:**

1. Open any record of the target type.
2. Click the **gear icon → "Configure page"** (Настроить страницу).
3. In the **Ownership** section:

   - **Dashboard id** — auto-generated identifier.
   - **Type** — select the ECOS type for which the dashboard will apply. Changing this defines the scope.
   - **Applied to record** — optionally bind the dashboard to a single specific record instead of the whole type.
   - **Apply for all users** — when checked, the saved dashboard becomes the default for all users of that type (no user-specific override).

4. In the **View** section, configure tabs, layout columns, and add widgets by dragging them.
5. Click **Save**.

.. note::

   Without the **"Apply for all users"** flag, the saved dashboard is personal to the current user.
   An administrator can create a shared dashboard by checking this flag.

**From the Dashboards journal (Admin section):**

Dashboards can be managed in the **Dashboards** journal
(Admin section → UI Configuration → Dashboards):

- **Download** (``ecos-module-download``) — export the dashboard as a JSON/YAML file.
- **Edit** — open the dashboard configuration form.
- **Edit JSON** — edit the raw YAML/JSON representation.
- **Copy** — duplicate an existing dashboard (creates a new record).
- **Delete** — remove the dashboard.

Default Protected Dashboards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following dashboards are protected from modification by non-system users. They act as global fallbacks and are delivered as application artifacts:

.. list-table::
   :widths: 40 60
   :header-rows: 1
   :class: tight-table

   * - Dashboard ID
     - Purpose
   * - ``user-dashboard``
     - Default home page for users.
   * - ``user-base-type-dashboard``
     - Default dashboard for base user-type records.
   * - ``base-type-dashboard``
     - Default dashboard for all base-type records (shows preview, properties, comments, history).
   * - ``site-dashboard``
     - Default for site/section pages.
   * - ``person-dashboard``
     - Person profile page.
   * - ``orgstructure-person-dashboard``
     - Person dashboard opened from the org structure context.
   * - ``default-doclib-dashboard``
     - Default document library dashboard.
   * - ``ws-dashboard-default``
     - Default workspace dashboard.
   * - ``personal-ws-dashboard-default``
     - Default personal workspace dashboard.

Save and Load Mechanisms
------------------------

Save flow
~~~~~~~~~

When a user saves a dashboard (via the UI gear menu or the Dashboards journal):

1. The client sends a **mutate** request to the Records API: ``uiserv/dashboard@<id>``.
2. ``DashboardRecords.mutate()`` validates that the record exists (if updating) and applies the incoming JSON attributes.
3. ``DashboardService.saveDashboard()`` is called:

   a. **Authority check** — a regular user can only save a dashboard for themselves; saving for another user or for all users (empty authority) in a global workspace requires admin/system privileges. Workspace managers may save shared dashboards within their workspace.
   b. If the dashboard is one of the protected defaults and is not workspace-specific, non-system users are rejected.
   c. The ``workspace`` field value ``"default"`` is normalised to an empty string before persistence.
   d. The DTO is mapped to a ``DashboardEntity`` (JPA entity): if an entity with matching ``typeRef`` + ``authority`` + ``scope`` + ``workspace`` already exists it is updated; otherwise a new entity with a generated UUID ``extId`` is created.
   e. The entity is persisted to the ``dashboards`` PostgreSQL table; the ``config`` field is stored as a BSON/JSON byte array.
   f. All registered change listeners are notified (``BiConsumer<DashboardDto?, DashboardDto>``).

Load flow
~~~~~~~~~

When the UI opens a record page and needs the dashboard configuration:

1. The client sends a **query** to ``uiserv/dashboard`` with:

   .. code-block:: json

      {
        "language": "dashboard",
        "query": {
          "recordRef": "emodel/type@contract@some-id",
          "typeRef": "emodel/type@contract",
          "authority": "admin",
          "scope": "",
          "workspace": "admin$workspace",
          "expandType": true,
          "includeForAll": true
        }
      }

2. ``DashboardRecords.queryRecords()`` delegates to ``DashboardService.getForAuthority()``.
3. The service checks workspace membership for the requesting user.
4. The resolution algorithm (see `Dashboard Resolution Algorithm`_) is applied.
5. The matching ``DashboardEntity`` is mapped to ``DashboardDto`` and returned as JSON.

The frontend caches the resolved dashboard configuration for the lifetime of the browser tab to avoid repeated queries.

Export and Import
-----------------

Dashboards are first-class **artifacts** in the Citeck application framework. Their artifact type is ``ui/dashboard``.

Export
~~~~~~

**Manual export from the UI:**

1. Open **Admin section → UI Configuration → Dashboards**.
2. Find the dashboard row.
3. Click **Download** (the ``ecos-module-download`` action).
4. A YAML file is downloaded with the full dashboard configuration.

**Automatic export (artifact synchronisation):**

``DashboardArtifactHandler.listenChanges()`` registers a change listener that fires on every dashboard save. Dashboards that belong to the default workspace (empty or ``"default"`` workspace field) are automatically published to the artifact system. This allows them to be packaged into ECOS application modules (``ecos-apps``) and distributed across environments.

Only default-workspace dashboards are exported automatically. Workspace-specific or user-personalised dashboards are not synced to the artifact system.

Import
~~~~~~

**Manual import via the UI:**

1. Open **Admin section → UI Configuration → Dashboards**.
2. Click **+ → Upload dashboard** (the ``ecos-module-upload`` create variant).
3. Select a ``*.json`` or ``*.yaml`` dashboard file.
4. The file is parsed and the dashboard is saved via the same save flow described above.

**Artifact deployment (application-level import):**

When a Citeck application is deployed (e.g., via ``ecos-apps``), all ``ui/dashboard`` artifacts inside the application package are processed by ``DashboardArtifactHandler.deployArtifact()``:

1. The artifact DTO is received as a ``DashboardDto``.
2. The handler calls ``AuthContext.runAsSystemJ()`` to run with system privileges.
3. ``DashboardService.saveDashboard()`` persists the dashboard.

This mechanism allows shipping pre-configured dashboards together with ECOS application modules. The deployed dashboards can later be overridden per-user or per-workspace through the UI.

**Placing dashboard artifacts in a module:**

Place dashboard JSON/YAML files under:

.. code-block:: text

   src/main/resources/eapps/artifacts/ui/dashboard/

The file name becomes part of the ``id`` if not explicitly specified inside the file. Example:

.. code-block:: yaml

   id: my-contract-dashboard
   typeRef: emodel/type@contract
   authority: null
   priority: 0
   config:
     version: v2
     v2:
       widgets:
         - id: widget-001
           name: properties
           label: dashboard-settings.widget.properties
           props:
             id: widget-001
             config: {}
       desktop:
         - id: layout_001
           tab:
             label: { en: General, ru: "Основное" }
             idLayout: layout_001
           type: 1-column
           columns:
             - widgets:
                 - widget-001
       mobile:
         - id: layout_m01
           tab:
             label: { en: Tab, ru: "Вкладка" }
             idLayout: layout_m01
           type: mobile
           columns:
             - widgets:
                 - widget-001

Access Control
--------------

Two dynamic configuration flags (``ecos-config``) control who can edit dashboards and widgets:

.. list-table::
   :widths: 45 55
   :header-rows: 1
   :class: tight-table

   * - Config key
     - Description
   * - ``restrict-access-to-edit-dashboard``
     - When ``true``, only administrators can configure dashboard layouts and tabs. Default: ``false``.
   * - ``restrict-access-to-edit-dashboard-widgets``
     - When ``true`` (or ``null``), only administrators can configure individual widgets. Default: ``null`` (unset).

These settings are managed in **Admin section → System management → ECOS Configuration**
(journal ``ecos-configs``).

Even when these flags allow editing, the service enforces the following rules:

- A regular user can only save a dashboard for **themselves** (their own ``authority``).
- Saving a dashboard for another user raises an ``AccessDeniedException``.
- Saving or deleting a **protected default** dashboard is blocked for non-system users.
- A **workspace manager** can save shared dashboards (empty authority) within their own workspace.

Database Schema
---------------

Dashboards are stored in the ``dashboards`` table in the ``ecos-uiserv`` PostgreSQL database:

.. list-table::
   :widths: 20 15 65
   :header-rows: 1
   :class: tight-table

   * - Column
     - Type
     - Description
   * - ``id``
     - BIGINT
     - Internal auto-generated primary key.
   * - ``ext_id``
     - VARCHAR
     - External identifier used in all API calls.
   * - ``type_ref``
     - VARCHAR(512)
     - Serialised ``EntityRef`` of the associated ECOS type.
   * - ``applied_to_ref``
     - VARCHAR
     - Serialised ``EntityRef`` of the specific record this dashboard applies to (optional).
   * - ``authority``
     - VARCHAR(64)
     - Username or group (stored lowercased). ``NULL`` means "for all users".
   * - ``scope``
     - VARCHAR
     - Contextual scope string (default: empty string).
   * - ``priority``
     - REAL
     - Dashboard priority; higher value = selected first.
   * - ``config``
     - BYTEA
     - JSON-serialised dashboard layout (widgets, tabs, columns).
   * - ``name``
     - VARCHAR
     - JSON-serialised ``MLText`` (multilingual name).
   * - ``workspace``
     - VARCHAR
     - Workspace identifier. Empty string means global (all workspaces).
   * - ``created_date``
     - TIMESTAMP
     - Audit: creation timestamp.
   * - ``created_by``
     - VARCHAR(50)
     - Audit: creator username.
   * - ``last_modified_date``
     - TIMESTAMP
     - Audit: last modification timestamp.
   * - ``last_modified_by``
     - VARCHAR(50)
     - Audit: last modifier username.

Related Documentation
---------------------

- :ref:`Dashboards overview <dashboard>` — dashboard types, search algorithm, caching, and permission settings.
- :ref:`Widgets <widgets>` — available widgets and their configuration options.
- :ref:`Journal configuration <journals>` — how to create and configure journals.
- :ref:`ECOS artifacts <ecos_artifacts>` — artifact system and application deployment.
- :ref:`Workspaces <workspaces>` — workspace concepts and membership rules.
