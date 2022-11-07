# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for NAS Server module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_nasserver_api \
    import MockNASServerApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.nas_server = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.unity.plugins.modules.nasserver import NASServer


class TestNASServer():

    NAS_SERVER_MODULE_ARGS = {'nas_server_name': 'nas0', 'nas_server_id': None, 'nas_server_new_name': None, 'default_unix_user': None,
                              'default_windows_user': None, 'is_replication_destination': None, 'is_multiprotocol_enabled': None,
                              'allow_unmapped_user': None, 'enable_windows_to_unix_username_mapping': None,
                              'is_backup_only': None, 'is_packet_reflect_enabled': None, 'current_unix_directory_service': None,
                              'replication_reuse_resource': None, 'replication_params': {}, 'replication_state': None, 'state': None}

    @pytest.fixture
    def nasserver_module_mock(self):
        nasserver_module_mock = NASServer()
        nasserver_module_mock.unity_conn = MagicMock()
        return nasserver_module_mock

    def get_nas_response(self):
        nasserver_response = MockNASServerApi.get_nas_server_response()
        nasserver_response['replicate_with_dst_resource_provisioning'] = MagicMock(return_value=True)
        return nasserver_response

    def test_enable_nas_replication(self, nasserver_module_mock):
        self.NAS_SERVER_MODULE_ARGS.update(MockNASServerApi.get_replication_params())
        nasserver_module_mock.module.params = self.NAS_SERVER_MODULE_ARGS
        nasserver_module_mock.to_update = MagicMock(return_value=False)
        nasserver_module_mock.get_nas_server = \
            MagicMock(return_value=MockSDKObject(self.get_nas_response()))
        nasserver_module_mock.perform_module_operation()
        assert nasserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_enable_nas_replication_invalid_params(self, nasserver_module_mock):
        self.NAS_SERVER_MODULE_ARGS.update(MockNASServerApi.get_replication_params(False))
        nasserver_module_mock.module.params = self.NAS_SERVER_MODULE_ARGS
        nasserver_module_mock.get_nas_server = \
            MagicMock(return_value=MockSDKObject(self.get_nas_response()))
        nasserver_module_mock.to_update = MagicMock(return_value=False)
        nasserver_module_mock.perform_module_operation()
        assert "rpo value should be in range of 5 to 1440" in \
            nasserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_enable_nas_replication_throws_ex(self, nasserver_module_mock):
        self.NAS_SERVER_MODULE_ARGS.update(MockNASServerApi.get_replication_params())
        nasserver_module_mock.module.params = self.NAS_SERVER_MODULE_ARGS
        nasserver_module_mock.to_update = MagicMock(return_value=False)
        nasserver_module_mock.get_nas_server = \
            MagicMock(return_value=MockSDKObject(self.get_nas_response()))
        nasserver_module_mock.get_remote_system = MagicMock(side_effect=Exception)
        nasserver_module_mock.perform_module_operation()
        assert "Enabling replication to the nas server %s failed with error" \
            % self.NAS_SERVER_MODULE_ARGS['nas_server_name'] in \
            nasserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_nas_replication(self, nasserver_module_mock):
        self.NAS_SERVER_MODULE_ARGS.update(MockNASServerApi.get_replication_params())
        nasserver_module_mock.module.params = self.NAS_SERVER_MODULE_ARGS
        nasserver_module_mock.to_update = MagicMock(return_value=False)
        nasserver_module_mock.get_nas_server = \
            MagicMock(return_value=MockSDKObject(self.get_nas_response()))
        nasserver_module_mock.get_replication_session_on_filter = MagicMock()
        nasserver_module_mock.perform_module_operation()
        assert nasserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_disable_replication(self, nasserver_module_mock):
        self.NAS_SERVER_MODULE_ARGS.update({'replication_state': 'disable', 'state': 'present'})
        nasserver_module_mock.module.params = self.NAS_SERVER_MODULE_ARGS
        nasserver_module_mock.get_nas_server = \
            MagicMock(return_value=MockSDKObject(self.get_nas_response()))
        nasserver_module_mock.to_update = MagicMock(return_value=False)
        nasserver_module_mock.update_replication_params = MagicMock()
        nasserver_module_mock.perform_module_operation()
        assert nasserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_disable_replication_throws_ex(self, nasserver_module_mock):
        self.NAS_SERVER_MODULE_ARGS.update({'replication_state': 'disable', 'state': 'present'})
        nasserver_module_mock.module.params = self.NAS_SERVER_MODULE_ARGS
        nasserver_module_mock.get_nas_server = \
            MagicMock(return_value=MockSDKObject(self.get_nas_response()))
        nasserver_module_mock.to_update = MagicMock(return_value=False)
        nasserver_module_mock.get_replication_session = MagicMock(side_effect=Exception)
        nasserver_module_mock.perform_module_operation()
        assert "Disabling replication on the nas server %s failed with error" \
            % self.NAS_SERVER_MODULE_ARGS['nas_server_name'] in \
            nasserver_module_mock.module.fail_json.call_args[1]['msg']
