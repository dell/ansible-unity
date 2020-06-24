#!/usr/bin/python
# Copyright: (c) 2020, DellEMC

"""Ansible module for Gathering information about DellEMC Unity"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: dellemc_unity_gatherfacts

version_added: '2.7'

short_description: Gathering information about DellEMC Unity

description:
- Gathering information about DellEMC Unity Storage System includes
  Get the details of Unity array,
  Get list of Hosts in Unity array,
  Get list of FC Initiators in Unity array,
  Get list of iSCSI Initiators in Unity array,
  Get list of Consistency Groups in Unity array,
  Get list of Storage Pools in Unity array,
  Get list of Volumes in Unity array,
  Get list of Snapshot Schedules in Unity array,
  
extends_documentation_fragment:
  - dellemc_unity.dellemc_unity

author:
- Rajshree Khare (@kharer5) <Rajshree.Khare@dell.com>

options:
  gather_subset:
    description:
    - List of string variables to specify the Unity storage system entities
      for which information is required.
    - host
    - fc_initiator
    - iscsi_initiator
    - cg
    - storage_pool
    - vol
    - snapshot_schedule
    choices: [host, fc_initiator, iscsi_initiator, cg, storage_pool, vol,
    snapshot_schedule]
    type: list
'''

EXAMPLES = r'''
 - name: Get detailed list of Unity entities.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
      - host
      - fc_initiator
      - iscsi_initiator
      - cg
      - storage_pool
      - vol
      - snapshot_schedule

 - name: Get information of Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"

 - name: Get list of hosts on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
      - host

 - name: Get list of FC initiators on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
      - fc_initiator

 - name: Get list of ISCSI initiators on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
      - iscsi_initiator

 - name: Get list of consistency groups on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - cg

 - name: Get list of storage pools on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - storage_pool

 - name: Get list of volumes on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - vol

 - name: Get list of snapshot schedules on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - snapshot_schedule
'''

RETURN = r'''
Array_Details:
    description: Details of the Unity Array.
    returned: always
    type: complex
    contains:
        api_version:
            description: The current api version of the Unity Array.
            type: str
        earliest_api_version:
            description: The earliest api version of the Unity Array.
            type: str
        model:
            description: The model of the Unity Array.
            type: str
        name:
            description: The name of the Unity Array.
            type: str
        software_version:
            description: The software version of the Unity Array.
            type: str

Hosts:
    description: Details of the hosts.
    returned: When hosts exist.
    type: complex
    contains:
        id:
            description: The ID of the host.
            type: str
        name:
            description: The name of the host.
            type: str

FC_initiators:
    description: Details of the FC initiators.
    returned: When FC initiator exist.
    type: complex
    contains:
        WWN:
            description: The WWN of the FC initiator.
            type: str
        id:
            description: The id of the FC initiator.
            type: str

ISCSI_initiators:
    description: Details of the ISCSI initiators.
    returned: When ISCSI initiators exist.
    type: complex
    contains:
        IQN:
            description: The IQN of the ISCSI initiator.
            type: str
        id:
            description: The id of the ISCSI initiator.
            type: str

Consistency_Groups:
    description: Details of the Consistency Groups.
    returned: When Consistency Groups exist.
    type: complex
    contains:
        id:
            description: The ID of the Consistency Group.
            type: str
        name:
            description: The name of the Consistency Group.
            type: str

Storage_Pools:
    description: Details of the Storage Pools.
    returned: When Storage Pools exist.
    type: complex
    contains:
        id:
            description: The ID of the Storage Pool.
            type: str
        name:
            description: The name of the Storage Pool.
            type: str

Volumes:
    description: Details of the Volumes.
    returned: When Volumes exist.
    type: complex
    contains:
        id:
            description: The ID of the Volume.
            type: str
        name:
            description: The name of the Volume.
            type: str

Snapshot_Schedules:
    description: Details of the Snapshot Schedules.
    returned: When Snapshot Schedules exist.
    type: complex
    contains:
        id:
            description: The ID of the Snapshot Schedule.
            type: str
        name:
            description: The name of the Snapshot Schedule.
            type: str
'''

import json
import logging
from storops.unity.resource import host, cg, snap_schedule
from storops.unity.enums import HostInitiatorTypeEnum
from storops.exception import UnityResourceNotFoundError
from storops.connection.exceptions import HttpError
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.storage.dell import \
    dellemc_ansible_unity_utils as utils

LOG = utils.get_logger('dellemc_unity_gatherfacts',
                       log_devel=utils.logging.INFO)
HAS_UNITY_SDK = utils.get_unity_sdk()
UNITY_SDK_VERSION_CHECK = utils.storops_version_check()


class UnityGatherfacts(object):
    """Class with Gatherfacts operations"""

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_unity_management_host_parameters()
        self.module_params.update(self.get_unity_gatherfacts_parameters())

        """ initialize the ansible module """
        self.module = AnsibleModule(argument_spec=self.module_params,
                                    supports_check_mode=False)

        if not HAS_UNITY_SDK:
            err_msg = "Ansible modules for Unity require the Unity " \
                      "python library to be installed. Please install the " \
                      "library  before using these modules."
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        if UNITY_SDK_VERSION_CHECK and \
                not UNITY_SDK_VERSION_CHECK['supported_version']:
            err_msg = UNITY_SDK_VERSION_CHECK['unsupported_version_message']
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        self.unity = utils.get_unity_unisphere_connection(self.module.params)
        LOG.info('Got the unity instance for provisioning on Unity')

    def get_unity_gatherfacts_parameters(self):
        """This method provides parameters required for the ansible
            gatherfacts module on Unity"""
        return dict(
            gather_subset=dict(type='list', required=False,
                               choices=['host',
                                        'fc_initiator',
                                        'iscsi_initiator',
                                        'cg',
                                        'storage_pool',
                                        'vol',
                                        'snapshot_schedule'
                                        ]),
        )

    def get_array_details(self):
        """ Get the list of snapshot schedules on a given Unity storage
            system """

        try:
            LOG.info('Getting array details ')
            array_details = self.unity.info
            return array_details._get_properties()

        except HttpError as e:
            if e.http_status == 401:
                msg = 'Incorrect username or password provided.'
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            else:
                msg = str(e)
                LOG.error(msg)
                self.module.fail_json(msg=msg)
        except Exception as e:
            msg = 'Get array details from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_hosts_list(self):
        """ Get the list of hosts on a given Unity storage system """

        try:
            LOG.info('Getting hosts list ')
            hosts = self.unity.get_host()
            return self.result_list(hosts)

        except Exception as e:
            msg = 'Get hosts list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_fc_initiators_list(self):
        """ Get the list of FC Initiators on a given Unity storage system """

        try:
            LOG.info('Getting FC initiators list ')
            fc_initiator = host.UnityHostInitiatorList\
                .get(cli=self.unity._cli, type=HostInitiatorTypeEnum.FC)
            return self.fc_initiators_result_list(fc_initiator)

        except Exception as e:
            msg = 'Get FC initiators list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_iscsi_initiators_list(self):
        """ Get the list of ISCSI initiators on a given Unity storage
            system """

        try:
            LOG.info('Getting ISCSI initiators list ')
            iscsi_initiator = host.UnityHostInitiatorList\
                .get(cli=self.unity._cli, type=HostInitiatorTypeEnum.ISCSI)
            return self.iscsi_initiators_result_list(iscsi_initiator)

        except Exception as e:
            msg = 'Get ISCSI initiators list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_consistency_groups_list(self):
        """ Get the list of consistency groups on a given Unity storage
            system """

        try:
            LOG.info('Getting consistency groups list ')
            consistency_groups = cg.UnityConsistencyGroupList\
                .get(self.unity._cli)
            return self.result_list(consistency_groups)

        except Exception as e:
            msg = 'Get consistency groups list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_storage_pools_list(self):
        """ Get the list of storage pools on a given Unity storage
            system """

        try:
            LOG.info('Getting storage pools list ')
            storage_pools = self.unity.get_pool()
            return self.result_list(storage_pools)

        except Exception as e:
            msg = 'Get storage pools list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_volumes_list(self):
        """ Get the list of volumes on a given Unity storage
            system """

        try:
            LOG.info('Getting volumes list ')
            volumes = self.unity.get_lun()
            return self.result_list(volumes)

        except Exception as e:
            msg = 'Get volumes list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_snapshot_schedules_list(self):
        """ Get the list of snapshot schedules on a given Unity storage
            system """

        try:
            LOG.info('Getting snapshot schedules list ')
            snapshot_schedules = snap_schedule.UnitySnapScheduleList\
                .get(cli=self.unity._cli)
            return self.result_list(snapshot_schedules)

        except Exception as e:
            msg = 'Get snapshot schedules list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def result_list(self, entity):
        """ Get the name and id associated with the Unity entities """
        result = []

        if entity:
            LOG.info('Successfully listed.')
            for item in entity:
                result.append(
                    {
                        "name": item.name,
                        "id": item.id
                    }
                )
            return result
        else:
            return None

    def fc_initiators_result_list(self, entity):
        """ Get the WWN and id associated with the Unity FC initiators """
        result = []

        if entity:
            LOG.info('Successfully listed.')
            for item in entity:
                result.append(
                    {
                        "WWN": item.initiator_id,
                        "id": item.id
                    }
                )
            return result
        else:
            return None

    def iscsi_initiators_result_list(self, entity):
        """ Get the IQN and id associated with the Unity ISCSI initiators """
        result = []

        if entity:
            LOG.info('Successfully listed.')
            for item in entity:
                result.append(
                    {
                        "IQN": item.initiator_id,
                        "id": item.id
                    }
                )
            return result
        else:
            return None

    def perform_module_operation(self):
        """ Perform different actions on Gatherfacts based on user parameter
            chosen in playbook """

        """ Get the array details a given Unity storage system """
        array_details = []
        array_details = self.get_array_details()

        host = []
        fc_initiator = []
        iscsi_initiator = []
        cg = []
        storage_pool = []
        vol = []
        snapshot_schedule = []

        subset = self.module.params['gather_subset']
        if subset is not None:
            if 'host' in subset:
                host = self.get_hosts_list()
            if 'fc_initiator' in subset:
                fc_initiator = self.get_fc_initiators_list()
            if 'iscsi_initiator' in subset:
                iscsi_initiator = self.get_iscsi_initiators_list()
            if 'cg' in subset:
                cg = self.get_consistency_groups_list()
            if 'storage_pool' in subset:
                storage_pool = self.get_storage_pools_list()
            if 'vol' in subset:
                vol = self.get_volumes_list()
            if 'snapshot_schedule' in subset:
                snapshot_schedule = self.get_snapshot_schedules_list()

        self.module.exit_json(
            Array_Details=array_details,
            Hosts=host,
            FC_initiators=fc_initiator,
            ISCSI_initiators=iscsi_initiator,
            Consistency_Groups=cg,
            Storage_Pools=storage_pool,
            Volumes=vol,
            Snapshot_Schedules=snapshot_schedule
        )


def main():
    """ Create Unity Gatherfacts object and perform action on it
        based on user input from playbook"""
    obj = UnityGatherfacts()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
