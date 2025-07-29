.. _snapshot_module:


snapshot -- Manage snapshots on the Unity storage system
========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing snapshots on the Unity storage system includes create snapshot, delete snapshot, update snapshot, get snapshot, map host and unmap host.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  snapshot_name (optional, str, None)
    The name of the snapshot.

    Mandatory parameter for creating a snapshot.

    For all other operations either *snapshot_name* or *snapshot_id* is required.


  vol_name (optional, str, None)
    The name of the volume for which snapshot is created.

    For creation of a snapshot either *vol_name* or *cg_name* is required.

    Not required for other operations.


  cg_name (optional, str, None)
    The name of the Consistency Group for which snapshot is created.

    For creation of a snapshot either *vol_name* or *cg_name* is required.

    Not required for other operations.


  snapshot_id (optional, str, None)
    The id of the snapshot.

    For all operations other than creation either *snapshot_name* or *snapshot_id* is required.


  auto_delete (optional, bool, None)
    This option specifies whether the snapshot is auto deleted or not.

    If set to ``true``, snapshot will expire based on the pool auto deletion policy.

    If set to (false), snapshot will not be auto deleted based on the pool auto deletion policy.

    Option *auto_delete* can not be set to ``true``, if *expiry_time* is specified.

    If during creation neither *auto_delete* nor *expiry_time* is mentioned then snapshot will be created keeping *auto_delete* as ``true``.

    Once the *expiry_time* is set then snapshot cannot be assigned to the auto delete policy.


  expiry_time (optional, str, None)
    This option is for specifying the date and time after which the snapshot will expire.

    The time is to be mentioned in UTC timezone.

    The format is "MM/DD/YYYY HH:MM". Year must be in 4 digits.


  description (optional, str, None)
    The additional information about the snapshot can be provided using this option.


  new_snapshot_name (optional, str, None)
    New name for the snapshot.


  state (True, str, None)
    The *state* option is used to mention the existence of the snapshot.


  host_name (optional, str, None)
    The name of the host.

    Either *host_name* or *host_id* is required to map or unmap a snapshot from a host.

    Snapshot can be attached to multiple hosts.


  host_id (optional, str, None)
    The id of the host.

    Either *host_name* or *host_id* is required to map or unmap a snapshot from a host.

    Snapshot can be attached to multiple hosts.


  host_state (optional, str, None)
    The *host_state* option is used to mention the existence of the host for snapshot.

    It is required when a snapshot is mapped or unmapped from host.


  unispherehost (True, str, None)
    IP or FQDN of the Unity management server.


  username (True, str, None)
    The username of the Unity management server.


  password (True, str, None)
    The password of the Unity management server.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether or not to validate SSL certificate.

    ``true`` - Indicates that the SSL certificate should be verified.

    ``false`` - Indicates that the SSL certificate should not be verified.


  port (optional, int, 443)
    Port number through which communication happens with Unity management server.





Notes
-----

.. note::
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
      - name: Create a Snapshot for a CG
        snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          port: "{{port}}"
          cg_name: "{{cg_name}}"
          snapshot_name: "{{cg_snapshot_name}}"
          description: "{{description}}"
          auto_delete: False
          state: "present"

      - name: Create a Snapshot for a volume with Host attached
        snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          port: "{{port}}"
          vol_name: "{{vol_name}}"
          snapshot_name: "{{vol_snapshot_name}}"
          description: "{{description}}"
          expiry_time: "04/15/2025 16:30"
          host_name: "{{host_name}}"
          host_state: "mapped"
          state: "present"

      - name: Unmap a host for a Snapshot
        snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          port: "{{port}}"
          snapshot_name: "{{vol_snapshot_name}}"
          host_name: "{{host_name}}"
          host_state: "unmapped"
          state: "present"

      - name: Map snapshot to a host
        snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          port: "{{port}}"
          snapshot_name: "{{vol_snapshot_name}}"
          host_name: "{{host_name}}"
          host_state: "mapped"
          state: "present"

      - name: Update attributes of a Snapshot for a volume
        snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_name: "{{vol_snapshot_name}}"
          new_snapshot_name: "{{new_snapshot_name}}"
          description: "{{new_description}}"
          host_name: "{{host_name}}"
          host_state: "unmapped"
          state: "present"

      - name: Delete Snapshot of CG
        snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_name: "{{cg_snapshot_name}}"
          state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


snapshot_details (When snapshot exists, dict, {'access_type': None, 'attached_wwn': None, 'creation_time': '2022-10-21 08:20:25.803000+00:00', 'creator_schedule': None, 'creator_type': 'SnapCreatorTypeEnum.USER_CUSTOM', 'creator_user': {'id': 'user_admin'}, 'description': 'Test snap creation', 'existed': True, 'expiration_time': None, 'hash': 8756689457056, 'hosts_list': [], 'id': '85899355291', 'io_limit_policy': None, 'is_auto_delete': True, 'is_modifiable': False, 'is_modified': False, 'is_read_only': True, 'is_system_snap': False, 'last_writable_time': None, 'lun': None, 'name': 'ansible_snap_cg_1_1', 'parent_snap': None, 'size': None, 'snap_group': None, 'state': 'SnapStateEnum.READY', 'storage_resource_id': 'res_95', 'storage_resource_name': 'CG_ansible_test_2_new'})
  Details of the snapshot.


  is_auto_delete (, str, )
    Additional information mentioned for snapshot.


  expiration_time (, str, )
    Date and time after which the snapshot will expire.


  hosts_list (, dict, )
    Contains the name and id of the associated hosts.


  id (, str, )
    Unique identifier of the snapshot instance.


  name (, str, )
    The name of the snapshot.


  storage_resource_name (, str, )
    Name of the storage resource for which the snapshot exists.


  storage_resource_id (, str, )
    Id of the storage resource for which the snapshot exists.






Status
------





Authors
~~~~~~~

- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

