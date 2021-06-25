#!/usr/bin/python
# Copyright: (c) 2020, DellEMC

"""Ansible module for managing FileSystem on Unity"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r"""

module: dellemc_unity_filesystem
version_added: '1.1.0'
short_description: Manage filesystem on Unity storage system
description:
- Managing filesystem on Unity storage system includes-
  Create new filesystem,
  Modify snapschedule attribute of filesystem
  Modify filesystem attributes,
  Display filesystem details,
  Display filesystem snapshots,
  Display filesystem snapschedule,
  Delete snapschedule associated with the filesystem,
  Delete filesystem,
  Create new filesystem with quota configuration

extends_documentation_fragment:
  -  dellemc.unity.dellemc_unity.unity

author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Meenakshi Dembi (@dembim) <ansible.team@dell.com>
- Spandita Panigrahi (@panigs7) <ansible.team@dell.com>

options:
  filesystem_name:
    description:
    - The name of the filesystem. Mandatory only for the create operation.
      All the operations are supported through 'filesystem_name'
    - It's mutually exclusive with 'filesystem_id'.
    required: False
    type: str
  filesystem_id:
    description:
    - The id of the filesystem.It's mutually exclusive with 'filesystem_name'
    - It can be used only for get, modify, or delete operations.
    required: False
    type: str
  pool_name:
    description:
    - This is the name of the pool where the filesystem will be created.
    - Either the pool_name or pool_id must be provided to create a new
      filesystem.
    type: str
  pool_id:
    description:
    - This is the ID of the pool where the filesystem will be created.
    - Either the pool_name or pool_id must be provided to create a new
      filesystem.
    type: str
  size:
    description:
     - The size of the filesystem.
    type: int
  cap_unit:
    description:
     - The unit of the filesystem size. It defaults to 'GB', if not specified.
    choices: ['GB' , 'TB']
    type: str
  nas_server_name:
    description:
    - Name of the NAS server on which filesystem will be hosted.
    type: str
  nas_server_id:
    description:
    - ID of the NAS server on which filesystem will be hosted.
    type: str
  supported_protocols:
    description:
    - Protocols supported by the file system.
    - It will be overridden by NAS server configuration if NAS Server is Multiprotocol
    type: str
    choices: ['NFS', 'CIFS', 'MULTIPROTOCOL']
  description:
    description:
    - Description about the filesystem.
    - Description can be removed by passing empty string ("").
    type: str
  smb_properties:
    description:
    - Advance settings for SMB. It contains optional candidate variables
    type: dict
    suboptions:
      is_smb_sync_writes_enabled:
        description:
        - Indicates whether the synchronous writes option is enabled on the
          file system.
        type: bool
      is_smb_notify_on_access_enabled:
        description:
        - Indicates whether notifications of changes to directory file
          structure are enabled.
        type: bool
      is_smb_op_locks_enabled:
        description:
        - Indicates whether opportunistic file locking is enabled on the file
          system.
        type: bool
      is_smb_notify_on_write_enabled:
        description:
        - Indicates whether file write notifications are enabled on the file
          system.
        type: bool
      smb_notify_on_change_dir_depth:
        description:
        - Integer variable, determines the lowest directory level to which
          the enabled notifications apply.
        - Minimum value is 1.
        type: int
  data_reduction:
    description:
    - Boolean variable, specifies whether or not to enable compression.
      Compression is supported only for thin filesystem
    type: bool
  is_thin:
    description:
    - Boolean variable, specifies whether or not it's a thin filesystem.
    type: bool
  access_policy:
    description:
    - Access policy of a filesystem.
    choices: ['NATIVE', 'UNIX', 'WINDOWS']
    type: str
  locking_policy:
    description:
    - File system locking policies. These policy choices control whether the
      NFSv4 range locks must be honored.
    type: str
    choices: ['ADVISORY', 'MANDATORY']
  tiering_policy:
    description:
    - Tiering policy choices for how the storage resource data will be
      distributed among the tiers available in the pool.
    choices: ['AUTOTIER_HIGH', 'AUTOTIER', 'HIGHEST', 'LOWEST']
    type: str
  quota_config:
    description:
    - Configuration for quota management. It contains optional parameters.
    type: dict
    suboptions:
        grace_period:
            description:
            - Grace period set in quota configuration after soft limit is reached.
            - If grace_period is not set during creation of filesystem,
              it will be set to '7 days' by default.
            type: int
        grace_period_unit:
            description:
            - Unit of grace period.
            - Default unit is 'days'.
            type: str
            choices: ['minutes', 'hours', 'days']
        default_hard_limit:
            description:
            - Default hard limit for user quotas and tree quotas.
            - If default_hard_limit is not set while creation of filesystem,
              it will be set to 0B by default.
            type: int
        default_soft_limit:
            description:
            - Default soft limit for user quotas and tree quotas.
            - If default_soft_limit is not set while creation of filesystem,
              it will be set to 0B by default.
            type: int
        is_user_quota_enabled:
            description:
            - Indicates whether the user quota is enabled.
            - Parameters 'is_user_quota_enabled' and 'quota_policy' are
              mutually exclusive.
            - If is_user_quota_enabled is not set while creation of filesystem,
              it will be set to false by default.
            type: bool
        quota_policy:
            description:
            - Quota policy set in quota configuration.
            - Parameters 'is_user_quota_enabled' and 'quota_policy' are
              mutually exclusive.
            - If quota_policy is not set while creation of filesystem, it will
              be set to "FILE_SIZE" by default.
            choices: ['FILE_SIZE','BLOCKS']
            type: str
        cap_unit:
            description:
            - Unit of default_soft_limit and default_hard_limit size.
            - Default unit is 'GB'.
            choices: ['MB', 'GB', 'TB']
            type: str
  state:
    description:
    - State variable to determine whether filesystem will exist or not.
    choices: ['absent', 'present']
    required: true
    type: str
  snap_schedule_name:
    description:
    - This is the name of an existing snapshot schedule which is to be associated with the filesystem.
      This is mutually exclusive with snapshot schedule id.
    required: false
    type: str
  snap_schedule_id:
    description:
    - This is the id of an existing snapshot schedule which is to be associated with the filesystem.
      This is mutually exclusive with snapshot schedule name.
      filesystem.
    required: false
    type: str

