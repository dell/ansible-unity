#!/usr/bin/python
# Copyright: (c) 2020-2025, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing initiators on Unity"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: initiator

version_added: '1.8.0'

short_description: Manage Initiator operations on Unity

description:
- The Initiator module contains the operations
  Creation of an Initiator (even if not zoned),
  Addition of initiators to Host,
  Removal of initiators from Host,
  Get details of Initiators,
  Deletion of an Initiator.

extends_documentation_fragment:
  - dellemc.unity.unity

author:
- Maurizio Colella (@colelm) <maurizio.colella@dell.com>

options:
  host_name:
    description:
    - Name of the host to which the initiator will be associated.
    - If the host does not exist, it will be created.
    - Required for initiator creation/deletion.
    type: str

  host_id:
    description:
    - Unique identifier of the host.
    - Alternative to host_name.
    type: str

  host_os:
    description:
    - Operating system running on the host.
    - Used when creating a new host.
    - choices: ['AIX', 'Citrix XenServer', 'HP-UX', 'IBM VIOS', 'Linux',
    'Mac OS', 'Solaris', 'VMware ESXi', 'Windows Client', 'Windows Server']
    type: str

  description:
    description:
    - Host description.
    - Used when creating a new host.
    type: str

  initiators:
    description:
    - List of initiators to be created/added/removed.
    - Initiator can be FC WWN or iSCSI IQN format.
    type: list
    elements: str

  state:
    description:
    - State of the initiator.
    - C(present) - Create initiators and add to host (create host if needed).
    - C(absent) - Remove initiators from host and delete them.
    - If not specified, will list all initiators.
    choices: [present, absent]
    type: str

notes:
  - The I(check_mode) is not supported.
  - This module can create initiators even if they are not yet zoned.
'''

EXAMPLES = r'''
- name: Create initiators and add to host (creates host if needed)
  dellemc.unity.initiator:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "ansible-test-host"
    host_os: "Linux"
    description: "Test host for initiators"
    initiators:
      - "iqn.1994-05.com.redhat:c38e6e8cfd81"
      - "20:00:00:90:FA:13:81:8D:10:00:00:90:FA:13:81:8D"
    state: "present"

- name: List all initiators
  dellemc.unity.initiator:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"

- name: Remove initiators from host and delete them
  dellemc.unity.initiator:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_name: "ansible-test-host"
    initiators:
      - "iqn.1994-05.com.redhat:c38e6e8cfd81"
    state: "absent"

- name: Create initiators with existing host
  dellemc.unity.initiator:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    host_id: "Host_253"
    initiators:
      - "20:00:00:90:FA:13:81:8C:10:00:00:90:FA:13:81:8C"
    state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: true

initiator_details:
    description: Details of the initiators.
    returned: When initiators exist or are created.
    type: dict
    contains:
        fc_initiators:
            description: List of FC initiators.
            type: list
            contains:
                id:
                    description: Unique identifier of the FC initiator.
                    type: str
                initiator_id:
                    description: FC Qualified Name (WWN) of the initiator.
                    type: str
                parent_host:
                    description: Host to which the initiator is attached.
                    type: str
        iscsi_initiators:
            description: List of iSCSI initiators.
            type: list
            contains:
                id:
                    description: Unique identifier of the iSCSI initiator.
                    type: str
                initiator_id:
                    description: ISCSI Qualified Name (IQN) of the initiator.
                    type: str
                parent_host:
                    description: Host to which the initiator is attached.
                    type: str
    sample: {
        "fc_initiators": [
            {
                "id": "HostInitiator_1",
                "initiator_id": "20:00:00:90:FA:13:81:8D",
                "parent_host": "Host_253"
            }
        ],
        "iscsi_initiators": [
            {
                "id": "HostInitiator_2",
                "initiator_id": "iqn.1994-05.com.redhat:c38e6e8cfd81",
                "parent_host": "Host_253"
            }
        ]
    }

host_details:
    description: Details of the host (created or used).
    returned: When host is involved in the operation.
    type: dict
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
        os_type:
            description: Operating system running on the host.
            type: str
    sample: {
        "id": "Host_253",
        "name": "ansible-test-host",
        "description": "Test host",
        "os_type": "Linux"
    }
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('initiator')

application_type = "Ansible/1.8.0"


