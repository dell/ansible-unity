# Copyright: (c) 2025, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of initiator module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject


class MockInitiatorApi:
    INITIATOR_MODULE_ARGS = {
        'unispherehost': '**.***.**.***',
        'port': '123',
        'host_name': None,
        'host_id': None,
        'host_os': None,
        'description': None,
        'initiators': None,
        'state': None
    }

    FC_INITIATOR_MOCK_VALUE = '20:00:00:90:FA:13:81:8D:10:00:00:90:FA:13:81:8D'
    IQN_INITIATOR_MOCK_VALUE = 'iqn.1994-05.com.redhat:c38e6e8cfd81'

    @staticmethod
    def get_host_count_response():
        return [{"auto_manage_type": "HostManageEnum.OTHERS", "description": "", "existed": True,
                 "fc_host_initiators": {"UnityHostInitiatorList": [{"UnityHostInitiator": {}}]}, "health":
                {"UnityHealth": {}}, "host_ip_ports": {"UnityHostIpPortList": [{"UnityHostIpPort": {}},
                 {"UnityHostIpPort": {}}]}, "host_pushed_uuid": "1-1-1-1-1",
                 "id": "Host_id_1", "iscsi_host_initiators": {"UnityHostInitiatorList": [{"UnityHostInitiator": {}}]},
                 "name": "host_name_1", "os_type": "Linux", "type": "HostTypeEnum.HOST_MANUAL"}]

    @staticmethod
    def get_host_details_response(response_type):
        if response_type == 'api':
            return {'auto_manage_type': 'HostManageEnum.OTHERS', 'datastores': None, 'description': 'Test host',
                    'fc_host_initiators': [], 'host_container': None, 'host_ip_ports': [],
                    'host_luns': None, 'host_polled_uuid': None, 'host_pushed_uuid': '1-1-1-1-1',
                    'host_uuid': None, 'host_v_vol_datastore': None, 'id': 'Host_253',
                    'iscsi_host_initiators': [], 'last_poll_time': None, 'name': 'ansible-test-host',
                    'os_type': 'Linux', 'registration_type': None, 'storage_resources': None, 'tenant': None,
                    'type': 'HostTypeEnum.HOST_MANUAL', 'vms': None, 'existed': True, 'health': {'UnityHealth': {}}}
        elif response_type == 'module':
            return {'auto_manage_type': 'HostManageEnum.OTHERS', 'description': 'Test host',
                    'id': 'Host_253', 'name': 'ansible-test-host', 'os_type': 'Linux', 'existed': True}
        elif response_type == 'error':
            return "Incorrect username or password provided."
        elif response_type == 'with_methods':
            # Return a mock object with necessary methods
            host_obj = MockSDKObject({'auto_manage_type': 'HostManageEnum.OTHERS', 'datastores': None,
                                     'description': 'Test host', 'fc_host_initiators': [],
                                     'host_container': None, 'host_ip_ports': [], 'host_luns': None,
                                     'host_polled_uuid': None, 'host_pushed_uuid': '1-1-1-1-1',
                                     'host_uuid': None, 'host_v_vol_datastore': None, 'id': 'Host_253',
                                     'iscsi_host_initiators': [], 'last_poll_time': None,
                                     'name': 'ansible-test-host', 'os_type': 'Linux',
                                     'registration_type': None, 'storage_resources': None, 'tenant': None,
                                     'type': 'HostTypeEnum.HOST_MANUAL', 'vms': None, 'existed': True,
                                     'health': {'UnityHealth': {}}})
            host_obj.add_initiator = MagicMock()
            host_obj.delete_initiator = MagicMock()
            return host_obj

    @staticmethod
    def get_host_details_with_initiators(response_type):
        if response_type == 'api':
            host_obj = MockSDKObject({'auto_manage_type': 'HostManageEnum.OTHERS', 'datastores': None,
                                     'description': 'Test host', 'host_container': None, 'host_ip_ports': [],
                                     'host_luns': None, 'host_polled_uuid': None, 'host_pushed_uuid': '1-1-1-1-1',
                                     'host_uuid': None, 'host_v_vol_datastore': None, 'id': 'Host_253',
                                     'last_poll_time': None, 'name': 'ansible-test-host', 'os_type': 'Linux',
                                     'registration_type': None, 'storage_resources': None, 'tenant': None,
                                     'type': 'HostTypeEnum.HOST_MANUAL', 'vms': None, 'existed': True,
                                     'health': {'UnityHealth': {}}})
            
            # Create FC initiators list with proper structure
            fc_initiators_list = MagicMock()
            fc_initiators_list.__len__ = MagicMock(return_value=1)
            fc_initiators_list.initiator_id = [MockInitiatorApi.FC_INITIATOR_MOCK_VALUE]
            host_obj.fc_host_initiators = fc_initiators_list
            
            # Create iSCSI initiators list with proper structure
            iscsi_initiators_list = MagicMock()
            iscsi_initiators_list.__len__ = MagicMock(return_value=1)
            iscsi_initiators_list.initiator_id = [MockInitiatorApi.IQN_INITIATOR_MOCK_VALUE]
            host_obj.iscsi_host_initiators = iscsi_initiators_list
            
            host_obj.add_initiator = MagicMock()
            host_obj.delete_initiator = MagicMock()
            return host_obj
        elif response_type == 'module':
            return {'auto_manage_type': 'HostManageEnum.OTHERS', 'description': 'Test host',
                    'id': 'Host_253', 'name': 'ansible-test-host', 'os_type': 'Linux', 'existed': True}

    @staticmethod
    def get_initiator_details_response(response_type):
        if response_type == 'api':
            initiator = MockSDKObject({'chap_user_name': None, 'health': {'UnityHealth': {}},
                                 'id': 'HostInitiator_1', 'initiator_id': MockInitiatorApi.FC_INITIATOR_MOCK_VALUE,
                                 'initiator_source_type': 'HostInitiatorSourceTypeEnum.OPEN_NATIVE',
                                 'is_bound': None, 'is_chap_secret_enabled': False, 'is_ignored': False,
                                 'iscsi_type': None, 'node_wwn': '11:12:13:14:**:**:**:**',
                                 'parent_host': {'UnityHost': {'id': 'Host_253'}}, 'paths': [],
                                 'port_wwn': '10:10:10:10:10:10:10:10:10', 'source_type': None,
                                 'type': 'HostInitiatorTypeEnum.FC', 'existed': True})
            initiator.delete = MagicMock()
            return initiator
        elif response_type == 'api_iscsi':
            initiator = MockSDKObject({'chap_user_name': None, 'health': {'UnityHealth': {}},
                                 'id': 'HostInitiator_2', 'initiator_id': MockInitiatorApi.IQN_INITIATOR_MOCK_VALUE,
                                 'initiator_source_type': 'HostInitiatorSourceTypeEnum.OPEN_NATIVE',
                                 'is_bound': True, 'is_chap_secret_enabled': False, 'is_ignored': False,
                                 'iscsi_type': 'HostInitiatorIscsiTypeEnum.SOFTWARE', 'node_wwn': None,
                                 'parent_host': {'UnityHost': {'id': 'Host_253'}}, 'paths': [],
                                 'port_wwn': None, 'source_type': None,
                                 'type': 'HostInitiatorTypeEnum.ISCSI', 'existed': True})
            initiator.delete = MagicMock()
            return initiator
        elif response_type == 'api_with_paths':
            initiator = MockSDKObject({'chap_user_name': None, 'health': {'UnityHealth': {}},
                                 'id': 'HostInitiator_1', 'initiator_id': MockInitiatorApi.FC_INITIATOR_MOCK_VALUE,
                                 'initiator_source_type': 'HostInitiatorSourceTypeEnum.OPEN_NATIVE',
                                 'is_bound': None, 'is_chap_secret_enabled': False, 'is_ignored': False,
                                 'iscsi_type': None, 'node_wwn': '11:12:13:14:**:**:**:**',
                                 'parent_host': {'UnityHost': {'id': 'Host_253'}},
                                 'paths': [MockSDKObject({'id': 'HostInitiator_mock_1', 'is_logged_in': True})],
                                 'port_wwn': '10:10:10:10:10:10:10:10:10', 'source_type': None,
                                 'type': 'HostInitiatorTypeEnum.FC', 'existed': True})
            initiator.delete = MagicMock()
            return initiator
        elif response_type == 'none':
            return None

    @staticmethod
    def get_all_initiators_response():
        return {
            'fc_initiators': [
                {
                    'id': 'HostInitiator_1',
                    'initiator_id': MockInitiatorApi.FC_INITIATOR_MOCK_VALUE,
                    'parent_host': 'ansible-test-host'
                }
            ],
            'iscsi_initiators': [
                {
                    'id': 'HostInitiator_2',
                    'initiator_id': MockInitiatorApi.IQN_INITIATOR_MOCK_VALUE,
                    'parent_host': 'ansible-test-host'
                }
            ]
        }

    @staticmethod
    def get_initiator_module_success_response():
        return {
            'changed': True,
            'initiator_details': MockInitiatorApi.get_all_initiators_response(),
            'host_details': MockInitiatorApi.get_host_details_response('module')
        }

    @staticmethod
    def get_initiator_module_list_response():
        return {
            'changed': False,
            'initiator_details': MockInitiatorApi.get_all_initiators_response(),
            'host_details': {}
        }
