# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import tempfile
from typing import Any, TypeVar

from azure.cli.core import AzCommandsLoader
from azure.cli.core._config import ENV_VAR_PREFIX
from azure.cli.core.cloud import get_active_cloud
from azure.cli.core.commands import AzCliCommand
from knack import CLI

MOCK_CLI_CONFIG_DIR = tempfile.mkdtemp()
MOCK_CLI_ENV_VAR_PREFIX = "MOCK_" + ENV_VAR_PREFIX

# type variables
ManagedCluster = TypeVar("ManagedCluster")


class MockClient:
    def __init__(self):
        pass

    def get(self):
        pass

    def begin_create_or_update(
        self, resource_group_name: str, resource_name: str, parameters: ManagedCluster, **kwargs: Any
    ):
        pass


class MockCLI(CLI):
    def __init__(self):
        super().__init__(
            cli_name="mock_cli",
            config_dir=MOCK_CLI_CONFIG_DIR,
            config_env_var_prefix=MOCK_CLI_ENV_VAR_PREFIX,
        )
        self.cloud = get_active_cloud(self)


class MockCmd:
    def __init__(self, cli_ctx):
        self.cli_ctx = cli_ctx
        self.cmd = AzCliCommand(AzCommandsLoader(cli_ctx), "mock-cmd", None)

    def supported_api_version(
        self,
        resource_type=None,
        min_api=None,
        max_api=None,
        operation_group=None,
        parameter_name=None,
    ):
        return self.cmd.supported_api_version(
            resource_type=resource_type,
            min_api=min_api,
            max_api=max_api,
            operation_group=operation_group,
            parameter_name=parameter_name,
        )

    def get_models(self, *attr_args, **kwargs):
        return self.cmd.get_models(*attr_args, **kwargs)


class MockUrlretrieveUrlValidator:
    def __init__(self, url, version):
        self.url = url
        self.version = version

    def __eq__(self, other):
        return other.startswith(self.url) and self.version in other
