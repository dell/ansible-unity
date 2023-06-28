# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of CIFS server module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockCIFSServerApi:
    CIFS_SERVER_MODULE_ARGS = {
        'nas_server_id': None,
        'nas_server_name': None,
        'netbios_name': None,
        'workgroup': None,
        'local_password': None,
        'domain': None,
        'domain_username': None,
        'domain_password': None,
        'cifs_server_id': None,
        'cifs_server_name': None,
        'interfaces': None,
        'unjoin_cifs_server_account': None,
        'state': None
    }

    @staticmethod
    def get_cifs_server_details_method_response():
        return {
            "description": None,
            "domain": "xxx.xxx.xxx.xxx",
            "existed": True,
            "file_interfaces": {
                "UnityFileInterfaceList": [
                    {
                        "UnityFileInterface": {
                            "hash": 8791477905949,
                            "id": "if_43"
                        }
                    }
                ]
            },
            "hash": 8791478461637,
            "health": {
                "UnityHealth": {
                    "hash": 8791478461623
                }
            },
            "id": "cifs_59",
            "is_standalone": False,
            "last_used_organizational_unit": "ou=Computers,ou=EMC NAS servers",
            "name": "test_cifs_server",
            "nas_server": {
                "UnityNasServer": {
                    "hash": 8791478461595,
                    "id": "nas_18"
                }
            },
            "netbios_name": "TEST_CIFS_SERVER",
            "smb_multi_channel_supported": True,
            "smb_protocol_versions": [
                "1.0",
                "2.0",
                "2.1",
                "3.0"
            ],
            "smbca_supported": True,
            "workgroup": None
        }

    @staticmethod
    def get_cifs_server_details_method_netbios_response():
        return {
            "UnityCifsServerList": [{
                "UnityCifsServer": {
                    "existed": True,
                    "file_interfaces": {
                        "UnityFileInterfaceList": [{
                            "UnityFileInterface": {
                                "hash": -9223363293222387298,
                                "id": "if_43"
                            }
                        }]
                    },
                    "hash": 8743632213638,
                    "health": {
                        "UnityHealth": {
                            "hash": -9223363293222562209
                        }
                    },
                    "id": "cifs_60",
                    "is_standalone": True,
                    "nas_server": {
                        "UnityNasServer": {
                            "hash": -9223363293221242245,
                            "id": "nas_18"
                        }
                    },
                    "netbios_name": "ANSIBLE_CIFS",
                    "smb_multi_channel_supported": True,
                    "smb_protocol_versions": ["1.0", "2.0", "2.1", "3.0"],
                    "smbca_supported": True,
                    "workgroup": "ANSIBLE"
                }
            }]
        }

    @staticmethod
    def create_cifs_server_without_nas():
        return "Please provide nas server id/name to create CIFS server."

    @staticmethod
    def invalid_credentials():
        return "Incorrect username or password provided."

    @staticmethod
    def modify_error_msg():
        return "Modification is not supported through Ansible module"

    @staticmethod
    def get_nas_server_details():
        return {
            "UnityNasServer": {
                "cifs_server": {
                    "UnityCifsServerList": [{
                        "UnityCifsServer": {
                            "hash": 8734183189936,
                            "id": "cifs_60"
                        }
                    }]
                },
                "current_sp": {
                    "UnityStorageProcessor": {
                        "hash": 8734188780762,
                        "id": "spa"
                    }
                },
                "current_unix_directory_service": "NasServerUnixDirectoryServiceEnum.NONE",
                "existed": True,
                "file_dns_server": {
                    "UnityFileDnsServer": {
                        "hash": 8734183189782,
                        "id": "dns_11"
                    }
                },
                "file_interface": {
                    "UnityFileInterfaceList": [{
                        "UnityFileInterface": {
                            "hash": -9223363302671584431,
                            "id": "if_43"
                        }
                    }]
                },
                "hash": -9223363302671053452,
                "health": {
                    "UnityHealth": {
                        "hash": 8734182402245
                    }
                },
                "home_sp": {
                    "UnityStorageProcessor": {
                        "hash": -9223363302671594510,
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
                        "hash": -9223363302672128291,
                        "id": "pool_7"
                    }
                },
                "preferred_interface_settings": {
                    "UnityPreferredInterfaceSettings": {
                        "hash": -9223363302671585904,
                        "id": "preferred_if_16"
                    }
                },
                "replication_type": "ReplicationTypeEnum.NONE",
                "size_allocated": 2952790016,
                "virus_checker": {
                    "UnityVirusChecker": {
                        "hash": 8734183191465,
                        "id": "cava_18"
                    }
                }
            }
        }
