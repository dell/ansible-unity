# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for FileSystem module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
import re
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_filesystem_api \
    import MockFileSystemApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.UnityReplicationSession = object

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.unity.plugins.modules.filesystem import Filesystem


class TestFileSystem():

    FILE_SYSTEM_MODULE_ARGS = {'filesystem_id': '123', 'filesystem_name': None, 'nas_server_name': None,
                               'nas_server_id': None, 'pool_name': None, 'pool_id': None, 'size': None,
                               'cap_unit': None, 'quota_config': None, 'snap_schedule_name': None,
                               'snap_schedule_id': None, 'replication_params': {}, 'replication_state': None, 'state': None}

    @pytest.fixture
    def filesystem_module_mock(self):
        filesystem_module_mock = Filesystem()
        filesystem_module_mock.unity_conn = MagicMock()
        return filesystem_module_mock

    def test_enable_fs_replication(self, filesystem_module_mock):
        self.FILE_SYSTEM_MODULE_ARGS.update(MockFileSystemApi.get_replication_params())
        filesystem_module_mock.module.params = self.FILE_SYSTEM_MODULE_ARGS
        filesystem_response = MockFileSystemApi.get_file_system_response()
        filesystem_response['replicate_with_dst_resource_provisioning'] = MagicMock(return_value=True)
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_enable_fs_replication_invalid_params(self, filesystem_module_mock):
        self.FILE_SYSTEM_MODULE_ARGS.update(MockFileSystemApi.get_replication_params(False))
        filesystem_module_mock.module.params = self.FILE_SYSTEM_MODULE_ARGS
        filesystem_module_mock.is_modify_required = MagicMock(return_value=False)
        filesystem_module_mock.perform_module_operation()
        assert "Invalid rpo value" in \
            filesystem_module_mock.module.fail_json.call_args[1]['msg']

    def test_enable_fs_replication_throws_ex(self, filesystem_module_mock):
        self.FILE_SYSTEM_MODULE_ARGS.update(MockFileSystemApi.get_replication_params())
        filesystem_module_mock.module.params = self.FILE_SYSTEM_MODULE_ARGS
        filesystem_module_mock.is_modify_required = MagicMock(return_value=False)
        filesystem_response = MockFileSystemApi.get_file_system_response()
        filesystem_response['replicate_with_dst_resource_provisioning'] = MagicMock(side_effect=Exception)
        filesystem_module_mock.get_filesystem = MagicMock(side_effect=[
            MockSDKObject(filesystem_response)])
        filesystem_module_mock.get_filesystem_display_attributes = MagicMock(side_effect=[
            MockSDKObject(filesystem_response)])
        filesystem_module_mock.perform_module_operation()
        assert "Enabling replication to the filesystem failed with error" in \
            re.sub(' <.*?>>', '', filesystem_module_mock.module.fail_json.call_args[1]['msg'])

    def test_modify_fs_replication(self, filesystem_module_mock):
        self.FILE_SYSTEM_MODULE_ARGS.update(MockFileSystemApi.get_replication_params())
        filesystem_module_mock.module.params = self.FILE_SYSTEM_MODULE_ARGS
        filesystem_module_mock.perform_module_operation()
        filesystem_module_mock.get_replication_session_on_filter = MagicMock()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_disable_replication(self, filesystem_module_mock):
        self.FILE_SYSTEM_MODULE_ARGS.update({'replication_state': 'disable', 'state': 'present'})
        filesystem_module_mock.module.params = self.FILE_SYSTEM_MODULE_ARGS
        filesystem_module_mock.get_filesystem_display_attributes = MagicMock()
        filesystem_module_mock.perform_module_operation()
        assert filesystem_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_disable_replication_throws_ex(self, filesystem_module_mock):
        self.FILE_SYSTEM_MODULE_ARGS.update({'replication_state': 'disable', 'state': 'present'})
        filesystem_module_mock.module.params = self.FILE_SYSTEM_MODULE_ARGS
        filesystem_module_mock.get_replication_session = MagicMock(side_effect=Exception)
        filesystem_module_mock.get_filesystem_display_attributes = MagicMock()
        filesystem_module_mock.perform_module_operation()
        assert "Disabling replication on the filesystem failed with error" in \
            re.sub(' <.*?>', '', filesystem_module_mock.module.fail_json.call_args[1]['msg'])
