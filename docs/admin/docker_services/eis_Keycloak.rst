eis (Keycloak)
===============

Назначение:
----------------

Аутентификация и авторизация: Keycloak предоставляет механизмы аутентификации и авторизации, позволяя пользователям входить в систему и контролировать доступ к ресурсам на основе определенных политик безопасности.

Единый вход (Single Sign-On, SSO): Keycloak поддерживает SSO, что позволяет пользователям авторизоваться один раз и получить доступ к нескольким приложениям без необходимости повторного ввода учетных данных.

Социальная аутентификация: Keycloak интегрируется с различными социальными платформами, такими как Google, Facebook, Twitter и другими, что позволяет пользователям использовать свои учетные записи на этих платформах для входа в ваше приложение.

Управление идентичностью: Keycloak предоставляет возможность управлять пользователями, ролями и группами, а также выполнять другие операции по управлению идентичностью, такие как сброс пароля, проверка электронной почты и другие.

Интеграция с веб-приложениями: Keycloak предоставляет клиентские адаптеры и библиотеки для интеграции с различными веб-приложениями и службами, обеспечивая безопасность и удобство взаимодействия с IAM-системой.

Теги:
----------------

*	**nexus.citeck.ru/keycloak:12.0.4** -  образ, собранный на основе **docker.io/jboss/keycloak:12.0.4** , в который добавлены переменные citeck

Базовые образы:
----------------

*	keycloak:12.0.4

Шаблон сервиса docker-compose:
--------------------------------

.. code-block::

	eis:
		logging:
		options:
			max-size: "10m"
			max-file: "5"
		image: docker.io/jboss/keycloak:12.0.4
		container_name: eis
		hostname: eis
		restart:  unless-stopped
		environment:
		PROXY_ADDRESS_FORWARDING: "true"
		DB_VENDOR: POSTGRES
		DB_ADDR: eis_postgres
		DB_DATABASE: keycloak
		DB_USER: keycloak
		DB_SCHEMA: public
		DB_PASSWORD: password
		KEYCLOAK_USER: admin
		KEYCLOAK_PASSWORD: password
			# Uncomment the line below if you want to specify JDBC parameters. The parameter below is just an example, and it shouldn't be used in production without knowledge. It is highly recommended that you read the PostgreSQL JDBC driver documentation in order to use it.
			#JDBC_PARAMS: "ssl=true"
		ports:
		- 443:8443
		depends_on:
		- eis_postgres
		networks:
		- app_network
	eis_postgres:
		image: postgres:11
		container_name: eis_postgres
		hostname: eis_postgres
		volumes:
		- /opt/postgresql/keycloak:/var/lib/postgresql/data
		environment:
		POSTGRES_DB: keycloak
		POSTGRES_USER: keycloak
		POSTGRES_PASSWORD: password
		networks:
		- app_network

Шаблон сервиса для k8s helm-template:
--------------------------------------

