#!/usr/bin/python
# Copyright: (c) 2020, DellEMC

"""Ansible module for managing host on Unity"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: dellemc_unity_host

version_added: '1.1.0'

short_description: Manage Host operations on Unity.

description:
- The Host module contains the following operations
  Creation of a Host.
  Addition of initiators to Host.
  Removal of initiators from Host.
  Modification of host attributes.
  Get details of a Host.
  Deletion of a Host.

extends_documentation_fragment:
  - dellemc.unity.dellemc_unity.unity

author:
- Rajshree Khare (@kharer5) <ansible.team@dell.com>

options:
  host_name:
    description:
    - Name of the host.
    - Mandatory for host creation.
    type: str

  host_id:
    description:
    - Unique identifier of the host.
    - host_id is auto generated during creation.
    - Except create, all other operations require either host_id or host_name.
    type: str

  description:
    description:
    - Host description.
    type: str

  host_os:
    description:
    - Operating system running on the host.
    choices: ['AIX', 'Citrix XenServer', 'HP-UX', 'IBM VIOS', 'Linux',
    'Mac OS', 'Solaris', 'VMware ESXi', 'Windows Client', 'Windows Server']
    type: str

  new_host_name:
    description:
    - New name for the host.
    - Only required in rename host operation.
    type: str

  initiators:
    description:
    - List of initiators to be added/removed to/from host.
    type: list
    elements: str

  initiator_state:
    description:
    - State of the initiator.
    choices: [present-in-host , absent-in-host]
    type: str

  state:
    description:
    - State of the host.
    choices: [present , absent]
    type: str
    required: True
'''

EXAMPLES = r'''
- name: Create empty Host.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host"
    host_os: "Linux"
    description: "ansible-test-host"
    state: "present"

- name: Create Host with Initiators.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host-1"
    host_os: "Linux"
    description: "ansible-test-host-1"
    initiators:
      - "iqn.1994-05.com.redhat:c38e6e8cfd81"
      - "20:00:00:90:FA:13:81:8D:10:00:00:90:FA:13:81:8D"
    initiator_state: "present-in-host"
    state: "present"

- name: Modify Host using host_id.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_id: "Host_253"
    new_host_name: "ansible-test-host-2"
    host_os: "Mac OS"
    description: "Ansible tesing purpose"
    state: "present"

- name: Add Initiators to Host.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host-2"
    initiators:
      - "20:00:00:90:FA:13:81:8C:10:00:00:90:FA:13:81:8C"
    initiator_state: "present-in-host"
    state: "present"

- name: Get Host details using host_name.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host-2"
    state: "present"

- name: Get Host details using host_id.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_id: "Host_253"
    state: "present"

- name: Delete Host.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host-2"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool

host_details:
    description: Details of the host.
    returned: When host exists.
    type: complex
    contains:
        id:
            description: The system ID given to the host.
            type: str
        name:
            description: The name of the host.
            type: str
        description:
            description: Description about the host.
            type: str
        fc_host_initiators:
            description: Details of the FC initiators associated with
                         the host.
            type: complex
            contains:
                UnityHostInitiatorList:
                    description: FC initiators with system generated
                                 unique hash value.
                    type: complex
        iscsi_host_initiators:
            description: Details of the ISCSI initiators associated
                         with the host.
            type: complex
            contains:
                UnityHostInitiatorList:
                    description: ISCSI initiators with sytem genrated unique
                                 hash value.
                    type: complex
        os_type:
            description: Operating system running on the host.
            type: str
        type:
            description: HostTypeEnum of the host.
            type: str
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import dellemc_ansible_unity_utils as utils

LOG = utils.get_logger('dellemc_unity_host', log_devel=utils.logging.INFO)
HAS_UNITY_SDK = utils.get_unity_sdk()
UNITY_SDK_VERSION_CHECK = utils.storops_version_check()

application_type = "Ansible/1.2.0"


class UnityHost(object):
    """Class with Host operations"""

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_unity_management_host_parameters()
        self.module_params.update(get_unity_host_parameters())

        mutually_exclusive = [['host_name', 'host_id']]
        required_one_of = [['host_name', 'host_id']]

        """ initialize the ansible module """
        self.module = AnsibleModule(argument_spec=self.module_params,
                                    supports_check_mode=False,
                                    mutually_exclusive=mutually_exclusive,
                                    required_one_of=required_one_of)

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

        self.unity = utils.get_unity_unisphere_connection(self.module.params, application_type)
        LOG.info('Got the unity instance for provisioning on Unity')

    def get_host_count(self, host_name):
        """ To get the count of hosts with same host_name """

        hosts = []
        host_count = 0
        hosts = utils.host.UnityHostList.get(cli=self.unity._cli,
                                             name=host_name)
        host_count = len(hosts)
        return host_count

    def get_host_details(self, host_id=None, host_name=None):
        """ Get details of a given host """

        host_id_or_name = host_id if host_id else host_name
        try:
            LOG.info("Getting host %s details", host_id_or_name)
            if host_id:
                host_details = self.unity.get_host(_id=host_id)
                if host_details.name is None:
                    return None
            if host_name:

                ''' get the count of hosts with same host_name '''
                host_count = self.get_host_count(host_name)

                if host_count < 1:
                    return None
                elif host_count > 1:
                    error_message = "Duplicate hosts found: There are "\
                                    + host_count + " hosts(s) with the same" \
                                    " host_name: " + host_name
                    LOG.error(error_message)
                    self.module.fail_json(msg=error_message)
                else:
                    host_details = self.unity.get_host(name=host_name)

            return host_details
        except utils.HttpError as e:
            if e.http_status == 401:
                msg = 'Incorrect username or password provided.'
                LOG.error(msg)
                self.module.fail_json(msg=msg)
            else:
                msg = "Got HTTP Connection Error while getting host " \
                      "details %s : Error %s " % (host_id_or_name, str(e))
                LOG.error(msg)
                self.module.fail_json(msg=msg)
        except utils.UnityResourceNotFoundError as e:
            error_message = "Failed to get details of host " \
                            "{0} with error {1}".format(host_id_or_name,
                                                        str(e))
            LOG.error(error_message)
            return None
        except Exception as e:
            error_message = "Got error %s while getting details of host %s" \
                            % (str(e), host_id_or_name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def create_host(self, host_name):
        """ Create a new host """

        try:
            description = self.module.params['description']
            host_os = self.module.params['host_os']
            host_type = utils.HostTypeEnum.HOST_MANUAL
            initiators = self.module.params['initiators']
            initiator_state = self.module.params['initiator_state']
            emptyInitiatorsFlag = False

            if (initiators and initiator_state == 'absent-in-host'):
                error_message = "Incorrect 'initiator_state' given."
                LOG.error(error_message)
                self.module.fail_json(msg=error_message)

            if (initiators is None or len(initiators) == 0
                    or not initiator_state
                    or initiator_state == 'absent-in-host'):
                emptyInitiatorsFlag = True

            """ if any of the Initiators is invalid or already mapped """
            if (initiators and initiator_state == 'present-in-host'):
                unmapped_initiators \
                    = self.get_list_unmapped_initiators(initiators)
                if unmapped_initiators is None \
                        or len(unmapped_initiators) < len(initiators):
                    error_message = "Provide valid initiators."
                    LOG.error(error_message)
                    self.module.fail_json(msg=error_message)

            LOG.info("Creating empty host %s ", host_name)
            new_host = utils.host.UnityHost.create(
                self.unity._cli, name=host_name, desc=description,
                os=host_os, host_type=host_type)

            # Add initiators, if given.
            if not emptyInitiatorsFlag:
                host_details = self.unity.get_host(name=host_name)
                LOG.info("Adding initiators to %s host", host_name)
                result, new_host \
                    = self.add_initiator_to_host(host_details, initiators)

            return True, new_host

        except Exception as e:
            error_message = "Got error %s while creation of host %s" \
                            % (str(e), host_name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def get_host_initiators_list(self, host_details):
        """ Get the list of existing initiators in host"""

        existing_initiators = []
        if host_details.fc_host_initiators is not None:
            fc_len = len(host_details.fc_host_initiators)
            if fc_len > 0:
                for count in range(fc_len):
                    """ get initiator 'wwn' id"""
                    ini_id \
                        = host_details.fc_host_initiators.initiator_id[count]

                    """ update existing_initiators list with 'wwn' """
                    existing_initiators.append(ini_id)

        if host_details.iscsi_host_initiators is not None:
            iscsi_len = len(host_details.iscsi_host_initiators)
            if iscsi_len > 0:
                for count in range(iscsi_len):
                    """ get initiator 'iqn' id"""
                    ini_id \
                        = host_details.iscsi_host_initiators.\
                        initiator_id[count]

                    """ update existing_initiators list with 'iqn' """
                    existing_initiators.append(ini_id)
        return existing_initiators

    def is_host_modified(self, host_details):
        """ Determines whether the Host details are to be updated or not """
        LOG.info("Checking host attribute values.")
        modified_flag = False

        if (self.module.params['description'] is not None
            and self.module.params['description']
            != host_details.description) \
                or (self.module.params['host_os'] is not None
                    and self.module.params['host_os'] != host_details.os_type) \
                or (self.module.params['new_host_name'] is not None
                    and self.module.params[
                        'new_host_name'] != host_details.name) \
                or (self.module.params['initiators'] is not None
                    and self.module.params['initiators']
                    != self.get_host_initiators_list(host_details)):
            LOG.info("Modification required.")
            modified_flag = True

        return modified_flag

    def modify_host(self, host_details, new_host_name=None, description=None,
                    host_os=None):
        """  Modify a host """
        try:
            hosts = utils.host.UnityHostList.get(cli=self.unity._cli)
            host_names_list = hosts.name
            for name in host_names_list:
                if new_host_name == name:
                    error_message = "Cannot modify name, new_host_name: " \
                                    + new_host_name + " already in use."
                    LOG.error(error_message)
                    self.module.fail_json(msg=error_message)
            host_details.modify(name=new_host_name, desc=description,
                                os=host_os)
            return True

        except Exception as e:
            error_message = "Got error %s while modifying host %s" \
                            % (str(e), host_details.name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def get_list_unmapped_initiators(self, initiators, host_id=None):
        """ Get the list of those initiators which are
            not mapped to any host"""

        unmapped_initiators = []
        for id in initiators:
            initiator_details = utils.host.UnityHostInitiatorList \
                .get(cli=self.unity._cli, initiator_id=id) \
                ._get_properties()

            """ if an already existing initiator is passed along with an
                unmapped initiator"""
            if None in initiator_details["parent_host"] \
                    or (host_id and host_id
                        in initiator_details["parent_host"][0]
                                            ["UnityHost"]["id"]):
                unmapped_initiators.append(initiator_details
                                           ["initiator_id"][0])
            else:
                error_message = "Initiator " + id + " mapped to another Host."
                LOG.error(error_message)
                self.module.fail_json(msg=error_message)
        return unmapped_initiators

    def add_initiator_to_host(self, host_details, initiators):
        """ Add initiator to host """

        try:
            existing_initiators = self.get_host_initiators_list(host_details)

            """ if current and exisitng initiators are same"""
            if initiators \
                    and (set(initiators).issubset(set(existing_initiators))):
                LOG.info("Initiators are already present in host: %s",
                         host_details.name)
                return False, host_details

            """ get the list of non-mapped initiators out of the
                given initiators"""
            host_id = host_details.id
            unmapped_initiators \
                = self.get_list_unmapped_initiators(initiators, host_id)

            """ if any of the Initiators is invalid or already mapped """
            if unmapped_initiators is None \
                    or len(unmapped_initiators) < len(initiators):
                error_message = "Provide valid initiators."
                LOG.error(error_message)
                self.module.fail_json(msg=error_message)

            LOG.info("Adding initiators to host %s", host_details.name)
            for id in unmapped_initiators:
                host_details.add_initiator(uid=id)
                updated_host \
                    = self.unity.get_host(name=host_details.name)
            return True, updated_host

        except Exception as e:
            error_message = "Got error %s while adding initiator to host %s" \
                            % (str(e), host_details.name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def remove_initiator_from_host(self, host_details, initiators):
        """ Remove initiator from host """

        try:
            existing_initiators = self.get_host_initiators_list(host_details)

            if existing_initiators is None:
                LOG.info("No exisiting initiators in host: %s",
                         host_details.name)
                return False, host_details

            if not (set(initiators).issubset(set(existing_initiators))):
                LOG.info("Initiators already absent in host: %s",
                         host_details.name)
                return False, host_details

            LOG.info("Removing initiators from host %s", host_details.name)
            for id in initiators:

                initiator_details = utils.host.UnityHostInitiatorList \
                    .get(cli=self.unity._cli, initiator_id=id) \
                    ._get_properties()

                """ if initiator has no active paths, then remove it """
                if "UnityHostInitiatorPathList" \
                        not in initiator_details["paths"]:
                    LOG.info("Initiator Path does not exist.")
                    host_details.delete_initiator(uid=id)
                    updated_host \
                        = self.unity.get_host(name=host_details.name)

                else:
                    """ Checking for initiator logged_in state """
                    for path in initiator_details["paths"][0]["UnityHostInitiatorPathList"]:
                        path_id = path["UnityHostInitiatorPath"]["id"]
                        path_id_details = utils.host.UnityHostInitiatorPathList \
                            .get(cli=self.unity._cli, _id=path_id) \
                            ._get_properties()

                        """ if is_logged_in is True, can't remove initiator"""
                        if (path_id_details["is_logged_in"]):
                            error_message = "Cannot remove initiator "\
                                            + id + ", as it is logged in " \
                                                   "the with host."
                            LOG.error(error_message)
                            self.module.fail_json(msg=error_message)

                        elif (not path_id_details["is_logged_in"]):
                            """ if is_logged_in is False, remove initiator """
                            path_id.delete()

                        else:
                            """ if logged_in state does not exist """
                            error_message = " logged_in state does not " \
                                            "exist for initiator " + id + "."
                            LOG.error(error_message)
                            self.module.fail_json(msg=error_message)

                    host_details.delete_initiator(uid=id)
                    updated_host \
                        = self.unity.get_host(name=host_details.name)

            return True, updated_host

        except Exception as e:
            error_message = "Got error %s while removing initiator from " \
                            "host %s" \
                            % (str(e), host_details.name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def delete_host(self, host_details):
        """ Delete an existing host """

        try:
            host_details.delete()
            return True
        except Exception as e:
            error_message = "Got error %s while deletion of host %s" \
                            % (str(e), host_details.name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def perform_module_operation(self):
        """ Perform different actions on host based on user parameter
            chosen in playbook """

        host_name = self.module.params['host_name']
        host_id = self.module.params['host_id']
        description = self.module.params['description']
        host_os = self.module.params['host_os']
        new_host_name = self.module.params['new_host_name']
        initiator_state = self.module.params['initiator_state']
        initiators = self.module.params['initiators']
        state = self.module.params['state']

        if host_name and len(host_name) > 255:
            err_msg = "'host_name' is greater than 255 characters."
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        if new_host_name and len(new_host_name) > 255:
            err_msg = "'new_host_name' is greater than 255 characters."
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        if description and len(description) > 255:
            err_msg = "'description' is greater than 255 characters."
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        if not initiators and initiator_state:
            err_msg = "'initiator_state' is given, " \
                      "'initiators' are not specified"
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        if not initiator_state and initiators:
            err_msg = "'initiators' are given, " \
                      "'initiator_state' is not specified"
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        if initiators:
            initiators_list = utils.host.UnityHostInitiatorList\
                .get(cli=self.unity._cli)
            for id in initiators:
                if id not in initiators_list.initiator_id:
                    err_msg = id + " - Invalid initiator passed."
                    LOG.error(err_msg)
                    self.module.fail_json(msg=err_msg)

        # result is a dictionary that contains changed status and
        # host details
        result = dict(
            changed=False,
            host_details=''
        )

        ''' Get host details based on host_name/host_id'''
        host_details = self.get_host_details(host_id, host_name)

        if not host_details and state == 'present':
            if host_id:
                err_msg = "Invalid argument 'host_id' while " \
                          "creating a host"
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)
            if not host_name:
                err_msg = "host_name is required to create a host"
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)
            if new_host_name:
                err_msg = "Invalid argument 'new_host_name' while " \
                          "creating a host"
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)

            if (initiators and initiator_state == 'absent-in-host'):
                error_message = "Incorrect 'initiator_state' given."
                LOG.error(error_message)
                self.module.fail_json(msg=error_message)

            # Create new host
            LOG.info("Creating host: %s", host_name)
            result['changed'], host_details \
                = self.create_host(host_name)
            result['host_details'] = host_details._get_properties()

        # Modify host (Attributes and ADD/REMOVE Initiators)
        elif (state == 'present' and host_details):
            modified_flag = self.is_host_modified(host_details)
            if modified_flag:

                # Modify host
                host_id_or_name = host_id if host_id else host_name
                result['changed'] = self.modify_host(host_details,
                                                     new_host_name,
                                                     description,
                                                     host_os)
                if new_host_name:
                    host_details = self.get_host_details(host_id,
                                                         new_host_name)
                else:
                    host_details = self.get_host_details(host_id, host_name)
                result['host_details'] = host_details._get_properties()

                # Add Initiators to host
                if (initiator_state == 'present-in-host' and initiators
                        and len(initiators) > 0):
                    LOG.info("Adding Initiators to Host %s",
                             host_details.name)
                    result['changed'], host_details \
                        = self.add_initiator_to_host(host_details, initiators)
                    result['host_details'] = host_details._get_properties()

            else:
                LOG.info('Host modification is not applicable, '
                         'as none of the attributes has changed.')
                result['changed'] = False
                result['host_details'] = host_details._get_properties()

        # Remove initiators from host
        if (host_details and initiator_state == 'absent-in-host'
                and initiators and len(initiators) > 0):
            LOG.info("Removing Initiators from Host %s",
                     host_details.name)
            result['changed'], host_details \
                = self.remove_initiator_from_host(host_details,
                                                  initiators)
            result['host_details'] = host_details._get_properties()

        """ display WWN/IQN w.r.t. initiators mapped to host,
            if host exists """
        if host_details and host_details.fc_host_initiators is not None:
            host_details.fc_host_initiators \
                = host_details.fc_host_initiators.initiator_id
            result['host_details'] = host_details._get_properties()
        if host_details and host_details.iscsi_host_initiators is not None:
            host_details.iscsi_host_initiators \
                = host_details.iscsi_host_initiators.initiator_id
            result['host_details'] = host_details._get_properties()

        # Delete a host
        if state == 'absent':
            if host_details:
                LOG.info("Deleting host %s", host_details.name)
                result['changed'] = self.delete_host(host_details)
            else:
                result['changed'] = False
            result['host_details'] = []

        self.module.exit_json(**result)


def get_unity_host_parameters():
    """This method provides parameters required for the ansible host
    module on Unity"""
    return dict(
        host_name=dict(required=False, type='str'),
        host_id=dict(required=False, type='str'),
        description=dict(required=False, type='str'),
        host_os=dict(required=False, type='str',
                     choices=['AIX', 'Citrix XenServer', 'HP-UX',
                              'IBM VIOS', 'Linux', 'Mac OS', 'Solaris',
                              'VMware ESXi', 'Windows Client',
                              'Windows Server']),
        new_host_name=dict(required=False, type='str'),
        initiators=dict(required=False, type='list', elements='str'),
        initiator_state=dict(required=False, type='str',
                             choices=['present-in-host',
                                      'absent-in-host']),
        state=dict(required=True, type='str',
                   choices=['present', 'absent'])
    )


def main():
    """ Create Unity host object and perform action on it
        based on user input from playbook"""
    obj = UnityHost()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
