# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for nfs module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_nfs_api \
    import MockNfsApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.unity.plugins.modules import nfs


class TestNfs():

    get_module_args = MockNfsApi.NFS_MODULE_ARGS

    @pytest.fixture
    def nfs_module_mock(self):
        nfs_module_mock = nfs.NFS()
        nfs_module_mock.unity = MagicMock()
        return nfs_module_mock

    def test_add_host_in_nfs_share_on_advhostmgmt_true(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "nfsshare_dummy_name",
            'filesystem_id': "fs_id_1",
            'adv_host_mgmt_enabled': True,
            'no_access_hosts': [{'host_name': "host1"}, {'ip_address': "**.***.2.2"}],
            'host_state': 'present-in-export',
            'state': 'present'
        })
        nfs_module_mock.module.params = self.get_module_args
        utils.UnityNfsShareList = MagicMock
        nfs_object = MockNfsApi.get_nfs_share_object_on_host_access('add', True)
        nfs_object.modify = MagicMock(return_value=None)
        nfs_object.add_to_skip_list('modify')
        fs_object = MockNfsApi.FILESYSTEM_OBJECT
        get_nfs_share_display_attrs_data = MockNfsApi.get_nfs_share_display_attr_on_host_access('add', True)
        nfs_module_mock.unity.get_filesystem = MagicMock(return_value=fs_object)
        nfs_module_mock.unity.get_nfs_share = MagicMock(return_value=nfs_object)
        nfs_module_mock.unity.get_host = MagicMock(side_effect=[MockNfsApi.get_host_obj(id=1), MockNfsApi.get_host_obj(id=2)])
        nfs.get_nfs_share_display_attrs = MagicMock(return_value=get_nfs_share_display_attrs_data)
        nfs_module_mock.perform_module_operation()
        assert nfs_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_remove_host_in_nfs_share_on_advhostmgmt_true(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "nfsshare_dummy_name",
            'filesystem_id': "fs_id_1",
            'adv_host_mgmt_enabled': True,
            'no_access_hosts': [{'host_name': "host1"}, {'ip_address': "**.***.2.2"}],
            'host_state': 'absent-in-export',
            'state': 'present'
        })
        nfs_module_mock.module.params = self.get_module_args
        utils.UnityNfsShareList = MagicMock
        nfs_object = MockNfsApi.get_nfs_share_object_on_host_access('remove', True)
        nfs_object.modify = MagicMock(return_value=None)
        nfs_object.add_to_skip_list('modify')
        fs_object = MockNfsApi.FILESYSTEM_OBJECT
        get_nfs_share_display_attrs_data = MockNfsApi.get_nfs_share_display_attr_on_host_access('remove', True)
        nfs_module_mock.unity.get_filesystem = MagicMock(return_value=fs_object)
        nfs_module_mock.unity.get_nfs_share = MagicMock(return_value=nfs_object)
        nfs_module_mock.unity.get_host = MagicMock(side_effect=[MockNfsApi.get_host_obj(id=1), MockNfsApi.get_host_obj(id=2),
                                                                MockNfsApi.get_host_obj(id=1), MockNfsApi.get_host_obj(id=2)])
        nfs.get_nfs_share_display_attrs = MagicMock(return_value=get_nfs_share_display_attrs_data)
        nfs_module_mock.perform_module_operation()
        assert nfs_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_add_host_in_nfs_share_on_advhostmgmt_false(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "nfsshare_dummy_name",
            'filesystem_id': "fs_id_1",
            'adv_host_mgmt_enabled': False,
            'read_only_root_hosts': [{'domain': MockNfsApi.DUMMY_DOMAIN_VALUE}, {'subnet': MockNfsApi.DUMMY_SUBNET_VALUE}],
            'host_state': 'present-in-export',
            'state': 'present'
        })
        nfs_module_mock.module.params = self.get_module_args
        utils.UnityNfsShareList = MagicMock
        nfs_object = MockNfsApi.get_nfs_share_object_on_host_access('add', False)
        nfs_object.modify = MagicMock(return_value=None)
        nfs_object.add_to_skip_list('modify')
        fs_object = MockNfsApi.FILESYSTEM_OBJECT
        get_nfs_share_display_attrs_data = MockNfsApi.get_nfs_share_display_attr_on_host_access('add', False)
        nfs_module_mock.unity.get_filesystem = MagicMock(return_value=fs_object)
        nfs_module_mock.unity.get_nfs_share = MagicMock(return_value=nfs_object)
        nfs.get_nfs_share_display_attrs = MagicMock(return_value=get_nfs_share_display_attrs_data)
        nfs_module_mock.perform_module_operation()
        assert nfs_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_remove_host_in_nfs_share_on_advhostmgmt_false(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "nfsshare_dummy_name",
            'filesystem_id': "fs_id_1",
            'adv_host_mgmt_enabled': False,
            'read_only_root_hosts': [{'domain': MockNfsApi.DUMMY_DOMAIN_VALUE}, {'subnet': MockNfsApi.DUMMY_SUBNET_VALUE}],
            'host_state': 'absent-in-export',
            'state': 'present'
        })
        nfs_module_mock.module.params = self.get_module_args
        utils.UnityNfsShareList = MagicMock
        nfs_object = MockNfsApi.get_nfs_share_object_on_host_access('remove', False)
        nfs_object.modify = MagicMock(return_value=None)
        nfs_object.add_to_skip_list('modify')
        fs_object = MockNfsApi.FILESYSTEM_OBJECT
        get_nfs_share_display_attrs_data = MockNfsApi.get_nfs_share_display_attr_on_host_access('remove', False)
        nfs_module_mock.unity.get_filesystem = MagicMock(return_value=fs_object)
        nfs_module_mock.unity.get_nfs_share = MagicMock(return_value=nfs_object)
        nfs.get_nfs_share_display_attrs = MagicMock(return_value=get_nfs_share_display_attrs_data)
        nfs_module_mock.perform_module_operation()
        assert nfs_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_host_access_nfs_share_subnet_negative(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "nfsshare_dummy_name",
            'filesystem_id': "fs_id_1",
            'adv_host_mgmt_enabled': False,
            'read_only_root_hosts': [{'subnet': "1x.x.x.x"}],
            'host_state': 'present-in-export',
            'state': 'present'
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.get_filesystem = MagicMock(return_value=None)
        nfs_module_mock.get_nfs_share = MagicMock(return_value=None)
        nfs_module_mock.create_nfs_share = MagicMock(return_value=None)
        nfs.get_nfs_share_display_attrs = MagicMock(return_value=None)
        nfs_module_mock.perform_module_operation()
        assert nfs_module_mock.module.fail_json.call_args[1]['msg'] == MockNfsApi.host_access_negative_response('subnet_validation')

    def test_host_access_nfs_share_advhostmngmt_negative(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "nfsshare_dummy_name",
            'filesystem_id': "fs_id_1",
            'read_only_root_hosts': [{'subnet': "1x.x.x.x/10"}],
            'host_state': 'present-in-export',
            'state': 'present'
        })
        nfs_module_mock.module.params = self.get_module_args
        nfs_module_mock.get_filesystem = MagicMock(return_value=None)
        nfs_module_mock.get_nfs_share = MagicMock(return_value=None)
        nfs_module_mock.create_nfs_share = MagicMock(return_value=None)
        nfs.get_nfs_share_display_attrs = MagicMock(return_value=None)
        nfs_module_mock.perform_module_operation()
        assert nfs_module_mock.module.fail_json.call_args[1]['msg'] == MockNfsApi.host_access_negative_response('advhostmngmnt_field_validation')

    def test_host_access_nfs_share_exception_negative(self, nfs_module_mock):
        self.get_module_args.update({
            'nfs_export_name': "nfsshare_dummy_name",
            'filesystem_id': "fs_id_1",
            'adv_host_mgmt_enabled': False,
            'read_only_root_hosts': [{'domain': MockNfsApi.DUMMY_DOMAIN_VALUE}, {'subnet': MockNfsApi.DUMMY_SUBNET_VALUE}],
            'host_state': 'absent-in-export',
            'state': 'present'
        })
        nfs_module_mock.module.params = self.get_module_args
        utils.UnityNfsShareList = MagicMock
        nfs_object = MockNfsApi.get_nfs_share_object_on_host_access('remove', False)
        nfs_object.modify = MagicMock(side_effect=MockApiException)
        nfs_object.add_to_skip_list('modify')
        fs_object = MockNfsApi.FILESYSTEM_OBJECT
        nfs_module_mock.unity.get_filesystem = MagicMock(return_value=fs_object)
        nfs_module_mock.unity.get_nfs_share = MagicMock(return_value=nfs_object)
        nfs.get_nfs_share_display_attrs = MagicMock(return_value=None)
        nfs_module_mock.perform_module_operation()
        assert nfs_module_mock.module.fail_json.call_args[1]['msg'] == MockNfsApi.host_access_negative_response('modify_exception')
