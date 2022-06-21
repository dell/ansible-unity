# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of FileSystem module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject


class MockFileSystemApi:
    @staticmethod
    def get_file_system_response():
        filesystem_response = {"UnityFileSystem": {
            "access_policy": "AccessPolicyEnum.NATIVE",
            "cifs_notify_on_change_dir_depth": 512,
            "data_reduction_percent": 0,
            "data_reduction_ratio": 1.0,
            "data_reduction_size_saved": 0,
            "description": "",
            "existed": True,
            "size_total": 5,
            "folder_rename_policy": "FSRenamePolicyEnum.SMB_RENAME_FORBIDDEN",
            "id": "fs_208",
            "replication_type": "Remote"}}
        filesystem_response['storage_resource'] = MockSDKObject({'replication_type': None})
        return filesystem_response

    @staticmethod
    def get_replication_params(is_valid=True):
        rpo = 60
        if not is_valid:
            rpo = 2
            return {'replication_params': {
                    'replication_name': None,
                    'new_replication_name': None,
                    'replication_mode': 'asynchronous',
                    'replication_type': 'local',
                    'rpo': rpo,
                    'remote_system': None,
                    'destination_pool_name': 'pool_test_name_1',
                    'destination_pool_id': None},
                    'replication_state': 'enable',
                    'state': 'present'
                    }
        else:
            return {'replication_params': {
                    'replication_name': None,
                    'replication_mode': 'asynchronous',
                    'new_replication_name': None,
                    'replication_type': 'remote',
                    'rpo': rpo,
                    'remote_system': {
                        'remote_system_host': '1.1.1.1',
                        'remote_system_verifycert': False,
                        'remote_system_username': 'username',
                        'remote_system_password': 'password',
                        'remote_system_port': 1
                    },
                    'destination_pool_name': 'pool_test_name_1',
                    'destination_pool_id': None},
                    'replication_state': 'enable',
                    'state': 'present'
                    }
