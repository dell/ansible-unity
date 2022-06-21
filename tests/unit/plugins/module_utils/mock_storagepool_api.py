# Copyright:  (c) 2022,  Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of storagepool module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject


class MockStoragePoolApi:
    STORAGE_POOL_MODULE_ARGS = {
        'unispherehost': '**.***.**.***',
        'port': '123',
        'pool_name': None,
        'pool_id': None,
        'new_pool_name': None,
        'pool_description': None,
        'fast_cache': None,
        'fast_vp': None,
        'raid_groups': {},
        'state': None
    }
    RAID_TYPE_5 = 'RaidTypeEnum.RAID5'

    @staticmethod
    def get_pool_details_response(response_type):
        if response_type == 'get_pool':
            return {'alert_threshold': 84, 'creation_time': '2021-11-11 11:11:11+00:00',
                    'description': '', 'harvest_state': 'UsageHarvestStateEnum.IDLE',
                    'health': {'UnityHealth': {}}, 'id': 'pool_mock_1',
                    'is_all_flash': True, 'is_empty': False, 'is_fast_cache_enabled': False,
                    'is_harvest_enabled': True, 'is_snap_harvest_enabled': False,
                    'metadata_size_subscribed': 1, 'metadata_size_used': 1,
                    'name': 'Ansible_Unity_TEST_1', 'object_id': 1, 'pool_fast_vp': {'UnityPoolFastVp': {}},
                    'pool_space_harvest_high_threshold': 95.0, 'pool_space_harvest_low_threshold': 85.0, 'pool_type':
                    'StoragePoolTypeEnum.DYNAMIC', 'raid_type': MockStoragePoolApi.RAID_TYPE_5, 'rebalance_progress': None, 'size_free': 1,
                    'size_subscribed': 1, 'size_total': 1, 'size_used': 1, 'snap_size_subscribed':
                    1, 'snap_size_used': 1, 'snap_space_harvest_high_threshold': 25.0, 'snap_space_harvest_low_threshold':
                    20.0, 'tiers': {'UnityPoolTierList': [{'UnityPoolTier': {}}, {'UnityPoolTier': {}}, {'UnityPoolTier': {}}]}, 'existed': True}
        elif response_type == 'pool_object':
            return {'alert_threshold': 84, 'creation_time': '2021-11-11 11:11:11+00:00',
                    'description': '', 'harvest_state': 'UsageHarvestStateEnum.IDLE',
                    'health': {'UnityHealth': {}}, 'id': 'pool_mock_1',
                    'is_all_flash': True, 'is_empty': False, 'is_fast_cache_enabled': False,
                    'is_harvest_enabled': True, 'is_snap_harvest_enabled': False,
                    'metadata_size_subscribed': 1, 'metadata_size_used': 1,
                    'name': 'Ansible_Unity_TEST_1', 'object_id': 1,
                    'pool_fast_vp': {'UnityPoolFastVp': {}},
                    'pool_space_harvest_high_threshold': 95.0,
                    'pool_space_harvest_low_threshold': 85.0, 'pool_type': 'StoragePoolTypeEnum.DYNAMIC',
                    'raid_type': MockStoragePoolApi.RAID_TYPE_5, 'rebalance_progress': None, 'size_free': 1,
                    'size_subscribed': 1, 'size_total': 1, 'size_used': 1,
                    'snap_size_subscribed': 1, 'snap_size_used': 1,
                    'snap_space_harvest_high_threshold': 25.0, 'snap_space_harvest_low_threshold': 20.0,
                    'tiers': MockSDKObject({'disk_count': [5, 0, 0], 'name': ['Extreme Performance', 'Performance', 'Capacity'],
                                            'pool_units': [{'UnityPoolUnitList': [{'UnityPoolUnit': {'id': 'pool_unit_mock_1'}}]}, None, None],
                                            'raid_type': [MockStoragePoolApi.RAID_TYPE_5, 'RaidTypeEnum.NONE', 'RaidTypeEnum.NONE'],
                                            'size_free': [1, 0, 0],
                                            'size_moving_down': [0, 0, 0], 'size_moving_up': [0, 0, 0],
                                            'size_moving_within': [0, 0, 0], 'size_total': [1, 0, 0],
                                            'size_used': [1, 0, 0], 'stripe_width': ['RaidStripeWidthEnum._5', None, None],
                                            'tier_type': ['TierTypeEnum.EXTREME_PERFORMANCE', 'TierTypeEnum.PERFORMANCE', 'TierTypeEnum.CAPACITY'],
                                            'existed': True}),
                    'existed': True}
        elif response_type == 'disk_list':
            return [MockSDKObject({"bus_id": 99, "current_speed": 1, "disk_group": {"UnityDiskGroup": {"id": "disk_mock_1"}},
                                   "disk_technology": MockSDKObject({"name": "mock_disk_tech"}), "emc_part_number": "XXXXXXXX",
                                   "emc_serial_number": "XXXXXXXX", "existed": True, "health": {"UnityHealth": {}},
                                   "id": "disk_mock_2", "is_fast_cache_in_use": False, "is_in_use": True,
                                   "is_sed": False, "manufacturer": "mock_disk_manufacturer",
                                   "max_speed": 1, "model": "mock_disk_model", "name": "Drive 12",
                                   "needs_replacement": False, "pool": MockSDKObject({"id": "pool_5", "name": "Pool_Mock_TEST_2", "UnityPool": {}}),
                                   "raw_size": 1, "rpm": 0, "size": 1, "slot_number": 12,
                                   "tier_type": MockSDKObject({"name": "EXTREME_PERFORMANCE"}), "vendor_size": 1,
                                   "version": "S109", "wwn": "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00"}),
                    MockSDKObject({"bus_id": 99, "current_speed": 1,
                                   "disk_group": {"UnityDiskGroup": {"id": "disk_mock_1"}},
                                   "disk_technology": MockSDKObject({"name": "mock_disk_tech"}), "emc_part_number": "XXXXXXXX",
                                   "emc_serial_number": "XXXXXXXX", "existed": True, "health": {"UnityHealth": {}},
                                   "id": "mock_disk_id", "is_fast_cache_in_use": False, "is_in_use": True, "is_sed": False,
                                   "manufacturer": "mock_disk_manufacturer", "max_speed": 1, "model": "mock_disk_model",
                                   "name": "disk_disk_name", "needs_replacement": False,
                                   "pool": MockSDKObject({"id": "pool_mock_1", "name": "Ansible_Unity_TEST_1"}),
                                   "raw_size": 1, "rpm": 0, "size": 1,
                                   "slot_number": 13, "tier_type": MockSDKObject({"name": "EXTREME_PERFORMANCE"}),
                                   "vendor_size": 1, "version": "S109",
                                   "wwn": "01:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00"})]
        elif response_type == 'module':
            return {"storage_pool_details":
                    {"alert_threshold": 84, "creation_time": "2021-11-11 11:11:11+00:00", "description": "",
                     "drives": [{"disk_technology": "mock_disk_tech", "id": "mock_disk_id", "name": "disk_disk_name",
                                 "size": 1, "tier_type": "EXTREME_PERFORMANCE"}],
                     "existed": True, "harvest_state": "UsageHarvestStateEnum.IDLE",
                     "health": {"UnityHealth": {}},
                     "id": "pool_mock_1", "is_all_flash": True, "is_empty": False,
                     "is_fast_cache_enabled": False, "is_fast_vp_enabled": True,
                     "is_harvest_enabled": True, "is_snap_harvest_enabled": False,
                     "metadata_size_subscribed": 1, "metadata_size_used":
                     1, "name": "Ansible_Unity_TEST_1", "object_id": 1,
                     "pool_fast_vp": {"UnityPoolFastVp": {}},
                     "pool_space_harvest_high_threshold": 95.0,
                     "pool_space_harvest_low_threshold": 85.0, "pool_type": "StoragePoolTypeEnum.DYNAMIC",
                     "raid_type": "RaidTypeEnum.RAID5", "rebalance_progress": None, "size_free": 1,
                     "size_free_with_unit": "1.0 B", "size_subscribed": 1, "size_subscribed_with_unit": "1.0 B",
                     "size_total": 1, "size_total_with_unit": "1.0 B", "size_used": 1, "size_used_with_unit": "1.0 B",
                     "snap_size_subscribed": 1, "snap_size_subscribed_with_unit": "1.0 B", "snap_size_used": 1,
                     "snap_size_used_with_unit": "1.0 B", "snap_space_harvest_high_threshold": 25.0, "snap_space_harvest_low_threshold": 20.0,
                     "tiers": {"UnityPoolTierList": [{"disk_count": [5, 0, 0], "existed": True,
                                                      "name": ["Extreme Performance", "Performance", "Capacity"],
                                                      "pool_units": [{"UnityPoolUnitList": [{"UnityPoolUnit": {"id": "pool_unit_mock_1"}}]}, None, None],
                                                      "raid_type": ["RaidTypeEnum.RAID5", "RaidTypeEnum.NONE", "RaidTypeEnum.NONE"],
                                                      "size_free": [1, 0, 0], "size_moving_down": [0, 0, 0],
                                                      "size_moving_up": [0, 0, 0],
                                                      "size_moving_within": [0, 0, 0],
                                                      "size_total": [1, 0, 0],
                                                      "size_used": [1, 0, 0],
                                                      "stripe_width": ["RaidStripeWidthEnum._5", None, None],
                                                      "tier_type": ["TierTypeEnum.EXTREME_PERFORMANCE", "TierTypeEnum.PERFORMANCE",
                                                                    "TierTypeEnum.CAPACITY"]}]}}}
        elif response_type == 'error':
            return 'Get details of storage pool failed with error: '

    @staticmethod
    def create_pool_response(response_type):
        if response_type == 'api':
            return {"storage_pool_details":
                    {"alert_threshold": 50, "creation_time": "2022-03-08 10:51:08+00:00", "description": "Unity test pool.",
                     "drives": [{"disk_technology": "SAS", "id": "disk_id_1", "name": "DPE Drive 1",
                                 "size": 1, "tier_type": "PERFORMANCE"},
                                {"disk_technology": "SAS", "id": "disk_id_2", "name": "DPE Drive 2",
                                 "size": 1, "tier_type": "PERFORMANCE"},
                                {"disk_technology": "SAS", "id": "disk_id_3", "name": "DPE Drive 3",
                                 "size": 1, "tier_type": "PERFORMANCE"}],
                     "existed": True, "harvest_state": "UsageHarvestStateEnum.IDLE",
                     "health": {"UnityHealth": {}},
                     "id": "pool_id_1", "is_all_flash": False, "is_empty": True,
                     "is_fast_cache_enabled": False, "is_fast_vp_enabled": True,
                     "is_harvest_enabled": True, "is_snap_harvest_enabled": True,
                     "metadata_size_subscribed": 0, "metadata_size_used":
                     0, "name": "Mock_Test", "object_id": 123,
                     "pool_fast_vp": {"UnityPoolFastVp": {}},
                     "pool_space_harvest_high_threshold": 59.0,
                     "pool_space_harvest_low_threshold": 40.0, "pool_type": "StoragePoolTypeEnum.DYNAMIC",
                     "raid_type": "RaidTypeEnum.RAID10", "rebalance_progress": None, "size_free": 1,
                     "size_free_with_unit": "1 GB", "size_subscribed": 0, "size_subscribed_with_unit": "0B",
                     "size_total": 1, "size_total_with_unit": "1 GB", "size_used": 0, "size_used_with_unit": "0B",
                     "snap_size_subscribed": 0, "snap_size_subscribed_with_unit": "0B", "snap_size_used": 0,
                     "snap_size_used_with_unit": "0B", "snap_space_harvest_high_threshold": 80.0, "snap_space_harvest_low_threshold": 60.0,
                     "tiers": {"UnityPoolTierList": [{"disk_count": [0, 3, 0], "existed": True,
                                                      "name": ["Extreme Performance", "Performance", "Capacity"],
                                                      "pool_units": [{"UnityPoolUnitList": [{"UnityPoolUnit": {"id": "rg_id_1"}},
                                                                     {"UnityPoolUnit": {"id": "rg_id_2"}}]}, None],
                                                      "raid_type": ["RaidTypeEnum.NONE", "RaidTypeEnum.RAID10", "RaidTypeEnum.NONE"],
                                                      "size_free": [0, 1, 0], "size_moving_down": [0, 0, 0],
                                                      "size_moving_up": [0, 0, 0],
                                                      "size_moving_within": [0, 0, 0],
                                                      "size_total": [0, 1, 0],
                                                      "size_used": [0, 0, 0],
                                                      "stripe_width": [None, "RaidStripeWidthEnum._2", None],
                                                      "tier_type": ["TierTypeEnum.EXTREME_PERFORMANCE", "TierTypeEnum.PERFORMANCE",
                                                                    "TierTypeEnum.CAPACITY"]}]}}}
        elif response_type == 'error':
            return 'Failed to create storage pool with error: '
