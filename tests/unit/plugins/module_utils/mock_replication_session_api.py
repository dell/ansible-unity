# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Replication session module on Unity"""

from __future__ import (absolute_import, division, print_function)
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject

__metaclass__ = type


class MockReplicationSessionApi:
    MODULE_ARGS = {
        'session_id': None,
        'session_name': None,
        'pause': None,
        'failback': None,
        'sync': None,
        'failover_with_sync': None,
        'force_full_copy': None,
        'force': None,
        'state': 'present'
    }

    @staticmethod
    def get_replication_session_details(status="ACTIVE"):
        return {
            "current_transfer_est_remain_time": 0,
            "daily_snap_replication_policy": None,
            "dst_resource_id": "nas_8",
            "dst_spa_interface": {
                "UnityRemoteInterface": {
                    "hash": 8771253398547,
                    "id": "APM00213404195:if_181"
                }
            },
            "dst_status": "ReplicationSessionStatusEnum.OK",
            "existed": True,
            "hash": 8771259012271,
            "health": {
                "UnityHealth": {
                    "hash": 8771253424168
                }
            },
            "hourly_snap_replication_policy": None,
            "id": "103079215114_APM00213404195_0000_103079215274_APM00213404194_0000",
            "last_sync_time": "2023-04-18 10:35:25+00:00",
            "local_role": "ReplicationSessionReplicationRoleEnum.DESTINATION",
            "max_time_out_of_sync": 0,
            "members": None,
            "name": "rep_session",
            "network_status": "ReplicationSessionNetworkStatusEnum.OK",
            "remote_system": {
                "UnityRemoteSystem": {
                    "hash": 8771253380142
                }
            },
            "replication_resource_type": "ReplicationEndpointResourceTypeEnum.NASSERVER",
            "src_resource_id": "nas_213",
            "src_spa_interface": {
                "UnityRemoteInterface": {
                    "hash": 8771253475010,
                    "id": "APM00213404194:if_195"
                }
            },
            "src_spb_interface": {
                "UnityRemoteInterface": {
                    "hash": 8771253374169,
                    "id": "APM00213404194:if_194"
                }
            },
            "src_status": "ReplicationSessionStatusEnum.OK",
            "status": Status(status),
            "sync_progress": 0,
            "sync_state": "ReplicationSessionSyncStateEnum.IN_SYNC"
        }


class Status:
    name = "ACTIVE"

    def __init__(self, status):
        self.name = status


class MockReplicationSessionObject(MockSDKObject):
    pause_session = False
    resume_session = False
    failover_session = False
    failback_session = False
    sync_session = False
    delete_session = False

    def pause(self):
        self.pause_session = True

    def resume(self, force_full_copy=None):
        self.resume_session = True

    def failover(self, sync=None, force=None):
        self.failover_session = True

    def failback(self, force_full_copy=None):
        self.failback_session = True

    def sync(self):
        self.sync_session = True

    def delete(self):
        self.delete_session = True
