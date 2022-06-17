# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http: //www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of host module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject


class MockHostApi:
    HOST_MODULE_ARGS = {
        'unispherehost': '**.***.**.***',
        'port': '123',
        'host_id': None,
        'host_name': None,
        'host_os': None,
        'description': None,
        'initiators': None,
        'initiator_state': None,
        'new_host_name': None,
        'network_address': None,
        'network_address_state': None,
        'state': None
    }

    IP_ADDRESS_MOCK_VALUE = '***.***.*.*'
    IQN_INITIATOR_MOCK_VALUE = 'iqn.1111-11.com.vmware: host_name_1-111111f'

    @staticmethod
    def get_host_count_response():
        return [{"auto_manage_type": "HostManageEnum.OTHERS", "description": "", "existed": True,
                 "fc_host_initiators": {"UnityHostInitiatorList": [{"UnityHostInitiator": {}}]}, "health":
                {"UnityHealth": {}}, "host_ip_ports": {"UnityHostIpPortList": [{"UnityHostIpPort": {}},
                 {"UnityHostIpPort": {}}]}, "host_pushed_uuid": "1-1-1-1-1",
                 "id": "Host_id_1", "iscsi_host_initiators": {"UnityHostInitiatorList": [{"UnityHostInitiator": {}}]},
                 "name": "host_name_1", "os_type": "XXXXXXXX", "type": "HostTypeEnum.HOST_AUTO"}]

    @staticmethod
    def get_host_initiators_list():
        return ['1:1:1:1:1:1:1:1:1', MockHostApi.IQN_INITIATOR_MOCK_VALUE]

    @staticmethod
    def get_host_details_response(response_type):
        if response_type == 'api':
            return {'auto_manage_type': 'HostManageEnum.OTHERS', 'datastores': None, 'description': '',
                    'fc_host_initiators': [MockSDKObject({'chap_user_name': None,
                                                          'health': {'UnityHealth': {}}, 'id': 'HostInitiator_fc_1',
                                                          'initiator_id': '1:1:1:1:1:1:1:1:1',
                                                          'initiator_source_type': 'HostInitiatorSourceTypeEnum.OPEN_NATIVE', 'is_bound': None,
                                                          'is_chap_secret_enabled': False,
                                                          'is_ignored': False, 'iscsi_type': None,
                                                          'node_wwn': '11:12:13:14:**:**:**:**',
                                                          'parent_host': {'UnityHost': {'id': 'Host_id_1'}},
                                                          'paths': [MockSDKObject({'id': 'HostInitiator_mock_6', 'is_logged_in': True}),
                                                                    MockSDKObject({'id': 'HostInitiator_mock_5', 'is_logged_in': True}),
                                                                    MockSDKObject({'id': 'HostInitiator_mock_4', 'is_logged_in': True}),
                                                                    MockSDKObject({'id': 'HostInitiator_mock_3', 'is_logged_in': True})],
                                                          'port_wwn': '10:10:10:10:10:10:10:10:10', 'source_type': None,
                                                          'type': 'HostInitiatorTypeEnum.FC', 'existed': True})],
                    'host_container': None, 'host_ip_ports': [MockSDKObject({'address': MockHostApi.IP_ADDRESS_MOCK_VALUE,
                                                                             'host': None, 'id': 'HostNetworkAddress_1',
                                                                             'is_ignored': None, 'name': None, 'netmask': None, 'type': None,
                                                                             'v6_prefix_length': None, 'existed': True}),
                                                              MockSDKObject({'address': 'host_name_1', 'host': None, 'id': 'HostNetworkAddress_2',
                                                                             'is_ignored': None, 'name': None, 'netmask': None, 'type': None,
                                                                             'v6_prefix_length': None, 'existed': True})],
                    'host_luns': MockSDKObject({'lun':
                                                [MockSDKObject({'hlu': 1, 'host': None, 'id': 'host_a', 'name': 'host_name_a', 'is_read_only': None,
                                                                'lun': {'UnityLun': {}}, 'snap': None, 'type': None, 'existed': True}),
                                                 MockSDKObject({'hlu': 0, 'host': None, 'id': 'host_b', 'name': 'host_name_b', 'is_read_only': None,
                                                               'lun': {'UnityLun': {}}, 'snap': None, 'type': None, 'existed': True})]}),
                    'host_polled_uuid': None, 'host_pushed_uuid': '1-1-1-1-1',
                    'host_uuid': None, 'host_v_vol_datastore': None, 'id': 'Host_id_1',
                    'iscsi_host_initiators': [MockSDKObject({'chap_user_name': None, 'health': {'UnityHealth': {}}, 'id': 'HostInitiator_iscsi_1',
                                                             'initiator_id': MockHostApi.IQN_INITIATOR_MOCK_VALUE,
                                                             'initiator_source_type': 'HostInitiatorSourceTypeEnum.OPEN_NATIVE', 'is_bound': True,
                                                             'is_chap_secret_enabled': False, 'is_ignored': False,
                                                             'iscsi_type': 'HostInitiatorIscsiTypeEnum.SOFTWARE', 'node_wwn': None,
                                                             'parent_host': {'UnityHost': {'id': 'Host_id_1'}},
                                                             'paths': [MockSDKObject({'id': 'HostInitiator_mock_1', 'is_logged_in': True}),
                                                                       MockSDKObject({'id': 'HostInitiator_mock_2', 'is_logged_in': True})],
                                                             'port_wwn': None, 'source_type': None, 'type': 'HostInitiatorTypeEnum.ISCSI',
                                                             'existed': True})],
                    'last_poll_time': None, 'name': 'host_name_1',
                    'os_type': 'XXXXXXXX', 'registration_type': None, 'storage_resources': None, 'tenant': None,
                    'type': 'HostTypeEnum.HOST_AUTO',
                    'vms': None, 'existed': True, 'health': {'UnityHealth': {}}}
        elif response_type == 'module':
            return {'changed': False,
                    'host_details': {'auto_manage_type': 'HostManageEnum.OTHERS', 'datastores': None, 'description': '',
                                     'fc_host_initiators': [{'id': 'HostInitiator_fc_1',
                                                             'name': '1:1:1:1:1:1:1:1:1',
                                                             'paths': [{'id': 'HostInitiator_mock_6',
                                                                        'is_logged_in': True},
                                                                       {'id': 'HostInitiator_mock_5',
                                                                        'is_logged_in': True},
                                                                       {'id': 'HostInitiator_mock_4',
                                                                        'is_logged_in': True},
                                                                       {'id': 'HostInitiator_mock_3',
                                                                        'is_logged_in': True}]}],
                                     'health': {'UnityHealth': {}},
                                     'host_container': None,
                                     'host_luns': [{'id': "host_a", 'name': 'host_name_a'}, {'id': 'host_b', 'name': 'host_name_b'}],
                                     'host_polled_uuid': None, 'host_pushed_uuid': '1-1-1-1-1',
                                     'host_uuid': None, 'host_v_vol_datastore': None, 'id': 'Host_id_1',
                                     'iscsi_host_initiators': [{'id': 'HostInitiator_iscsi_1',
                                                                'name': MockHostApi.IQN_INITIATOR_MOCK_VALUE,
                                                                'paths': [{'id': 'HostInitiator_mock_1',
                                                                           'is_logged_in': True},
                                                                          {'id': 'HostInitiator_mock_2',
                                                                           'is_logged_in': True}]}],
                                     'last_poll_time': None, 'name': 'host_name_1', 'os_type': 'XXXXXXXX',
                                     'registration_type': None, 'storage_resources': None, 'tenant': None,
                                     'type': 'HostTypeEnum.HOST_AUTO', 'vms': None, 'existed': True,
                                     'network_addresses': [MockHostApi.IP_ADDRESS_MOCK_VALUE, 'host_name_1']}}
        elif response_type == 'error':
            return "Incorrect username or password provided."

    @staticmethod
    def get_host_details_after_network_address_addition(response_type):
        if response_type == 'api':
            host_object = MockHostApi.get_host_details_response('api')
            host_object['host_ip_ports'].append(MockSDKObject({'address': 'net_add_1', 'host': None, 'id': 'HostNetworkAddress_3',
                                                               'is_ignored': None, 'name': None, 'netmask': None, 'type': None,
                                                               'v6_prefix_length': None, 'existed': True}))
            return host_object
        elif response_type == 'module':
            host_module_response = MockHostApi.get_host_details_response('module')
            host_module_response['host_details']['network_addresses'].append('net_add_1')
            host_module_response['changed'] = True
            return host_module_response
        elif response_type == 'invalid_address':
            return 'Please enter valid IPV4 address or host name for network address'

    @staticmethod
    def get_host_details_after_network_address_removal(response_type):
        if response_type == 'api':
            host_object = MockHostApi.get_host_details_response('api')
            host_object['host_ip_ports'] = [MockSDKObject({'address': MockHostApi.IP_ADDRESS_MOCK_VALUE, 'host': None, 'id': 'HostNetworkAddress_1',
                                                           'is_ignored': None, 'name': None, 'netmask': None, 'type': None,
                                                           'v6_prefix_length': None, 'existed': True})]
            return host_object
        elif response_type == 'module':
            host_module_response = MockHostApi.get_host_details_response('module')
            host_module_response['host_details']['network_addresses'].remove('host_name_1')
            host_module_response['changed'] = True
            return host_module_response
        elif response_type == 'invalid_IPV4':
            return 'Please enter valid IPV4 address for network address'
