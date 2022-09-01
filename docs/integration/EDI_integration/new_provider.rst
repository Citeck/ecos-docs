Реализация интеграции с новым ЭДО-провайдером
===================================================

1. Со стороны бандла работы с ЭДО-провайдером (мкр. интеграции)
----------------------------------------------------------------

Создать java проект с бандлом. Пример создания нового бандла можно посмотреть тут: Пример создания бандла.

В данном проекте обязательно надо импортнуть зависимость ``ru.citeck.ecos.ecos-edi-commons``. Версия должна соответствовать той, которая находится в микросервисе интеграции необходимой Вам версии.

В активаторе (класс интерфейса ``org.osgi.framework.BundleActivator``) необходимо зарегистрировать свои реализации ``ru.citeck.ecos.domain.edi.service.sync.EdiEventsSyncService`` и ``ru.citeck.ecos.domain.edi.service.api.EdiApiService в бинах микросервиса integrations``. Пример из Контура (не забудьте при выгрузке бандла выполнять unregister(…)):

.. code-block::

        EdiEventsSyncServiceResolver ediEventsSyncServiceResolver = ApplicationContextReflection.getBean(EdiEventsSyncServiceResolver.class);
        MandatoryParam.check("ediEventsSyncServiceResolver", ediEventsSyncServiceResolver);
        ediEventsSyncServiceResolver.register(getKonturEventsSyncService()); // в методе get* происходит ленивое создание сервиса

        EdiApiServiceResolver ediApiServiceResolver = ApplicationContextReflection.getBean(EdiApiServiceResolver.class);
        MandatoryParam.check("ediApiServiceResolver", ediApiServiceResolver);
        ediApiServiceResolver.register(getKonturEdiApiService()); // в методе get* происходит ленивое создание сервиса

После этого шага, запросы к Вашему ЭДО-провайдеру в рамках этих интерфейсов будут транслироваться в Ваш сервис.

В существующих на данный момент бандлах можно так же найти примеры регистрации слушателя изменения данных по какому-то ящику (сущности ящика, кредов, датасорса). Можно использовать для чистки кешей внутри бандла.

В случае отсутствия Вашего провайдера в enum ``ru.citeck.ecos.domain.edi.dto.enums.EdiProviderType`` либы ``ecos-edi-commons`` - необходимо будет его завести.

2. Со стороны связующей либы ecos-edi-integration (мкр. интеграции)
-------------------------------------------------------------------

Как бы не хотелось полностью унифицировать обработку одного ЭДО-провайдера от другого - не получится. Разные атрибуты для идентификаторов, немного разная политика поиска и тд.

Поэтому, создан небольшой интерфейс ``ru.citeck.ecos.edi.domain.integration.service.provider.ProviderHandler`` на стороне ``ecos-edi-integration``, которая выполняет действия по поиску записей в альфреске (пока в альфреске).

Реализацию для нового провайдера необходимо зарегистрировать. Делается это просто - ``ru.citeck.ecos.edi.domain.integration.factory.ApplicationCamelContextFactoryImpl#createProviderResolver``:

.. code-block::

    QOverride
    protected ProviderResolver createProviderResolver() {
    return new ProviderResolver(
    ew CopyOnliriteArrayList<>(Arrays.asList(
    new KonturProviderHandLer(getSignatureService(), getEcosConfigService()),
    new CorusProviderHandler(),,
    new SbisProviderHandler())));

3. Со стороны хранилки (альфреско)
------------------------------------

На данный момент, хранилка - альфреско. Ее можно сменить при наличии подобного варианта, переделав лишь либу ``ecos-edi-integration`` или сделав аналогичную для конкретной хранилки.

1. Создать аспект для хранения идентификаторов документов (подписей, в случае некоторых провайдеров).

2. Зарегистрировать свою реализацию ``ru.citeck.ecos.integration.edi.documents.identifiers.EdiIdentifiersProvider`` в ``ru.citeck.ecos.integration.edi.documents.identifiers.EdiIdentifiersProviderRegistry``. Если вы наследуетесь от ``ru.citeck.ecos.integration.edi.documents.identifiers.AbstractEdiIdentifiersProvider``, то регистрация при инициализации бина произойдет автоматически за счет ``@PostConstruct``.

Данный сервис необходим для генерации печатных форм (проверка существования идентификаторов ЭДО у нод) и для определения типа документа EDI (не путать с ЮЗДО).

3. Зарегистрировать свою реализацию ``ru.citeck.ecos.integration.edi.documents.titles.TitleTypeService`` в ``ru.citeck.ecos.integration.edi.documents.titles.TitleTypeServiceRegistry``. Если вы наследуетесь от ``ru.citeck.ecos.integration.edi.documents.titles.AbstractTitleTypeService``, то регистрация при инициализации бина произойдет автоматически за счет ``@PostConstruct``.

Данный сервис необходим при подписании ЮЗДО. Благодаря ему определяется, нужно ли генерировать и подписывать титул документа или достаточно подписи самого вложения.

4. Самая основная часть - подготовка запросов и постобработка ответов. За кастомную часть этого процесса отвечает ``ru.citeck.ecos.integration.edi.service.EdiProviderHelper``, которому делегируется составление DTO, которые будут отправлены в микросервис и, далее, в бандл. Как и с остальными сервисами, тут надо зарегистрировать свой компонент в своем registry, как и у остальных сервисов, тут есть авторегистрирующий ``ru.citeck.ecos.integration.edi.service.AbstractEdiProviderHelper``. Лучше использовать его, в нем частично функционал класса уже реализован.