notes:
- SMB shares, NFS exports, and snapshots associated with filesystem need
  to be deleted prior to deleting a filesystem.
- quota_config parameter can be used to update default hard limit
  and soft limit values to limit the maximum space that can be used.
  By default they both are set to 0 during filesystem
  creation which means unlimited.
"""

EXAMPLES = r"""
- name: Create FileSystem
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    pool_name: "pool_1"
    size: 5
    state: "present"

- name: Create FileSystem with quota configuration
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    pool_name: "pool_1"
    size: 5
    quota_config:
        grace_period: 8
        grace_period_unit: "days"
        default_soft_limit: 10
        is_user_quota_enabled: False
    state: "present"

- name: Expand FileSystem size
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    size: 10
    state: "present"

- name: Expand FileSystem size
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    size: 10
    state: "present"

- name: Modify FileSystem smb_properties
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    smb_properties:
      is_smb_op_locks_enabled: True
      smb_notify_on_change_dir_depth: 5
      is_smb_notify_on_access_enabled: True
    state: "present"

- name: Modify FileSystem Snap Schedule
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_id: "fs_141"
    snap_schedule_id: "{{snap_schedule_id}}"
    state: "{{state_present}}"

- name: Get details of FileSystem using id
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_id: "rs_405"
    state: "present"

- name: Delete a FileSystem using id
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_id: "rs_405"
    state: "absent"
