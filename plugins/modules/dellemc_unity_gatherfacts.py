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

version_added: '1.1.0'

short_description: Gathering information about DellEMC Unity

description:
- Gathering information about DellEMC Unity storage system includes
  Get the details of Unity array,
  Get list of Hosts in Unity array,
  Get list of FC initiators in Unity array,
  Get list of iSCSI initiators in Unity array,
  Get list of Consistency groups in Unity array,
  Get list of Storage pools in Unity array,
  Get list of Volumes in Unity array,
  Get list of Snapshot schedules in Unity array,
  Get list of NAS servers in Unity array,
  Get list of File systems in Unity array,
  Get list of Snapshots in Unity array,
  Get list of SMB shares in Unity array,
  Get list of NFS exports in Unity array,
  Get list of User quotas in Unity array,
  Get list of Quota tree in Unity array

extends_documentation_fragment:
  - dellemc.unity.dellemc_unity.unity

author:
- Rajshree Khare (@kharer5) <ansible.team@dell.com>
- Akash Shendge (@shenda1) <ansible.team@dell.com>

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
    - nas_server
    - file_system
    - snapshot
    - nfs_export
    - smb_share
    - user_quota
    - tree_quota
    choices: [host, fc_initiator, iscsi_initiator, cg, storage_pool, vol,
    snapshot_schedule, nas_server, file_system, snapshot, nfs_export,
    smb_share, user_quota, tree_quota]
    type: list
    elements: str
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
       - nas_server
       - file_system
       - snapshot
       - nfs_export
       - smb_share
       - user_quota
       - tree_quota

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

 - name: Get list of NAS Servers on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - nas_server

 - name: Get list of File Systems on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - file_system

 - name: Get list of Snapshots on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - snapshot

 - name: Get list of NFS exports on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - nfs_export

 - name: Get list of SMB shares on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - smb_share

 - name: Get list of user quotas on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - user_quota

 - name: Get list of quota trees on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - tree_quota
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

NAS_Servers:
    description: Details of the NAS Servers.
    returned: When NAS Servers exist.
    type: complex
    contains:
        id:
            description: The ID of the NAS Server.
            type: str
        name:
            description: The name of the NAS Server.
            type: str

File_Systems:
    description: Details of the File Systems.
    returned: When File Systems exist.
    type: complex
    contains:
        id:
            description: The ID of the File System.
            type: str
        name:
            description: The name of the File System.
            type: str

Snapshots:
    description: Details of the Snapshots.
    returned: When Snapshots exist.
    type: complex
    contains:
        id:
            description: The ID of the Snapshot.
            type: str
        name:
            description: The name of the Snapshot.
            type: str

NFS_Exports:
    description: Details of the NFS Exports.
    returned: When NFS Exports exist.
    type: complex
    contains:
        id:
            description: The ID of the NFS Export.
            type: str
        name:
            description: The name of the NFS Export.
            type: str

SMB_Shares:
    description: Details of the SMB Shares.
    returned: When SMB Shares exist.
    type: complex
    contains:
        id:
            description: The ID of the SMB Share.
            type: str
        name:
            description: The name of the SMB Share.
            type: str

User_Quotas:
    description: Details of the user quotas.
    returned: When user quotas exist.
    type: complex
    contains:
        id:
            description: The ID of the user quota.
            type: str
        uid:
            description: The UID of the user quota.
            type: str

Tree_Quotas:
    description: Details of the quota trees.
    returned: When quota trees exist.
    type: complex
    contains:
        id:
            description: The ID of the quota tree.
            type: str
        path:
            description: The path of the quota tree.
            type: str
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import dellemc_ansible_unity_utils as utils

LOG = utils.get_logger('dellemc_unity_gatherfacts')
HAS_UNITY_SDK = utils.get_unity_sdk()
UNITY_SDK_VERSION_CHECK = utils.storops_version_check()

application_type = "Ansible/1.2.0"


