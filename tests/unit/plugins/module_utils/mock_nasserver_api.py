# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of NASServer module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockNASServerApi:
    @staticmethod
    def get_nas_server_response():
        return ({"access_policy": "AccessPolicyEnum.NATIVE",
                 "cifs_notify_on_change_dir_depth": 512,
                 "data_reduction_percent": 0,
                 "data_reduction_ratio": 1.0,
                 "data_reduction_size_saved": 0,
                 "description": "",
                 "existed": True,
                 "size_total": 5,
                 "id": "nas0",
                 "name": "nas0",
                 "replication_type": "Remote"})

    @staticmethod
    def get_replication_params(is_valid=True):
        rpo = 60
        if not is_valid:
            rpo = 2
            return {'replication_params': {
                    'replication_name': None,
                    'new_replication_name': None,
                    'replication_type': 'local',
                    'replication_mode': 'asynchronous',
                    'rpo': rpo,
                    'remote_system': None,
                    'destination_nas_server_name': None,
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
                    'destination_nas_server_name': None,
                    'destination_pool_name': 'pool_test_name_1',
                    'destination_pool_id': None},
                    'replication_state': 'enable',
                    'state': 'present'
                    }
