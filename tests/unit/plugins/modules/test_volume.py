# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for volume module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_volume_api \
    import MockVolumeApi
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
utils.UnityPool = MagicMock()
utils.UnityPool.get_size_in_gb = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.unity.plugins.modules.volume import Volume


class TestUnityVolume():

    get_module_args = MockVolumeApi.VOLUME_MODULE_ARGS

    @pytest.fixture
    def volume_module_mock(self):
        volume_module_mock = Volume()
        volume_module_mock.conn = MagicMock()
        return volume_module_mock

    def test_create_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "Atest",
            'pool_name': "Extreme_Perf_tier",
            'size': 2,
            'cap_unit': "GB",
            'is_thin': True,
            'compression': True,
            'advanced_dedup': True,
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.host_access_modify_required = MagicMock(return_value=False)
        obj_pool = MockSDKObject(MockVolumeApi.pool)
        volume_object = MockVolumeApi.create_volume_response('api')['volume_details']
        volume_module_mock.unity_conn.get_pool = MagicMock(return_value=obj_pool)
        volume_module_mock.unity_conn.get_lun = MagicMock(return_value=None)
        obj_pool.create_lun = MagicMock(return_value=MockSDKObject(volume_object))
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_volume_exception(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "Atest",
            'pool_name': "Extreme_Perf_tier",
            'size': 2,
            'cap_unit': "GB",
            'is_thin': True,
            'compression': True,
            'advanced_dedup': True,
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.host_access_modify_required = MagicMock(return_value=False)
        obj_pool = MockSDKObject(MockVolumeApi.pool)
        volume_module_mock.unity_conn.get_pool = MagicMock(return_value=obj_pool)
        volume_module_mock.unity_conn.get_lun = MagicMock(return_value=None)
        obj_pool.create_lun = MagicMock(side_effect=MockApiException)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.create_volume_response('error') in \
            volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_volume(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "Atest",
            'pool_name': "Extreme_Perf_tier",
            'size': 2,
            'cap_unit': "GB",
            'is_thin': True,
            'compression': True,
            'advanced_dedup': False,
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.host_access_modify_required = MagicMock(return_value=False)
        obj_vol = MockSDKObject(MockVolumeApi.modify_volume_response('api')['volume_details'])
        volume_object = MockVolumeApi.modify_volume_response('api')['volume_details']
        volume_module_mock.unity_conn.get_lun = MagicMock(return_value=obj_vol)
        obj_vol.modify = MagicMock(return_value=MockSDKObject(volume_object))
        volume_module_mock.volume_modify_required = MagicMock()
        volume_module_mock.get_volume_display_attributes = MagicMock()
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_volume_exception(self, volume_module_mock):
        self.get_module_args.update({
            'vol_name': "Atest",
            'pool_name': "Extreme_Perf_tier",
            'size': 2,
            'cap_unit': "GB",
            'is_thin': True,
            'compression': True,
            'advanced_dedup': False,
            'state': 'present'
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.host_access_modify_required = MagicMock(return_value=False)
        obj_vol = MockSDKObject(MockVolumeApi.modify_volume_response('api')['volume_details'])
        volume_module_mock.unity_conn.get_lun = MagicMock(return_value=obj_vol)
        obj_vol.modify = MagicMock(side_effect=MockApiException)
        volume_module_mock.volume_modify_required = MagicMock()
        volume_module_mock.get_volume_display_attributes = MagicMock()
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.modify_volume_response('error') in \
            volume_module_mock.module.fail_json.call_args[1]['msg']