class UnityGatherfacts(object):
    """Class with Gatherfacts operations"""

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_unity_management_host_parameters()
        self.module_params.update(get_unity_gatherfacts_parameters())

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

        self.unity = utils.get_unity_unisphere_connection(self.module.params,
                                                          application_type)
        LOG.info('Got the unity instance for provisioning on Unity')

    def get_array_details(self):
        """ Get the list of snapshot schedules on a given Unity storage
            system """

        try:
            LOG.info('Getting array details ')
            array_details = self.unity.info
            return array_details._get_properties()

        except utils.HttpError as e:
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
            return result_list(hosts)

        except Exception as e:
            msg = 'Get hosts list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_fc_initiators_list(self):
        """ Get the list of FC Initiators on a given Unity storage system """

        try:
            LOG.info('Getting FC initiators list ')
            fc_initiator = utils.host.UnityHostInitiatorList \
                .get(cli=self.unity._cli, type=utils.HostInitiatorTypeEnum.FC)
            return fc_initiators_result_list(fc_initiator)

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
            iscsi_initiator = utils.host.UnityHostInitiatorList \
                .get(cli=self.unity._cli, type=utils.HostInitiatorTypeEnum.
                     ISCSI)
            return iscsi_initiators_result_list(iscsi_initiator)

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
            consistency_groups = utils.cg.UnityConsistencyGroupList \
                .get(self.unity._cli)
            return result_list(consistency_groups)

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
            return result_list(storage_pools)

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
            return result_list(volumes)

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
            snapshot_schedules = utils.snap_schedule.UnitySnapScheduleList \
                .get(cli=self.unity._cli)
            return result_list(snapshot_schedules)

        except Exception as e:
            msg = 'Get snapshot schedules list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_nas_servers_list(self):
        """Get the list of NAS servers on a given Unity storage system"""

        try:
            LOG.info("Getting NAS servers list")
            nas_servers = self.unity.get_nas_server()
            return result_list(nas_servers)

        except Exception as e:
            msg = 'Get NAS servers list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_file_systems_list(self):
        """Get the list of file systems on a given Unity storage system"""

        try:
            LOG.info("Getting file systems list")
            file_systems = self.unity.get_filesystem()
            return result_list(file_systems)

        except Exception as e:
            msg = 'Get file systems list from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_snapshots_list(self):
        """Get the list of snapshots on a given Unity storage system"""

        try:
            LOG.info("Getting snapshots list")
            snapshots = self.unity.get_snap()
            return result_list(snapshots)

        except Exception as e:
            msg = 'Get snapshots from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_nfs_exports_list(self):
        """Get the list of NFS exports on a given Unity storage system"""

        try:
            LOG.info("Getting NFS exports list")
            nfs_exports = self.unity.get_nfs_share()
            return result_list(nfs_exports)

        except Exception as e:
            msg = 'Get NFS exports from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_smb_shares_list(self):
        """Get the list of SMB shares on a given Unity storage system"""

        try:
            LOG.info("Getting SMB shares list")
            smb_shares = self.unity.get_cifs_share()
            return result_list(smb_shares)

        except Exception as e:
            msg = 'Get SMB shares from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_user_quota_list(self):
        """Get the list of user quotas on a given Unity storage system"""

        try:
            LOG.info("Getting user quota list")
            user_quotas = self.unity.get_user_quota()
            return user_quota_result_list(user_quotas)

        except Exception as e:
            msg = 'Get user quotas from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_tree_quota_list(self):
        """Get the list of quota trees on a given Unity storage system"""

        try:
            LOG.info("Getting quota tree list")
            tree_quotas = self.unity.get_tree_quota()
            return tree_quota_result_list(tree_quotas)

        except Exception as e:
            msg = 'Get quota trees from unity array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        """ Perform different actions on Gatherfacts based on user parameter
            chosen in playbook """

        """ Get the array details a given Unity storage system """

        array_details = self.get_array_details()
        host = []
        fc_initiator = []
        iscsi_initiator = []
        cg = []
        storage_pool = []
        vol = []
        snapshot_schedule = []
        nas_server = []
        file_system = []
        snapshot = []
        nfs_export = []
        smb_share = []
        user_quota = []
        tree_quota = []

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
            if 'nas_server' in subset:
                nas_server = self.get_nas_servers_list()
            if 'file_system' in subset:
                file_system = self.get_file_systems_list()
            if 'snapshot' in subset:
                snapshot = self.get_snapshots_list()
            if 'nfs_export' in subset:
                nfs_export = self.get_nfs_exports_list()
            if 'smb_share' in subset:
                smb_share = self.get_smb_shares_list()
            if 'user_quota' in subset:
                user_quota = self.get_user_quota_list()
            if 'tree_quota' in subset:
                tree_quota = self.get_tree_quota_list()

        self.module.exit_json(
            Array_Details=array_details,
            Hosts=host,
            FC_initiators=fc_initiator,
            ISCSI_initiators=iscsi_initiator,
            Consistency_Groups=cg,
            Storage_Pools=storage_pool,
            Volumes=vol,
            Snapshot_Schedules=snapshot_schedule,
            NAS_Servers=nas_server,
            File_Systems=file_system,
            Snapshots=snapshot,
            NFS_Exports=nfs_export,
            SMB_Shares=smb_share,
            User_Quotas=user_quota,
            Tree_Quotas=tree_quota
        )


def result_list(entity):
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


def fc_initiators_result_list(entity):
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


def iscsi_initiators_result_list(entity):
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


def user_quota_result_list(entity):
    """ Get the id and uid associated with the Unity user quotas """
    result = []

    if entity:
        LOG.info('Successfully listed.')
        for item in entity:
            result.append(
                {
                    "uid": item.uid,
                    "id": item.id
                }
            )
        return result
    else:
        return None


def tree_quota_result_list(entity):
    """ Get the id and path associated with the Unity quota trees """
    result = []

    if entity:
        LOG.info('Successfully listed.')
        for item in entity:
            result.append(
                {
                    "path": item.path,
                    "id": item.id
                }
            )
        return result
    else:
        return None


def get_unity_gatherfacts_parameters():
    """This method provides parameters required for the ansible
    gatherfacts module on Unity"""
    return dict(gather_subset=dict(type='list', required=False,
                                   elements='str',
                                   choices=['host', 'fc_initiator',
                                            'iscsi_initiator', 'cg',
                                            'storage_pool', 'vol',
                                            'snapshot_schedule', 'nas_server',
                                            'file_system', 'snapshot',
                                            'nfs_export', 'smb_share',
                                            'user_quota', 'tree_quota']))


def main():
    """ Create Unity Gatherfacts object and perform action on it
        based on user input from playbook"""
    obj = UnityGatherfacts()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
