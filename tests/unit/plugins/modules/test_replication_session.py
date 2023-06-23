# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock Api response for Unit tests of Replication session module on Unity"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from enum import Enum
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_replication_session_api \
    import MockReplicationSessionApi, MockReplicationSessionObject
from ansible_collections.dellemc.unity.tests.unit.plugins.module_utils.mock_api_exception \
    import HttpError as http_error
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell import utils

utils.get_logger = MagicMock()
utils.get_unity_management_host_parameters = MagicMock()
utils.ensure_required_libs = MagicMock()
utils.get_unity_unisphere_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.unity.plugins.modules.replication_session import ReplicationSession, ReplicationSessionHandler


class ReplicationOpStatusEnum(Enum):
    FAILED_OVER_WITH_SYNC = (0x8400, 'Failed_Over_with_Sync')
    FAILED_OVER = (0x8401, 'Failed_Over')
    PAUSED = (0x8403, 'Paused')


class TestReplicationSession():

    get_module_args = MockReplicationSessionApi.MODULE_ARGS
    session_name = "rep_session"
    FAILED_WITH_ERROR = " failed with error"
    replication_session_obj = MockReplicationSessionObject(MockReplicationSessionApi.get_replication_session_details())

    @pytest.fixture
    def replication_session_module_mock(self):
        setattr(utils, 'ReplicationOpStatusEnum', ReplicationOpStatusEnum)
        replication_session_module_mock = ReplicationSession()
        replication_session_module_mock.unity_conn = MagicMock()
        replication_session_module_mock.module.check_mode = False
        return replication_session_module_mock

    def test_get_replication_session_details(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1'})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert replication_session_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_get_replication_session_details_throws_exception(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1'})
        replication_session_module_mock.module.params = self.get_module_args
        utils.HttpError = http_error
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(side_effect=http_error)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert "is invalid" in \
            replication_session_module_mock.module.fail_json.call_args[1]['msg']

    def test_pause_replication_session(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'pause': True})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert self.replication_session_obj.pause_session is True

    def test_pause_replication_session_throws_exception(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'pause': True})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        self.replication_session_obj.pause = MagicMock(side_effect=Exception)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert "Pause replication session " + self.session_name + self.FAILED_WITH_ERROR in \
               replication_session_module_mock.module.fail_json.call_args[1]['msg']

    def test_resume_replication_session(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'pause': False})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_obj = MockReplicationSessionObject(MockReplicationSessionApi.get_replication_session_details("PAUSED"))
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=replication_session_obj)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert replication_session_obj.resume_session is True

    def test_resume_replication_session_throws_exception(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'pause': False})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_obj = MockReplicationSessionObject(MockReplicationSessionApi.get_replication_session_details("PAUSED"))
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=replication_session_obj)
        replication_session_obj.resume = MagicMock(side_effect=Exception)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert "Resume replication session " + self.session_name + self.FAILED_WITH_ERROR in \
               replication_session_module_mock.module.fail_json.call_args[1]['msg']

    def test_failover_replication_session(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'failover_with_sync': True, 'force': True})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert self.replication_session_obj.failover_session is True

    def test_failover_replication_session_throws_exception(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'failover_with_sync': True, 'force': True})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        self.replication_session_obj.failover = MagicMock(side_effect=Exception)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert "Failover replication session " + self.session_name + self.FAILED_WITH_ERROR in \
               replication_session_module_mock.module.fail_json.call_args[1]['msg']

    def test_failback_replication_session_details(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'failback': True, 'force_full_copy': True})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_obj = MockReplicationSessionObject(MockReplicationSessionApi.get_replication_session_details("FAILED_OVER"))
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=replication_session_obj)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert replication_session_obj.failback_session is True

    def test_failback_replication_session_throws_exception(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'failback': True, 'force_full_copy': True})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_obj = MockReplicationSessionObject(MockReplicationSessionApi.get_replication_session_details("FAILED_OVER"))
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=replication_session_obj)
        replication_session_obj.failback = MagicMock(side_effect=Exception)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert "Failback replication session " + self.session_name + self.FAILED_WITH_ERROR in \
               replication_session_module_mock.module.fail_json.call_args[1]['msg']

    def test_sync_replication_session(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'sync': True})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert self.replication_session_obj.sync_session is True

    def test_sync_replication_session_throws_exception(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'sync': True})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        self.replication_session_obj.sync = MagicMock(side_effect=Exception)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert "Sync replication session " + self.session_name + self.FAILED_WITH_ERROR in \
               replication_session_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_replication_session(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'state': 'absent'})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert self.replication_session_obj.delete_session is True

    def test_delete_replication_session_throws_exception(self, replication_session_module_mock):
        self.get_module_args.update({'session_name': 'session1', 'state': 'absent'})
        replication_session_module_mock.module.params = self.get_module_args
        replication_session_module_mock.unity_conn.get_replication_session = \
            MagicMock(return_value=self.replication_session_obj)
        self.replication_session_obj.delete = MagicMock(side_effect=Exception)
        ReplicationSessionHandler().handle(replication_session_module_mock, replication_session_module_mock.module.params)
        assert "Deleting replication session " + self.session_name + self.FAILED_WITH_ERROR in \
               replication_session_module_mock.module.fail_json.call_args[1]['msg']