.. code-block::

		{{- if .Values.EcosIdentityApp.enabled -}}
		apiVersion: apps/v1
		kind: Deployment
		metadata:
		labels:
			app: ecos-identity-app
		name: ecos-identity-app
		spec:
		{{- if .Values.EcosIdentityApp.highAvailability.enabled }}
		replicas: {{ .Values.EcosIdentityApp.replicas | default "2" }}
		{{- else }}
		replicas: {{ .Values.EcosIdentityApp.replicas | default "1" }}
		{{- end }}
		selector:
			matchLabels:
			app: ecos-identity-app
		strategy:
			rollingUpdate:
			maxSurge: 0
			maxUnavailable: 1
			type: RollingUpdate
		template:
			metadata:
			labels:
				app: ecos-identity-app
			annotations:
			{{- if and .Values.global.vault.enabled .Values.global.vault.annotations }}
			{{- with .Values.global.vault.annotations }}
				{{- toYaml . | nindent 8 }}
			{{- end }}
			{{- end }}
			spec:
			{{- if .Values.EcosIdentityApp.nodeSelector }}
			nodeSelector:
		{{ toYaml .Values.EcosIdentityApp.nodeSelector | indent 8 }}
			{{- end }}
			containers:
			- command:
				- /scripts/keycloak.sh
				env:
				- name: KEYCLOAK_FRONTEND_URL
				{{- if .Values.EcosIdentityApp.environments.frontendURL }}
				value: {{ .Values.EcosIdentityApp.environments.frontendURL }}
				{{ else }}
				value: https://{{ .Values.FQDN }}/auth
				{{- end }}
				{{- if .Values.EcosIdentityApp.import.realm.enabled }}
				- name: KEYCLOAK_IMPORT
				value: /import/realm-export.json
				{{- end }}
				- name: HOSTNAME
				value: ecos-identity-app
				- name: KEYCLOAK_LOGLEVEL
				value: {{ .Values.EcosIdentityApp.environments.logLevel| default "INFO" }}
				- name: KEYCLOAK_USER
				value: {{ .Values.EcosIdentityApp.environments.username | default "admin" }}
				- name: KEYCLOAK_PASSWORD
				{{- if .Values.global.vault.keycloak.appPassword }}
				value: {{ .Values.global.vault.keycloak.appPassword | quote }}
				{{- else }}
				valueFrom:
					secretKeyRef:
					key: ecos-identity-app-password
					name: ecos-secret
				{{- end }}
				- name: JAVA_TOOL_OPTIONS
				value: -XX:+UseContainerSupport -XX:MaxRAMPercentage=50.0
				- name: PROXY_ADDRESS_FORWARDING
				value: "true"
				- name: DB_VENDOR
				value: postgres
				- name: DB_ADDR
				value: {{ .Values.EcosIdentityApp.dataSource.host | default "ecos-microservices-postgresql-app-service" }}.{{ .Release.Namespace }}{{ .Values.clusterName | default "" }}
				- name: DB_PORT
				value: {{ .Values.EcosIdentityApp.dataSource.port | default "5432" | quote }}
				- name: DB_DATABASE
				value: {{ .Values.EcosIdentityApp.dataSource.database| default "ecos_identity" }}
				- name: DB_USER
				{{- if .Values.global.vault.keycloak.psqlUsername }}
				value: {{ .Values.global.vault.keycloak.psqlUsername | quote }}
				{{- else }}
				valueFrom:
					secretKeyRef:
					key: ecos-identity-postgresql-app-username
					name: ecos-secret
				{{- end }}
				- name: DB_PASSWORD
				{{- if .Values.global.vault.keycloak.psqlPassword }}
				value: {{ .Values.global.vault.keycloak.psqlPassword | quote }}
				{{- else }}
				valueFrom:
					secretKeyRef:
					key: ecos-identity-postgresql-app-password
					name: ecos-secret
				{{- end }}
				{{- if .Values.EcosIdentityApp.highAvailability.enabled }}
				- name: JGROUPS_DISCOVERY_PROTOCOL
				value: dns.DNS_PING
				- name: JGROUPS_DISCOVERY_PROPERTIES
				value: dns_query=ecos-identity-app-service-headless
				- name: CACHE_OWNERS_COUNT
				value: '2'
				- name: CACHE_OWNERS_AUTH_SESSIONS_COUNT
				value: '2'
				{{- end }}
				{{- if .Values.EcosIdentityApp.ecosExtensions.enabled }}
				- name: ECOS_KK_RMQ_HOST
				value: rabbitmq-app-service.{{ .Release.Namespace }}{{ .Values.clusterName | default "" }}
				- name: ECOS_KK_RMQ_USERNAME
				value: {{ .Values.RabbitmqApp.environments.username | default "rabbitmqadmin" }}
				- name: ECOS_KK_RMQ_PASSWORD
				value: {{ .Values.RabbitmqApp.environments.password | default "RabbitmqStrongPassword" }}
				- name: ECOS_KK_ZK_HOST
				value: zookeeper-app-service-headless.{{ .Release.Namespace }}{{ .Values.clusterName | default "" }}
				- name: ECOS_KK_LISTEN_PERSON_DISABLED_STATUS
				value: {{ .Values.EcosIdentityApp.ecosExtensions.listenPersonDisabledStatus | quote }}
				{{- end }}
				image: {{ .Values.EcosIdentityApp.image.registry }}/{{ .Values.EcosIdentityApp.image.repository }}:{{ .Values.EcosIdentityApp.image.tag }}
				imagePullPolicy: {{ .Values.EcosIdentityApp.image.pullPolicy | default "IfNotPresent" }}
				name: ecos-identity-app
				ports:
				- containerPort: 8080
				name: http
				protocol: TCP
				- containerPort: 8443
				name: https
				protocol: TCP
				securityContext:
				runAsNonRoot: true
				runAsUser: 1000
				{{- with .Values.EcosIdentityApp.resources }}
				resources:
				{{- tpl . $ | nindent 12 }}
				{{- end }}
				livenessProbe:
				failureThreshold: 3
				httpGet:
					path: /auth/
					port: http
					scheme: HTTP
				initialDelaySeconds: 300
				periodSeconds: 10
				successThreshold: 1
				timeoutSeconds: 5
				readinessProbe:
				failureThreshold: 3
				httpGet:
					path: /auth/realms/master
					port: http
					scheme: HTTP
				initialDelaySeconds: 30
				periodSeconds: 10
				successThreshold: 1
				timeoutSeconds: 1
				volumeMounts:
				- mountPath: /scripts
				name: sh
				readOnly: true
				- mountPath: /opt/jboss/startup-scripts
				name: startup
				readOnly: true
				{{- if .Values.EcosIdentityApp.import.certs.enabled }}
				- mountPath: /opt/certs
				name: certs
				readOnly: true
				{{- end }}
				{{- if .Values.EcosIdentityApp.import.realm.enabled }}
				- mountPath: /import
				name: realm-export
				readOnly: true
				{{- end }}
				{{- if .Values.EcosIdentityApp.KerberosIntegration.enabled }}
				- mountPath: /etc/krb5.conf.d
				name: krb5-conf
				readOnly: true
				- mountPath: /opt/keytab
				name: keytab
				readOnly: true
				{{- end }}
				{{- if .Values.EcosIdentityApp.ecosExtensions.enabled }}
				- mountPath: '/opt/jboss/keycloak/standalone/deployments/ecos'
				name: ecos-extensions
				{{- end }}
			initContainers:
			- command:
				- /bin/sh
				- -c
				- |
				while true
				do
					{{- if .Values.EcosMicroservicesPostgresqlApp.enabled }}
					rt=$(nc -z -w 1 {{ .Values.EcosIdentityApp.dataSource.host | default "ecos-microservices-postgresql-app-service" }}.{{ .Release.Namespace }}{{ .Values.clusterName | default "" }} {{ .Values.EcosIdentityApp.dataSource.port | default "5432" }})
					{{ else }}
					rt=$(nc -z -w 1 {{ .Values.EcosIdentityApp.dataSource.host | default "ecos-microservices-postgresql-app-service" }} {{ .Values.EcosIdentityApp.dataSource.port | default "5432" }})
					{{- end }}
					if [ $? -eq 0 ]; then
					echo "DB is UP"
					break
					fi
					echo "DB is not yet reachable, sleep for 10s before retry"
					sleep 10
				done
				image: {{ .Values.global.initContainers.image.registry }}/{{ .Values.global.initContainers.image.repository }}:{{ .Values.global.initContainers.image.tag }}
				imagePullPolicy: Always
				name: init-db
				resources:
				limits:
					cpu: 100m
					memory: 128Mi
				requests:
					cpu: 100m
					memory: 128Mi
			{{- if .Values.EcosIdentityApp.ecosExtensions.enabled }}
			- image: {{ .Values.global.initContainers.image.registry }}/ecos-keycloak-ext:{{ .Values.EcosIdentityApp.ecosExtensions.version }}
				imagePullPolicy: Always
				name: init-extensions
				env:
				- name: KK_EXT_TARGET_ROOT
					value: /run/extensions-target
				resources:
				limits:
					cpu: 100m
					memory: 128Mi
				requests:
					cpu: 100m
					memory: 128Mi
				volumeMounts:
				- mountPath: /run/extensions-target
					name: ecos-extensions
			{{- end }}
			dnsPolicy: ClusterFirst
			{{- if .Values.EcosIdentityApp.image.pullSecrets }}
			imagePullSecrets:
			- name: {{ .Values.EcosIdentityApp.image.pullSecrets }}
			{{- end }}
			securityContext:
				fsGroup: 1000
			restartPolicy: Always
			terminationGracePeriodSeconds: 120
			volumes:
			{{- if .Values.EcosIdentityApp.import.certs.enabled }}
			- name: certs
				configMap:
				defaultMode: 365
				name: {{ .Values.EcosIdentityApp.import.certs.configMap }}
			{{- end }}
			{{- if .Values.EcosIdentityApp.KerberosIntegration.enabled }}
			- name: krb5-conf
				configMap:
				defaultMode: 365
				name: ecos-identity-app-configmap
				items:
					- key: krb5.conf
					path: krb5.conf
			- name: keytab
				secret:
				secretName: ecos-secret
				items:
					- key: keytab-file
					path: keytab-file
			{{- end }}
			- name: sh
				configMap:
				defaultMode: 365
				name: ecos-identity-app-configmap
				items:
					- key: keycloak.sh
					path: keycloak.sh
			- name: startup
				configMap:
				defaultMode: 365
				name: ecos-identity-app-configmap
				items:
					- key: keycloak.cli
					path: keycloak.cli
			- name: realm-export
				configMap:
				defaultMode: 365
				name: ecos-identity-app-configmap
				items:
					- key: realm-export.json
					path: realm-export.json
		{{- if .Values.EcosIdentityApp.ecosExtensions.enabled }}
			- name: ecos-extensions
				emptyDir: {}
		{{- end }}
		{{- end }}

