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
  Modify filesystem attributes,
  Display filesystem details,
  Display filesystem snapshots,
  Delete filesystem

extends_documentation_fragment:
  -  dellemc.unity.dellemc_unity.unity

author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>

options:
  filesystem_name:
    description:
    - The name of the filesystem. Mandatory only for create operation.
      All the operations are supported through 'filesystem_name'
    - It's mutually exclusive with 'filesystem_id'.
    required: False
    type: str
  filesystem_id:
    description:
    - The id of the filesystem.It's mutually exclusive with 'filesystem_name'
    - It can be used only for get, modify or delete operations.
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
  state:
    description:
    - State variable to determine whether filesystem will exist or not.
    choices: ['absent', 'present']
    required: true
    type: str

notes:
- SMB shares, NFS exports and snapshots associated with filesystem needs
  to be deleted prior to deleting a filesystem.
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
            description:
                - The system generated ID given to the filesystem
            type: str
        name:
            description:
                - Name of the filesystem
            type: str
        description:
            description:
                - description about the filesystem
            type: str
        is_data_reduction_enabled:
            description:
                - Whether or not compression enabled on this filesystem
            type: bool
        size_total_with_unit:
            description:
                - Size of the filesystem with actual unit.
            type: str
        tiering_policy:
            description:
                - Tiering policy applied to this filesystem
            type: str
        is_cifs_notify_on_access_enabled:
            description:
                - Indicates whether the system generates a notification when
                  a user accesses the file system.
            type: bool
        is_cifs_notify_on_write_enabled:
            description:
                - Indicates whether the system generates a notification when
                  the file system is written to.
            type: bool
        is_cifs_op_locks_enabled:
            description:
                - Indicates whether opportunistic file locks are enabled for
                  the file system.
            type: bool
        is_cifs_sync_writes_enabled:
            description:
                - Indicates whether the CIFS synchronous writes option is
                  enabled for the file system.
            type: bool
        cifs_notify_on_change_dir_depth:
            description:
                - Indicates the lowest directory level to which the enabled
                  notifications apply, if any.
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
                            description:
                                - The system ID given to the pool
                            type: str
                        name:
                            description:
                                - The name of the storage pool
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
                            description:
                                - The system ID given to the NAS Server
                            type: str
                        name:
                            description:
                                - The name of the NAS Server
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
                            description:
                                - The system ID given to the filesystem snapshot
                            type: str
                        name:
                            description:
                                - The name of the filesystem snapshot
                            type: str
        is_thin_enabled:
            description:
                - Indicates whether thin provisioning is enabled for this
                  filesystem
            type: bool

'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell\
    import dellemc_ansible_unity_utils as utils

LOG = utils.get_logger('dellemc_unity_filesystem')

HAS_UNITY_SDK = utils.get_unity_sdk()

UNITY_SDK_VERSION_CHECK = utils.storops_version_check()


class UnityFilesystem(object):

    """Class with FileSystem operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_unity_management_host_parameters()
        self.module_params.update(get_unity_filesystem_parameters())

        mutually_exclusive = [['filesystem_name', 'filesystem_id'],
                              ['pool_name', 'pool_id'],
                              ['nas_server_name', 'nas_server_id']]

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
            self.module.params)

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
            LOG.info("desc 1st check: %s", to_update)

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

            LOG.info("CIFS Modify Payload: %s", cifs_fs_payload)

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

            LOG.info("Modify Payload: %s", fs_update_payload)
            obj_fs = obj_fs.update()
            resp = obj_fs.modify(**fs_update_payload)
            LOG.info("Successfully modified the FS with response %s", resp)
            if resp:
                return True

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
                if key == "description":
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
        state = self.module.params['state']

        # result is a dictionary to contain end state and FileSystem details
        changed = False
        result = dict(
            changed=False,
            filesystem_details=None
        )

        to_modify_dict = None
        filesystem_details = None

        self.validate_input_string()

        if size is not None and size == 0:
            self.module.fail_json(msg="Size can not be 0 (Zero)")

        if size and not cap_unit:
            cap_unit = 'GB'

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

        if state == 'absent' and filesystem_details:
            changed = self.delete_filesystem(filesystem_id)
            filesystem_details = None

        if state == 'present' and filesystem_details:
            filesystem_details = self.get_filesystem_display_attributes(
                obj_fs=obj_fs)

        result['changed'] = changed
        result['filesystem_details'] = filesystem_details
        self.module.exit_json(**result)


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
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create Unity FileSystem object and perform action on it
        based on user input from playbook"""
    obj = UnityFilesystem()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
