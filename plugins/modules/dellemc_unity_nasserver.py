#!/usr/bin/python
# Copyright: (c) 2020, DellEMC
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_unity_nasserver
version_added: '1.1.0'
short_description:  Manage NAS servers on Unity storage system
extends_documentation_fragment:
- dellemc.unity.dellemc_unity.unity
author:
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>
description:
- Managing NAS servers on Unity storage system includes get,
  modification to the NAS servers.
options:
  nas_server_id:
    description:
    - The ID of the NAS server.
    - nas_server_name and nas_server_id are mutually exclusive parameters.
    - Either one is required to perform the task.
    type: str
  nas_server_name:
    description:
    - The Name of the NAS server.
    - nas_server_name and nas_server_id are mutually exclusive parameters.
    - Either one  is required to perform the task.
    type: str
  nas_server_new_name:
    description:
    - The new name of the NAS server.
    - It can be mentioned during modification of the NAS server.
    type: str
  is_replication_destination:
    description:
    - It specifies whether the NAS server is a replication destination.
    - It can be mentioned during modification of the NAS server.
    type: bool
  is_backup_only:
    description:
    - It specifies whether the NAS server is used as backup only.
    - It can be mentioned during modification of the NAS server.
    type: bool
  is_multiprotocol_enabled:
    description:
    - This parameter indicates whether multiprotocol sharing mode is enabled.
    - It can be mentioned during modification of the NAS server.
    type: bool
  allow_unmapped_user:
    description:
    - This flag is used to mandatorily disable access in case of any user
      mapping failure.
    - If true, then enable access in case of any user mapping failure.
    - If false, then disable access in case of any user mapping failure.
    - It can be mentioned during modification of the NAS server.
    type: bool
  default_windows_user:
    description:
    - Default windows user name used for granting access in the case of Unix
      to Windows user mapping failure.
    - It can be mentioned during modification of the NAS server.
    type: str
  default_unix_user:
    description:
    - Default Unix user name used for granting access in the case of Windows
     to Unix user mapping failure.
    - It can be mentioned during modification of the NAS server.
    type: str
  enable_windows_to_unix_username_mapping:
    description:
    - This parameter indicates whether a Unix to/from Windows user name
      mapping is enabled.
    - It can be mentioned during modification of the NAS server.
    type: bool
  is_packet_reflect_enabled:
    description:
    - If the packet has to be reflected, then this parameter
      has to be set to True.
    - It can be mentioned during modification of the NAS server.
    type: bool
  current_unix_directory_service:
    description:
    - This is the directory service used for querying identity information
      for UNIX (such as UIDs, GIDs, net groups).
    - It can be mentioned during modification of the NAS server.
    type: str
    choices: ["NONE", "NIS", "LOCAL", "LDAP", "LOCAL_THEN_NIS", "LOCAL_THEN_LDAP"]
  state:
    description:
    - Define the state of NAS server on the array.
    - present indicates that NAS server should exist on the system after
      the task is executed.
    - Right now deletion of NAS server is not supported. Hence, if state is
      set to absent for any existing NAS server then error will be thrown.
    - For any non-existing NAS server, if state is set to absent then it will return None.
    type: str
    required: true
    choices: ['present', 'absent']
'''
EXAMPLES = r'''

    - name: Get Details of NAS Server
      dellemc_unity_nasserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        verifycert: "{{verifycert}}"
        nas_server_name: "{{nas_server_name}}"
        state: "present"

    - name: Modify Details of NAS Server
      dellemc_unity_nasserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        verifycert: "{{verifycert}}"
        nas_server_name: "{{nas_server_name}}"
        nas_server_new_name: "updated_sample_nas_server"
        is_replication_destination: False
        is_backup_only: False
        is_multiprotocol_enabled: True
        allow_unmapped_user: True
        default_unix_user: "default_unix_sample_user"
        default_windows_user: "default_windows_sample_user"
        enable_windows_to_unix_username_mapping: True
        current_unix_directory_service: "LDAP"
        is_packet_reflect_enabled: True
        state: "present"

'''
RETURN = r'''
changed:
    description: Whether or not the resource has changed
    returned: always
    type: bool
    sample: True