Используемые переменные:
-------------------------

*	**KEYCLOAK_FRONTEND_URL** -  https://example.ecos24.ru url кейклока, где добавлен realm
*	**KEYCLOAK_IMPORT** - стандартное значение /import/realm-export.json успользует для того, чтоб вместе с ecos стартанул Keycloak, в котором уже будет необходимы Realm
*	**HOSTNAME** - переменная задающая имя сервиса
*	**KEYCLOAK_LOGLEVEL** - переменная задающая loglevel Keycloak
*	**KEYCLOAK_USER** - admin user для входа в https://example.ecos24.ru/auth
*	**KEYCLOAK_PASSWORD** - пароль для dmin user для входа в https://example.ecos24.ru/auth
*	**JAVA_TOOL_OPTIONS** - параметры Java
*	**DB_VENDOR** -  вендор БД
*	**DB_ADDR** - имя сервиса БД
*	**DB_PORT** -  порт , по которому доступна база данных
*	**DB_DATABASE** - имя БД
*	**DB_USER** - пользователь БД
*	**DB_PASSWORD** - пароль для входа в БД
*	**JGROUPS_DISCOVERY_PROTOCOL** - протокол, для возможности работы Keycloak в режиме HA с 2 репликами
*	**JGROUPS_DISCOVERY_PROPERTIES** - имя сервиса, для общения 2х реплик Keycloak при развертывании в режиме HA
*	**CACHE_OWNERS_COUNT** - количество owner при режиме HA
*	**CACHE_OWNERS_AUTH_SESSIONS_COUNT** - количество активных сеансов для владельца кеша ( установить в соответсвии с CACHE_OWNERS_COUNT )
*	**ECOS_KK_RMQ_HOST** - хост для подключения к RabbitMQ
*	**ECOS_KK_RMQ_USERNAME** -  имя пользователя для подключения к RabbitMQ
*	**ECOS_KK_RMQ_PASSWORD** - пароль пользователя для подключения к RabbitMQ
*	**ECOS_KK_ZK_HOST** - хост  zookeeper

