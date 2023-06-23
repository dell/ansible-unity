# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of NFS server module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject


class MockNFSServerApi:
    NFS_SERVER_MODULE_ARGS = {
        'nas_server_id': None,
        'nas_server_name': None,
        'host_name': None,
        'is_secure_enabled': None,
        'kerberos_domain_controller_type': None,
        'kerberos_domain_controller_username': None,
        'kerberos_domain_controller_password': None,
        'is_extended_credentials_enabled': None,
        'nfs_v4_enabled': None,
        'nfs_server_id': None,
        'interfaces': None,
        'remove_spn_from_kerberos': None,
        'state': None
    }

    NAS_SERVER_OBJ = MockSDKObject({"id": "nas_10"})

    @staticmethod
    def get_nfs_server_details_method_response():
        return {
            "credentials_cache_ttl": "0:15:00",
            "existed": True,
            "file_interfaces": {
                "UnityFileInterfaceList": [{
                    "UnityFileInterface": {
                        "hash": 1111111111111,
                        "id": "if_3"
                    }
                }]
            },
            "hash": 1111111111111,
            "id": "nfs_95",
            "is_extended_credentials_enabled": False,
            "is_secure_enabled": False,
            "nas_server": MockNFSServerApi.NAS_SERVER_OBJ,
            "nfs_v4_enabled": True,
            'servicee_principal_name': None
        }

    @staticmethod
    def get_nfs_server_details():
        return [MockSDKObject({
            "credentials_cache_ttl": "0:15:00",
            "existed": True,
            "file_interfaces": {
                "UnityFileInterfaceList": [{
                    "UnityFileInterface": {
                        "hash": 1111111111111,
                        "id": "if_3"
                    }
                }]
            },
            "hash": 1111111111111,
            "id": "nfs_95",
            "is_extended_credentials_enabled": False,
            "is_secure_enabled": False,
            "nas_server": MockNFSServerApi.NAS_SERVER_OBJ,
            "nfs_v4_enabled": True,
            'servicee_principal_name': None})]

    @staticmethod
    def validate_params_exception():
        return "Please provide valid value for:"

    @staticmethod
    def create_nfs_server_without_nas_server_id():
        return "Please provide nas server id/name to create NFS server."

    @staticmethod
    def get_nas_server_id_api_exception():
        return "Failed to get details of NAS server:"

    @staticmethod
    def create_nfs_server_without_is_secure_enabled():
        return "For create NFS Server nfs_v4_enabled and is_secure_enabled should be true."

    @staticmethod
    def create_nfs_server_with_api_exception():
        return "Failed to create NFS server with on NAS Server"

    @staticmethod
    def get_nfs_server_api_exception():
        return "Incorrect username or password provided."

    @staticmethod
    def get_nfs_server_api_exception_1():
        return "Failed to get details of NFS Server with error"

    @staticmethod
    def delete_exception():
        return "Failed to delete NFS server:"

    @staticmethod
    def modify_error_msg():
        return "Modification of NFS Server parameters is not supported through Ansible module"

    @staticmethod
    def get_nas_server_details():
        return {
            "UnityNasServer": {
                "cifs_server": {
                    "UnityCifsServerList": [{
                        "UnityCifsServer": {
                            "hash": 1111111111111,
                            "id": "cifs_60"
                        }
                    }]
                },
                "current_sp": {
                    "UnityStorageProcessor": {
                        "hash": 1111111111111,
                        "id": "spa"
                    }
                },
                "current_unix_directory_service": "NasServerUnixDirectoryServiceEnum.NONE",
                "existed": True,
                "file_dns_server": {
                    "UnityFileDnsServer": {
                        "hash": 1111111111111,
                        "id": "dns_11"
                    }
                },
                "file_interface": {
                    "UnityFileInterfaceList": [{
                        "UnityFileInterface": {
                            "hash": -1111111111111,
                            "id": "if_43"
                        }
                    }]
                },
                "hash": -1111111111111,
                "health": {
                    "UnityHealth": {
                        "hash": 1111111111111
                    }
                },
                "home_sp": {
                    "UnityStorageProcessor": {
                        "hash": -1111111111111,
                        "id": "spa"
                    }
                },
                "id": "nas_18",
                "is_backup_only": False,
                "is_multi_protocol_enabled": False,
                "is_packet_reflect_enabled": False,
                "is_replication_destination": False,
                "is_replication_enabled": False,
                "name": "test_nas1",
                "pool": {
                    "UnityPool": {
                        "hash": -1111111111111,
                        "id": "pool_7"
                    }
                },
                "preferred_interface_settings": {
                    "UnityPreferredInterfaceSettings": {
                        "hash": -1111111111111,
                        "id": "preferred_if_16"
                    }
                },
                "replication_type": "ReplicationTypeEnum.NONE",
                "size_allocated": 1111111111111,
                "virus_checker": {
                    "UnityVirusChecker": {
                        "hash": 1111111111111,
                        "id": "cava_18"
                    }
                }
            }
        }

    @staticmethod
    def get_nas_server_id():
        return MockSDKObject({
            "cifs_server": {
                "UnityCifsServerList": [{
                    "UnityCifsServer": {
                        "hash": 1111111111111,
                        "id": "cifs_34"
                    }
                }]
            },
            "current_sp": {
                "UnityStorageProcessor": {
                    "hash": 1111111111111,
                    "id": "spb"
                }
            },
            "current_unix_directory_service": "NasServerUnixDirectoryServiceEnum.NIS",
            "existed": True,
            "file_dns_server": {
                "UnityFileDnsServer": {
                    "hash": 1111111111111,
                    "id": "dns_12"
                }
            },
            "file_interface": {
                "UnityFileInterfaceList": [{
                    "UnityFileInterface": {
                        "hash": 1111111111111,
                        "id": "if_37"
                    }
                }]
            },
            "hash": 1111111111111,
            "health": {
                "UnityHealth": {
                    "hash": 1111111111111
                }
            },
            "home_sp": {
                "UnityStorageProcessor": {
                    "hash": 1111111111111,
                    "id": "spb"
                }
            },
            "id": "nas_10",
            "is_backup_only": False,
            "is_multi_protocol_enabled": False,
            "is_packet_reflect_enabled": False,
            "is_replication_destination": False,
            "is_replication_enabled": True,
            "name": "dummy_nas",
            "pool": {
                "UnityPool": {
                    "hash": 1111111111111,
                    "id": "pool_7"
                }
            },
            "preferred_interface_settings": {
                "UnityPreferredInterfaceSettings": {
                    "hash": 1111111111111,
                    "id": "preferred_if_10"
                }
            },
            "replication_type": "ReplicationTypeEnum.REMOTE",
            "size_allocated": 1111111111111,
            "virus_checker": {
                "UnityVirusChecker": {
                    "hash": 1111111111111,
                    "id": "cava_10"}}})
