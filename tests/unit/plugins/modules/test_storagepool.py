# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for host module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_storagepool_api \
    import MockStoragePoolApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
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

from ansible_collections.dellemc.unity.plugins.modules.storagepool import StoragePool


class TestUnityStoragePool():

    get_module_args = MockStoragePoolApi.STORAGE_POOL_MODULE_ARGS

    @pytest.fixture
    def storagepool_module_mock(self):
        storagepool_module_mock = StoragePool()
        storagepool_module_mock.conn = MagicMock()
        return storagepool_module_mock

    def test_get_host_details(self, storagepool_module_mock):
        self.get_module_args.update({
            'pool_name': 'Ansible_Unity_TEST_1',
        })
        storagepool_module_mock.module.params = self.get_module_args
        get_pool = MockSDKObject(MockStoragePoolApi.get_pool_details_response('get_pool'))
        get_pool._get_property_from_raw = MagicMock(return_value=MockSDKObject({'is_schedule_enabled': True}))
        get_pool.add_to_skip_list('_get_property_from_raw')
        storagepool_module_mock.conn.get_pool = MagicMock(return_value=get_pool)
        pool_object = MockStoragePoolApi.get_pool_details_response('pool_object')
        utils.UnityPool = MagicMock()
        utils.UnityPool.get = MagicMock(return_value=MockSDKObject(pool_object))
        disk_list = MockStoragePoolApi.get_pool_details_response('disk_list')
        utils.UnityDiskList = MagicMock()
        utils.UnityDiskList.get = MagicMock(return_value=disk_list)
        storagepool_module_mock.perform_module_operation()
        assert MockStoragePoolApi.get_pool_details_response('module')['storage_pool_details'] == \
               storagepool_module_mock.module.exit_json.call_args[1]['storage_pool_details']

    def test_get_host_details_throws_exception(self, storagepool_module_mock):
        self.get_module_args.update({
            'pool_name': 'Ansible_Unity_SP_3',
        })
        storagepool_module_mock.module.params = self.get_module_args
        storagepool_module_mock.conn.get_pool = MagicMock(side_effect=MockApiException)
        storagepool_module_mock.result = MagicMock()
        storagepool_module_mock.get_pool_drives = MagicMock()
        storagepool_module_mock.perform_module_operation()
        storagepool_module_mock.is_pool_modification_required = MagicMock(return_value=False)
        assert MockStoragePoolApi.get_pool_details_response('error') == storagepool_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_pool(self, storagepool_module_mock):
        self.get_module_args.update({
            'pool_name': 'test_pool',
            'pool_description': 'Unity test pool.',
            'raid_groups': {
                'disk_group_id': "dg_16",
                'disk_num': 3,
                'raid_type': 'RAID10',
                'stripe_width': 'BEST_FIT',
            },
            'alert_threshold': 50,
            'is_harvest_enabled': True,
            'pool_harvest_high_threshold': 59,
            'pool_harvest_low_threshold': 40,
            'is_snap_harvest_enabled': True,
            'snap_harvest_high_threshold': 80,
            'snap_harvest_low_threshold': 60,
            'fast_vp': "enabled",
            'fast_cache': "disabled",
            'pool_type': 'TRADITIONAL',
            'state': 'present'
        })
        storagepool_module_mock.module.params = self.get_module_args
        storagepool_module_mock.get_raid_groups_response = MagicMock(return_value=None)
        storagepool_module_mock.get_details = MagicMock(return_value=None)
        pool_object = MockStoragePoolApi.create_pool_response('api')
        utils.UnityPool = MagicMock()
        utils.UnityPool.create = MagicMock(return_value=MockSDKObject(pool_object))
        storagepool_module_mock.perform_module_operation()
        assert storagepool_module_mock.module.exit_json.call_args[1]['changed']

    def test_create_pool_throws_exception(self, storagepool_module_mock):
        self.get_module_args.update({
            'pool_name': 'test_pool',
            'pool_description': 'Unity test pool.',
            'raid_groups': {
                'disk_group_id': "dg_16",
                'disk_num': 3,
                'raid_type': 'RAID10',
                'stripe_width': 'BEST_FIT',
            },
            'alert_threshold': 50,
            'is_harvest_enabled': True,
            'pool_harvest_high_threshold': 59,
            'pool_harvest_low_threshold': 40,
            'is_snap_harvest_enabled': True,
            'snap_harvest_high_threshold': 80,
            'snap_harvest_low_threshold': 60,
            'fast_vp': "enabled",
            'fast_cache': "disabled",
            'pool_type': 'TRADITIONAL',
            'state': 'present'
        })
        storagepool_module_mock.module.params = self.get_module_args
        storagepool_module_mock.get_details = MagicMock(return_value=None)
        utils.UnityPool = MagicMock()
        storagepool_module_mock.get_raid_groups_response = MagicMock(side_effect=MockApiException)
        storagepool_module_mock.perform_module_operation()
        assert MockStoragePoolApi.create_pool_response('error') in \
            storagepool_module_mock.module.fail_json.call_args[1]['msg']