"""

RETURN = r'''
changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool

filesystem_details:
    description: Details of the filesystem
    returned: When filesystem exists
    type: complex
    contains:
        id:
            description: The system generated ID given to the filesystem
            type: str
        name:
            description: Name of the filesystem
            type: str
        description:
            description: Description about the filesystem
            type: str
        is_data_reduction_enabled:
            description: Whether or not compression enabled on this
                         filesystem
            type: bool
        size_total_with_unit:
            description: Size of the filesystem with actual unit.
            type: str
        tiering_policy:
            description: Tiering policy applied to this filesystem
            type: str
        is_cifs_notify_on_access_enabled:
            description: Indicates whether the system generates a
                         notification when a user accesses the file system.
            type: bool
        is_cifs_notify_on_write_enabled:
            description: Indicates whether the system generates a notification
                         when the file system is written to.
            type: bool
        is_cifs_op_locks_enabled:
            description: Indicates whether opportunistic file locks are enabled
                         for the file system.
            type: bool
        is_cifs_sync_writes_enabled:
            description: Indicates whether the CIFS synchronous writes option
                         is enabled for the file system.
            type: bool
        cifs_notify_on_change_dir_depth:
            description: Indicates the lowest directory level to which the
                         enabled notifications apply, if any.
            type: int
        pool:
            description: The pool in which this filesystem is allocated
            type: complex
            contains:
                UnityPool:
                    description: Unity pool in which this filesystem is
                                 allocated
                    type: complex
                    contains:
                        id:
                            description: The system ID given to the pool
                            type: str
                        name:
                            description: The name of the storage pool
                            type: str
        nas_server:
            description: The NAS Server details on which this filesystem is hosted.
            type: complex
            contains:
                nas_server:
                    description: nas_server details.
                    type: complex
                    contains:
                        id:
                            description: The system ID given to the NAS Server
                            type: str
                        name:
                            description: The name of the NAS Server
                            type: str
        snap_list:
            description: The list of snapshots of this filesystem.
            type: list
            contains:
                snap_list:
                    description: Filesystem snapshots.
                    type: complex
                    contains:
                        id:
                            description: The system ID given to the filesystem
                                         snapshot
                            type: str
                        name:
                            description: The name of the filesystem snapshot
                            type: str
        is_thin_enabled:
            description: Indicates whether thin provisioning is enabled for
                         this filesystem
            type: bool
        snap_schedule_id:
            description: Indicates the id of the snap schedule associated
                         with the filesystem
            type: str
        snap_schedule_name:
            description: Indicates the name of the snap schedule associated
                         with the filesystem
            type: str
        quota_config:
            description: Details of quota configuration of the filesystem
                         created.
            type: complex
            contains:
                grace_period:
                    description: Grace period set in quota configuration
                                 after soft limit is reached.
                    type: str
                default_hard_limit:
                    description: Default hard limit for user quotas
                                 and tree quotas.
                    type: int
                default_soft_limit:
                    description: Default soft limit for user quotas
                                 and tree quotas.
                    type: int
                is_user_quota_enabled:
                    description: Indicates whether the user quota is enabled.
                    type: bool
                quota_policy:
                    description: Quota policy set in quota configuration.
                    type: str

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import dellemc_ansible_unity_utils as utils

LOG = utils.get_logger('dellemc_unity_filesystem')

HAS_UNITY_SDK = utils.get_unity_sdk()

UNITY_SDK_VERSION_CHECK = utils.storops_version_check()

application_type = "Ansible/1.2.0"


class UnityFilesystem(object):
    """Class with FileSystem operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_unity_management_host_parameters()
        self.module_params.update(get_unity_filesystem_parameters())

        mutually_exclusive = [['filesystem_name', 'filesystem_id'],
                              ['pool_name', 'pool_id'],
                              ['nas_server_name', 'nas_server_id'],
                              ['snap_schedule_name', 'snap_schedule_id']]

        required_one_of = [['filesystem_name', 'filesystem_id']]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of)

        if not HAS_UNITY_SDK:
            self.module.fail_json(msg="Ansible modules for Unity require the"
                                      " Unity python library to be "
                                      "installed. Please install the library "
                                      "before using these modules.")

        if UNITY_SDK_VERSION_CHECK and not UNITY_SDK_VERSION_CHECK[
           'supported_version']:
            err_msg = UNITY_SDK_VERSION_CHECK['unsupported_version_message']
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        self.unity_conn = utils.get_unity_unisphere_connection(
            self.module.params, application_type)

    def get_filesystem(self, name=None, id=None, obj_nas_server=None):
        """Get the details of a FileSystem.
            :param filesystem_name: The name of the filesystem
            :param filesystem_id: The id of the filesystem
            :param obj_nas_server: NAS Server object instance
            :return: instance of the respective filesystem if exist.
        """

        id_or_name = id if id else name
        errormsg = "Failed to get the filesystem {0} with error {1}"

        try:
            obj_fs = None
            if id:
                if obj_nas_server:
                    obj_fs = self.unity_conn.get_filesystem(
                        _id=id,
                        nas_server=obj_nas_server)
                else:
                    obj_fs = self.unity_conn.get_filesystem(_id=id)

                if obj_fs and obj_fs.existed:
                    LOG.info("Successfully got the filesystem "
                             "object %s ", obj_fs)
                    return obj_fs
            elif name:
                if not obj_nas_server:
                    err_msg = "NAS Server is required to get the FileSystem"
                    LOG.error(err_msg)
                    self.module.fail_json(msg=err_msg)

                obj_fs = self.unity_conn.get_filesystem(
                    name=name,
                    nas_server=obj_nas_server)
                if obj_fs:
                    LOG.info(
                        "Successfully got the filesystem object %s ", obj_fs)
                    return obj_fs
            else:
                LOG.info("Failed to get the filesystem %s", id_or_name)
            return None

        except utils.HttpError as e:
            if e.http_status == 401:
                cred_err = "Incorrect username or password , {0}".format(
                    e.message)
                msg = errormsg.format(id_or_name, cred_err)
                self.module.fail_json(msg=msg)
            else:
                msg = errormsg.format(id_or_name, str(e))
                self.module.fail_json(msg=msg)

        except utils.UnityResourceNotFoundError as e:
            errormsg.format(id_or_name, str(e))
            LOG.error(errormsg)
            return None

        except Exception as e:
            msg = errormsg.format(id_or_name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_nas_server(self, name=None, id=None):
        """Get the instance of a NAS Server.
            :param name: The NAS Server name
            :param id: The NAS Server id
            :return: instance of the respective NAS Server if exists.
        """

        errormsg = "Failed to get the NAS Server {0} with error {1}"
        id_or_name = name if name else id

        try:
            obj_nas = self.unity_conn.get_nas_server(_id=id, name=name)
            if id and obj_nas.existed:
                LOG.info("Successfully got the nas server object %s",
                         obj_nas)
                return obj_nas
            elif name:
                LOG.info("Successfully got the nas server object %s ",
                         obj_nas)
                return obj_nas
            else:
                msg = "Failed to get the nas server with {0}".format(
                    id_or_name)
                LOG.error(msg)
                self.module.fail_json(msg=msg)

        except Exception as e:
            msg = errormsg.format(name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_pool(self, pool_name=None, pool_id=None):
        """Get the instance of a pool.
            :param pool_name: The name of the pool
            :param pool_id: The id of the pool
            :return: Dict containing pool details if exists
        """

        id_or_name = pool_id if pool_id else pool_name
        errormsg = "Failed to get the pool {0} with error {1}"

        try:
            obj_pool = self.unity_conn.get_pool(name=pool_name, _id=pool_id)

            if pool_id and obj_pool.existed:
                LOG.info("Successfully got the pool object %s",
                         obj_pool)
                return obj_pool
            if pool_name:
                LOG.info("Successfully got pool %s", obj_pool)
                return obj_pool
            else:
                msg = "Failed to get the pool with {0}".format(
                    id_or_name)
                LOG.error(msg)
                self.module.fail_json(msg=msg)

        except Exception as e:
            msg = errormsg.format(id_or_name, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_tiering_policy_enum(self, tiering_policy):
        """Get the tiering_policy enum.
             :param tiering_policy: The tiering_policy string
             :return: tiering_policy enum
        """

        if tiering_policy in utils.TieringPolicyEnum.__members__:
            return utils.TieringPolicyEnum[tiering_policy]
        else:
            errormsg = "Invalid choice {0} for tiering policy".format(
                tiering_policy)
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_supported_protocol_enum(self, supported_protocol):
        """Get the supported_protocol enum.
             :param supported_protocol: The supported_protocol string
             :return: supported_protocol enum
        """

        supported_protocol = "MULTI_PROTOCOL" if \
            supported_protocol == "MULTIPROTOCOL" else supported_protocol
        if supported_protocol in utils.FSSupportedProtocolEnum.__members__:
            return utils.FSSupportedProtocolEnum[supported_protocol]
        else:
            errormsg = "Invalid choice {0} for supported_protocol".format(
                supported_protocol)
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_locking_policy_enum(self, locking_policy):
        """Get the locking_policy enum.
             :param locking_policy: The locking_policy string
             :return: locking_policy enum
        """
        if locking_policy in utils.FSLockingPolicyEnum.__members__:
            return utils.FSLockingPolicyEnum[locking_policy]
        else:
            errormsg = "Invalid choice {0} for locking_policy".format(
                locking_policy)
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_access_policy_enum(self, access_policy):
        """Get the access_policy enum.
             :param access_policy: The access_policy string
             :return: access_policy enum
        """
        if access_policy in utils.AccessPolicyEnum.__members__:
            return utils.AccessPolicyEnum[access_policy]
        else:
            errormsg = "Invalid choice {0} for access_policy".format(
                access_policy)
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def create_filesystem(self, name, obj_pool, obj_nas_server, size):
        """Create a FileSystem.
            :param name: Name of the FileSystem
            :param obj_pool: Storage Pool obj instance
            :param obj_nas_server: NAS Server obj instance
            :param size: Total size of a filesystem in bytes
            :return: FileSystem object on successful creation
        """
        try:

            supported_protocol = self.module.params['supported_protocols']
            supported_protocol = self.get_supported_protocol_enum(
                supported_protocol) if supported_protocol else None
            is_thin = self.module.params['is_thin']

            tiering_policy = self.module.params['tiering_policy']
            tiering_policy = self.get_tiering_policy_enum(tiering_policy) \
                if tiering_policy else None

            obj_fs = utils.UnityFileSystem.create(
                self.unity_conn._cli,
                pool=obj_pool,
                nas_server=obj_nas_server,
                name=name,
                size=size,
                proto=supported_protocol,
                is_thin=is_thin,
                tiering_policy=tiering_policy)

            LOG.info("Successfully created file system , %s", obj_fs)
            return obj_fs

        except Exception as e:
            errormsg = "Create filesystem {0} operation  failed" \
                       " with error {1}".format(name, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def delete_filesystem(self, id):
        """Delete a FileSystem.
        :param id: The object instance of the filesystem to be deleted
        """

        try:
            obj_fs = self.get_filesystem(id=id)
            obj_fs_dict = obj_fs._get_properties()
            if obj_fs_dict['cifs_share'] is not None:
                errormsg = "The Filesystem has SMB Shares. Hence deleting " \
                           "this filesystem is not safe."
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)
            if obj_fs_dict['nfs_share'] is not None:
                errormsg = "The FileSystem has NFS Exports. Hence deleting " \
                           "this filesystem is not safe."
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)
            obj_fs.delete()
            return True

        except Exception as e:
            errormsg = "Delete operation of FileSystem id:{0} " \
                       "failed with error {1}".format(id,
                                                      str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def is_modify_required(self, obj_fs, cap_unit):
        """Checks if any modify required for filesystem attributes
        :param obj_fs: filesystem instance
        :param cap_unit: capacity unit
        :return: filesystem to update dict
        """
        try:
            to_update = {}
            obj_fs = obj_fs.update()
            description = self.module.params['description']

            if description is not None and description != obj_fs.description:
                to_update.update({'description': description})

            size = self.module.params['size']
            if size and cap_unit:
                size_byte = int(utils.get_size_bytes(size, cap_unit))
                if size_byte < obj_fs.size_total:
                    self.module.fail_json(msg="Filesystem size can be "
                                              "expanded only")
                elif size_byte > obj_fs.size_total:
                    to_update.update({'size': size_byte})

            tiering_policy = self.module.params['tiering_policy']
            if tiering_policy and self.get_tiering_policy_enum(
                    tiering_policy) != obj_fs.tiering_policy:
                to_update.update({'tiering_policy':
                                  self.get_tiering_policy_enum(
                                      tiering_policy)})

            is_thin = self.module.params['is_thin']
            if is_thin is not None and is_thin != obj_fs.is_thin_enabled:
                to_update.update({'is_thin': is_thin})

            data_reduction = self.module.params['data_reduction']
            if data_reduction is not None and \
                    data_reduction != obj_fs.is_data_reduction_enabled:
                to_update.update({'is_compression': data_reduction})

            access_policy = self.module.params['access_policy']
            if access_policy and self.get_access_policy_enum(
                    access_policy) != obj_fs.access_policy:
                to_update.update({'access_policy':
                                  self.get_access_policy_enum(access_policy)})

            locking_policy = self.module.params['locking_policy']
            if locking_policy and self.get_locking_policy_enum(
                    locking_policy) != obj_fs.locking_policy:
                to_update.update({'locking_policy':
                                  self.get_locking_policy_enum(
                                      locking_policy)})

            snap_sch = obj_fs.storage_resource.snap_schedule

            if self.snap_sch_id is not None:
                if self.snap_sch_id == "":
                    if snap_sch and snap_sch.id != self.snap_sch_id:
                        to_update.update({'is_snap_schedule_paused': False})
                elif snap_sch is None or snap_sch.id != self.snap_sch_id:
                    to_update.update({'snap_sch_id': self.snap_sch_id})

            smb_properties = self.module.params['smb_properties']
            if smb_properties:
                sync_writes_enabled = \
                    smb_properties['is_smb_sync_writes_enabled']
                oplocks_enabled = \
                    smb_properties['is_smb_op_locks_enabled']
                notify_on_write = \
                    smb_properties['is_smb_notify_on_write_enabled']
                notify_on_access = \
                    smb_properties['is_smb_notify_on_access_enabled']
                notify_on_change_dir_depth = \
                    smb_properties['smb_notify_on_change_dir_depth']

                if sync_writes_enabled is not None and \
                        sync_writes_enabled != obj_fs.is_cifs_sync_writes_enabled:
                    to_update.update(
                        {'is_cifs_sync_writes_enabled': sync_writes_enabled})

                if oplocks_enabled is not None and \
                        oplocks_enabled != obj_fs.is_cifs_op_locks_enabled:
                    to_update.update(
                        {'is_cifs_op_locks_enabled': oplocks_enabled})

                if notify_on_write is not None and \
                        notify_on_write != \
                        obj_fs.is_cifs_notify_on_write_enabled:
                    to_update.update(
                        {'is_cifs_notify_on_write_enabled': notify_on_write})

                if notify_on_access is not None and \
                        notify_on_access != \
                        obj_fs.is_cifs_notify_on_access_enabled:
                    to_update.update(
                        {'is_cifs_notify_on_access_enabled':
                         notify_on_access})

                if notify_on_change_dir_depth is not None and \
                        notify_on_change_dir_depth != \
                        obj_fs.cifs_notify_on_change_dir_depth:
                    to_update.update(
                        {'cifs_notify_on_change_dir_depth':
                         notify_on_change_dir_depth})
            if len(to_update) > 0:
                return to_update
            else:
                return None

        except Exception as e:
            errormsg = "Failed to determine if FileSystem id: {0}" \
                       " modification required with error {1}".format(obj_fs.id,
                                                                      str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def modify_filesystem(self, update_dict, obj_fs):
        """ modifes attributes for a filesystem instance
        :param update_dict: modify dict
        :return: True on Success
        """
        try:
            adv_smb_params = [
                'is_cifs_sync_writes_enabled',
                'is_cifs_op_locks_enabled',
                'is_cifs_notify_on_write_enabled',
                'is_cifs_notify_on_access_enabled',
                'cifs_notify_on_change_dir_depth']

            cifs_fs_payload = {}
            fs_update_payload = {}

            for smb_param in adv_smb_params:
                if smb_param in update_dict.keys():
                    cifs_fs_payload.update({smb_param: update_dict[smb_param]})

            LOG.debug("CIFS Modify Payload: %s", cifs_fs_payload)

            cifs_fs_parameters = obj_fs.prepare_cifs_fs_parameters(
                **cifs_fs_payload)

            fs_update_params = [
                'size',
                'is_thin',
                'tiering_policy',
                'is_compression',
                'access_policy',
                'locking_policy',
                'description',
                'cifs_fs_parameters']

            for fs_param in fs_update_params:
                if fs_param in update_dict.keys():
                    fs_update_payload.update({fs_param: update_dict[fs_param]})

            if cifs_fs_parameters:
                fs_update_payload.update(
                    {'cifs_fs_parameters': cifs_fs_parameters})

            if "snap_sch_id" in update_dict.keys():
                fs_update_payload.update(
                    {'snap_schedule_parameters': {'snapSchedule':
                     {'id': update_dict.get('snap_sch_id')}
                    }}
                )
            elif "is_snap_schedule_paused" in update_dict.keys():
                fs_update_payload.update(
                    {'snap_schedule_parameters': {'isSnapSchedulePaused': False}
                     })

            obj_fs = obj_fs.update()
            resp = obj_fs.modify(**fs_update_payload)
            LOG.info("Successfully modified the FS with response %s", resp)
            changed = True if resp else False

        except Exception as e:
            errormsg = "Failed to modify FileSystem instance id: {0}" \
                       " with error {1}".format(obj_fs.id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_filesystem_display_attributes(self, obj_fs):
        """get display filesystem attributes
        :param obj_fs: filesystem instance
        :return: filesystem dict to display
        """
        try:
            obj_fs = obj_fs.update()
            filesystem_details = obj_fs._get_properties()
            filesystem_details['size_total_with_unit'] = utils. \
                convert_size_with_unit(int(filesystem_details['size_total']))
            if obj_fs.pool:
                filesystem_details.update(
                    {'pool': {'name': obj_fs.pool.name,
                              'id': obj_fs.pool.id}})
            if obj_fs.nas_server:
                filesystem_details.update(
                    {'nas_server': {'name': obj_fs.nas_server.name,
                                    'id': obj_fs.nas_server.id}})
            snap_list = []
            if obj_fs.has_snap():
                for snap in obj_fs.snapshots:
                    d = {'name': snap.name, 'id': snap.id}
                    snap_list.append(d)
            filesystem_details['snapshots'] = snap_list

            if obj_fs.storage_resource.snap_schedule:
                filesystem_details['snap_schedule_id'] = obj_fs.storage_resource.snap_schedule.id
                filesystem_details['snap_schedule_name'] = obj_fs.storage_resource.snap_schedule.name

            quota_config_obj = self.get_quota_config_details(obj_fs)

            if quota_config_obj:

                hard_limit = utils.convert_size_with_unit(
                    quota_config_obj.default_hard_limit)
                soft_limit = utils.convert_size_with_unit(
                    quota_config_obj.default_soft_limit)
                grace_period = get_time_with_unit(
                    quota_config_obj.grace_period)

                filesystem_details.update({'quota_config':
                                          {'id': quota_config_obj.id,
                                           'default_hard_limit': hard_limit,
                                           'default_soft_limit': soft_limit,
                                           'is_user_quota_enabled':
                                               quota_config_obj.is_user_quota_enabled,
                                           'quota_policy': quota_config_obj._get_properties()[
                                               'quota_policy'],
                                           'grace_period': grace_period}
                                           })
            return filesystem_details

        except Exception as e:
            errormsg = "Failed to display the filesystem {0} with " \
                       "error {1}".format(obj_fs.name, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def validate_input_string(self):
        """ validates the input string checks if it's empty string """
        invalid_string = ""
        try:
            for key in self.module.params:
                val = self.module.params[key]
                if key == "description" or key == "snap_schedule_name" \
                          or key == "snap_schedule_id":
                    continue
                if isinstance(val, str) \
                        and val == invalid_string:
                    errmsg = 'Invalid input parameter "" for {0}'.format(
                        key)
                    self.module.fail_json(msg=errmsg)

        except Exception as e:
            errormsg = "Failed to validate the module param with " \
                       "error {0}".format(str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def resolve_to_snapschedule_id(self, params):
        """ Get snapshot id for a give snap schedule name
        :param params: snap schedule name or id
        :return: snap schedule id after validation
        """

        try:
            snap_sch_id = None
            snapshot_schedule = {}
            if params["name"]:
                snapshot_schedule = utils.UnitySnapScheduleList.get(self.unity_conn._cli, name=params["name"])
            elif params["id"]:
                snapshot_schedule = utils.UnitySnapScheduleList.get(self.unity_conn._cli, id=params["id"])

            if snapshot_schedule:
                snap_sch_id = snapshot_schedule.id[0]

            if not snap_sch_id:
                errormsg = "Failed to find the snapshot schedule id against given name " \
                           "or id: {0}".format(params["name"]), (params["id"])
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)

            return snap_sch_id

        except Exception as e:
            errormsg = "Failed to find the snapshot schedules with " \
                       "error {0}".format(str(e))

    def get_quota_config_details(self, obj_fs):
        """
        Get the quota config ID mapped to the filesystem
        :param obj_fs: Filesystem instance
        :return: Quota config object if exists else None
        """
        try:
            all_quota_config = self.unity_conn.get_quota_config(filesystem=obj_fs)
            fs_id = obj_fs.id

            if len(all_quota_config) == 0:
                LOG.error("The quota_config object for new filesystem "
                          "is not updated yet.")
                return None

            for quota_config in range(len(all_quota_config)):
                if fs_id and all_quota_config[quota_config].filesystem.id == fs_id and \
                        not all_quota_config[quota_config].tree_quota:
                    msg = "Quota config id for filesystem %s is %s" \
                          % (fs_id, all_quota_config[quota_config].id)
                    LOG.info(msg)
                    return all_quota_config[quota_config]

        except Exception as e:
            errormsg = "Failed to fetch quota config for filesystem {0} " \
                       " with error {1}".format(fs_id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def modify_quota_config(self, quota_config_obj, quota_config_params):
        """
        Modify default quota config settings of newly created filesystem.
        The default setting of quota config after filesystem creation is:
        default_soft_limit and default_hard_limit are 0,
        is_user_quota_enabled is false,
        grace_period is 7 days and,
        quota_policy is FILE_SIZE.
        :param quota_config_obj: Quota config instance
        :param quota_config_params: Quota config parameters to be modified
        :return: Boolean whether quota config is modified
        """

        if quota_config_params:
            soft_limit = quota_config_params['default_soft_limit']
            hard_limit = quota_config_params['default_hard_limit']
            is_user_quota_enabled = quota_config_params['is_user_quota_enabled']
            quota_policy = quota_config_params['quota_policy']
            grace_period = quota_config_params['grace_period']
            cap_unit = quota_config_params['cap_unit']
            gp_unit = quota_config_params['grace_period_unit']

        if soft_limit:
            soft_limit_in_bytes = utils.get_size_bytes(soft_limit, cap_unit)
        else:
            soft_limit_in_bytes = quota_config_obj.default_soft_limit

        if hard_limit:
            hard_limit_in_bytes = utils.get_size_bytes(hard_limit, cap_unit)
        else:
            hard_limit_in_bytes = quota_config_obj.default_hard_limit

        if grace_period:
            grace_period_in_sec = get_time_in_seconds(grace_period, gp_unit)
        else:
            grace_period_in_sec = quota_config_obj.grace_period

        policy_enum = None
        policy_enum_val = None
        if quota_policy:
            if utils.QuotaPolicyEnum[quota_policy]:
                policy_enum = utils.QuotaPolicyEnum[quota_policy]
                policy_enum_val = \
                    utils.QuotaPolicyEnum[quota_policy]._get_properties()['value']
            else:
                errormsg = "Invalid choice {0} for quota policy".format(
                    quota_policy)
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)

        # Verify if modify is required. If not required, return False
        if quota_config_obj.default_hard_limit == hard_limit_in_bytes and \
                quota_config_obj.default_soft_limit == soft_limit_in_bytes and \
                quota_config_obj.grace_period == grace_period_in_sec and \
                ((quota_policy is not None and
                  quota_config_obj.quota_policy == policy_enum) or
                 quota_policy is None) and \
                (is_user_quota_enabled is None or
                 (is_user_quota_enabled is not None and
                  is_user_quota_enabled == quota_config_obj.is_user_quota_enabled)):
            return False

        try:
            resp = self.unity_conn.modify_quota_config(
                quota_config_id=quota_config_obj.id,
                grace_period=grace_period_in_sec,
                default_hard_limit=hard_limit_in_bytes,
                default_soft_limit=soft_limit_in_bytes,
                is_user_quota_enabled=is_user_quota_enabled,
                quota_policy=policy_enum_val)
            LOG.info("Successfully modified the quota config with response %s", resp)
            return True

        except Exception as e:
            errormsg = "Failed to modify quota config for filesystem {0} " \
                       " with error {1}".format(quota_config_obj.filesystem.id, str(e))
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def perform_module_operation(self):
        """
        Perform different actions on filesystem module based on parameters
        passed in the playbook
        """
        filesystem_name = self.module.params['filesystem_name']
        filesystem_id = self.module.params['filesystem_id']
        nas_server_name = self.module.params['nas_server_name']
        nas_server_id = self.module.params['nas_server_id']
        pool_name = self.module.params['pool_name']
        pool_id = self.module.params['pool_id']
        size = self.module.params['size']
        cap_unit = self.module.params['cap_unit']
        quota_config = self.module.params['quota_config']
        state = self.module.params['state']
        snap_schedule_name = self.module.params['snap_schedule_name']
        snap_schedule_id = self.module.params['snap_schedule_id']

        # result is a dictionary to contain end state and FileSystem details
        changed = False
        result = dict(
            changed=False,
            filesystem_details=None
        )

        to_modify_dict = None
        filesystem_details = None
        quota_config_obj = None

        self.validate_input_string()

        if size is not None and size == 0:
            self.module.fail_json(msg="Size can not be 0 (Zero)")

        if size and not cap_unit:
            cap_unit = 'GB'

        if quota_config:
            if (quota_config['default_hard_limit'] is not None
                or quota_config['default_soft_limit'] is not None) and \
                    not quota_config['cap_unit']:
                quota_config['cap_unit'] = 'GB'

            if quota_config['grace_period'] is not None \
                    and quota_config['grace_period_unit'] is None:
                quota_config['grace_period_unit'] = 'days'

            if quota_config['grace_period'] is not None \
                    and quota_config['grace_period'] <= 0:
                self.module.fail_json(msg="Invalid grace_period provided. "
                                          "Must be greater than 0.")

            if quota_config['default_soft_limit'] is not None \
                    and utils.is_size_negative(quota_config['default_soft_limit']):
                self.module.fail_json(msg="Invalid default_soft_limit provided. "
                                          "Must be greater than or equal to 0.")

            if quota_config['default_hard_limit'] is not None \
                    and utils.is_size_negative(quota_config['default_hard_limit']):
                self.module.fail_json(msg="Invalid default_hard_limit provided. "
                                          "Must be greater than or equal to 0.")

        if (cap_unit is not None) and not size:
            self.module.fail_json(msg="cap_unit can be specified along "
                                      "with size")

        nas_server = None
        if nas_server_name or nas_server_id:
            nas_server = self.get_nas_server(
                name=nas_server_name, id=nas_server_id)

        obj_pool = None
        if pool_name or pool_id:
            obj_pool = self.get_pool(pool_name=pool_name, pool_id=pool_id)

        obj_fs = None
        obj_fs = self.get_filesystem(name=filesystem_name,
                                     id=filesystem_id,
                                     obj_nas_server=nas_server)

        self.snap_sch_id = None
        if snap_schedule_name or snap_schedule_id:
            snap_schedule_params = {
                "name": snap_schedule_name,
                "id": snap_schedule_id
            }
            self.snap_sch_id = self.resolve_to_snapschedule_id(snap_schedule_params)
        elif snap_schedule_name == "" or snap_schedule_id == "":
            self.snap_sch_id = ""

        if obj_fs:
            filesystem_details = obj_fs._get_properties()
            filesystem_id = obj_fs.get_id()
            to_modify_dict = self.is_modify_required(obj_fs, cap_unit)
            LOG.info("From Mod Op, to_modify_dict: %s", to_modify_dict)

        if state == 'present' and not filesystem_details:
            if not filesystem_name:
                msg_noname = "FileSystem with id {0} is not found, unable to " \
                             "create a FileSystem without a valid " \
                             "filesystem_name".format(filesystem_id)
                self.module.fail_json(msg=msg_noname)

            if not pool_name and not pool_id:
                self.module.fail_json(msg="pool_id or pool_name is required "
                                          "to create new filesystem")
            if not size:
                self.module.fail_json(msg="Size is required to create"
                                          " a filesystem")
            size = utils.get_size_bytes(size, cap_unit)

            obj_fs = self.create_filesystem(name=filesystem_name,
                                            obj_pool=obj_pool,
                                            obj_nas_server=nas_server,
                                            size=size)

            LOG.debug("Successfully created filesystem , %s", obj_fs)
            filesystem_id = obj_fs.id
            filesystem_details = obj_fs._get_properties()
            to_modify_dict = self.is_modify_required(obj_fs, cap_unit)
            LOG.debug("Got filesystem id , %s", filesystem_id)
            changed = True

        if state == 'present' and filesystem_details and to_modify_dict:
            self.modify_filesystem(update_dict=to_modify_dict, obj_fs=obj_fs)
            changed = True

        """
        Set quota configuration
        """
        if state == "present" and filesystem_details and quota_config:
            quota_config_obj = self.get_quota_config_details(obj_fs)

            if quota_config_obj is not None:
                is_quota_config_modified = self.modify_quota_config(
                    quota_config_obj=quota_config_obj,
                    quota_config_params=quota_config)

                if is_quota_config_modified:
                    changed = True
            else:
                self.module.fail_json(msg="One or more operations related"
                                          " to this task failed because the"
                                          " new object created could not be fetched."
                                          " Please rerun the task for expected result.")

        if state == 'absent' and filesystem_details:
            changed = self.delete_filesystem(filesystem_id)
            filesystem_details = None

        if state == 'present' and filesystem_details:
            filesystem_details = self.get_filesystem_display_attributes(
                obj_fs=obj_fs)

        result['changed'] = changed
        result['filesystem_details'] = filesystem_details
        self.module.exit_json(**result)


def get_time_in_seconds(time, time_units):
    """This method get time is seconds"""
    min_in_sec = 60
    hour_in_sec = 60 * 60
    day_in_sec = 24 * 60 * 60
    if time is not None and time > 0:
        if time_units in 'minutes':
            return time * min_in_sec
        elif time_units in 'hours':
            return time * hour_in_sec
        elif time_units in 'days':
            return time * day_in_sec
        else:
            return time
    else:
        return 0


def get_time_with_unit(time):
    """This method sets seconds in minutes, hours or days."""
    sec_in_min = 60
    sec_in_hour = 60 * 60
    sec_in_day = 24 * 60 * 60

    if time % sec_in_day == 0:
        time = time / sec_in_day
        unit = 'days'

    elif time % sec_in_hour == 0:
        time = time / sec_in_hour
        unit = 'hours'

    else:
        time = time / sec_in_min
        unit = 'minutes'
    return "%s %s" % (time, unit)


def get_unity_filesystem_parameters():
    """This method provide parameters required for the ansible filesystem
       module on Unity"""
    return dict(
        filesystem_name=dict(required=False, type='str'),
        filesystem_id=dict(required=False, type='str'),
        nas_server_name=dict(required=False, type='str'),
        nas_server_id=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        pool_name=dict(required=False, type='str'),
        pool_id=dict(required=False, type='str'),
        size=dict(required=False, type='int'),
        cap_unit=dict(required=False, type='str', choices=['GB', 'TB']),
        is_thin=dict(required=False, type='bool'),
        data_reduction=dict(required=False, type='bool'),
        supported_protocols=dict(required=False, type='str',
                                 choices=['NFS', 'CIFS', 'MULTIPROTOCOL']),
        smb_properties=dict(type='dict', options=dict(
            is_smb_sync_writes_enabled=dict(type='bool'),
            is_smb_notify_on_access_enabled=dict(type='bool'),
            is_smb_op_locks_enabled=dict(type='bool'),
            is_smb_notify_on_write_enabled=dict(type='bool'),
            smb_notify_on_change_dir_depth=dict(type='int')
        )),
        access_policy=dict(required=False, type='str',
                           choices=['NATIVE', 'UNIX', 'WINDOWS']),
        locking_policy=dict(required=False, type='str',
                            choices=['ADVISORY', 'MANDATORY']),
        tiering_policy=dict(required=False, type='str', choices=[
            'AUTOTIER_HIGH', 'AUTOTIER', 'HIGHEST', 'LOWEST']),
        snap_schedule_name=dict(required=False, type='str'),
        snap_schedule_id=dict(required=False, type='str'),
        quota_config=dict(required=False, type='dict', options=dict(
            grace_period=dict(required=False, type='int'),
            grace_period_unit=dict(required=False, type='str', choices=['minutes', 'hours', 'days']),
            default_hard_limit=dict(required=False, type='int'),
            default_soft_limit=dict(required=False, type='int'),
            is_user_quota_enabled=dict(required=False, type='bool'),
            quota_policy=dict(required=False, type='str', choices=['FILE_SIZE', 'BLOCKS']),
            cap_unit=dict(required=False, type='str', choices=['MB', 'GB', 'TB']),
        ), mutually_exclusive=[['is_user_quota_enabled', 'quota_policy']]),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create Unity FileSystem object and perform action on it
        based on user input from playbook"""
    obj = UnityFilesystem()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
