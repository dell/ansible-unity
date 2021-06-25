#!/usr/bin/python
# Copyright: (c) 2020, DellEMC

"""Ansible module for managing storage pool on Unity"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_unity_storagepool

version_added: '1.1.0'

short_description: Manage storage pool on Unity

description:
- Managing storage pool on Unity storage system contains the following operations
- Get details of storage pool
- Modify storage pool

extends_documentation_fragment:
  - dellemc.unity.dellemc_unity.unity

author:
- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>

options:
  pool_name:
    description:
    - Name of the storage pool, unique in the storage system.
    type: str

  pool_id:
    description:
    - Unique identifier of the pool instance.
    type: str

  new_pool_name:
    description:
    - New name of the storage pool, unique in the storage system.
    type: str

  pool_description:
    description:
    - The description of the storage pool.
    type: str

  fast_cache:
    description:
    - Indicates whether the fast cache is enabled for the storage pool.
    - enabled - FAST Cache is enabled for the pool.
    - disabled - FAST Cache is disabled for the pool.
    choices: [enabled, disabled]
    type: str

  fast_vp:
    description:
    - Indicates whether to enable scheduled data relocations for the pool.
    - enabled - Enabled scheduled data relocations for the pool.
    - disabled - Disabled scheduled data relocations for the pool.
    choices: [enabled, disabled]
    type: str

  state:
    description:
    - Define whether the storage pool should exist or not.
    - present - indicates that the storage pool should exist on the system.
    - absent - indicates that the storage pool should not exist on the system.
    choices: [absent, present]
    type: str
    required: True

notes:
- Creation/Deletion of storage pool is not allowed through Ansible module.
'''

EXAMPLES = r'''
- name: Get Storage pool details using pool_name
  dellemc_unity_storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    pool_name: "{{pool_name}}"
    state: "present"

- name: Get Storage pool details using pool_id
  dellemc_unity_storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    pool_id: "{{pool_id}}"
    state: "present"

- name: Modify Storage pool attributes using pool_name
  dellemc_unity_storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    pool_name: "{{pool_name}}"
    new_pool_name: "{{new_pool_name}}"
    pool_description: "{{pool_description}}"
    fast_cache: "{{fast_cache_enabled}}"
    fast_vp: "{{fast_vp_enabled}}"
    state: "present"

- name: Modify Storage pool attributes using pool_id
  dellemc_unity_storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    pool_id: "{{pool_id}}"
    new_pool_name: "{{new_pool_name}}"
    pool_description: "{{pool_description}}"
    fast_cache: "{{fast_cache_enabled}}"
    fast_vp: "{{fast_vp_enabled}}"
    state: "present"

'''

RETURN = r'''
 changed:
    description: Whether or not the storage pool has changed.
    returned: always
    type: bool

 storage_pool_details:
    description: The storage pool details.
    returned: When storage pool exists.
    type: complex
    contains:
        id:
            description: Pool id, unique identifier of the pool.
            type: str
        name:
            description: Pool name, unique in the storage system.
            type: str
        is_fast_cache_enabled:
            description: Indicates whether the fast cache is enabled for the storage
                         pool.
                         true - FAST Cache is enabled for the pool.
                         false - FAST Cache is disabled for the pool.
            type: bool
        is_fast_vp_enabled:
            description: Indicates whether to enable scheduled data relocations
                         for the storage pool.
                         true - Enabled scheduled data relocations for the pool.
                         false - Disabled scheduled data relocations for the pool.
            type: bool
        size_free_with_unit:
            description: Indicates size_free with its appropriate unit
                         in human readable form.
            type: str
        size_subscribed_with_unit:
            description: Indicates size_subscribed with its appropriate unit in
                         human readable form.
            type: str
        size_total_with_unit:
            description: Indicates size_total with its appropriate unit in human
                         readable form.
            type: str
        size_used_with_unit:
            description: Indicates size_used with its appropriate unit in human
                         readable form.
            type: str
        snap_size_subscribed_with_unit:
            description: Indicates snap_size_subscribed with its
                         appropriate unit in human readable form.
            type: str
        snap_size_used_with_unit:
            description: Indicates snap_size_used with its
                         appropriate unit in human readable form.
            type: str
 '''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell \
    import dellemc_ansible_unity_utils as utils
import logging

LOG = utils.get_logger('dellemc_unity_storagepool', log_devel=logging.INFO)
HAS_UNITY_SDK = utils.get_unity_sdk()

UNITY_SDK_VERSION = utils.storops_version_check()
UNITY_SDK_VERSION_CHECK = UNITY_SDK_VERSION['supported_version']
UNITY_SDK_VERSION_ERROR = UNITY_SDK_VERSION['unsupported_version_message']

application_type = "Ansible/1.2.0"


class UnityStoragePool(object):
    """Class with storage pool operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_unity_management_host_parameters()
        self.module_params.update(get_unity_storagepool_parameters())

        mutually_exclusive = [['pool_name', 'pool_id']]
        required_one_of = [['pool_name', 'pool_id']]

        # initialize the Ansible module
        self.module = AnsibleModule(argument_spec=self.module_params,
                                    supports_check_mode=False,
                                    mutually_exclusive=mutually_exclusive,
                                    required_one_of=required_one_of)

        if not HAS_UNITY_SDK:
            self.module.fail_json(msg="Ansible modules for Unity require the"
                                      " Unity python library to be "
                                      "installed. Please install the library "
                                      "before using these modules.")

        if not UNITY_SDK_VERSION_CHECK:
            LOG.error(UNITY_SDK_VERSION_ERROR)
            self.module.fail_json(msg=UNITY_SDK_VERSION_ERROR)

        self.conn = utils.\
            get_unity_unisphere_connection(self.module.params, application_type)

    def get_details(self, pool_id, pool_name):
        """ Get storage pool details"""
        try:
            api_response = self.conn.get_pool(_id=pool_id, name=pool_name)
            details = api_response._get_properties()

            is_fast_vp_enabled = api_response._get_property_from_raw(
                'pool_fast_vp').is_schedule_enabled
            details['is_fast_vp_enabled'] = is_fast_vp_enabled

            details['size_free_with_unit'] = utils.\
                convert_size_with_unit(int(details['size_free']))

            details['size_subscribed_with_unit'] = utils.\
                convert_size_with_unit(int(details['size_subscribed']))

            details['size_total_with_unit'] = utils.\
                convert_size_with_unit(int(details['size_total']))

            details['size_used_with_unit'] = utils.\
                convert_size_with_unit(int(details['size_used']))

            details['snap_size_subscribed_with_unit'] = utils.\
                convert_size_with_unit(int(details['snap_size_subscribed']))

            details['snap_size_used_with_unit'] = utils.\
                convert_size_with_unit(int(details['snap_size_used']))

            pool_instance = utils.UnityPool.get(self.conn._cli, details['id'])
            pool_tier_list = []
            pool_tier_list.append((pool_instance.tiers)._get_properties())
            pool_tier_dict = {}
            pool_tier_dict['UnityPoolTierList'] = pool_tier_list
            details['tiers'] = pool_tier_dict
            return details
        except Exception as e:
            error = str(e)
            check_list = ['not found', 'no attribute']
            if any(ele in error for ele in check_list):
                error_message = "pool details are not found"
                LOG.info(error_message)
                return None
            error_message = 'Get details of storage pool failed with ' \
                            'error: {0}'.format(str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def is_pool_modification_required(self, storage_pool_details):
        """ Check if attributes of storage pool needs to be modified
        """
        try:
            if self.module.params['new_pool_name'] and \
                    self.module.params['new_pool_name'] != \
                    storage_pool_details['name']:
                return True

            if self.module.params['pool_description'] is not None and \
                    self.module.params['pool_description'] != \
                    storage_pool_details['description']:
                return True

            if self.module.params['fast_cache']:
                if self.module.params['fast_cache'] == "enabled" and\
                        not storage_pool_details['is_fast_cache_enabled']:
                    return True
                elif self.module.params['fast_cache'] == "disabled" and \
                        storage_pool_details['is_fast_cache_enabled']:
                    return True

            if self.module.params['fast_vp']:
                if self.module.params['fast_vp'] == "enabled" and\
                        not storage_pool_details['is_fast_vp_enabled']:
                    return True
                elif self.module.params['fast_vp'] == "disabled" and\
                        storage_pool_details['is_fast_vp_enabled']:
                    return True

            LOG.info("modify not required")
            return False

        except Exception as e:
            error_message = 'Failed to determine if any modification'\
                'required for pool attributes with error: {0}'.format(str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def pool_modify(self, id, new_pool_name,
                    pool_description, fast_cache, fast_vp):
        """ Modify attributes of storage pool """
        pool_obj = utils.UnityPool.get(self.conn._cli, id)
        try:
            pool_obj.modify(name=new_pool_name, description=pool_description,
                            is_fast_cache_enabled=fast_cache,
                            is_fastvp_enabled=fast_vp)
            new_storage_pool_details = self.get_details(pool_id=id,
                                                        pool_name=None)
            LOG.info("Modification Successful")
            return new_storage_pool_details
        except Exception as e:
            if self.module.params['pool_id']:
                pool_identifier = self.module.params['pool_id']
            else:
                pool_identifier = self.module.params['pool_name']
            error_message = 'Modify attributes of storage pool {0} ' \
                'failed with error: {1}'.format(pool_identifier, str(e))
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

    def perform_module_operation(self):
        """
        Perform different actions on storage pool module based on parameters
        chosen in playbook
        """
        pool_name = self.module.params['pool_name']
        pool_id = self.module.params['pool_id']
        new_pool_name = self.module.params['new_pool_name']
        pool_description = self.module.params['pool_description']
        fast_cache = self.module.params['fast_cache']
        fast_vp = self.module.params['fast_vp']
        state = self.module.params['state']

        if fast_cache:
            if fast_cache == "enabled":
                fast_cache = True
            else:
                fast_cache = False

        if fast_vp:
            if fast_vp == "enabled":
                fast_vp = True
            else:
                fast_vp = False

        # result is a dictionary that contains changed status and storage pool
        # details
        result = dict(
            changed=False,
            storage_pool_details=''
        )

        storage_pool_details = self.get_details(pool_id, pool_name)
        result['storage_pool_details'] = storage_pool_details

        if state == 'present' and not storage_pool_details:
            error_message = 'Storage pool not found - Creation of storage' \
                            ' pool is not allowed through Ansible module'
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

        if state == 'absent' and storage_pool_details:
            error_message = 'Deletion of storage pool is not allowed through'\
                            ' Ansible module'
            LOG.error(error_message)
            self.module.fail_json(msg=error_message)

        if state == 'present' and storage_pool_details:
            if new_pool_name is not None and len(new_pool_name) == 0:
                error_message = 'The parameter new_pool_name length is 0. It'\
                                ' is too short. The min length is 1'
                LOG.error(error_message)
                self.module.fail_json(msg=error_message)
            pool_modify_flag = self.\
                is_pool_modification_required(storage_pool_details)
            LOG.info("Storage pool modification flag %s",
                     str(pool_modify_flag))

            if pool_modify_flag:
                id = storage_pool_details['id']
                result['storage_pool_details'] = \
                    self.pool_modify(id, new_pool_name,
                                     pool_description, fast_cache, fast_vp)
                result['changed'] = True
        self.module.exit_json(**result)


def get_unity_storagepool_parameters():
    """This method provides parameters required for the ansible storage pool
    module on Unity"""
    return dict(
        pool_name=dict(required=False, type='str'),
        pool_id=dict(required=False, type='str'),
        new_pool_name=dict(required=False, type='str'),
        pool_description=dict(required=False, type='str'),
        fast_cache=dict(required=False, type='str', choices=['enabled',
                                                             'disabled']),
        fast_vp=dict(required=False, type='str', choices=['enabled',
                                                          'disabled']),
        state=dict(required=True, type='str', choices=['present', 'absent'])
    )


def main():
    """ Create Unity storage pool object and perform action on it
        based on user input from playbook"""
    obj = UnityStoragePool()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
