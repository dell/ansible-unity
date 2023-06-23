# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of CIFS server module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_cifsserver_api \
    import MockCIFSServerApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell import utils

utils.get_logger = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock()
utils.UnityCifsServer = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.unity.plugins.modules.cifsserver import CIFSServer


class TestCIFSServer():

    get_module_args = MockCIFSServerApi.CIFS_SERVER_MODULE_ARGS

    @pytest.fixture
    def cifsserver_module_mock(self):
        cifsserver_module_mock = CIFSServer()
        cifsserver_module_mock.unity_conn = MagicMock()
        utils.cifsserver = MagicMock()
        return cifsserver_module_mock

    def test_get_cifs_server_details(self, cifsserver_module_mock):
        cifs_server_details = MockCIFSServerApi.get_cifs_server_details_method_response()
        self.get_module_args.update({
            'cifs_server_name': 'test_cifs_server',
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.unity_conn.get_cifs_server = MagicMock(return_value=MockSDKObject(cifs_server_details))
        cifsserver_module_mock.perform_module_operation()
        assert MockCIFSServerApi.get_cifs_server_details_method_response() == \
               cifsserver_module_mock.module.exit_json.call_args[1]['cifs_server_details']

    def test_get_cifs_server_details_using_id(self, cifsserver_module_mock):
        cifs_server_details = MockCIFSServerApi.get_cifs_server_details_method_response()
        self.get_module_args.update({
            'cifs_server_id': 'cifs_59',
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.unity_conn.get_cifs_server = MagicMock(return_value=MockSDKObject(cifs_server_details))
        cifsserver_module_mock.perform_module_operation()
        assert MockCIFSServerApi.get_cifs_server_details_method_response() == \
               cifsserver_module_mock.module.exit_json.call_args[1]['cifs_server_details']

    def test_get_get_nas_server_id(self, cifsserver_module_mock):
        nas_server_details = MockCIFSServerApi.get_nas_server_details()
        self.get_module_args.update({
            'cifs_server_id': 'cifs_59',
            'nas_server_name': 'test_nas1',
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.unity_conn.get_nas_server = MagicMock(return_value=MockSDKObject(nas_server_details))
        cifsserver_module_mock.perform_module_operation()
        cifsserver_module_mock.unity_conn.get_nas_server.assert_called()

    def test_create_cifs_server(self, cifsserver_module_mock):
        self.get_module_args.update({
            'nas_server_id': 'nas_18',
            'cifs_server_name': 'test_cifs_server',
            'domain': 'xxx.xxx.xxx.xxx',
            'domain_username': 'xxxxxxxx',
            'domain_password': 'xxxxxxxx',
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.get_details = MagicMock(return_value=None)
        cifsserver_module_mock.unity_conn.create_cifs_server = MagicMock(return_value=True)
        cifsserver_module_mock.perform_module_operation()
        assert cifsserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_cifs_server_throws_exception(self, cifsserver_module_mock):
        self.get_module_args.update({
            'cifs_server_name': 'test_cifs_server',
            'domain': 'xxx.xxx.xxx.xxx',
            'domain_username': 'xxxxxxxx',
            'domain_password': 'xxxxxxxx',
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.get_details = MagicMock(return_value=None)
        cifsserver_module_mock.perform_module_operation()
        assert MockCIFSServerApi.create_cifs_server_without_nas() == cifsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_cifs_server(self, cifsserver_module_mock):
        cifs_server_details = MockCIFSServerApi.get_cifs_server_details_method_response()
        self.get_module_args.update({
            'cifs_server_name': 'test_cifs_server',
            'unjoin_cifs_server_account': False,
            'domain_username': 'xxxxxxxx',
            'domain_password': 'xxxxxxxx',
            'state': 'absent'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.get_details = MagicMock(return_value=cifs_server_details)
        cifsserver_module_mock.get_cifs_server_instance = MagicMock(return_value=MockSDKObject(cifs_server_details))
        cifsserver_module_mock.perform_module_operation()
        assert cifsserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_is_modification_required(self, cifsserver_module_mock):
        cifs_server_details = MockCIFSServerApi.get_cifs_server_details_method_response()
        self.get_module_args.update({
            'cifs_server_name': 'test_cifs_server',
            'netbios_name': 'ansible_netbios',
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.get_details = MagicMock(return_value=cifs_server_details)
        cifsserver_module_mock.perform_module_operation()
        assert MockCIFSServerApi.modify_error_msg() == cifsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_is_domain_modification_required(self, cifsserver_module_mock):
        cifs_server_details = MockCIFSServerApi.get_cifs_server_details_method_response()
        self.get_module_args.update({
            'cifs_server_name': 'test_cifs_server',
            'domain': 'yyy.yyy.yyy.yyy',
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.get_details = MagicMock(return_value=cifs_server_details)
        cifsserver_module_mock.perform_module_operation()
        print(cifsserver_module_mock.module.fail_json.call_args[1])
        assert MockCIFSServerApi.modify_error_msg() == cifsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_is_modify_interfaces(self, cifsserver_module_mock):
        cifs_server_details = MockCIFSServerApi.get_cifs_server_details_method_response()
        self.get_module_args.update({
            'cifs_server_name': 'test_cifs_server',
            'interfaces': ['if_39'],
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.get_details = MagicMock(return_value=cifs_server_details)
        cifsserver_module_mock.perform_module_operation()
        print(cifsserver_module_mock.module.fail_json.call_args[1])
        assert MockCIFSServerApi.modify_error_msg() == cifsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_is_modify_interfaces_idempotency(self, cifsserver_module_mock):
        cifs_server_details = MockCIFSServerApi.get_cifs_server_details_method_response()
        self.get_module_args.update({
            'cifs_server_name': 'test_cifs_server',
            'interfaces': ['if_43'],
            'state': 'present'
        })
        cifsserver_module_mock.module.params = self.get_module_args
        cifsserver_module_mock.get_details = MagicMock(return_value=cifs_server_details)
        cifsserver_module_mock.perform_module_operation()
        assert cifsserver_module_mock.module.exit_json.call_args[1]['changed'] is False
