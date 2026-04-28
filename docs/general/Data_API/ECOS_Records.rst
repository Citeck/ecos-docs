.. _Records_API:

Records API
==============

**Records API** — a system-level interface for accessing and manipulating data. The data entities are called records.

**Record** — an entity with a set of attributes and a record identifier (:ref:`RecordRef <RecordRef>`).

Data can be retrieved:

 - using the browser — see :ref:`using Records API in the browser <using_in_browser>` and :ref:`CRUD operations <CRUD_records_api>`;
 - backend — see :ref:`server-side interaction <java_kotlin_backend>` and `Records API kotlin/java engine source code <https://github.com/Citeck/ecos-records>`_.


Overview
--------------

An API designed to provide simple and easily scalable communication between a data consumer and a data source. Data sources can be databases, REST services, and others.

Advantages:

- A unified API for data access across the system for all consumers (browser, mobile app, reporting system, data indexing, various microservices, etc.);
- Support for loading data from related entities. For example, if a contract references a power of attorney, having the contract identifier allows retrieving any attribute of the related power of attorney;
- Efficiency. Only the attributes required by the consumer are loaded and computed;
- Ease of development — the data source developer describes all attributes that consumers may request, regardless of the complexity of their computation. The consumer specifies only the attributes it is interested in;
- Ease of maintenance — no API versioning is needed, since new attributes can be added at any time without affecting existing ones;
- The type of returned data is fully described by the request. The data source returns attributes of any type, and Records API converts them to the type required by the consumer;
- Computed attributes. The ability to add attributes that are not stored in a database or any other storage, but are computed based on existing ones;
- Support for merging attributes from different sources. For example, a data source can be written that takes some attributes from Alfresco and others from an external database, joining them by identifier.


.. toctree::
    :maxdepth: 2

    ECOS_Records/records_intro
    ECOS_Records/attributes
    ECOS_Records/RecordsService
    ECOS_Records/RecordRef
    ECOS_Records/using_in_browser
    ECOS_Records/java_kotlin_backend
    ECOS_Records/records_syntax
    ECOS_Records/ECOS_Records_examples
