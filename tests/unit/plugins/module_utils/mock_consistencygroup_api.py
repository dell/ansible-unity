# Copyright:  (c) 2022,  Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of consistency group module on Unity"""

from __future__ import (absolute_import, division, print_function)
from unittest.mock import MagicMock

__metaclass__ = type

from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject


class MockConsistenyGroupApi:
    CONSISTENCY_GROUP_MODULE_ARGS = {
        'unispherehost': '**.***.**.***',
        'port': '123',
        'cg_id': None,
        'cg_name': None,
        'new_cg_name': None,
        'pool_id': None,
        'description': None,
        'snap_schedule': None,
        'tiering_policy': None,
        'volumes': [],
        'vol_state': None,
        'hosts': [],
        'mapping_state': None,
        'replication_params': {},
        'replication_state': None,
        'state': None
    }
    IP_ADDRESS_MOCK_VALUE = '***.***.***.**'

    @staticmethod
    def cg_get_details_method_response():
        return {'advanced_dedup_status': 'DedupStatusEnum.DISABLED', 'block_host_access': None, 'data_reduction_percent': 0,
                'data_reduction_ratio': 1.0, 'data_reduction_size_saved': 0, 'data_reduction_status': 'DataReductionStatusEnum.DISABLED',
                'datastores': None, 'dedup_status': None, 'description': '', 'esx_filesystem_block_size': None,
                'esx_filesystem_major_version': None, 'filesystem': None, 'health': {}, 'host_v_vol_datastore': None,
                'id': 'cg_id_1', 'is_replication_destination': False, 'is_snap_schedule_paused': None,
                'luns': [{'id': 'lun_id_1', 'name': 'test_lun_cg_issue', 'is_thin_enabled': False,
                          'size_total': 1, 'is_data_reduction_enabled': False}],
                'name': 'lun_test_cg_source_12', 'per_tier_size_used': [1, 0, 0],
                'pools': [{'id': 'pool_id_1'}],
                'relocation_policy': 'TieringPolicyEnum.AUTOTIER_HIGH', 'replication_type': 'ReplicationTypeEnum.NONE',
                'size_allocated': 0, 'size_total': 1, 'size_used': None, 'snap_count': 0, 'snap_schedule': None,
                'snaps_size_allocated': 0, 'snaps_size_total': 0, 'thin_status': 'ThinStatusEnum.TRUE',
                'type': 'StorageResourceTypeEnum.CONSISTENCY_GROUP', 'virtual_volumes': None, 'vmware_uuid': None,
                'existed': True, 'snapshots': [], 'cg_replication_enabled': False}

    @staticmethod
    def get_cg_object():
        return MockSDKObject({'advanced_dedup_status': 'DedupStatusEnum.DISABLED', 'block_host_access': None,
                              'data_reduction_percent': 0, 'data_reduction_ratio': 1.0, 'data_reduction_size_saved': 0,
                              'data_reduction_status': 'DataReductionStatusEnum.DISABLED',
                              'datastores': None, 'dedup_status': None, 'description': '', 'esx_filesystem_block_size': None,
                              'esx_filesystem_major_version': None, 'filesystem': None, 'health': {}, 'host_v_vol_datastore': None,
                              'id': 'cg_id_1', 'is_replication_destination': False, 'is_snap_schedule_paused': None,
                              'luns': [MockSDKObject({'id': 'lun_id_1', 'name': 'test_lun_cg_issue',
                                                      'is_thin_enabled': False, 'size_total': 1, 'is_data_reduction_enabled': False})],
                              'name': 'lun_test_cg_source_12', 'per_tier_size_used': [1, 0, 0],
                              'pools': [MockSDKObject({'id': 'pool_id_1'})],
                              'relocation_policy': 'TieringPolicyEnum.AUTOTIER_HIGH', 'replication_type': 'ReplicationTypeEnum.NONE',
                              'size_allocated': 0, 'size_total': 1, 'size_used': None, 'snap_count': 0, 'snap_schedule': None,
                              'snaps_size_allocated': 0, 'snaps_size_total': 0, 'thin_status': 'ThinStatusEnum.TRUE',
                              'type': 'StorageResourceTypeEnum.CONSISTENCY_GROUP', 'virtual_volumes': None, 'vmware_uuid': None,
                              'existed': True, 'snapshots': [], 'cg_replication_enabled': False})

    @staticmethod
    def get_cg_replication_dependent_response(response_type):
        if response_type == 'cg_replication_enabled_details':
            cg_replication_enabled_details = MockConsistenyGroupApi.cg_get_details_method_response()
            cg_replication_enabled_details['cg_replication_enabled'] = True
            return cg_replication_enabled_details
        elif response_type == 'remote_system':
            return [MockSDKObject({"connection_type": "ReplicationCapabilityEnum.ASYNC", "existed": True,
                                   "health": {"UnityHealth": {}}, "id": "system_id_1", "local_spa_interfaces": [MockConsistenyGroupApi.IP_ADDRESS_MOCK_VALUE],
                                   "local_spb_interfaces": [MockConsistenyGroupApi.IP_ADDRESS_MOCK_VALUE],
                                   "management_address": "**.***.**.**", "model": "U XXX",
                                   "name": "ABXXXXXX", "remote_spa_interfaces": [MockConsistenyGroupApi.IP_ADDRESS_MOCK_VALUE],
                                   "remote_spb_interfaces": [MockConsistenyGroupApi.IP_ADDRESS_MOCK_VALUE],
                                   "serial_number": "ABXXXXXX", "sync_fc_ports": ["abc_def", "ghi_jkl"], "username": "username"})]
        elif response_type == 'remote_system_pool_object':
            return MockSDKObject({"alert_threshold": 60, "creation_time": "2021-10-18 12:51:27+00:00", "description": "",
                                  "existed": True, "harvest_state": "UsageHarvestStateEnum.IDLE", "health": {"UnityHealth": {}},
                                  "id": "pool_3", "is_all_flash": True, "is_empty": False, "is_fast_cache_enabled": False,
                                  "is_harvest_enabled": True, "is_snap_harvest_enabled": True, "name": "Extreme_Perf_tier",
                                  "object_id": 1, "pool_fast_vp": {"UnityPoolFastVp": {}}, "pool_space_harvest_high_threshold": 95.0,
                                  "pool_space_harvest_low_threshold": 70.5, "pool_type": "StoragePoolTypeEnum.DYNAMIC",
                                  "raid_type": "RaidTypeEnum.RAID5", "size_free": 1, "size_subscribed": 1, "size_total": 1,
                                  "size_used": 1, "snap_size_subscribed": 1, "snap_size_used": 1, "snap_space_harvest_high_threshold": 20.5,
                                  "snap_space_harvest_low_threshold": 1.0,
                                  "tiers": {"UnityPoolTierList": [{"UnityPoolTier": {}}, {"UnityPoolTier": {}}, {"UnityPoolTier": {}}]}})
        elif response_type == 'replication_session':
            return MockSDKObject({"current_transfer_est_remain_time": 0, "daily_snap_replication_policy": {},
                                  "dst_resource_id": "dest_id_1", "dst_status": "ReplicationSessionStatusEnum.OK", "existed": True,
                                  "health": {}, "hourly_snap_replication_policy": {},
                                  "id": "111111_XXX1111111_0000_1111111_XXX111111111_0000",
                                  "last_sync_time": "2022-02-17 09: 50: 54+00: 00",
                                  "local_role": "ReplicationSessionReplicationRoleEnum.LOOPBACK",
                                  "max_time_out_of_sync": 60, "members": {}, "name": "rep_session_1",
                                  "network_status": "ReplicationSessionNetworkStatusEnum.OK", "remote_system": {},
                                  "replication_resource_type": "ReplicationEndpointResourceTypeEnum.CONSISTENCYGROUP",
                                  "src_resource_id": "src_id_1",
                                  "src_status": "ReplicationSessionStatusEnum.OK",
                                  "status": "ReplicationOpStatusEnum.AUTO_SYNC_CONFIGURED",
                                  "sync_progress": 0, "sync_state": "ReplicationSessionSyncStateEnum.IDLE"})
        elif response_type == 'destination_cg_name_validation':
            return 'destination_cg_name value should be in range of 1 to 95'
        elif response_type == 'enable_cg_exception':
            return 'Enabling replication to the consistency group lun_test_cg_source_12 failed with error '
        elif response_type == 'disable_cg_exception':
            return 'Disabling replication to the consistency group lun_test_cg_source_12 failed with error '

    @staticmethod
    def get_remote_system_conn_response():
        conn = MockConsistenyGroupApi.get_cg_replication_dependent_response("remote_system")[0]
        conn.get_pool = MagicMock(return_value=MockConsistenyGroupApi.get_cg_replication_dependent_response('remote_system_pool_object'))
        return conn
