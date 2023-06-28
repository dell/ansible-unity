# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of NFS server module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_nfsserver_api \
    import MockNFSServerApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_api_exception \
    import HttpError as http_error, MockApiException
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell import utils

utils.get_logger = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock()
utils.UnityNfsServer = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.unity.plugins.modules.nfsserver import NFSServer


class TestNFSServer():

    get_module_args = MockNFSServerApi.NFS_SERVER_MODULE_ARGS

    @pytest.fixture
    def nfsserver_module_mock(self):
        nfsserver_module_mock = NFSServer()
        nfsserver_module_mock.unity_conn = MagicMock()
        utils.nfsserver = MagicMock()
        nfsserver_module_mock.module.check_mode = False
        return nfsserver_module_mock

    def test_get_nfs_server_details(self, nfsserver_module_mock):
        self.get_module_args.update({
            'nfs_server_id': 'nfs_95',
            'state': 'present'
        })
        nfsserver_module_mock.module.params = self.get_module_args
        host_details = MockNFSServerApi.get_nas_server_id()
        host_details.get_id = MagicMock(return_value="nas_10")
        host_details.add_to_skip_list('get_id')
        nfsserver_module_mock.unity_conn.get_nas_server = MagicMock(return_value=host_details)
        nfsserver_module_mock.unity_conn.get_nfs_server = MagicMock(return_value=MockNFSServerApi.get_nfs_server_details()[0])
        nfsserver_module_mock.perform_module_operation()
        assert MockNFSServerApi.get_nfs_server_details_method_response() == \
               nfsserver_module_mock.module.exit_json.call_args[1]['nfs_server_details']

    def test_get_nfs_server_details_with_exception(self, nfsserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': 'test_nas_server',
            'state': 'present'
        })
        nfsserver_module_mock.module.params = self.get_module_args
        host_details = MockNFSServerApi.get_nas_server_id()
        host_details.get_id = MagicMock(return_value="nas_10")
        host_details.add_to_skip_list('get_id')
        nfsserver_module_mock.unity_conn.get_nas_server = MagicMock(return_value=host_details)
        utils.HttpError = http_error
        nfsserver_module_mock.unity_conn.get_nfs_server = MagicMock(side_effect=http_error)
        nfsserver_module_mock.perform_module_operation()
        assert MockNFSServerApi.get_nfs_server_api_exception() == \
               nfsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_nfs_server(self, nfsserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': 'dummy_name',
            'host_name': "dummy_nas23",
            'is_secure_enabled': True,
            'kerberos_domain_controller_type': "WINDOWS",
            'kerberos_domain_controller_username': "xxxxxxxx",
            'kerberos_domain_controller_password': "xxxxxxxx",
            'is_extended_credentials_enabled': False,
            'nfs_v4_enabled': True,
            'state': "present"
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=None)
        utils.KdcTypeEnum = MagicMock(return_value={"KdcTypeEnum": {"description": "Windows", "name": "WINDOWS", "value": 2}})
        utils.UnityNfsServer = MagicMock()
        utils.UnityNfsServer.create = MagicMock(return_value=True)
        nfsserver_module_mock.perform_module_operation()
        assert nfsserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_nfs_server_with_unix(self, nfsserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': 'dummy_name',
            'host_name': "dummy_nas23",
            'is_secure_enabled': True,
            'kerberos_domain_controller_type': "UNIX",
            'kerberos_domain_controller_username': "xxxxxxxx",
            'kerberos_domain_controller_password': "xxxxxxxx",
            'is_extended_credentials_enabled': False,
            'nfs_v4_enabled': True,
            'state': "present"
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=None)
        utils.KdcTypeEnum = MagicMock(return_value={"KdcTypeEnum": {"description": "Windows", "name": "UNIX", "value": 1}})
        utils.UnityNfsServer = MagicMock()
        utils.UnityNfsServer.create = MagicMock(return_value=True)
        nfsserver_module_mock.perform_module_operation()
        assert nfsserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_nfs_server_throws_exception(self, nfsserver_module_mock):
        self.get_module_args.update({
            'nas_server_name': 'dummy_name',
            'host_name': "dummy_nas23",
            'is_secure_enabled': True,
            'kerberos_domain_controller_type': "WINDOWS",
            'kerberos_domain_controller_username': "xxxxxxxx",
            'kerberos_domain_controller_password': "xxxxxxxx",
            'is_extended_credentials_enabled': False,
            'nfs_v4_enabled': True,
            'state': "present"
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=None)
        utils.UnityNfsServer = MagicMock()
        utils.UnityNfsServer.create = MagicMock(side_effect=MockApiException)
        nfsserver_module_mock.perform_module_operation()
        assert MockNFSServerApi.create_nfs_server_with_api_exception() in nfsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_nfs_server(self, nfsserver_module_mock):
        nfs_server_details = MockNFSServerApi.get_nfs_server_details_method_response()
        self.get_module_args.update({
            'nas_server_name': 'test_nas_server',
            'kerberos_domain_controller_username': "xxxxxxxx",
            'kerberos_domain_controller_password': "xxxxxxxx",
            'remove_spn_from_kerberos': True,
            'state': "absent"
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=nfs_server_details)
        nfsserver_module_mock.perform_module_operation()
        assert nfsserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_nfs_server_with_spn_false(self, nfsserver_module_mock):
        nfs_server_details = MockNFSServerApi.get_nfs_server_details_method_response()
        self.get_module_args.update({
            'nas_server_name': 'test_nas_server',
            'kerberos_domain_controller_username': "xxxxxxxx",
            'kerberos_domain_controller_password': "xxxxxxxx",
            'remove_spn_from_kerberos': False,
            'state': "absent"
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=nfs_server_details)
        nfsserver_module_mock.perform_module_operation()
        assert nfsserver_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_nfs_server_with_exception(self, nfsserver_module_mock):
        nfs_server_details = MockNFSServerApi.get_nfs_server_details_method_response()
        self.get_module_args.update({
            'nas_server_name': 'test_nas_server',
            'kerberos_domain_controller_username': "xxxxxxxx",
            'kerberos_domain_controller_password': "xxxxxxxx",
            'remove_spn_from_kerberos': False,
            'state': "absent"
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=nfs_server_details)
        nfsserver_module_mock.unity_conn.get_nfs_server = MagicMock(side_effect=MockApiException)
        nfsserver_module_mock.perform_module_operation()
        assert MockNFSServerApi.delete_exception() in nfsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_is_modification_required(self, nfsserver_module_mock):
        nfs_server_details = MockNFSServerApi.get_nfs_server_details_method_response()
        self.get_module_args.update({
            'nas_server_name': 'test_nas_server',
            'is_extended_credentials_enabled': True,
            'state': 'present'
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=nfs_server_details)
        nfsserver_module_mock.perform_module_operation()
        assert MockNFSServerApi.modify_error_msg() == nfsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_nas_server_id_exception(self, nfsserver_module_mock):
        nfs_server_details = MockNFSServerApi.get_nfs_server_details_method_response()
        self.get_module_args.update({
            'nas_server_name': 'dummy_name',
            'is_secure_enabled': True,
            'host_name': "dummy_nas23",
            'kerberos_domain_controller_type': "WINDOWS",
            'kerberos_domain_controller_username': "xxxxxxxx",
            'kerberos_domain_controller_password': "xxxxxxxx",
            'is_extended_credentials_enabled': False,
            'nfs_v4_enabled': True,
            'state': "present"
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.unity_conn.get_nas_server = MagicMock(side_effect=MockApiException)
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=nfs_server_details)
        nfsserver_module_mock.perform_module_operation()
        assert MockNFSServerApi.get_nas_server_id_api_exception() in \
               nfsserver_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_nas_server_without_nas_server_id(self, nfsserver_module_mock):
        self.get_module_args.update({
            'is_secure_enabled': True,
            'host_name': "dummy_nas23",
            'kerberos_domain_controller_type': "WINDOWS",
            'kerberos_domain_controller_username': "xxxxxxxx",
            'kerberos_domain_controller_password': "xxxxxxxx",
            'is_extended_credentials_enabled': False,
            'nfs_v4_enabled': True,
            'state': "present"
        })
        nfsserver_module_mock.module.params = self.get_module_args
        nfsserver_module_mock.get_nas_server_id = MagicMock(return_value=None)
        nfsserver_module_mock.get_nfs_server_details = MagicMock(return_value=None)
        nfsserver_module_mock.create_nfs_server = MagicMock(return_value=None)
        nfsserver_module_mock.perform_module_operation()
        assert MockNFSServerApi.create_nfs_server_without_nas_server_id() in \
               nfsserver_module_mock.module.fail_json.call_args[1]['msg']