Известные проблемы:
--------------------
 

Дополнительно:
----------------

Keycloak подключается к сервису с БД ecos-app-microservice-postgresql и используются  в собственную базу данных  

Типовой вывод успешного развертывания в лог контейнера:
--------------------------------------------------------

.. code-block::

	Picked up JAVA_TOOL_OPTIONS: -XX:+UseContainerSupport -XX:MaxRAMPercentage=50.0
	Added 'admin' to '/opt/jboss/keycloak/standalone/configuration/keycloak-add-user.json', restart server to load user
	=========================================================================
	Using PostgreSQL database
	=========================================================================
	Picked up JAVA_TOOL_OPTIONS: -XX:+UseContainerSupport -XX:MaxRAMPercentage=50.0
	21:08:34,603 INFO  [org.jboss.modules] (CLI command executor) JBoss Modules version 1.10.2.Final
	21:08:35,001 INFO  [org.jboss.msc] (CLI command executor) JBoss MSC version 1.4.12.Final
	21:08:35,011 INFO  [org.jboss.threads] (CLI command executor) JBoss Threads version 2.4.0.Final
	21:08:35,897 INFO  [org.jboss.as] (MSC service thread 1-2) WFLYSRV0049: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) starting
	21:08:36,404 INFO  [org.jboss.vfs] (MSC service thread 1-1) VFS000002: Failed to clean existing content for temp file provider of type temp. Enable DEBUG level log to find what caused this
	21:08:42,002 INFO  [org.wildfly.security] (ServerService Thread Pool -- 17) ELY00001: WildFly Elytron version 1.13.1.Final
	21:08:46,614 INFO  [org.jboss.as.controller.management-deprecated] (Controller Boot Thread) WFLYCTL0028: Attribute 'security-realm' in the resource at address '/core-service=management/management-interface=http-interface' is deprecated, and may be removed in a future version. See the attribute description in the output of the read-resource-description operation to learn more about the deprecation.
	21:08:47,214 INFO  [org.jboss.as.controller.management-deprecated] (Controller Boot Thread) WFLYCTL0028: Attribute 'security-realm' in the resource at address '/subsystem=undertow/server=default-server/https-listener=https' is deprecated, and may be removed in a future version. See the attribute description in the output of the read-resource-description operation to learn more about the deprecation.
	21:08:48,302 INFO  [org.jboss.as.patching] (MSC service thread 1-1) WFLYPAT0050: Keycloak cumulative patch ID is: base, one-off patches include: none
	21:08:48,915 INFO  [org.jboss.as.server] (Controller Boot Thread) WFLYSRV0212: Resuming server
	21:08:48,917 INFO  [org.jboss.as] (Controller Boot Thread) WFLYSRV0025: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) started in 14219ms - Started 56 of 79 services (32 services are lazy, passive or on-demand)
	The batch executed successfully
	21:08:50,099 INFO  [org.jboss.as] (MSC service thread 1-1) WFLYSRV0050: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) stopped in 186ms
	Picked up JAVA_TOOL_OPTIONS: -XX:+UseContainerSupport -XX:MaxRAMPercentage=50.0
	21:08:58,406 INFO  [org.jboss.modules] (CLI command executor) JBoss Modules version 1.10.2.Final
	21:08:58,810 INFO  [org.jboss.msc] (CLI command executor) JBoss MSC version 1.4.12.Final
	21:08:58,820 INFO  [org.jboss.threads] (CLI command executor) JBoss Threads version 2.4.0.Final
	21:08:59,514 INFO  [org.jboss.as] (MSC service thread 1-2) WFLYSRV0049: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) starting
	21:09:00,210 INFO  [org.jboss.vfs] (MSC service thread 1-2) VFS000002: Failed to clean existing content for temp file provider of type temp. Enable DEBUG level log to find what caused this
	21:09:07,226 INFO  [org.wildfly.security] (ServerService Thread Pool -- 21) ELY00001: WildFly Elytron version 1.13.1.Final
	21:09:13,710 INFO  [org.jboss.as.controller.management-deprecated] (Controller Boot Thread) WFLYCTL0028: Attribute 'security-realm' in the resource at address '/core-service=management/management-interface=http-interface' is deprecated, and may be removed in a future version. See the attribute description in the output of the read-resource-description operation to learn more about the deprecation.
	21:09:14,500 INFO  [org.jboss.as.controller.management-deprecated] (Controller Boot Thread) WFLYCTL0028: Attribute 'security-realm' in the resource at address '/subsystem=undertow/server=default-server/https-listener=https' is deprecated, and may be removed in a future version. See the attribute description in the output of the read-resource-description operation to learn more about the deprecation.
	21:09:15,735 INFO  [org.jboss.as.patching] (MSC service thread 1-1) WFLYPAT0050: Keycloak cumulative patch ID is: base, one-off patches include: none
	21:09:16,618 INFO  [org.jboss.as.server] (Controller Boot Thread) WFLYSRV0212: Resuming server
	21:09:16,624 INFO  [org.jboss.as] (Controller Boot Thread) WFLYSRV0025: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) started in 18211ms - Started 56 of 86 services (39 services are lazy, passive or on-demand)
	The batch executed successfully
	21:09:17,745 INFO  [org.jboss.as] (MSC service thread 1-2) WFLYSRV0050: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) stopped in 129ms
	Executing cli script: /opt/jboss/startup-scripts/keycloak.cli
	Picked up JAVA_TOOL_OPTIONS: -XX:+UseContainerSupport -XX:MaxRAMPercentage=50.0
	21:09:26,817 INFO  [org.jboss.modules] (CLI command executor) JBoss Modules version 1.10.2.Final
	21:09:27,218 INFO  [org.jboss.msc] (CLI command executor) JBoss MSC version 1.4.12.Final
	21:09:27,241 INFO  [org.jboss.threads] (CLI command executor) JBoss Threads version 2.4.0.Final
	21:09:28,008 INFO  [org.jboss.as] (MSC service thread 1-1) WFLYSRV0049: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) starting
	21:09:28,627 INFO  [org.jboss.vfs] (MSC service thread 1-2) VFS000002: Failed to clean existing content for temp file provider of type temp. Enable DEBUG level log to find what caused this
	21:09:34,848 INFO  [org.wildfly.security] (ServerService Thread Pool -- 22) ELY00001: WildFly Elytron version 1.13.1.Final
	21:09:41,713 INFO  [org.jboss.as.controller.management-deprecated] (Controller Boot Thread) WFLYCTL0028: Attribute 'security-realm' in the resource at address '/core-service=management/management-interface=http-interface' is deprecated, and may be removed in a future version. See the attribute description in the output of the read-resource-description operation to learn more about the deprecation.
	21:09:42,454 INFO  [org.jboss.as.controller.management-deprecated] (Controller Boot Thread) WFLYCTL0028: Attribute 'security-realm' in the resource at address '/subsystem=undertow/server=default-server/https-listener=https' is deprecated, and may be removed in a future version. See the attribute description in the output of the read-resource-description operation to learn more about the deprecation.
	21:09:43,734 INFO  [org.jboss.as.patching] (MSC service thread 1-1) WFLYPAT0050: Keycloak cumulative patch ID is: base, one-off patches include: none
	21:09:44,615 INFO  [org.jboss.as.server] (Controller Boot Thread) WFLYSRV0212: Resuming server
	21:09:44,617 INFO  [org.jboss.as] (Controller Boot Thread) WFLYSRV0025: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) started in 17788ms - Started 56 of 86 services (39 services are lazy, passive or on-demand)
	Configuring node identifier
	Finished configuring node identifier
	The batch executed successfully
	21:09:45,770 INFO  [org.jboss.as] (MSC service thread 1-2) WFLYSRV0050: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) stopped in 148ms
	=========================================================================
	JBoss Bootstrap Environment
	JBOSS_HOME: /opt/jboss/keycloak
	JAVA: java
	JAVA_OPTS:  -server -Xms64m -Xmx512m -XX:MetaspaceSize=96M -XX:MaxMetaspaceSize=256m -Djava.net.preferIPv4Stack=true -Djboss.modules.system.pkgs=org.jboss.byteman -Djava.awt.headless=true   --add-exports=java.base/sun.nio.ch=ALL-UNNAMED --add-exports=jdk.unsupported/sun.misc=ALL-UNNAMED --add-exports=jdk.unsupported/sun.reflect=ALL-UNNAMED
	=========================================================================
	Picked up JAVA_TOOL_OPTIONS: -XX:+UseContainerSupport -XX:MaxRAMPercentage=50.0
	21:09:50,000 INFO  [org.jboss.modules] (main) JBoss Modules version 1.10.2.Final
	21:09:54,026 INFO  [org.jboss.msc] (main) JBoss MSC version 1.4.12.Final
	21:09:54,156 INFO  [org.jboss.threads] (main) JBoss Threads version 2.4.0.Final
	21:09:55,106 INFO  [org.jboss.as] (MSC service thread 1-2) WFLYSRV0049: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) starting
	21:09:55,703 INFO  [org.jboss.vfs] (MSC service thread 1-1) VFS000002: Failed to clean existing content for temp file provider of type temp. Enable DEBUG level log to find what caused this
	21:10:01,709 INFO  [org.wildfly.security] (ServerService Thread Pool -- 19) ELY00001: WildFly Elytron version 1.13.1.Final
	21:10:06,431 INFO  [org.jboss.as.controller.management-deprecated] (Controller Boot Thread) WFLYCTL0028: Attribute 'security-realm' in the resource at address '/core-service=management/management-interface=http-interface' is deprecated, and may be removed in a future version. See the attribute description in the output of the read-resource-description operation to learn more about the deprecation.
	21:10:06,846 INFO  [org.jboss.as.controller.management-deprecated] (ServerService Thread Pool -- 12) WFLYCTL0028: Attribute 'security-realm' in the resource at address '/subsystem=undertow/server=default-server/https-listener=https' is deprecated, and may be removed in a future version. See the attribute description in the output of the read-resource-description operation to learn more about the deprecation.
	21:10:07,716 INFO  [org.jboss.as.server] (Controller Boot Thread) WFLYSRV0039: Creating http management service using socket-binding (management-http)
	21:10:07,835 INFO  [org.xnio] (MSC service thread 1-2) XNIO version 3.8.2.Final
	21:10:07,935 INFO  [org.xnio.nio] (MSC service thread 1-2) XNIO NIO Implementation Version 3.8.2.Final
	21:10:08,219 INFO  [org.jboss.remoting] (MSC service thread 1-1) JBoss Remoting version 5.0.19.Final
	21:10:08,298 INFO  [org.wildfly.extension.microprofile.config.smallrye._private] (ServerService Thread Pool -- 45) WFLYCONF0001: Activating WildFly MicroProfile Config Subsystem
	21:10:08,568 INFO  [org.jboss.as.security] (ServerService Thread Pool -- 51) WFLYSEC0002: Activating Security Subsystem
	21:10:08,648 INFO  [org.jboss.as.naming] (ServerService Thread Pool -- 48) WFLYNAM0001: Activating Naming Subsystem
	21:10:08,696 INFO  [org.wildfly.extension.microprofile.health.smallrye] (ServerService Thread Pool -- 46) WFLYHEALTH0001: Activating Eclipse MicroProfile Health Subsystem21:10:08,843 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 37) WFLYCLINF0001: Activating Infinispan subsystem.
	21:10:09,025 INFO  [org.jboss.as.connector.subsystems.datasources] (ServerService Thread Pool -- 32) WFLYJCA0004: Deploying JDBC-compliant driver class org.h2.Driver (version 1.4)
	21:10:09,101 INFO  [org.wildfly.extension.io] (ServerService Thread Pool -- 38) WFLYIO001: Worker 'default' has auto-configured to 2 IO threads with 16 max task threads based on your 1 available processors
	21:10:09,417 INFO  [org.wildfly.extension.microprofile.metrics.smallrye] (ServerService Thread Pool -- 47) WFLYMETRICS0001: Activating Eclipse MicroProfile Metrics Subsystem
	21:10:09,434 INFO  [org.jboss.as.jaxrs] (ServerService Thread Pool -- 39) WFLYRS0016: RESTEasy version 3.13.2.Final
	21:10:09,333 INFO  [org.jboss.as.security] (MSC service thread 1-1) WFLYSEC0001: Current PicketBox version=5.0.3.Final-redhat-00006
	21:10:09,898 INFO  [org.jboss.as.connector.subsystems.datasources] (ServerService Thread Pool -- 32) WFLYJCA0005: Deploying non-JDBC-compliant driver class org.postgresql.Driver (version 42.2)
	21:10:10,122 INFO  [org.wildfly.extension.undertow] (MSC service thread 1-2) WFLYUT0003: Undertow 2.2.2.Final starting
	21:10:11,115 INFO  [org.wildfly.extension.undertow] (ServerService Thread Pool -- 54) WFLYUT0014: Creating file handler for path '/opt/jboss/keycloak/welcome-content' with options [directory-listing: 'false', follow-symlink: 'false', case-sensitive: 'true', safe-symlink-paths: '[]']
	21:10:11,315 INFO  [org.jboss.as.connector] (MSC service thread 1-2) WFLYJCA0009: Starting JCA Subsystem (WildFly/IronJacamar 1.4.23.Final)
	21:10:12,701 INFO  [org.jboss.as.naming] (MSC service thread 1-2) WFLYNAM0003: Starting Naming Service
	21:10:13,232 INFO  [org.jboss.as.connector.deployers.jdbc] (MSC service thread 1-1) WFLYJCA0018: Started Driver service with driver-name = h2
	21:10:13,235 INFO  [org.jboss.as.connector.deployers.jdbc] (MSC service thread 1-2) WFLYJCA0018: Started Driver service with driver-name = postgresql
	21:10:13,238 INFO  [org.jboss.as.ejb3] (MSC service thread 1-2) WFLYEJB0482: Strict pool mdb-strict-max-pool is using a max instance size of 4 (per class), which is derived from the number of CPUs on this host.
	21:10:13,303 INFO  [org.jboss.as.ejb3] (MSC service thread 1-2) WFLYEJB0481: Strict pool slsb-strict-max-pool is using a max instance size of 16 (per class), which is derived from thread worker pool sizing.
	21:10:13,412 INFO  [org.jboss.as.mail.extension] (MSC service thread 1-1) WFLYMAIL0001: Bound mail session [java:jboss/mail/Default]
	21:10:14,720 INFO  [org.wildfly.extension.undertow] (MSC service thread 1-1) WFLYUT0012: Started server default-server.
	21:10:14,825 INFO  [org.jboss.as.patching] (MSC service thread 1-1) WFLYPAT0050: Keycloak cumulative patch ID is: base, one-off patches include: none
	21:10:15,000 INFO  [org.wildfly.extension.undertow] (MSC service thread 1-1) WFLYUT0018: Host default-host starting
	21:10:15,202 INFO  [org.jboss.as.server.deployment.scanner] (MSC service thread 1-1) WFLYDS0013: Started FileSystemDeploymentService for directory /opt/jboss/keycloak/standalone/deployments
	21:10:15,225 INFO  [org.jboss.as.server.deployment] (MSC service thread 1-1) WFLYSRV0027: Starting deployment of "keycloak-server.war" (runtime-name: "keycloak-server.war")
	21:10:15,415 INFO  [org.wildfly.extension.undertow] (MSC service thread 1-2) WFLYUT0006: Undertow HTTP listener default listening on 0.0.0.0:8080
	21:10:15,804 INFO  [org.jboss.as.ejb3] (MSC service thread 1-2) WFLYEJB0493: EJB subsystem suspension complete
	21:10:16,703 INFO  [org.wildfly.extension.undertow] (MSC service thread 1-2) WFLYUT0006: Undertow HTTPS listener https listening on 0.0.0.0:8443
	21:10:17,815 INFO  [org.jboss.as.connector.subsystems.datasources] (MSC service thread 1-2) WFLYJCA0001: Bound data source [java:jboss/datasources/ExampleDS]
	21:10:17,816 INFO  [org.jboss.as.connector.subsystems.datasources] (MSC service thread 1-2) WFLYJCA0001: Bound data source [java:jboss/datasources/KeycloakDS]
	21:10:22,815 INFO  [org.infinispan.CONTAINER] (ServerService Thread Pool -- 57) ISPN000128: Infinispan version: Infinispan 'Corona Extra' 11.0.4.Final
	21:10:23,327 INFO  [org.infinispan.CONFIG] (MSC service thread 1-1) ISPN000152: Passivation configured without an eviction policy being selected. Only manually evicted entities will be passivated.
	21:10:23,346 INFO  [org.infinispan.CONFIG] (MSC service thread 1-1) ISPN000152: Passivation configured without an eviction policy being selected. Only manually evicted entities will be passivated.
	21:10:23,804 INFO  [org.infinispan.PERSISTENCE] (ServerService Thread Pool -- 58) ISPN000556: Starting user marshaller 'org.wildfly.clustering.infinispan.marshalling.jboss.JBossMarshaller'
	21:10:23,814 INFO  [org.infinispan.PERSISTENCE] (ServerService Thread Pool -- 57) ISPN000556: Starting user marshaller 'org.wildfly.clustering.infinispan.spi.marshalling.InfinispanProtoStreamMarshaller'
	21:10:25,221 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 57) WFLYCLINF0002: Started http-remoting-connector cache from ejb container
	21:10:25,417 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 57) WFLYCLINF0002: Started offlineClientSessions cache from keycloak container
	21:10:25,599 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 57) WFLYCLINF0002: Started actionTokens cache from keycloak container
	21:10:25,414 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 58) WFLYCLINF0002: Started offlineSessions cache from keycloak container
	21:10:25,616 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 61) WFLYCLINF0002: Started sessions cache from keycloak container
	21:10:25,826 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 63) WFLYCLINF0002: Started keys cache from keycloak container
	21:10:25,799 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 64) WFLYCLINF0002: Started clientSessions cache from keycloak container
	21:10:25,809 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 65) WFLYCLINF0002: Started loginFailures cache from keycloak container
	21:10:25,816 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 66) WFLYCLINF0002: Started authenticationSessions cache from keycloak container
	21:10:25,907 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 57) WFLYCLINF0002: Started users cache from keycloak container
	21:10:25,908 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 62) WFLYCLINF0002: Started authorization cache from keycloak container
	21:10:25,915 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 59) WFLYCLINF0002: Started realms cache from keycloak container
	21:10:25,918 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 60) WFLYCLINF0002: Started work cache from keycloak container
	21:10:30,634 INFO  [org.keycloak.services] (ServerService Thread Pool -- 67) KC-SERVICES0001: Loading config from standalone.xml or domain.xml
	21:10:33,334 INFO  [org.keycloak.url.DefaultHostnameProviderFactory] (ServerService Thread Pool -- 67) Frontend: https://enterprise.ecos24.ru/auth, Admin: <frontend>, Backend: <request>
	21:10:33,938 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 67) WFLYCLINF0002: Started realmRevisions cache from keycloak container
	21:10:34,019 INFO  [org.jboss.as.clustering.infinispan] (ServerService Thread Pool -- 67) WFLYCLINF0002: Started authorizationRevisions cache from keycloak container
	21:10:34,021 INFO  [org.keycloak.connections.infinispan.DefaultInfinispanConnectionProviderFactory] (ServerService Thread Pool -- 67) Node name: ecos-identity-app, Site name: null
	21:10:36,606 INFO  [org.keycloak.connections.jpa.DefaultJpaConnectionProviderFactory] (ServerService Thread Pool -- 67) Database info: {databaseUrl=jdbc:postgresql://ecos-microservices-postgresql-app-service.enterprise-ecos24.svc.cluster.local:5432/ecos_identity, databaseUser=eis, databaseProduct=PostgreSQL 12.7, databaseDriver=PostgreSQL JDBC Driver 42.2.5}
	21:10:48,599 INFO  [org.hibernate.jpa.internal.util.LogHelper] (ServerService Thread Pool -- 67) HHH000204: Processing PersistenceUnitInfo [
		name: keycloak-default
		...]
	21:10:48,912 INFO  [org.hibernate.Version] (ServerService Thread Pool -- 67) HHH000412: Hibernate Core {5.3.20.Final}
	21:10:48,915 INFO  [org.hibernate.cfg.Environment] (ServerService Thread Pool -- 67) HHH000206: hibernate.properties not found
	21:10:49,723 INFO  [org.hibernate.annotations.common.Version] (ServerService Thread Pool -- 67) HCANN000001: Hibernate Commons Annotations {5.0.5.Final}
	21:10:50,729 INFO  [org.hibernate.dialect.Dialect] (ServerService Thread Pool -- 67) HHH000400: Using dialect: org.hibernate.dialect.PostgreSQL95Dialect
	21:10:51,809 INFO  [org.hibernate.engine.jdbc.env.internal.LobCreatorBuilderImpl] (ServerService Thread Pool -- 67) HHH000424: Disabling contextual LOB creation as createClob() method threw error : java.lang.reflect.InvocationTargetException
	21:10:51,815 INFO  [org.hibernate.type.BasicTypeRegistry] (ServerService Thread Pool -- 67) HHH000270: Type registration [java.util.UUID] overrides previous : org.hibernate.type.UUIDBinaryType@429b0d6e
	21:10:51,822 INFO  [org.hibernate.envers.boot.internal.EnversServiceImpl] (ServerService Thread Pool -- 67) Envers integration enabled? : true
	21:10:54,716 INFO  [org.hibernate.orm.beans] (ServerService Thread Pool -- 67) HHH10005002: No explicit CDI BeanManager reference was passed to Hibernate, but CDI is available on the Hibernate ClassLoader.
	21:10:55,207 INFO  [org.hibernate.validator.internal.util.Version] (ServerService Thread Pool -- 67) HV000001: Hibernate Validator 6.0.21.Final
	21:11:03,531 INFO  [org.hibernate.hql.internal.QueryTranslatorFactoryInitiator] (ServerService Thread Pool -- 67) HHH000397: Using ASTQueryTranslatorFactory
	21:11:11,215 INFO  [org.keycloak.services] (ServerService Thread Pool -- 67) KC-SERVICES0003: Not importing realm ecos-app from file /import/realm-export.json.  It already exists.
	21:11:11,308 INFO  [org.keycloak.services] (ServerService Thread Pool -- 67) KC-SERVICES0003: Not importing realm ecos-app from file /import/realm-export.json.  It already exists.
	21:11:11,399 INFO  [org.keycloak.services] (ServerService Thread Pool -- 67) KC-SERVICES0006: Importing users from '/opt/jboss/keycloak/standalone/configuration/keycloak-add-user.json'
	21:11:12,001 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002225: Deploying javax.ws.rs.core.Application: class org.keycloak.services.resources.KeycloakApplication
	21:11:12,003 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002205: Adding provider class org.keycloak.services.filters.KeycloakSecurityHeadersFilter from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,005 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002200: Adding class resource org.keycloak.services.resources.JsResource from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,005 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002205: Adding provider class org.keycloak.services.error.KeycloakErrorHandler from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,006 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002200: Adding class resource org.keycloak.services.resources.ThemeResource from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,006 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002210: Adding provider singleton org.keycloak.services.util.ObjectMapperResolver from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,006 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002220: Adding singleton resource org.keycloak.services.resources.admin.AdminRoot from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,006 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002220: Adding singleton resource org.keycloak.services.resources.WelcomeResource from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,006 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002220: Adding singleton resource org.keycloak.services.resources.RealmsResource from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,006 INFO  [org.jboss.resteasy.resteasy_jaxrs.i18n] (ServerService Thread Pool -- 67) RESTEASY002220: Adding singleton resource org.keycloak.services.resources.RobotsResource from Application class org.keycloak.services.resources.KeycloakApplication
	21:11:12,498 INFO  [org.wildfly.extension.undertow] (ServerService Thread Pool -- 67) WFLYUT0021: Registered web context: '/auth' for server 'default-server'
	21:11:13,200 INFO  [org.jboss.as.server] (ServerService Thread Pool -- 43) WFLYSRV0010: Deployed "keycloak-server.war" (runtime-name : "keycloak-server.war")
	21:11:13,508 INFO  [org.jboss.as.server] (Controller Boot Thread) WFLYSRV0212: Resuming server
	21:11:13,511 INFO  [org.jboss.as] (Controller Boot Thread) WFLYSRV0025: Keycloak 12.0.4 (WildFly Core 13.0.3.Final) started in 86028ms - Started 590 of 868 services (585 services are lazy, passive or on-demand)
	21:11:13,513 INFO  [org.jboss.as] (Controller Boot Thread) WFLYSRV0060: Http management interface listening on http://127.0.0.1:9990/management
	21:11:13,513 INFO  [org.jboss.as] (Controller Boot Thread) WFLYSRV0051: Admin console listening on http://127.0.0.1:9990