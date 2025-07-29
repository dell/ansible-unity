.. _filesystem_snapshot_module:


filesystem_snapshot -- Manage filesystem snapshot on the Unity storage system
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing Filesystem Snapshot on the Unity storage system includes create filesystem snapshot, get filesystem snapshot, modify filesystem snapshot and delete filesystem snapshot.



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
    The name of the filesystem snapshot.

    Mandatory parameter for creating a filesystem snapshot.

    For all other operations either *snapshot_name* or *snapshot_id* is required.


  snapshot_id (optional, str, None)
    During creation snapshot_id is auto generated.

    For all other operations either *snapshot_id* or *snapshot_name* is required.


  filesystem_name (optional, str, None)
    The name of the Filesystem for which snapshot is created.

    For creation of filesystem snapshot either *filesystem_name* or *filesystem_id* is required.

    Not required for other operations.


  filesystem_id (optional, str, None)
    The ID of the Filesystem for which snapshot is created.

    For creation of filesystem snapshot either *filesystem_id* or *filesystem_name* is required.

    Not required for other operations.


  nas_server_name (optional, str, None)
    The name of the NAS server in which the Filesystem is created.

    For creation of filesystem snapshot either *nas_server_name* or *nas_server_id* is required.

    Not required for other operations.


  nas_server_id (optional, str, None)
    The ID of the NAS server in which the Filesystem is created.

    For creation of filesystem snapshot either *filesystem_id* or *filesystem_name* is required.

    Not required for other operations.


  auto_delete (optional, bool, None)
    This option specifies whether or not the filesystem snapshot will be automatically deleted.

    If set to ``true``, the filesystem snapshot will expire based on the pool auto deletion policy.

    If set to ``false``, the filesystem snapshot will not be auto deleted based on the pool auto deletion policy.

    Option *auto_delete* can not be set to ``true``, if *expiry_time* is specified.

    If during creation neither *auto_delete* nor *expiry_time* is mentioned then the filesystem snapshot will be created keeping *auto_delete* as ``true``.

    Once the *expiry_time* is set, then the filesystem snapshot cannot be assigned to the auto delete policy.


  expiry_time (optional, str, None)
    This option is for specifying the date and time after which the filesystem snapshot will expire.

    The time is to be mentioned in UTC timezone.

    The format is "MM/DD/YYYY HH:MM". Year must be in 4 digits.


  description (optional, str, None)
    The additional information about the filesystem snapshot can be provided using this option.

    The description can be removed by passing an empty string.


  fs_access_type (optional, str, None)
    Access type of the filesystem snapshot.

    Required only during creation of filesystem snapshot.

    If not given, snapshot's access type will be ``Checkpoint``.


  state (True, str, None)
    The state option is used to mention the existence of the filesystem snapshot.


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
   - Filesystem snapshot cannot be deleted, if it has nfs or smb share.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
      - name: Create Filesystem Snapshot
        filesystem_snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_name: "ansible_test_FS_snap"
          filesystem_name: "ansible_test_FS"
          nas_server_name: "lglad069"
          description: "Created using playbook"
          auto_delete: True
          fs_access_type: "Protocol"
          state: "present"

      - name: Create Filesystem Snapshot with expiry time
        filesystem_snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_name: "ansible_test_FS_snap_1"
          filesystem_name: "ansible_test_FS_1"
          nas_server_name: "lglad069"
          description: "Created using playbook"
          expiry_time: "04/15/2021 2:30"
          fs_access_type: "Protocol"
          state: "present"

      - name: Get Filesystem Snapshot Details using Name
        filesystem_snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_name: "ansible_test_FS_snap"
          state: "present"

      - name: Get Filesystem Snapshot Details using ID
        filesystem_snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_id: "10008000403"
          state: "present"

      - name: Update Filesystem Snapshot attributes
        filesystem_snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_name: "ansible_test_FS_snap"
          description: "Description updated"
          auto_delete: False
          expiry_time: "04/15/2021 5:30"
          state: "present"

      - name: Update Filesystem Snapshot attributes using ID
        filesystem_snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_id: "10008000403"
          expiry_time: "04/18/2021 8:30"
          state: "present"

      - name: Delete Filesystem Snapshot using Name
        filesystem_snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_name: "ansible_test_FS_snap"
          state: "absent"

      - name: Delete Filesystem Snapshot using ID
        filesystem_snapshot:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          snapshot_id: "10008000403"
          state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


filesystem_snapshot_details (When filesystem snapshot exists, dict, {'access_type': 'FilesystemSnapAccessTypeEnum.CHECKPOINT', 'attached_wwn': None, 'creation_time': '2022-10-21 04:42:53.951000+00:00', 'creator_schedule': None, 'creator_type': 'SnapCreatorTypeEnum.USER_CUSTOM', 'creator_user': {'id': 'user_admin'}, 'description': 'Created using playbook', 'existed': True, 'expiration_time': None, 'filesystem_id': 'fs_137', 'filesystem_name': 'test', 'hash': 8739894572587, 'host_access': None, 'id': '171798721695', 'io_limit_policy': None, 'is_auto_delete': True, 'is_modifiable': False, 'is_modified': False, 'is_read_only': True, 'is_system_snap': False, 'last_writable_time': None, 'lun': None, 'name': 'test_FS_snap_1', 'nas_server_id': 'nas_1', 'nas_server_name': 'lglad072', 'parent_snap': None, 'size': 107374182400, 'snap_group': None, 'state': 'SnapStateEnum.READY'})
  Details of the filesystem snapshot.


  access_type (, str, )
    Access type of filesystem snapshot.


  attached_wwn (, str, )
    Attached WWN details.


  creation_time (, str, )
    Creation time of filesystem snapshot.


  creator_schedule (, str, )
    Creator schedule of filesystem snapshot.


  creator_type (, str, )
    Creator type for filesystem snapshot.


  creator_user (, str, )
    Creator user for filesystem snapshot.


  description (, str, )
    Description of the filesystem snapshot.


  expiration_time (, str, )
    Date and time after which the filesystem snapshot will expire.


  is_auto_delete (, bool, )
    Is the filesystem snapshot is auto deleted or not.


  id (, str, )
    Unique identifier of the filesystem snapshot instance.


  name (, str, )
    The name of the filesystem snapshot.


  size (, int, )
    Size of the filesystem snapshot.


  filesystem_name (, str, )
    Name of the filesystem for which the snapshot exists.


  filesystem_id (, str, )
    Id of the filesystem for which the snapshot exists.


  nas_server_name (, str, )
    Name of the NAS server on which filesystem exists.


  nas_server_id (, str, )
    Id of the NAS server on which filesystem exists.






Status
------





Authors
~~~~~~~

- Rajshree Khare (@kharer5) <ansible.team@dell.com>

