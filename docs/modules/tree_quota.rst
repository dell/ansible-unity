.. _tree_quota_module:


tree_quota -- Manage quota tree on the Unity storage system
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing Quota tree on the Unity storage system includes Create quota tree, Get quota tree, Modify quota tree and Delete quota tree.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  filesystem_name (optional, str, None)
    The name of the filesystem for which quota tree is created.

    For creation or modification of a quota tree either *filesystem_name* or *filesystem_id* is required.


  filesystem_id (optional, str, None)
    The ID of the filesystem for which the quota tree is created.

    For creation of a quota tree either *filesystem_id* or *filesystem_name* is required.


  nas_server_name (optional, str, None)
    The name of the NAS server in which the filesystem is created.

    For creation of a quota tree either *nas_server_name* or *nas_server_id* is required.


  nas_server_id (optional, str, None)
    The ID of the NAS server in which the filesystem is created.

    For creation of a quota tree either *filesystem_id* or *filesystem_name* is required.


  tree_quota_id (optional, str, None)
    The ID of the quota tree.

    Either *tree_quota_id* or *path* to quota tree is required to view/modify/delete quota tree.


  path (optional, str, None)
    The path to the quota tree.

    Either *tree_quota_id* or *path* to quota tree is required to create/view/modify/delete a quota tree.

    Path must start with a forward slash '/'.


  hard_limit (optional, int, None)
    Hard limitation for a quota tree on the total space available. If exceeded, users in quota tree cannot write data.

    Value ``0`` implies no limit.

    One of the values of *soft_limit* and *hard_limit* can be ``0``, however, both cannot be both ``0`` during creation of a quota tree.


  soft_limit (optional, int, None)
    Soft limitation for a quota tree on the total space available. If exceeded, notification will be sent to users in the quota tree for the grace period mentioned, beyond which users cannot use space.

    Value ``0`` implies no limit.

    Both *soft_limit* and *hard_limit* cannot be ``0`` during creation of quota tree.


  cap_unit (optional, str, None)
    Unit of *soft_limit* and *hard_limit* size.

    It defaults to ``GB`` if not specified.


  description (optional, str, None)
    Description of a quota tree.


  state (True, str, None)
    The state option is used to mention the existence of the filesystem quota tree.


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

    
      - name: Get quota tree details by quota tree id
        tree_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          tree_quota_id: "treequota_171798700679_10"
          state: "present"

      - name: Get quota tree details by quota tree path
        tree_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_name: "fs_2171"
          nas_server_id: "nas_21"
          path: "/test"
          state: "present"

      - name: Create quota tree for a filesystem with filesystem id
        tree_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          hard_limit: 6
          cap_unit: "TB"
          soft_limit: 5
          path: "/test_new"
          state: "present"

      - name: Create quota tree for a filesystem with filesystem name
        tree_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_name: "Test_filesystem"
          nas_server_name: "lglad068"
          hard_limit: 6
          cap_unit: "TB"
          soft_limit:  5
          path: "/test_new"
          state: "present"

      - name: Modify quota tree limit usage by quota tree path
        tree_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          path: "/test_new"
          hard_limit: 10
          cap_unit: "TB"
          soft_limit: 8
          state: "present"

      - name: Modify quota tree by quota tree id
        tree_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          tree_quota_id: "treequota_171798700679_10"
          hard_limit: 12
          cap_unit: "TB"
          soft_limit: 10
          state: "present"

      - name: Delete quota tree by quota tree id
        tree_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          tree_quota_id: "treequota_171798700679_10"
          state: "absent"

      - name: Delete quota tree by path
        tree_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          path: "/test_new"
          state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


get_tree_quota_details (When quota tree exists, dict, {'description': '', 'existed': True, 'filesystem': {'UnityFileSystem': {'hash': 8788549469862, 'id': 'fs_137', 'name': 'test', 'nas_server': {'id': 'nas_1', 'name': 'lglad072'}}}, 'gp_left': None, 'hard_limit': '6.0 TB', 'hash': 8788549497558, 'id': 'treequota_171798694897_1', 'path': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 'size_used': 0, 'soft_limit': '5.0 TB', 'state': 0})
  Details of the quota tree.


  filesystem (, dict, )
    Filesystem details for which the quota tree is created.


    UnityFileSystem (, dict, )
      Filesystem details for which the quota tree is created.


      id (, str, )
        ID of the filesystem for which the quota tree is create.




  description (, str, )
    Description of the quota tree.


  path (, str, )
    Path to quota tree. A valid path must start with a forward slash '/'. It is mandatory while creating a quota tree.


  hard_limit (, int, )
    Hard limit of quota tree. If the quota tree's space usage exceeds the hard limit, users in quota tree cannot write data.


  soft_limit (, int, )
    Soft limit of the quota tree. If the quota tree's space usage exceeds the soft limit, the storage system starts to count down based on the specified grace period.


  id (, str, )
    Quota tree ID.


  size_used (, int, )
    Size of used space in the filesystem by the user files.


  gp_left (, int, )
    The grace period left after the soft limit for the user quota is exceeded.


  state (, int, )
    State of the quota tree.






Status
------





Authors
~~~~~~~

- Spandita Panigrahi (@panigs7) <ansible.team@dell.com>

