# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor diagnostic-settings create",
)
class Create(AAZCommand):
    """Create diagnostic settings for the specified resource. For more information, visit: https://learn.microsoft.com/rest/api/monitor/diagnosticsettings/createorupdate#metricsettings.

    :example: Create diagnostic settings, retention here only applies when the target is a storage account.
        az monitor diagnostic-settings create --resource {ID} -n {name} --storage-account {storageAccount} --logs "[{category:WorkflowRuntime,enabled:true,retention-policy:{enabled:false,days:0}}]" --metrics "[{category:WorkflowRuntime,enabled:true,retention-policy:{enabled:false,days:0}}]"
    """

    _aaz_info = {
        "version": "2021-05-01-preview",
        "resources": [
            ["mgmt-plane", "/{resourceuri}/providers/microsoft.insights/diagnosticsettings/{}", "2021-05-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the diagnostic setting. Required.",
            required=True,
        )
        _args_schema.event_hub_rule = AAZStrArg(
            options=["--event-hub-rule"],
            help="Name or ID of the event hub authorization rule.",
        )
        _args_schema.event_hub = AAZStrArg(
            options=["--event-hub"],
            help="Name or ID an event hub. If none is specified, the default event hub will be selected.",
        )
        _args_schema.log_analytics_destination_type = AAZStrArg(
            options=["--log-analytics-destination-type"],
            help="A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type constructed as follows: `<normalized service identity>_<normalized category name>`. Possible values are: Dedicated and null (null is default.)",
        )
        _args_schema.logs = AAZListArg(
            options=["--logs"],
            help="JSON encoded list of logs settings. Use '@{file}' to load from a file.For more information, visit: https://learn.microsoft.com/rest/api/monitor/diagnosticsettings/createorupdate#logsettings.",
        )
        _args_schema.marketplace_partner_id = AAZStrArg(
            options=["--marketplace-partner-id"],
            help="The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs.",
        )
        _args_schema.metrics = AAZListArg(
            options=["--metrics"],
            help="The list of metric settings.",
        )
        _args_schema.service_bus_rule_id = AAZStrArg(
            options=["--service-bus-rule-id"],
            help="The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.",
        )
        _args_schema.storage_account = AAZStrArg(
            options=["--storage-account"],
            help="Name or ID of the storage account to send diagnostic logs to.",
        )
        _args_schema.workspace = AAZStrArg(
            options=["--workspace"],
            help="Name or ID of the Log Analytics workspace to send diagnostic logs to.",
        )

        logs = cls._args_schema.logs
        logs.Element = AAZObjectArg()

        _element = cls._args_schema.logs.Element
        _element.category = AAZStrArg(
            options=["category"],
            help="Name of a Diagnostic Log category for a resource type this setting is applied to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET diagnostic settings operation.",
        )
        _element.category_group = AAZStrArg(
            options=["category-group"],
            help="Name of a Diagnostic Log category group for a resource type this setting is applied to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET diagnostic settings operation.",
        )
        _element.enabled = AAZBoolArg(
            options=["enabled"],
            help="a value indicating whether this log is enabled.",
            required=True,
        )
        _element.retention_policy = AAZObjectArg(
            options=["retention-policy"],
            help="the retention policy for this log.",
        )
        cls._build_args_retention_policy_create(_element.retention_policy)

        metrics = cls._args_schema.metrics
        metrics.Element = AAZObjectArg()

        _element = cls._args_schema.metrics.Element
        _element.category = AAZStrArg(
            options=["category"],
            help="Name of a Diagnostic Metric category for a resource type this setting is applied to. To obtain the list of Diagnostic metric categories for a resource, first perform a GET diagnostic settings operation.",
        )
        _element.enabled = AAZBoolArg(
            options=["enabled"],
            help="a value indicating whether this category is enabled.",
            required=True,
        )
        _element.retention_policy = AAZObjectArg(
            options=["retention-policy"],
            help="the retention policy for this category.",
        )
        cls._build_args_retention_policy_create(_element.retention_policy)
        _element.time_grain = AAZDurationArg(
            options=["time-grain"],
            help="the timegrain of the metric in ISO8601 format.",
        )

        # define Arg Group "Target Resource"

        _args_schema = cls._args_schema
        _args_schema.resource = AAZStrArg(
            options=["--resource"],
            arg_group="Target Resource",
            help="Name or ID of the target resource.",
            required=True,
        )
        return cls._args_schema

    _args_retention_policy_create = None

    @classmethod
    def _build_args_retention_policy_create(cls, _schema):
        if cls._args_retention_policy_create is not None:
            _schema.days = cls._args_retention_policy_create.days
            _schema.enabled = cls._args_retention_policy_create.enabled
            return

        cls._args_retention_policy_create = AAZObjectArg()

        retention_policy_create = cls._args_retention_policy_create
        retention_policy_create.days = AAZIntArg(
            options=["days"],
            help="the number of days for the retention in days. A value of 0 will retain the events indefinitely.",
            required=True,
            fmt=AAZIntArgFormat(
                minimum=0,
            ),
        )
        retention_policy_create.enabled = AAZBoolArg(
            options=["enabled"],
            help="a value indicating whether the retention policy is enabled.",
            required=True,
        )

        _schema.days = cls._args_retention_policy_create.days
        _schema.enabled = cls._args_retention_policy_create.enabled

    def _execute_operations(self):
        self.pre_operations()
        self.DiagnosticSettingsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DiagnosticSettingsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/{resourceUri}/providers/Microsoft.Insights/diagnosticSettings/{name}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "name", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceUri", self.ctx.args.resource,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-05-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("eventHubAuthorizationRuleId", AAZStrType, ".event_hub_rule")
                properties.set_prop("eventHubName", AAZStrType, ".event_hub")
                properties.set_prop("logAnalyticsDestinationType", AAZStrType, ".log_analytics_destination_type")
                properties.set_prop("logs", AAZListType, ".logs")
                properties.set_prop("marketplacePartnerId", AAZStrType, ".marketplace_partner_id")
                properties.set_prop("metrics", AAZListType, ".metrics")
                properties.set_prop("serviceBusRuleId", AAZStrType, ".service_bus_rule_id")
                properties.set_prop("storageAccountId", AAZStrType, ".storage_account")
                properties.set_prop("workspaceId", AAZStrType, ".workspace")

            logs = _builder.get(".properties.logs")
            if logs is not None:
                logs.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.logs[]")
            if _elements is not None:
                _elements.set_prop("category", AAZStrType, ".category")
                _elements.set_prop("categoryGroup", AAZStrType, ".category_group")
                _elements.set_prop("enabled", AAZBoolType, ".enabled", typ_kwargs={"flags": {"required": True}})
                _build_schema_retention_policy_create(_elements.set_prop("retentionPolicy", AAZObjectType, ".retention_policy"))

            metrics = _builder.get(".properties.metrics")
            if metrics is not None:
                metrics.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.metrics[]")
            if _elements is not None:
                _elements.set_prop("category", AAZStrType, ".category")
                _elements.set_prop("enabled", AAZBoolType, ".enabled", typ_kwargs={"flags": {"required": True}})
                _build_schema_retention_policy_create(_elements.set_prop("retentionPolicy", AAZObjectType, ".retention_policy"))
                _elements.set_prop("timeGrain", AAZStrType, ".time_grain")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.event_hub_authorization_rule_id = AAZStrType(
                serialized_name="eventHubAuthorizationRuleId",
            )
            properties.event_hub_name = AAZStrType(
                serialized_name="eventHubName",
            )
            properties.log_analytics_destination_type = AAZStrType(
                serialized_name="logAnalyticsDestinationType",
            )
            properties.logs = AAZListType()
            properties.marketplace_partner_id = AAZStrType(
                serialized_name="marketplacePartnerId",
            )
            properties.metrics = AAZListType()
            properties.service_bus_rule_id = AAZStrType(
                serialized_name="serviceBusRuleId",
            )
            properties.storage_account_id = AAZStrType(
                serialized_name="storageAccountId",
            )
            properties.workspace_id = AAZStrType(
                serialized_name="workspaceId",
            )

            logs = cls._schema_on_200.properties.logs
            logs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.logs.Element
            _element.category = AAZStrType()
            _element.category_group = AAZStrType(
                serialized_name="categoryGroup",
            )
            _element.enabled = AAZBoolType(
                flags={"required": True},
            )
            _element.retention_policy = AAZObjectType(
                serialized_name="retentionPolicy",
            )
            _build_schema_retention_policy_read(_element.retention_policy)

            metrics = cls._schema_on_200.properties.metrics
            metrics.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.metrics.Element
            _element.category = AAZStrType()
            _element.enabled = AAZBoolType(
                flags={"required": True},
            )
            _element.retention_policy = AAZObjectType(
                serialized_name="retentionPolicy",
            )
            _build_schema_retention_policy_read(_element.retention_policy)
            _element.time_grain = AAZStrType(
                serialized_name="timeGrain",
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


def _build_schema_retention_policy_create(_builder):
    if _builder is None:
        return
    _builder.set_prop("days", AAZIntType, ".days", typ_kwargs={"flags": {"required": True}})
    _builder.set_prop("enabled", AAZBoolType, ".enabled", typ_kwargs={"flags": {"required": True}})


_schema_retention_policy_read = None


def _build_schema_retention_policy_read(_schema):
    global _schema_retention_policy_read
    if _schema_retention_policy_read is not None:
        _schema.days = _schema_retention_policy_read.days
        _schema.enabled = _schema_retention_policy_read.enabled
        return

    _schema_retention_policy_read = AAZObjectType()

    retention_policy_read = _schema_retention_policy_read
    retention_policy_read.days = AAZIntType(
        flags={"required": True},
    )
    retention_policy_read.enabled = AAZBoolType(
        flags={"required": True},
    )

    _schema.days = _schema_retention_policy_read.days
    _schema.enabled = _schema_retention_policy_read.enabled


__all__ = ["Create"]
