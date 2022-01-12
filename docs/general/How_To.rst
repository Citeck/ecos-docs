=============
How To
=============
Создание бандла из архетипа
---------------------------------------------

1. Распаковать архив с архетипом
2. В папке архетипа в комндной строке выполнить::

mvn -B -U clean install

3. Перейти в папку, где должен быть сгенерирован бандл. Папка не должна содержать pom.xml файла
4. В командной строке выполнить

Для бандла с эндпойнтом::

mvn archetype:generate -DarchetypeGroupId=ru.citeck.ecos.bundle -DarchetypeArtifactId=ecos-web-endpoint-bundle-archetype -DarchetypeVersion=1.0 -DgroupId=<new_bundle_groupId> -DartifactId=<new_bundle_artefactId> 

Для просто бандла:: 

mvn archetype:generate -DarchetypeGroupId=ru.citeck.ecos.bundle -DarchetypeArtifactId=ecos-osgi-bundle-archetype -DarchetypeVersion=1.0 -DgroupId=<new_bundle_groupId> -DartifactId=<new_bundle_artefactId>




To be documented
