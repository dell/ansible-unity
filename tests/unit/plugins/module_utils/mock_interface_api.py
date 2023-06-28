# Copyright:  (c) 2022,  Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of interface on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
from copy import deepcopy


class MockInterfaceApi:
    INTERFACE_MODULE_ARGS = {
        'unispherehost': '**.***.**.***',
        'port': '123',
        'nas_server_id': None,
        'nas_server_name': None,
        'ethernet_port_name': None,
        'ethernet_port_id': None,
        'role': None,
        'interface_ip': None,
        'netmask': None,
        'prefix_length': None,
        'gateway': None,
        'vlan_id': None,
        'state': None
    }
    ETHERNET_PORT_NAME = "Card Ethernet Port"
    NETMASK_DUMMY = "255.xx.xx.xx"
    GATEWAY_DUMMY = "10.***.**.1"
    INTERFACE_DUMMY = "10.***.**.**"

    NAS_SERVER_OBJECT = \
        MockSDKObject({'allow_unmapped_user': None, 'cifs_server': {'UnityCifsServerList': [{'UnityCifsServer': {'id': 'cifs_id_0'}}]},
                       'current_sp': {'UnityStorageProcessor': {'id': 'abc'}},
                       'current_unix_directory_service': 'NasServerUnixDirectoryServiceEnum.NIS', 'default_unix_user': None,
                       'default_windows_user': None, 'file_dns_server': {'UnityFileDnsServer': {'id': 'dns_id_0'}},
                       'file_interface': {'UnityFileInterfaceList': [{'UnityFileInterface': {'id': 'file_interface_id_0'}}]},
                       'filesystems': {'UnityFileSystemList': [{'UnityFileSystem': {'id': 'fs_id_0'}}]},
                       'home_sp': {'UnityStorageProcessor': {'id': 'abd'}},
                       'id': 'nas_id_00', 'is_backup_only': False, 'is_multi_protocol_enabled': False,
                       'is_packet_reflect_enabled': False, 'is_replication_destination': False,
                       'is_replication_enabled': True, 'is_windows_to_unix_username_mapping_enabled': None,
                       'name': 'dummy_nas', 'pool': {'UnityPool': {'id': 'pool_id_0'}},
                       'preferred_interface_settings': {'UnityPreferredInterfaceSettings': {'id': 'preferred_interface_0'}},
                       'replication_type': 'ReplicationTypeEnum.MIXED',
                       'tenant': None, 'virus_checker': {'UnityVirusChecker': {'id': 'cava_id_0'}},
                       'existed': True})

    INTERFACE_OBJECT = \
        MockSDKObject({"existed": True,
                       "gateway": GATEWAY_DUMMY,
                       "id": "file_interface_id_0",
                       "ip_address": INTERFACE_DUMMY,
                       "ip_port": {"UnityIpPort": {"id": "ethernet_port_id_0"}},
                       "ip_protocol_version": "IpProtocolVersionEnum.IPv4",
                       "is_disabled": False, "is_preferred": True,
                       "mac_address": "AA:AA:AA:**:**:**",
                       "name": "dummy_if_name",
                       "nas_server": {"UnityNasServer": {"id": "nas_id_00"}},
                       "netmask": NETMASK_DUMMY,
                       "role": "FileInterfaceRoleEnum.BACKUP",
                       "vlan_id": 324})

    FILE_INTERFACE_ROLE_ENUM_DUMMY = {
        'PRODUCTION': (0, 'Production'),
        'BACKUP': (1, 'Backup')
    }

    @staticmethod
    def get_nas_without_interface():
        nas_object = deepcopy(MockInterfaceApi.NAS_SERVER_OBJECT)
        nas_object.file_interface['UnityFileInterfaceList'] = []
        return nas_object

    @staticmethod
    def get_nas_server_obj_existed_false():
        nas_object = deepcopy(MockInterfaceApi.NAS_SERVER_OBJECT)
        nas_object.existed = False
        return nas_object

    @staticmethod
    def get_interface_exception_response(response_type):
        if response_type == 'nas_server_id_exception':
            return "Failed to get details of NAS server: dummy_nas with error: "
        elif response_type == 'interface_exception':
            return "Getting Interface details failed with error "
        elif response_type == 'add_interface_exception':
            return "Failed to add interface to NAS Server with error: "
        elif response_type == 'delete_interface_exception':
            return "Failed to delete interface with error: "

    @staticmethod
    def get_interface_error_response(response_type):
        if response_type == 'invalid_ethernet_port_name':
            return "Please provide valid value for: ethernet_port_name"
        elif response_type == 'invalid_vlan_id':
            return "vlan_id should be in the range of 3 to 4094"
        elif response_type == 'invalid_interface_ip':
            return 'The value for interface ip is invalid'
        elif response_type == 'invalid_gateway':
            return "The value for gateway is invalid"
        elif response_type == 'invalid_netmask':
            return 'Invalid IPV4 address specified for netmask'
        elif response_type == 'modify_failure':
            return "Modification of Interfaces for NAS server is not supported through Ansible module"
        elif response_type == 'no_role':
            return "Role is a mandatory parameter for adding interface to NAS Server."
        elif response_type == 'no_ethernet':
            return "ethernet_port_name/ethernet_port_id is mandatory parameter for adding interface to NAS Server."

    @staticmethod
    def get_nas_server_obj_errors(response_type):
        if response_type == 'existed_false':
            return "NAS server with id nas_id_00 does not exist"
        elif response_type == 'exception':
            return "Failed to get details of NAS server with error: "
