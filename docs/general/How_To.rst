How To
=======
Создание бандла из архетипа
-----------------------------

1. Перейти в папку, где должен быть сгенерирован бандл. Папка не должна содержать pom.xml файла
2. В командной строке выполнить

Для бандла с эндпойнтом::

    mvn archetype:generate -DarchetypeGroupId=ru.citeck.ecos.bundle -DarchetypeArtifactId=ecos-web-endpoint-bundle-archetype -DarchetypeVersion=1.0-SNAPSHOT -DgroupId=<new_bundle_groupId> -DartifactId=<new_bundle_artefactId> 

Для просто бандла:: 

    mvn archetype:generate -DarchetypeGroupId=ru.citeck.ecos.bundle -DarchetypeArtifactId=ecos-osgi-bundle-archetype -DarchetypeVersion=1.0-SNAPSHOT -DgroupId=<new_bundle_groupId> -DartifactId=<new_bundle_artefactId>

To be documented
