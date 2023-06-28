# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for host module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_host_api \
    import MockHostApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_api_exception \
    import HttpError as http_error
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.unity.plugins.modules.host import Host


class TestHost():

    get_module_args = MockHostApi.HOST_MODULE_ARGS

    @pytest.fixture
    def host_module_mock(self):
        host_module_mock = Host()
        host_module_mock.unity = MagicMock()
        utils.host = MagicMock()
        return host_module_mock

    def test_get_host_details(self, host_module_mock):
        host_details = MockHostApi.get_host_details_response('api')
        self.get_module_args.update({
            'host_name': 'host_name_1',
        })
        host_module_mock.module.params = self.get_module_args
        host_module_mock.get_host_initiators_list = MagicMock(return_value=MockHostApi.get_host_initiators_list())
        utils.host.UnityHostList.get = MagicMock(return_value=MockHostApi.get_host_count_response())
        host_module_mock.unity.get_initiator = MagicMock(side_effect=[host_details['fc_host_initiators'][0], host_details['iscsi_host_initiators'][0]])
        host_module_mock.unity.get_host = MagicMock(return_value=MockSDKObject(host_details))
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_details_response('module')['host_details'] == host_module_mock.module.exit_json.call_args[1]['host_details']

    def test_get_host_details_throws_exception(self, host_module_mock):
        self.get_module_args.update({
            'host_name': 'name1'
        })
        host_module_mock.module.params = self.get_module_args
        utils.HttpError = http_error
        utils.host.UnityHostList.get = MagicMock(side_effect=http_error)
        host_module_mock.create_host = MagicMock(return_value=(False, MagicMock()))
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_details_response('error') == host_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_network_address_to_host(self, host_module_mock):
        self.get_module_args.update({
            'host_name': 'host_name_1',
            'network_address': 'net_add_1',
            'network_address_state': 'present-in-host',
            'state': 'present'
        })
        host_module_mock.module.params = self.get_module_args
        host_details = MockHostApi.get_host_details_response('api')
        host_module_mock.unity.get_initiator = MagicMock(side_effect=[host_details['fc_host_initiators'][0], host_details['iscsi_host_initiators'][0]])
        host_module_mock.get_host_initiators_list = MagicMock(return_value=MockHostApi.get_host_initiators_list())
        host_module_mock.unity.get_host = MagicMock(return_value=MockSDKObject(MockHostApi.get_host_details_after_network_address_addition('api')))
        host_details = MockSDKObject(host_details)
        host_details.add_ip_port = MagicMock(return_value=None)
        host_details.add_to_skip_list('add_ip_port')
        host_module_mock.get_host_details = MagicMock(return_value=host_details)
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_details_after_network_address_addition('module')['host_details'] == \
            host_module_mock.module.exit_json.call_args[1]['host_details']
        assert MockHostApi.get_host_details_after_network_address_addition('module')['changed'] == host_module_mock.module.exit_json.call_args[1]['changed']

    def test_add_network_address_to_host_negative(self, host_module_mock):
        self.get_module_args.update({
            'host_name': 'host_name_1',
            'network_address': 'net_ad$$$$$d_12',
            'network_address_state': 'present-in-host',
            'state': 'present'
        })
        host_module_mock.module.params = self.get_module_args
        host_details = MockHostApi.get_host_details_response('api')
        host_module_mock.unity.get_initiator = MagicMock(side_effect=[host_details['fc_host_initiators'][0], host_details['iscsi_host_initiators'][0]])
        host_module_mock.get_host_initiators_list = MagicMock(return_value=MockHostApi.get_host_initiators_list())
        host_module_mock.manage_network_address = MagicMock(return_value=(None, False))
        host_module_mock.get_host_details = MagicMock(return_value=MockSDKObject(host_details))
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_details_after_network_address_addition('invalid_address') == \
            host_module_mock.module.fail_json.call_args[1]['msg']
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_remove_network_address_from_host(self, host_module_mock):
        self.get_module_args.update({
            'host_name': 'host_name_1',
            'network_address': 'host_name_1',
            'network_address_state': 'absent-in-host',
            'state': 'present'
        })
        host_module_mock.module.params = self.get_module_args
        host_details = MockHostApi.get_host_details_response('api')
        host_module_mock.unity.get_initiator = MagicMock(side_effect=[host_details['fc_host_initiators'][0], host_details['iscsi_host_initiators'][0]])
        host_module_mock.get_host_initiators_list = MagicMock(return_value=MockHostApi.get_host_initiators_list())
        host_module_mock.unity.get_host = MagicMock(return_value=MockSDKObject(MockHostApi.get_host_details_after_network_address_removal('api')))
        host_details = MockSDKObject(host_details)
        host_details.delete_ip_port = MagicMock(return_value=None)
        host_details.add_to_skip_list('delete_ip_port')
        host_module_mock.get_host_details = MagicMock(return_value=host_details)
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_details_after_network_address_removal('module')['host_details'] == \
            host_module_mock.module.exit_json.call_args[1]['host_details']
        assert MockHostApi.get_host_details_after_network_address_removal('module')['changed'] == host_module_mock.module.exit_json.call_args[1]['changed']

    def test_remove_network_address_from_host_negative(self, host_module_mock):
        self.get_module_args.update({
            'host_name': 'host_name_1',
            'network_address': '1.1.1',
            'network_address_state': 'absent-in-host',
            'state': 'present'
        })
        host_module_mock.module.params = self.get_module_args
        host_details = MockHostApi.get_host_details_response('api')
        host_module_mock.unity.get_initiator = MagicMock(side_effect=[host_details['fc_host_initiators'][0], host_details['iscsi_host_initiators'][0]])
        host_module_mock.get_host_initiators_list = MagicMock(return_value=MockHostApi.get_host_initiators_list())
        host_module_mock.manage_network_address = MagicMock(return_value=(None, False))
        host_module_mock.get_host_details = MagicMock(return_value=MockSDKObject(host_details))
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_details_after_network_address_removal('invalid_IPV4') == \
            host_module_mock.module.fail_json.call_args[1]['msg']
        assert host_module_mock.module.exit_json.call_args[1]['changed'] is False
