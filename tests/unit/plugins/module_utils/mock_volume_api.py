# Copyright:  (c) 2023,  Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of volume module on Unity"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockVolumeApi:

    VOLUME_MODULE_ARGS = {
        'unispherehost': '**.***.**.***',
        'port': '123',
        'vol_name': None,
        'vol_id': None,
        'description': None,
        'pool_name': None,
        'pool_id': None,
        'size': None,
        'cap_unit': None,
        'is_thin': None,
        'compression': None,
        'advanced_dedup': None,
        'sp': None,
        'io_limit_policy': None,
        'snap_schedule': None,
        'host_name': None,
        'host_id': None,
        'hosts': {},
        'hlu': None,
        'mapping_state': None,
        'new_vol_name': None,
        'tiering_policy': None,
        'state': None,
    }

    pool = {
        'alert_threshold': 60,
        'creation_time': '2021-10-18 12:51:27+00:00',
        'description': 'A2Z',
        'existed': True,
        'harvest_state': 'UsageHarvestStateEnum.IDLE',
        'hash': 8778647453970,
        'health': {'UnityHealth': {'hash': 8778647453730}},
        'id': 'pool_3',
        'is_all_flash': True,
        'is_empty': False,
        'is_fast_cache_enabled': False,
        'is_harvest_enabled': True,
        'is_snap_harvest_enabled': True,
        'metadata_size_subscribed': 646124142592,
        'metadata_size_used': 357287591936,
        'name': 'Extreme_Perf_tier',
        'object_id': 12884901892,
        'pool_fast_vp': {'UnityPoolFastVp': {'hash': 8778647539688}},
        'pool_space_harvest_high_threshold': 95.0,
        'pool_space_harvest_low_threshold': 70.5,
        'pool_type': 'StoragePoolTypeEnum.TRADITIONAL',
        'raid_type': 'RaidTypeEnum.RAID5',
        'size_free': 1174673555456,
        'size_subscribed': 8703230820352,
        'size_total': 3141768577024,
        'size_used': 1802576257024,
        'snap_size_subscribed': 290195193856,
        'snap_size_used': 43098112,
        'snap_space_harvest_high_threshold': 20.5,
        'snap_space_harvest_low_threshold': 1.0,
        'tiers': {'UnityPoolTierList': [{'UnityPoolTier': {'hash': 8778647538737}},
                  {'UnityPoolTier': {'hash': 8778647538749}},
                  {'UnityPoolTier': {'hash': 8778647526797}}]},
    }

    @staticmethod
    def create_volume_response(response_type):
        if response_type == 'api':
            return {'volume_details': {
                    'current_node': 'NodeEnum.SPB',
                    'data_reduction_percent': 0,
                    'data_reduction_ratio': 1.0,
                    'data_reduction_size_saved': 0,
                    'default_node': 'NodeEnum.SPB',
                    'description': None,
                    'effective_io_limit_max_iops': None,
                    'effective_io_limit_max_kbps': None,
                    'existed': True,
                    'family_base_lun': {'UnityLun': {}},
                    'family_clone_count': 0,
                    'hash': 8769317548849,
                    'health': {'UnityHealth': {}},
                    'host_access': [],
                    'id': 'sv_214551',
                    'io_limit_policy': True,
                    'is_advanced_dedup_enabled': True,
                    'is_compression_enabled': True,
                    'is_data_reduction_enabled': True,
                    'is_replication_destination': False,
                    'is_snap_schedule_paused': False,
                    'is_thin_clone': False,
                    'is_thin_enabled': True,
                    'metadata_size': 3758096384,
                    'metadata_size_allocated': 3221225472,
                    'name': 'Atest',
                    'per_tier_size_used': [3489660928, 0, 0],
                    'pool': {'id': 'pool_3', 'name': 'Extreme_Perf_tier'},
                    'size_allocated': 0,
                    'size_total': 2147483648,
                    'size_total_with_unit': '2.0 GB',
                    'size_used': None,
                    'snap_count': 0,
                    'snap_schedule': None,
                    'snap_wwn': '60:06:01:60:5C:F0:50:00:F6:42:70:38:7A:90:40:FF',
                    'snaps_size': 0,
                    'snaps_size_allocated': 0,
                    'storage_resource': {'UnityStorageResource': {}},
                    'tiering_policy': 'TieringPolicyEnum.AUTOTIER_HIGH',
                    'type': 'LUNTypeEnum.STANDALONE',
                    'wwn': '60:06:01:60:5C:F0:50:00:41:25:EA:63:94:92:92:AE',
                    }}
        else:
            return 'Create volume operation Atest failed with error'

    @staticmethod
    def modify_volume_response(response_type):
        if response_type == 'api':
            return {'volume_details': {
                    'current_node': 'NodeEnum.SPB',
                    'data_reduction_percent': 0,
                    'data_reduction_ratio': 1.0,
                    'data_reduction_size_saved': 0,
                    'default_node': 'NodeEnum.SPB',
                    'description': None,
                    'effective_io_limit_max_iops': None,
                    'effective_io_limit_max_kbps': None,
                    'existed': True,
                    'family_base_lun': {'UnityLun': {}},
                    'family_clone_count': 0,
                    'hash': 8769317548849,
                    'health': {'UnityHealth': {}},
                    'host_access': [],
                    'id': 'sv_214551',
                    'io_limit_policy': None,
                    'is_advanced_dedup_enabled': False,
                    'is_compression_enabled': True,
                    'is_data_reduction_enabled': True,
                    'is_replication_destination': False,
                    'is_snap_schedule_paused': False,
                    'is_thin_clone': False,
                    'is_thin_enabled': True,
                    'metadata_size': 3758096384,
                    'metadata_size_allocated': 3221225472,
                    'name': 'Atest',
                    'per_tier_size_used': [3489660928, 0, 0],
                    'pool': {'id': 'pool_3', 'name': 'Extreme_Perf_tier'},
                    'size_allocated': 0,
                    'size_total': 2147483648,
                    'size_total_with_unit': '2.0 GB',
                    'size_used': None,
                    'snap_count': 0,
                    'snap_schedule': None,
                    'snap_wwn': '60:06:01:60:5C:F0:50:00:F6:42:70:38:7A:90:40:FF',
                    'snaps_size': 0,
                    'snaps_size_allocated': 0,
                    'storage_resource': {'UnityStorageResource': {}},
                    'tiering_policy': 'TieringPolicyEnum.AUTOTIER_HIGH',
                    'type': 'LUNTypeEnum.STANDALONE',
                    'wwn': '60:06:01:60:5C:F0:50:00:41:25:EA:63:94:92:92:AE',
                    }}
        else:
            return 'Failed to modify the volume Atest with error'
