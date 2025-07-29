.. _user_quota_module:


user_quota -- Manage user quota on the Unity storage system
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing User Quota on the Unity storage system includes Create user quota, Get user quota, Modify user quota, Delete user quota, Create user quota for quota tree, Modify user quota for quota tree and Delete user quota for quota tree.



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
    The name of the filesystem for which the user quota is created.

    For creation of a user quota either *filesystem_name* or *filesystem_id* is required.


  filesystem_id (optional, str, None)
    The ID of the filesystem for which the user quota is created.

    For creation of a user quota either *filesystem_id* or *filesystem_name* is required.


  nas_server_name (optional, str, None)
    The name of the NAS server in which the filesystem is created.

    For creation of a user quota either *nas_server_name* or *nas_server_id* is required.


  nas_server_id (optional, str, None)
    The ID of the NAS server in which the filesystem is created.

    For creation of a user quota either *filesystem_id* or *filesystem_name* is required.


  hard_limit (optional, int, None)
    Hard limitation for a user on the total space available. If exceeded, user cannot write data.

    Value ``0`` implies no limit.

    One of the values of *soft_limit* and *hard_limit* can be ``0``, however, both cannot be ``0`` during creation or modification of user quota.


  soft_limit (optional, int, None)
    Soft limitation for a user on the total space available. If exceeded, notification will be sent to the user for the grace period mentioned, beyond which the user cannot use space.

    Value ``0`` implies no limit.

    Both *soft_limit* and *hard_limit* cannot be ``0`` during creation or modification of user quota.


  cap_unit (optional, str, None)
    Unit of *soft_limit* and *hard_limit* size.

    It defaults to ``GB`` if not specified.


  user_type (optional, str, None)
    Type of user creating a user quota.

    Mandatory while creating or modifying user quota.


  win_domain (optional, str, None)
    Fully qualified or short domain name for Windows user type.

    Mandatory when *user_type* is ``Windows``.


  user_name (optional, str, None)
    User name of the user quota when *user_type* is ``Windows`` or ``Unix``.

    Option *user_name* must be specified along with *win_domain* when *user_type* is ``Windows``.


  uid (optional, str, None)
    User ID of the user quota.


  user_quota_id (optional, str, None)
    User quota ID generated after creation of a user quota.


  tree_quota_id (optional, str, None)
    The ID of the quota tree.

    Either *tree_quota_id* or *path* to quota tree is required to create/modify/delete user quota for a quota tree.


  path (optional, str, None)
    The path to the quota tree.

    Either *tree_quota_id* or *path* to quota tree is required to create/modify/delete user quota for a quota tree.

    Path must start with a forward slash '/'.


  state (True, str, None)
    The *state* option is used to mention the existence of the user quota.


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

    
      - name: Get user quota details by user quota id
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          user_quota_id: "userquota_171798700679_0_123"
          state: "present"

      - name: Get user quota details by user quota uid/user name
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_name: "fs_2171"
          nas_server_id: "nas_21"
          user_name: "test"
          state: "present"

      - name: Create user quota for a filesystem with filesystem id
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          hard_limit: 6
          cap_unit: "TB"
          soft_limit: 5
          uid: "111"
          state: "present"

      - name: Create user quota for a filesystem with filesystem name
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_name: "Test_filesystem"
          nas_server_name: "lglad068"
          hard_limit: 6
          cap_unit: "TB"
          soft_limit:  5
          uid: "111"
          state: "present"

      - name: Modify user quota limit usage by user quota id
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          user_quota_id: "userquota_171798700679_0_123"
          hard_limit: 10
          cap_unit: "TB"
          soft_limit: 8
          state: "present"

      - name: Modify user quota by filesystem id and user quota uid/user_name
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          user_type: "Windows"
          win_domain: "prod"
          user_name: "sample"
          hard_limit: 12
          cap_unit: "TB"
          soft_limit: 10
          state: "present"

      - name: Delete user quota
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          win_domain: "prod"
          user_name: "sample"
          state: "absent"

      - name: Create user quota of a quota tree
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          tree_quota_id: "treequota_171798700679_4"
          user_type: "Windows"
          win_domain: "prod"
          user_name: "sample"
          soft_limit: 9
          cap_unit: "TB"
          state: "present"

      - name: Create user quota of a quota tree by quota tree path
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          path: "/sample"
          user_type: "Unix"
          user_name: "test"
          hard_limit: 2
          cap_unit: "TB"
          state: "present"

      - name: Modify user quota of a quota tree
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          tree_quota_id: "treequota_171798700679_4"
          user_type: "Windows"
          win_domain: "prod"
          user_name: "sample"
          soft_limit: 10
          cap_unit: "TB"
          state: "present"

      - name: Modify user quota of a quota tree by quota tree path
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          path: "/sample"
          user_type: "Windows"
          win_domain: "prod"
          user_name: "sample"
          hard_limit: 12
          cap_unit: "TB"
          state: "present"

      - name: Delete user quota of a quota tree by quota tree path
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          filesystem_id: "fs_2171"
          path: "/sample"
          win_domain: "prod"
          user_name: "sample"
          state: "absent"

      - name: Delete user quota of a quota tree by quota tree id
        user_quota:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          tree_quota_id: "treequota_171798700679_4"
          win_domain: "prod"
          user_name: "sample"
          state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