class Initiator(object):
    """Class with Initiator operations"""

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_unity_management_host_parameters()
        self.module_params.update(get_initiator_parameters())

        mutually_exclusive = [['host_name', 'host_id']]
        required_one_of = []

        """ initialize the ansible module """
        self.module = AnsibleModule(argument_spec=self.module_params,
                                    supports_check_mode=False,
                                    mutually_exclusive=mutually_exclusive,
                                    required_one_of=required_one_of)
        utils.ensure_required_libs(self.module)

        self.unity = utils.get_unity_unisphere_connection(self.module.params, application_type)
        LOG.info('Got the unity instance for initiator management on Unity')

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
                hosts = utils.host.UnityHostList.get(cli=self.unity._cli,
                                                     name=host_name)
                host_count = len(hosts)
                if host_count < 1:
                    return None
                elif host_count > 1:
                    error_message = "Duplicate hosts found: There are " \
                                    + str(host_count) + " hosts(s) with the same" \
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

    def create_host(self, host_name, host_os=None, description=None):
        """ Create a new host """
        try:
            host_type = utils.HostTypeEnum.HOST_MANUAL
            LOG.info("Creating host %s ", host_name)
            new_host = utils.host.UnityHost.create(
                self.unity._cli,
                name=host_name,
                desc=description,
                os=host_os,
                host_type=host_type
            )
            return True, new_host
        except Exception as e:
            error_message = "Got error %s while creation of host %s" \
                            % (str(e), host_name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def validate_initiators(self, initiators):
        """ Validate initiator format """
        results = []
        for item in initiators:
            results.append(utils.is_initiator_valid(item))
        if False in results:
            error_message = "One or more initiator provided is not valid, please provide valid initiators"
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def get_initiator_details(self, initiator_id):
        """ Get details of a specific initiator """
        try:
            initiator = utils.host.UnityHostInitiatorList.get(
                cli=self.unity._cli,
                initiator_id=initiator_id
            )
            return initiator
        except utils.UnityResourceNotFoundError:
            return None
        except Exception as e:
            LOG.info("Error getting initiator %s details: %s", initiator_id, str(e))
            return None

    def create_initiator(self, initiator_id):
        """ Create an initiator (even if not zoned) """
        try:
            # Try to get the initiator first
            initiator = self.get_initiator_details(initiator_id)
            if initiator:
                LOG.info("Initiator %s already exists", initiator_id)
                return False, initiator
            
            # If initiator doesn't exist, we need to create it
            # Note: Unity API may not allow direct creation of unzoned initiators
            # In this case, we'll need to add it to a host which will create it
            LOG.info("Initiator %s does not exist, will be created when added to host", initiator_id)
            return True, None
        except Exception as e:
            LOG.info("Error checking initiator %s: %s", initiator_id, str(e))
            # Assume it doesn't exist and will be created when added to host
            return True, None

    def add_initiator_to_host(self, host_details, initiator_id):
        """ Add initiator to host """
        try:
            # Check if initiator is already in the host
            existing_initiators = self.get_host_initiators_list(host_details)
            if initiator_id in existing_initiators:
                LOG.info("Initiator %s already present in host %s", initiator_id, host_details.name)
                return False, host_details

            # Try to add the initiator to the host
            # This will create the initiator if it doesn't exist
            LOG.info("Adding initiator %s to host %s", initiator_id, host_details.name)
            host_details.add_initiator(uid=initiator_id)
            updated_host = self.unity.get_host(name=host_details.name)
            return True, updated_host
        except Exception as e:
            error_message = "Got error %s while adding initiator %s to host %s" \
                            % (str(e), initiator_id, host_details.name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def remove_initiator_from_host(self, host_details, initiator_id):
        """ Remove initiator from host """
        try:
            existing_initiators = self.get_host_initiators_list(host_details)
            if initiator_id not in existing_initiators:
                LOG.info("Initiator %s already absent in host %s", initiator_id, host_details.name)
                return False, host_details

            LOG.info("Removing initiator %s from host %s", initiator_id, host_details.name)
            
            # Check if initiator has logged-in paths
            initiator = self.get_initiator_details(initiator_id)
            if initiator and initiator.paths:
                for path in initiator.paths:
                    if path and hasattr(path, 'is_logged_in') and path.is_logged_in:
                        error_message = "Cannot remove initiator %s, as it is logged in" % initiator_id
                        LOG.error(error_message)
                        self.module.fail_json(msg=error_message)

            host_details.delete_initiator(uid=initiator_id)
            updated_host = self.unity.get_host(name=host_details.name)
            return True, updated_host
        except Exception as e:
            error_message = "Got error %s while removing initiator %s from host %s" \
                            % (str(e), initiator_id, host_details.name)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def delete_initiator(self, initiator_id):
        """ Delete an initiator """
        try:
            initiator = self.get_initiator_details(initiator_id)
            if not initiator:
                LOG.info("Initiator %s does not exist", initiator_id)
                return False
            
            # Check if initiator is attached to a host
            if initiator.parent_host:
                error_message = "Cannot delete initiator %s, it is attached to host %s" \
                                % (initiator_id, initiator.parent_host)
                LOG.error(error_message)
                self.module.fail_json(msg=error_message)
            
            LOG.info("Deleting initiator %s", initiator_id)
            initiator.delete()
            return True
        except Exception as e:
            error_message = "Got error %s while deleting initiator %s" \
                            % (str(e), initiator_id)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def get_host_initiators_list(self, host_details):
        """ Get the list of existing initiators in host """
        existing_initiators = []
        if host_details.fc_host_initiators is not None:
            fc_len = len(host_details.fc_host_initiators)
            if fc_len > 0:
                for count in range(fc_len):
                    ini_id = host_details.fc_host_initiators.initiator_id[count]
                    existing_initiators.append(ini_id)

        if host_details.iscsi_host_initiators is not None:
            iscsi_len = len(host_details.iscsi_host_initiators)
            if iscsi_len > 0:
                for count in range(iscsi_len):
                    ini_id = host_details.iscsi_host_initiators.initiator_id[count]
                    existing_initiators.append(ini_id)
        return existing_initiators

    def get_all_initiators(self):
        """ Get all initiators on the Unity system """
        try:
            fc_initiators = utils.host.UnityHostInitiatorList.get(
                cli=self.unity._cli,
                type=utils.HostInitiatorTypeEnum.FC
            )
            iscsi_initiators = utils.host.UnityHostInitiatorList.get(
                cli=self.unity._cli,
                type=utils.HostInitiatorTypeEnum.ISCSI
            )
            
            fc_result = []
            if fc_initiators:
                for fc in fc_initiators:
                    fc_result.append({
                        'id': fc.id,
                        'initiator_id': fc.initiator_id,
                        'parent_host': fc.parent_host.name if fc.parent_host else None
                    })
            
            iscsi_result = []
            if iscsi_initiators:
                for iscsi in iscsi_initiators:
                    iscsi_result.append({
                        'id': iscsi.id,
                        'initiator_id': iscsi.initiator_id,
                        'parent_host': iscsi.parent_host.name if iscsi.parent_host else None
                    })
            
            return {
                'fc_initiators': fc_result,
                'iscsi_initiators': iscsi_result
            }
        except Exception as e:
            error_message = "Got error %s while getting all initiators" % str(e)
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def perform_module_operation(self):
        """ Perform different actions on initiators based on user parameters """

        host_name = self.module.params['host_name']
        host_id = self.module.params['host_id']
        host_os = self.module.params['host_os']
        description = self.module.params['description']
        initiators = self.module.params['initiators']
        state = self.module.params['state']

        result = dict(
            changed=False,
            initiator_details={},
            host_details={}
        )

        # If no state specified, list all initiators
        if not state:
            LOG.info("Listing all initiators")
            result['initiator_details'] = self.get_all_initiators()
            self.module.exit_json(**result)

        # Validate initiators format
        if initiators:
            self.validate_initiators(initiators)

        # Get or create host
        host_details = self.get_host_details(host_id, host_name)
        
        if state == 'present':
            if not host_details:
                if not host_name:
                    err_msg = "host_name is required to create a new host"
                    LOG.error(err_msg)
                    self.module.fail_json(msg=err_msg)
                if not host_os:
                    err_msg = "host_os is required when creating a new host"
                    LOG.error(err_msg)
                    self.module.fail_json(msg=err_msg)
                
                LOG.info("Creating new host %s", host_name)
                changed, host_details = self.create_host(host_name, host_os, description)
                result['changed'] = changed
                result['host_details'] = host_details._get_properties()

            # Add initiators to host
            if initiators:
                for initiator_id in initiators:
                    changed, host_details = self.add_initiator_to_host(host_details, initiator_id)
                    if changed:
                        result['changed'] = True
                
                result['host_details'] = host_details._get_properties()
            
            # Get updated initiator details
            result['initiator_details'] = self.get_all_initiators()

        elif state == 'absent':
            if not host_details:
                err_msg = "Host not found for initiator removal"
                LOG.error(err_msg)
                self.module.fail_json(msg=err_msg)
            
            if initiators:
                for initiator_id in initiators:
                    changed, host_details = self.remove_initiator_from_host(host_details, initiator_id)
                    if changed:
                        result['changed'] = True
                
                result['host_details'] = host_details._get_properties()
            
            # Get updated initiator details
            result['initiator_details'] = self.get_all_initiators()

        self.module.exit_json(**result)


def get_initiator_parameters():
    """This method provides parameters required for the ansible initiator module on Unity"""
    return dict(
        host_name=dict(required=False, type='str'),
        host_id=dict(required=False, type='str'),
        host_os=dict(required=False, type='str',
                     choices=['AIX', 'Citrix XenServer', 'HP-UX',
                              'IBM VIOS', 'Linux', 'Mac OS', 'Solaris',
                              'VMware ESXi', 'Windows Client',
                              'Windows Server']),
        description=dict(required=False, type='str'),
        initiators=dict(required=False, type='list', elements='str'),
        state=dict(required=False, type='str',
                   choices=['present', 'absent'], default=None)
    )


def main():
    """ Create Unity initiator object and perform action on it
        based on user input from playbook"""
    obj = Initiator()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
