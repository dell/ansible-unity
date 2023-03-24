# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of nfs module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
from mock.mock import MagicMock


class MockNfsApi:
    NFS_MODULE_ARGS = {
        'unispherehost': '**.***.**.***',
        'port': '123',
        'description': None,
        'anonymous_uid': None,
        'anonymous_gid': None,
        'min_security': None,
        'default_access': None,
        'nas_server_id': None,
        'nas_server_name': None,
        'nfs_export_id': None,
        'nfs_export_name': None,
        'snapshot_name': None,
        'snapshot_id': None,
        'filesystem_name': None,
        'filesystem_id': None,
        'host_state': None,
        'adv_host_mgmt_enabled': None,
        'no_access_hosts': None,
        'read_only_hosts': None,
        'read_only_root_hosts': None,
        'read_write_hosts': None,
        'read_write_root_hosts': None,
        'path': None,
        'state': None
    }

    DUMMY_DOMAIN_VALUE = "google.com"
    DUMMY_SUBNET_VALUE = "**.***.2.2/10"

    FILESYSTEM_OBJECT = MockSDKObject({"access_policy": "AccessPolicyEnum.UNIX", "cifs_notify_on_change_dir_depth": 512,
                                       "data_reduction_percent": 0, "data_reduction_ratio": 1.0, "data_reduction_size_saved": 0,
                                       "description": "", "existed": True,
                                       "folder_rename_policy": "FSRenamePolicyEnum.SMB_RENAME_FORBIDDEN",
                                       "format": "FSFormatEnum.UFS64", "host_io_size": "HostIOSizeEnum.GENERAL_16K",
                                       "id": "fs_id_1", "is_advanced_dedup_enabled": False, "is_cifs_notify_on_access_enabled": False,
                                       "is_cifs_notify_on_write_enabled": False, "is_cifs_op_locks_enabled": True,
                                       "is_cifs_sync_writes_enabled": False, "is_data_reduction_enabled": False, "is_read_only": False,
                                       "is_smbca": False, "is_thin_enabled": True, "locking_policy": "FSLockingPolicyEnum.MANDATORY",
                                       "min_size_allocated": 0, "name": "fs_dummy_name", "nas_server": {"id": "nas_id_1"},
                                       "nfs_share": [{"id": "NFSShare_id_1"}], "pool": {"id": "pool_id_1"},
                                       "pool_full_policy": "ResourcePoolFullPolicyEnum.FAIL_WRITES", "snap_count": 0, "snaps_size": 0,
                                       "snaps_size_allocated": 0, "storage_resource": {"id": "stg_id_1"},
                                       "supported_protocols": "FSSupportedProtocolEnum.NFS",
                                       "tiering_policy": "TieringPolicyEnum.AUTOTIER_HIGH",
                                       "type": "FilesystemTypeEnum.FILESYSTEM"})

    NFS_SHARE_OBJECT = MockSDKObject({"anonymous_gid": 4294967294, "anonymous_uid": 4294967294,
                                      "default_access": "NFSShareDefaultAccessEnum.NO_ACCESS", "description": "", "existed": True,
                                      "export_option": 1, "export_paths": ["**.***.**.**:/nfsshare_dummy_name"],
                                      "filesystem": MockSDKObject({"id": "fs_id_1", "name": "fs_name1", "nas_server": "not_none"}),
                                      "id": "NFSShare_id_1",
                                      "min_security": "NFSShareSecurityEnum.SYS",
                                      "modification_time": "2022-04-24 17:07:57.749000+00:00",
                                      "name": "nfsshare_dummy_name",
                                      "no_access_hosts": None,
                                      "no_access_hosts_string": None,
                                      "read_only_hosts": None,
                                      "read_only_hosts_string": None,
                                      "read_only_root_access_hosts": None,
                                      "read_only_root_hosts_string": None,
                                      "read_write_hosts": None,
                                      "read_write_hosts_string": None,
                                      "read_write_root_hosts_string": None,
                                      "root_access_hosts": None,
                                      "path": "/",
                                      "role": "NFSShareRoleEnum.PRODUCTION",
                                      "type": "NFSTypeEnum.NFS_SHARE"})

    NFS_SHARE_DISPLAY_ATTR = {'anonymous_gid': 4294967294, 'anonymous_uid': 4294967294, 'creation_time': '2022-03-09 15:05:34.720000+00:00',
                              'default_access': 'NFSShareDefaultAccessEnum.NO_ACCESS', 'description': '', 'export_option': 1,
                              'export_paths': ['**.***.**.**:/nfsshare_dummy_name'],
                              'filesystem': {'UnityFileSystem': {'id': 'fs_id_1', 'name': 'fs_name1'}}, 'host_accesses': None,
                              'id': 'NFSShare_id_1', 'is_read_only': None, 'min_security': 'NFSShareSecurityEnum.SYS',
                              'modification_time': '2022-04-24 17:07:57.749000+00:00', 'name': 'nfsshare_dummy_name',
                              'nfs_owner_username': None, 'no_access_hosts': None,
                              'no_access_hosts_string': None,
                              'path': '/', 'read_only_hosts': None, 'read_only_hosts_string': '', 'read_only_root_access_hosts': None,
                              'read_only_root_hosts_string': '', 'read_write_hosts': None, 'read_write_hosts_string': '',
                              'read_write_root_hosts_string': '', 'role': 'NFSShareRoleEnum.PRODUCTION', 'root_access_hosts': None,
                              'snap': None, 'type': 'NFSTypeEnum.NFS_SHARE', 'existed': True,
                              'nas_server': {'UnityNasServer': {'id': 'nas_id_1', 'name': 'lglad068'}}}

    @staticmethod
    def get_nfs_share_object_on_host_access(action, advhostmgmt):
        if advhostmgmt:
            if action == 'add':
                nfs_share_object = MockNfsApi.NFS_SHARE_OBJECT
                return nfs_share_object
            elif action == 'remove':
                nfs_share_object = MockNfsApi.NFS_SHARE_OBJECT
                nfs_share_object.no_access_hosts = {
                    'UnityHostList': [
                        {
                            'UnityHost': {
                                'id': 'Host_1389'
                            }
                        },
                        {
                            'UnityHost': {
                                'id': 'Host_1330'
                            }
                        }
                    ]
                }
                return nfs_share_object
        else:
            if action == 'add':
                nfs_share_display_attr = MockNfsApi.NFS_SHARE_OBJECT
                nfs_share_display_attr.read_only_root_hosts_string = ''
                return nfs_share_display_attr
            elif action == 'remove':
                nfs_share_display_attr = MockNfsApi.NFS_SHARE_OBJECT
                nfs_share_display_attr.read_only_root_hosts_string = '*.google.com,**.***.0.0/255.***.*.*'
                return nfs_share_display_attr

    @staticmethod
    def get_nfs_share_display_attr_on_host_access(action, advhostmgmt):
        if advhostmgmt:
            if action == 'add':
                nfs_share_display_attr = MockNfsApi.NFS_SHARE_DISPLAY_ATTR
                nfs_share_display_attr['no_access_hosts'] = {
                    'UnityHostList': [
                        {
                            'UnityHost': {
                                'id': 'Host_1389'
                            }
                        },
                        {
                            'UnityHost': {
                                'id': 'Host_1330'
                            }
                        }
                    ]
                }
                return nfs_share_display_attr
            elif action == 'remove':
                nfs_share_display_attr = MockNfsApi.NFS_SHARE_DISPLAY_ATTR
                nfs_share_display_attr['no_access_hosts'] = None
                return nfs_share_display_attr
        else:
            if action == 'add':
                nfs_share_display_attr = MockNfsApi.NFS_SHARE_DISPLAY_ATTR
                nfs_share_display_attr['read_only_root_hosts_string'] = '*.google.com,**.***.0.0/255.***.*.*'
                return nfs_share_display_attr
            elif action == 'remove':
                nfs_share_display_attr = MockNfsApi.NFS_SHARE_DISPLAY_ATTR
                nfs_share_display_attr['read_only_root_hosts_string'] = ''
                return nfs_share_display_attr

    @staticmethod
    def get_host_obj(id):
        if id == 1:
            host_1 = MagicMock()
            host_1.id = 'Host_1389'
            host_1.name = 'host_1'
            return host_1
        elif id == 2:
            host_2 = MagicMock()
            host_2.id = 'Host_1330'
            host_2.name = 'host_2'
            return host_2

    @staticmethod
    def host_access_negative_response(response_type):
        if response_type == 'subnet_validation':
            return "Subnet should be in format 'IP address/netmask' or 'IP address/prefix length'"
        elif response_type == 'advhostmngmnt_field_validation':
            return "'host_state' and 'adv_host_mgmt_enabled' is required along with: read_only_root_hosts"
        elif response_type == 'modify_exception':
            return 'Failed to modify nfs error: '
