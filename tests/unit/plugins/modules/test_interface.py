# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for interface module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_interface_api \
    import MockInterfaceApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.unity.plugins.modules.interface import Interface


class TestInterface():

    interface_module_args = MockInterfaceApi.INTERFACE_MODULE_ARGS

    @pytest.fixture
    def interface_module_mock(self):
        interface_module_mock = Interface()
        interface_module_mock.module.check_mode = False
        interface_module_mock.unity_conn = MagicMock()
        return interface_module_mock

    def test_validate_param_ethernet_port_name_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'ethernet_port_name': " ",
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        mock_none_response = MagicMock(return_value=None)
        interface_module_mock.get_nas_server_obj = mock_none_response
        interface_module_mock.validate_create_params = mock_none_response
        interface_module_mock.add_interface = mock_none_response
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert MockInterfaceApi.get_interface_error_response('invalid_ethernet_port_name') == \
            interface_module_mock.module.fail_json.call_args[1]['msg']

    def test_validate_param_vlan_id_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'vlan_id': 2,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        mock_none_response = MagicMock(return_value=None)
        interface_module_mock.get_nas_server_obj = mock_none_response
        interface_module_mock.validate_create_params = mock_none_response
        interface_module_mock.add_interface = mock_none_response
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert MockInterfaceApi.get_interface_error_response('invalid_vlan_id') == \
            interface_module_mock.module.fail_json.call_args[1]['msg']

    def test_validate_param_interface_ip_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': "10.2.2",
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        mock_none_response = MagicMock(return_value=None)
        interface_module_mock.get_nas_server_obj = mock_none_response
        interface_module_mock.validate_create_params = mock_none_response
        interface_module_mock.add_interface = mock_none_response
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert MockInterfaceApi.get_interface_error_response('invalid_interface_ip') == \
            interface_module_mock.module.fail_json.call_args[1]['msg']

    def test_validate_param_gateway_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'gateway': "10.2.1",
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        mock_none_response = MagicMock(return_value=None)
        interface_module_mock.get_nas_server_obj = mock_none_response
        interface_module_mock.validate_create_params = mock_none_response
        interface_module_mock.add_interface = mock_none_response
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert MockInterfaceApi.get_interface_error_response('invalid_gateway') == \
            interface_module_mock.module.fail_json.call_args[1]['msg']

    def test_validate_param_netmask_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'netmask': "10.2.0/2",
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        mock_none_response = MagicMock(return_value=None)
        interface_module_mock.get_nas_server_obj = mock_none_response
        interface_module_mock.validate_create_params = mock_none_response
        interface_module_mock.add_interface = mock_none_response
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert MockInterfaceApi.get_interface_error_response('invalid_netmask') == \
            interface_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_nas_server_obj_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_id': "nas_id_00",
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        mock_none_response = MagicMock(return_value=None)
        interface_module_mock.unity_conn.get_nas_server = MagicMock(return_value=MockInterfaceApi.get_nas_server_obj_existed_false())
        interface_module_mock.validate_create_params = mock_none_response
        interface_module_mock.add_interface = mock_none_response
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert MockInterfaceApi.get_nas_server_obj_errors('existed_false') == \
            interface_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_nas_server_obj_exception(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_id': "nas_id_00",
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        mock_none_response = MagicMock(return_value=None)
        interface_module_mock.unity_conn.get_nas_server = MagicMock(side_effect=MockApiException)
        interface_module_mock.validate_create_params = mock_none_response
        interface_module_mock.add_interface = mock_none_response
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert MockInterfaceApi.get_nas_server_obj_errors('exception') == \
            interface_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_operation_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'vlan_id': 4,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_object = MockInterfaceApi.NAS_SERVER_OBJECT
        interface_module_mock.unity_conn.get_nas_server = MagicMock(return_value=nas_server_object)
        interface_module_mock.unity_conn.get_file_interface = MagicMock(return_value=MockInterfaceApi.INTERFACE_OBJECT)
        interface_module_mock.perform_module_operation()
        assert MockInterfaceApi.get_interface_error_response('modify_failure') == \
            interface_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_interface_details(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_object = MockInterfaceApi.NAS_SERVER_OBJECT
        interface_module_mock.unity_conn.get_nas_server = MagicMock(return_value=nas_server_object)
        interface_module_mock.unity_conn.get_file_interface = MagicMock(return_value=MockInterfaceApi.INTERFACE_OBJECT)
        interface_module_mock.perform_module_operation()
        interface_details = MockInterfaceApi.INTERFACE_OBJECT._get_properties()
        assert interface_module_mock.module.exit_json.call_args[1]['interface_details'] == interface_details

    def test_get_interface_details_exception(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_object = MockInterfaceApi.NAS_SERVER_OBJECT
        interface_module_mock.unity_conn.get_nas_server = MagicMock(return_value=nas_server_object)
        interface_module_mock.unity_conn.get_file_interface = MagicMock(side_effect=[MockApiException, MockInterfaceApi.INTERFACE_OBJECT])
        interface_module_mock.validate_create_params = MagicMock(return_value=None)
        interface_module_mock.add_interface = MagicMock(return_value=None)
        interface_module_mock.perform_module_operation()
        assert interface_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockInterfaceApi.get_interface_exception_response('interface_exception')

    def test_add_interface_without_role_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'ethernet_port_name': MockInterfaceApi.ETHERNET_PORT_NAME,
            'netmask': MockInterfaceApi.NETMASK_DUMMY,
            'gateway': MockInterfaceApi.GATEWAY_DUMMY,
            'vlan_id': 324,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_existing = MockInterfaceApi.get_nas_without_interface()
        interface_module_mock.unity_conn.get_nas_server = MagicMock(return_Value=nas_server_existing)
        interface_module_mock.add_interface = MagicMock(return_value=None)
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert interface_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockInterfaceApi.get_interface_error_response('no_role')

    def test_add_interface_without_ethernet_negative(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'role': "PRODUCTION",
            'netmask': MockInterfaceApi.NETMASK_DUMMY,
            'gateway': MockInterfaceApi.GATEWAY_DUMMY,
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'vlan_id': 324,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_existing = MockInterfaceApi.get_nas_without_interface()
        interface_module_mock.unity_conn.get_nas_server = MagicMock(return_Value=nas_server_existing)
        interface_module_mock.add_interface = MagicMock(return_value=None)
        interface_module_mock.get_interface_details = MagicMock(side_effect=[None, MockSDKObject({})])
        interface_module_mock.perform_module_operation()
        assert interface_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockInterfaceApi.get_interface_error_response('no_ethernet')

    def test_add_interface(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'ethernet_port_name': MockInterfaceApi.ETHERNET_PORT_NAME,
            'role': "PRODUCTION",
            'netmask': MockInterfaceApi.NETMASK_DUMMY,
            'gateway': MockInterfaceApi.GATEWAY_DUMMY,
            'vlan_id': 324,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_object = MockInterfaceApi.NAS_SERVER_OBJECT
        nas_server_existing = MockInterfaceApi.get_nas_without_interface()
        nas_server_existing.get_id = MagicMock(return_value='nas_id_00')
        nas_server_existing.add_to_skip_list('get_id')
        interface_module_mock.unity_conn.get_nas_server = MagicMock(side_effect=[nas_server_existing,
                                                                                 nas_server_object])
        interface_module_mock.unity_conn.get_file_interface = MagicMock(return_value=MockInterfaceApi.INTERFACE_OBJECT)
        utils.FileInterfaceRoleEnum = MockInterfaceApi.FILE_INTERFACE_ROLE_ENUM_DUMMY
        ethernet_port_info = MagicMock()
        ethernet_port_info.id = 'ethernet_port_id_0'
        interface_module_mock.unity_conn.get_ethernet_port = MagicMock(return_value=ethernet_port_info)
        utils.UnityFileInterface = MagicMock()
        utils.UnityFileInterface.create = MagicMock(return_value=None)
        interface_module_mock.perform_module_operation()
        interface_details = MockInterfaceApi.INTERFACE_OBJECT._get_properties()
        assert interface_module_mock.module.exit_json.call_args[1]['interface_details'] == interface_details

    def test_add_interface_no_change(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'ethernet_port_name': MockInterfaceApi.ETHERNET_PORT_NAME,
            'role': "PRODUCTION",
            'netmask': MockInterfaceApi.NETMASK_DUMMY,
            'gateway': MockInterfaceApi.GATEWAY_DUMMY,
            'vlan_id': 324,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_object = MockInterfaceApi.NAS_SERVER_OBJECT
        interface_module_mock.unity_conn.get_nas_server = MagicMock(side_effect=[nas_server_object,
                                                                                 nas_server_object])
        interface_module_mock.unity_conn.get_file_interface = MagicMock(return_value=MockInterfaceApi.INTERFACE_OBJECT)
        utils.FileInterfaceRoleEnum = MockInterfaceApi.FILE_INTERFACE_ROLE_ENUM_DUMMY
        ethernet_port_info = MagicMock()
        ethernet_port_info.id = 'ethernet_port_id_0'
        interface_module_mock.unity_conn.get_ethernet_port = MagicMock(return_value=ethernet_port_info)
        utils.UnityFileInterface = MagicMock()
        utils.UnityFileInterface.create = MagicMock(return_value=None)
        interface_module_mock.perform_module_operation()
        assert interface_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_add_interface_exception(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'ethernet_port_name': MockInterfaceApi.ETHERNET_PORT_NAME,
            'role': "PRODUCTION",
            'netmask': MockInterfaceApi.NETMASK_DUMMY,
            'gateway': MockInterfaceApi.GATEWAY_DUMMY,
            'vlan_id': 324,
            'state': "present"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_object = MockInterfaceApi.NAS_SERVER_OBJECT
        nas_server_existing = MockInterfaceApi.get_nas_without_interface()
        nas_server_existing.get_id = MagicMock(return_value='nas_id_00')
        nas_server_existing.add_to_skip_list('get_id')
        interface_module_mock.unity_conn.get_nas_server = MagicMock(side_effect=[nas_server_existing,
                                                                                 nas_server_object])
        interface_module_mock.unity_conn.get_file_interface = MagicMock(return_value=MockInterfaceApi.INTERFACE_OBJECT)
        utils.FileInterfaceRoleEnum = MockInterfaceApi.FILE_INTERFACE_ROLE_ENUM_DUMMY
        ethernet_port_info = MagicMock()
        ethernet_port_info.id = 'ethernet_port_id_0'
        interface_module_mock.unity_conn.get_ethernet_port = MagicMock(return_value=ethernet_port_info)
        utils.UnityFileInterface = MagicMock()
        utils.UnityFileInterface.create = MagicMock(side_effect=MockApiException)
        interface_module_mock.perform_module_operation()
        assert interface_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockInterfaceApi.get_interface_exception_response('add_interface_exception')

    def test_delete_interface(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'state': "absent"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_object = MockInterfaceApi.NAS_SERVER_OBJECT
        interface_module_mock.unity_conn.get_nas_server = MagicMock(return_value=nas_server_object)
        interface_object = MockInterfaceApi.INTERFACE_OBJECT
        interface_object.delete = MagicMock(return_value=None)
        interface_object.add_to_skip_list('delete')
        interface_module_mock.unity_conn.get_file_interface = MagicMock(return_value=interface_object)
        interface_module_mock.perform_module_operation()
        assert interface_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_interface_exception(self, interface_module_mock):
        self.interface_module_args.update({
            'nas_server_name': "dummy_nas",
            'interface_ip': MockInterfaceApi.INTERFACE_DUMMY,
            'state': "absent"
        })
        interface_module_mock.module.params = self.interface_module_args
        nas_server_object = MockInterfaceApi.NAS_SERVER_OBJECT
        interface_module_mock.unity_conn.get_nas_server = MagicMock(return_value=nas_server_object)
        interface_object = MockInterfaceApi.INTERFACE_OBJECT
        interface_object.delete = MagicMock(side_effect=MockApiException)
        interface_object.add_to_skip_list('delete')
        interface_module_mock.unity_conn.get_file_interface = MagicMock(return_value=interface_object)
        interface_module_mock.perform_module_operation()
        assert interface_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockInterfaceApi.get_interface_exception_response('delete_interface_exception')
