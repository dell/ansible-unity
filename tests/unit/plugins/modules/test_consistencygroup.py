# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for consistency group module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_consistencygroup_api \
    import MockConsistenyGroupApi
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKObject
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock(side_effect=[MagicMock(),
                                                              MockConsistenyGroupApi.get_remote_system_conn_response()])
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.unity.plugins.modules.consistencygroup import ConsistencyGroup


class TestConsistencyGroup():

    get_module_args = MockConsistenyGroupApi.CONSISTENCY_GROUP_MODULE_ARGS

    @pytest.fixture
    def consistencygroup_module_mock(self):
        consistencygroup_module_mock = ConsistencyGroup()
        consistencygroup_module_mock.unity_conn = MagicMock()
        utils.cg = MagicMock()
        return consistencygroup_module_mock

    def test_enable_cg_replication(self, consistencygroup_module_mock):
        self.get_module_args.update({
            'cg_name': 'lun_test_cg_source_12',
            'replication_params': {
                'destination_cg_name': 'destination_cg_1',
                'replication_mode': 'asynchronous',
                'rpo': 60,
                'replication_type': 'remote',
                'remote_system': {
                    'remote_system_host': '11.111.11.11',
                    'remote_system_verifycert': False,
                    'remote_system_username': 'username',
                    'remote_system_password': 'password',
                    'remote_system_port': 1111
                },
                'destination_pool_name': 'pool_test_name_1',
                'destination_pool_id': None
            },
            'replication_state': 'enable',
            'state': 'present'
        })
        consistencygroup_module_mock.module.params = self.get_module_args
        cg_details = MockConsistenyGroupApi.cg_get_details_method_response()
        cg_object = MockConsistenyGroupApi.get_cg_object()
        consistencygroup_module_mock.unity_conn.get_cg = MagicMock(return_value=cg_object)
        consistencygroup_module_mock.get_details = MagicMock(side_effect=[
            cg_details,
            MockConsistenyGroupApi.get_cg_replication_dependent_response('cg_replication_enabled_details')])
        cg_object.get_id = MagicMock(return_value=cg_details['id'])
        utils.cg.UnityConsistencyGroup.get = MagicMock(return_value=cg_object)
        cg_object.check_cg_is_replicated = MagicMock(return_value=False)
        consistencygroup_module_mock.unity_conn.get_remote_system = \
            MagicMock(return_value=MockConsistenyGroupApi.get_cg_replication_dependent_response('remote_system'))
        utils.UnityStorageResource = MagicMock(return_value=MockSDKObject({}))
        cg_object.replicate_cg_with_dst_resource_provisioning = MagicMock(return_value=None)
        consistencygroup_module_mock.perform_module_operation()
        assert consistencygroup_module_mock.module.exit_json.call_args[1]['consistency_group_details']['cg_replication_enabled'] is True
        assert consistencygroup_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_enable_cg_replication_negative_1(self, consistencygroup_module_mock):
        self.get_module_args.update({
            'cg_name': 'lun_test_cg_source_12',
            'replication_params': {
                'destination_cg_name': '',
                'replication_mode': 'asynchronous',
                'rpo': 60,
                'replication_type': 'local',
                'destination_pool_name': None,
                'destination_pool_id': 'pool_test_1'
            },
            'replication_state': 'enable',
            'state': 'present'
        })
        consistencygroup_module_mock.module.params = self.get_module_args
        cg_details = MockConsistenyGroupApi.cg_get_details_method_response()
        cg_object = MockConsistenyGroupApi.get_cg_object()
        consistencygroup_module_mock.unity_conn.get_cg = MagicMock(return_value=cg_object)
        consistencygroup_module_mock.get_details = MagicMock(side_effect=[
            cg_details,
            MockConsistenyGroupApi.get_cg_replication_dependent_response('cg_replication_enabled_details')])
        cg_object.get_id = MagicMock(return_value=cg_details['id'])
        utils.cg.UnityConsistencyGroup.get = MagicMock(return_value=cg_object)
        cg_object.check_cg_is_replicated = MagicMock(return_value=False)
        consistencygroup_module_mock.unity_conn.get_remote_system = \
            MagicMock(return_value=MockConsistenyGroupApi.get_cg_replication_dependent_response('remote_system'))
        utils.UnityStorageResource = MagicMock(return_value=MockSDKObject({}))
        cg_object.replicate_cg_with_dst_resource_provisioning = MagicMock(return_value=None)
        consistencygroup_module_mock.perform_module_operation()
        assert consistencygroup_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockConsistenyGroupApi.get_cg_replication_dependent_response('destination_cg_name_validation')

    def test_enable_cg_replication_negative_2(self, consistencygroup_module_mock):
        self.get_module_args.update({
            'cg_name': 'lun_test_cg_source_12',
            'replication_params': {
                'destination_cg_name': 'destination_cg_1',
                'replication_mode': 'asynchronous',
                'rpo': 60,
                'replication_type': 'remote',
                'remote_system': {
                    'remote_system_host': '11.111.11.11',
                    'remote_system_verifycert': False,
                    'remote_system_username': 'username',
                    'remote_system_password': 'password',
                    'remote_system_port': 1111
                },
                'destination_pool_name': None,
                'destination_pool_id': 'pool_test_1'
            },
            'replication_state': 'enable',
            'state': 'present'
        })
        consistencygroup_module_mock.module.params = self.get_module_args
        cg_details = MockConsistenyGroupApi.cg_get_details_method_response()
        cg_object = MockConsistenyGroupApi.get_cg_object()
        consistencygroup_module_mock.unity_conn.get_cg = MagicMock(return_value=cg_object)
        consistencygroup_module_mock.get_details = MagicMock(side_effect=[
            cg_details,
            MockConsistenyGroupApi.get_cg_replication_dependent_response('cg_replication_enabled_details')])
        cg_object.get_id = MagicMock(return_value=cg_details['id'])
        utils.cg.UnityConsistencyGroup.get = MagicMock(return_value=cg_object)
        cg_object.check_cg_is_replicated = MagicMock(return_value=False)
        consistencygroup_module_mock.unity_conn.get_remote_system = MagicMock(side_effect=MockApiException)
        consistencygroup_module_mock.perform_module_operation()
        assert consistencygroup_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockConsistenyGroupApi.get_cg_replication_dependent_response('enable_cg_exception')

    def test_disable_cg_replication(self, consistencygroup_module_mock):
        self.get_module_args.update({
            'cg_name': 'lun_test_cg_source_12',
            'replication_state': 'disable',
            'state': 'present'
        })
        consistencygroup_module_mock.module.params = self.get_module_args
        cg_details = MockConsistenyGroupApi.cg_get_details_method_response()
        cg_object = MockConsistenyGroupApi.get_cg_object()
        consistencygroup_module_mock.unity_conn.get_cg = MagicMock(return_value=cg_object)
        consistencygroup_module_mock.get_details = MagicMock(side_effect=[
            MockConsistenyGroupApi.get_cg_replication_dependent_response('cg_replication_enabled_details'),
            cg_details])
        cg_object.get_id = MagicMock(return_value=cg_details['id'])
        utils.cg.UnityConsistencyGroup.get = MagicMock(return_value=cg_object)
        cg_object.check_cg_is_replicated = MagicMock(return_value=True)
        repl_session = MockConsistenyGroupApi.get_cg_replication_dependent_response('replication_session')
        repl_session.delete = MagicMock(return_value=None)
        consistencygroup_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=[repl_session])
        consistencygroup_module_mock.perform_module_operation()
        assert consistencygroup_module_mock.module.exit_json.call_args[1]['consistency_group_details']['cg_replication_enabled'] is False
        assert consistencygroup_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_disable_cg_replication_throws_exception(self, consistencygroup_module_mock):
        self.get_module_args.update({
            'cg_name': 'lun_test_cg_source_12',
            'replication_state': 'disable',
            'state': 'present'
        })
        consistencygroup_module_mock.module.params = self.get_module_args
        cg_details = MockConsistenyGroupApi.cg_get_details_method_response()
        cg_object = MockConsistenyGroupApi.get_cg_object()
        consistencygroup_module_mock.unity_conn.get_cg = MagicMock(return_value=cg_object)
        consistencygroup_module_mock.get_details = MagicMock(side_effect=[
            MockConsistenyGroupApi.get_cg_replication_dependent_response('cg_replication_enabled_details'),
            cg_details])
        cg_object.get_id = MagicMock(return_value=cg_details['id'])
        utils.cg.UnityConsistencyGroup.get = MagicMock(return_value=cg_object)
        cg_object.check_cg_is_replicated = MagicMock(side_effect=MockApiException)
        consistencygroup_module_mock.perform_module_operation()
        assert consistencygroup_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockConsistenyGroupApi.get_cg_replication_dependent_response('disable_cg_exception')
