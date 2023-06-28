# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Info module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_info_api \
    import MockInfoApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_api_exception \
    import HttpError as http_error
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell import utils

utils.get_logger = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.unity.plugins.modules.info import Info


class TestInfo():

    get_module_args = {"gather_subset": None, "state": "present"}

    @pytest.fixture
    def info_module_mock(self):
        info_module_mock = Info()
        info_module_mock.unity = MagicMock()
        return info_module_mock

    def test_get_replication_session_details(self, info_module_mock):
        self.get_module_args.update({'gather_subset': 'replication_session'})
        info_module_mock.module.params = self.get_module_args
        info_module_mock.unity.get_replication_session = \
            MagicMock(return_value=MockInfoApi.get_replication_sessions_response())
        info_module_mock.perform_module_operation()
        assert info_module_mock.module.exit_json.call_args[1]['Replication_sessions'] is not None

    def test_get_replication_session_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({'gather_subset': 'replication_session'})
        info_module_mock.module.params = self.get_module_args
        utils.HttpError = http_error
        info_module_mock.unity.get_replication_session = \
            MagicMock(side_effect=http_error)
        info_module_mock.perform_module_operation()
        assert "Get replication session list from unity array failed with error" in \
            info_module_mock.module.fail_json.call_args[1]['msg']
