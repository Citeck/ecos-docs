.. _how-to:

How-to руководства 
====================

.. _how-to-bundle-archetype:

Создание бандла из архетипа
---------------------------------------------------

1. Перейти в папку, где должен быть сгенерирован бандл. Папка не должна содержать ``pom.xml`` файла.
2. В командной строке выполнить одну из команд ниже.

Для бандла с эндпойнтом:

.. code-block:: bash

    mvn archetype:generate \
        -DarchetypeGroupId=ru.citeck.ecos.bundle \
        -DarchetypeArtifactId=ecos-web-endpoint-bundle-archetype \
        -DarchetypeVersion=1.0-SNAPSHOT \
        -DgroupId=<new_bundle_groupId> \
        -DartifactId=<new_bundle_artefactId>

Для обычного бандла:

.. code-block:: bash

    mvn archetype:generate \
        -DarchetypeGroupId=ru.citeck.ecos.bundle \
        -DarchetypeArtifactId=ecos-osgi-bundle-archetype \
        -DarchetypeVersion=1.0-SNAPSHOT \
        -DgroupId=<new_bundle_groupId> \
        -DartifactId=<new_bundle_artefactId>