nas_server_details:
    description: The NAS server details.
    type: complex
    returned: When NAS server exists.
    contains:
        name:
            description: Name of the NAS server
            type: str
        id:
            description: ID of the NAS server
            type: str
        allow_unmapped_user:
            description: enable/disable access status in case of any user
                         mapping failure
            type: bool
        current_unix_directory_service:
            description: Directory service used for querying identity
                         information for UNIX (such as UIDs, GIDs, net groups).
            type: str
        default_unix_user:
            description: Default Unix user name used for granting access
                         in the case of Windows to Unix user mapping failure.
            type: str
        default_windows_user:
            description: Default windows user name used for granting
                         access in the case of Unix to Windows user mapping
                         failure
            type: str
        is_backup_only:
            description: Whether the NAS server is used as backup only.
            type: bool
        is_multi_protocol_enabled:
            description: Indicates whether multiprotocol sharing mode is
                         enabled
            type: bool
        is_packet_reflect_enabled:
            description: If the packet reflect has to be enabled
            type: bool
        is_replication_destination:
            description: If the NAS server is a replication destination
                         then True.
            type: bool
        is_windows_to_unix_username_mapping_enabled:
            description: Indicates whether a Unix to/from Windows user name
                         mapping is enabled.
            type: bool
'''
from ansible.module_utils.basic import AnsibleModule
# from ansible.module_utils.storage.dell \
#     import dellemc_ansible_unity_utils as utils
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import dellemc_ansible_unity_utils as utils
LOG = utils.get_logger('dellemc_unity_nasserver')

HAS_UNITY_SDK = utils.get_unity_sdk()
UNITY_SDK_VERSION_CHECK = utils.storops_version_check()

application_type = "Ansible/1.2.0"


class UnityNASServer(object):
    """Class with NAS Server operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_unity_management_host_parameters()
        self.module_params.update(get_unity_nasserver_parameters())

        # initialize the ansible module
        mut_ex_args = [['nas_server_name', 'nas_server_id']]
        required_one_of = [['nas_server_name', 'nas_server_id']]

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            mutually_exclusive=mut_ex_args,
            required_one_of=required_one_of
        )

        # result is a dictionary that contains changed status and
        # nas server details
        self.result = {"changed": False,
                       'nas_server_details': None}

        if not HAS_UNITY_SDK:
            self.module.fail_json(msg="Ansible modules for Unity require the"
                                      " Unity python library to be"
                                      " installed. Please install the "
                                      "library before using these modules.")

        if UNITY_SDK_VERSION_CHECK and \
                not UNITY_SDK_VERSION_CHECK['supported_version']:
            err_msg = UNITY_SDK_VERSION_CHECK['unsupported_version_message']
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        self.unity_conn = utils.get_unity_unisphere_connection(
            self.module.params, application_type)
        self.nas_server_conn_obj = utils.nas_server.UnityNasServer(
            self.unity_conn)
        LOG.info('Connection established with the Unity Array')

    def get_current_uds_enum(self, current_uds):
        """
        Get the enum of the Offline Availability parameter.
        :param current_uds: Current Unix Directory Service string
        :return: current_uds enum
        """
        if current_uds in \
                utils.NasServerUnixDirectoryServiceEnum.__members__:
            return utils.NasServerUnixDirectoryServiceEnum[current_uds]
        else:
            error_msg = "Invalid value {0} for Current Unix Directory" \
                        " Service provided".format(current_uds)
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_nas_server(self, nas_server_name, nas_server_id):
        """
        Get the NAS Server Object using NAME/ID of the NAS Server.
        :param nas_server_name: Name of the NAS Server
        :param nas_server_id: ID of the NAS Server
        :return: NAS Server object.
        """
        nas_server = nas_server_name if nas_server_name else nas_server_id
        try:
            obj_nas = self.unity_conn.get_nas_server(_id=nas_server_id,
                                                     name=nas_server_name)
            if nas_server_id and obj_nas and not obj_nas.existed:
                #  if obj_nas is not None and existed is observed as False,
                #  then None will be returned.
                LOG.error("NAS Server object does not exist"
                          " with ID: %s ", nas_server_id)
                return None
            return obj_nas
        except utils.HttpError as e:
            if e.http_status == 401:
                cred_err = "Incorrect username or password , {0}".format(
                    e.message)
                self.module.fail_json(msg=cred_err)
            else:
                err_msg = "Failed to get details of NAS Server" \
                          " {0} with error {1}".format(nas_server, str(e))
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)

        except utils.UnityResourceNotFoundError as e:
            err_msg = "Failed to get details of NAS Server" \
                      " {0} with error {1}".format(nas_server, str(e))
            LOG.error(err_msg)
            return None

        except Exception as e:
            nas_server = nas_server_name if nas_server_name \
                else nas_server_id
            err_msg = "Failed to get nas server details {0} with" \
                      " error {1}".format(nas_server, str(e))
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def to_update(self, nas_server_obj, current_uds):
        LOG.info("Checking Whether the parameters are modified or not.")

        # Checking all parameters individually because the nas obj return
        # names are different compared to ansible parameter names.

        # Current Unix Directory Service
        if current_uds is not None and \
                current_uds != nas_server_obj.current_unix_directory_service:
            return True

        # Rename NAS Server
        if self.module.params['nas_server_new_name'] is not None and \
                self.module.params['nas_server_new_name'] != \
                nas_server_obj.name:
            return True

        # Is Replication Destination
        if self.module.params["is_replication_destination"] is not None:
            if nas_server_obj.is_replication_destination is None:
                return True
            elif self.module.params["is_replication_destination"] != \
                    nas_server_obj.is_replication_destination:
                return True

        # Is Multiprotocol Enabled
        if self.module.params["is_multiprotocol_enabled"] is not None:
            if nas_server_obj.is_multi_protocol_enabled is None:
                return True
            elif self.module.params["is_multiprotocol_enabled"] != \
                    nas_server_obj.is_replication_destination:
                return True

        # Is Back Up Enabled
        if self.module.params["is_backup_only"] is not None:
            if nas_server_obj.is_backup_only is None:
                return True
            elif self.module.params["is_backup_only"] != \
                    nas_server_obj.is_backup_only:
                return True

        # Is Packet Reflect Enabled
        if self.module.params["is_packet_reflect_enabled"] is not None:
            if nas_server_obj.is_packet_reflect_enabled is None:
                return True
            elif self.module.params["is_packet_reflect_enabled"] != \
                    nas_server_obj.is_packet_reflect_enabled:
                return True

        # Allow Unmapped User
        if self.module.params["allow_unmapped_user"] is not None:
            if nas_server_obj.allow_unmapped_user is None:
                return True
            elif self.module.params["allow_unmapped_user"] != \
                    nas_server_obj.allow_unmapped_user:
                return True

        # Enable Windows To Unix User Mapping Flag
        nas_win_flag = \
            nas_server_obj.is_windows_to_unix_username_mapping_enabled
        input_win_flag = \
            self.module.params["enable_windows_to_unix_username_mapping"]
        if input_win_flag is not None:
            if nas_win_flag is None:
                return True
            elif nas_win_flag != input_win_flag:
                return True

        # Default Windows User
        if self.module.params["default_windows_user"] is not None:
            if nas_server_obj.default_windows_user is None:
                return True
            elif self.module.params["default_windows_user"] != \
                    nas_server_obj.default_windows_user:
                return True

        # Default Unix User
        if self.module.params["default_unix_user"] is not None:
            if nas_server_obj.default_unix_user is None:
                return True
            elif self.module.params["default_unix_user"] != \
                    nas_server_obj.default_unix_user:
                return True

        return False

    def update_nas_server(self, nas_server_obj, new_name=None,
                          default_unix_user=None, default_windows_user=None,
                          is_rep_dest=None, is_multiprotocol_enabled=None,
                          allow_unmapped_user=None, is_backup_only=None,
                          is_packet_reflect_enabled=None, current_uds=None,
                          enable_win_to_unix_name_map=None):
        """
        The Details of the NAS Server will be updated in the function.
        """
        try:
            nas_server_obj.modify(
                name=new_name,
                is_replication_destination=is_rep_dest,
                is_backup_only=is_backup_only,
                is_multi_protocol_enabled=is_multiprotocol_enabled,
                default_unix_user=default_unix_user,
                default_windows_user=default_windows_user,
                allow_unmapped_user=allow_unmapped_user,
                is_packet_reflect_enabled=is_packet_reflect_enabled,
                enable_windows_to_unix_username=enable_win_to_unix_name_map,
                current_unix_directory_service=current_uds)

        except Exception as e:
            error_msg = "Failed to Update parameters of NAS Server" \
                        " %s with error %s" % (nas_server_obj.name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def perform_module_operation(self):
        """
        Perform different actions on NAS Server based on user parameters
        chosen in playbook
        """
        state = self.module.params['state']
        nas_server_name = self.module.params['nas_server_name']
        nas_server_id = self.module.params['nas_server_id']
        nas_server_new_name = self.module.params['nas_server_new_name']
        default_unix_user = self.module.params['default_unix_user']
        default_windows_user = self.module.params['default_windows_user']

        is_replication_destination = \
            self.module.params['is_replication_destination']
        is_multiprotocol_enabled = \
            self.module.params['is_multiprotocol_enabled']
        allow_unmapped_user = self.module.params['allow_unmapped_user']
        enable_windows_to_unix_username_mapping = \
            self.module.params['enable_windows_to_unix_username_mapping']

        is_backup_only = self.module.params['is_backup_only']
        is_packet_reflect_enabled = \
            self.module.params['is_packet_reflect_enabled']

        current_uds = self.module.params['current_unix_directory_service']
        # Get the enum for the corresponding offline_availability
        if current_uds:
            current_uds = \
                self.get_current_uds_enum(current_uds)

        changed = False

        '''
        Get details of NAS Server.
        '''
        nas_server_obj = None
        if nas_server_name or nas_server_id:
            nas_server_obj = self.get_nas_server(nas_server_name,
                                                 nas_server_id)

        # As creation is not supported and if NAS Server does not exist
        # along with state as present, then error will be thrown.
        if not nas_server_obj and state == "present":
            msg = "NAS Server Resource not found. Please enter a valid " \
                  "Name/ID to get or modify the parameters of nas server."
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        '''
            Update the parameters of NAS Server
        '''
        if nas_server_obj and state == "present":
            update_flag = self.to_update(nas_server_obj, current_uds)
            if update_flag:
                self.update_nas_server(
                    nas_server_obj, nas_server_new_name, default_unix_user,
                    default_windows_user, is_replication_destination,
                    is_multiprotocol_enabled, allow_unmapped_user,
                    is_backup_only, is_packet_reflect_enabled,
                    current_uds, enable_windows_to_unix_username_mapping)
                changed = True

        # As deletion is not supported and if NAS Server exists along with
        # state as absent, then error will be thrown.
        if nas_server_obj and state == 'absent':
            self.module.fail_json(msg="Deletion of NAS Server is "
                                      "currently not supported.")

        '''
            Update the changed state and NAS Server details
        '''

        nas_server_details = None
        if nas_server_obj:
            nas_server_details = self.get_nas_server(
                None, nas_server_obj.id)._get_properties()

        self.result["changed"] = changed
        self.result["nas_server_details"] = nas_server_details
        self.module.exit_json(**self.result)


def get_unity_nasserver_parameters():
    """
    This method provides parameters required for the ansible NAS Server
    modules on Unity
    """

    return dict(
        nas_server_name=dict(), nas_server_id=dict(),
        nas_server_new_name=dict(),
        default_unix_user=dict(),
        default_windows_user=dict(),
        current_unix_directory_service=dict(
            choices=["NIS", "LDAP", "LOCAL_THEN_NIS",
                     "LOCAL_THEN_LDAP", "NONE", "LOCAL"]),
        is_replication_destination=dict(type='bool'),
        is_backup_only=dict(type='bool'),
        is_multiprotocol_enabled=dict(type='bool'),
        allow_unmapped_user=dict(type='bool'),
        enable_windows_to_unix_username_mapping=dict(type='bool'),
        is_packet_reflect_enabled=dict(type='bool'),
        state=dict(required=True, choices=['present', 'absent'], type='str')
    )


def main():
    """ Create Unity NAS Server object and perform action on it
        based on user input from playbook"""
    obj = UnityNASServer()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