get_user_quota_details (When user quota exists, dict, {'existed': True, 'filesystem': {'UnityFileSystem': {'hash': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 'id': 'fs_120', 'name': 'nfs-multiprotocol', 'nas_server': {'id': 'nas_1', 'name': 'lglad072'}}}, 'gp_left': None, 'hard_limit': '10.0 GB', 'hard_ratio': None, 'hash': 8752448438089, 'id': 'userquota_171798694698_0_60000', 'size_used': 0, 'soft_limit': '10.0 GB', 'soft_ratio': None, 'state': 0, 'tree_quota': None, 'uid': 60000, 'unix_name': None, 'windows_names': None, 'windows_sids': None})
  Details of the user quota.


  filesystem (, dict, )
    Filesystem details for which the user quota is created.


    UnityFileSystem (, dict, )
      Filesystem details for which the user quota is created.


      id (, str, )
        ID of the filesystem for which the user quota is created.


      name (, str, )
        Name of filesystem.


      nas_server (, dict, )
        Nasserver details where filesystem is created.


        name (, str, )
          Name of nasserver.


        id (, str, )
          ID of nasserver.





  tree_quota (, dict, )
    Quota tree details for which the user quota is created.


    UnityTreeQuota (, dict, )
      Quota tree details for which the user quota is created.


      id (, str, )
        ID of the quota tree.


      path (, str, )
        Path to quota tree.




  gp_left (, int, )
    The grace period left after the soft limit for the user quota is exceeded.


  hard_limit (, int, )
    Hard limitation for a user on the total space available. If exceeded, user cannot write data.


  hard_ratio (, str, )
    The hard ratio is the ratio between the hard limit size of the user quota and the amount of storage actually consumed.


  soft_limit (, int, )
    Soft limitation for a user on the total space available. If exceeded, notification will be sent to user for the grace period mentioned, beyond which user cannot use space.


  soft_ratio (, str, )
    The soft ratio is the ratio between the soft limit size of the user quota and the amount of storage actually consumed.


  id (, str, )
    User quota ID.


  size_used (, int, )
    Size of used space in the filesystem by the user files.


  state (, int, )
    State of the user quota.


  uid (, int, )
    User ID of the user.


  unix_name (, str, )
    Unix user name for this user quota's uid.


  windows_names (, str, )
    Windows user name that maps to this quota's uid.


  windows_sids (, str, )
    Windows SIDs that maps to this quota's uid






Status
------





Authors
~~~~~~~

- Spandita Panigrahi (@panigs7) <ansible.team@dell.com>

