.. _smbshare_module:


smbshare -- Manage SMB shares on Unity storage system
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing SMB Shares on Unity storage system includes create, get, modify, and delete the smb shares.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  share_name (optional, str, None)
    Name of the SMB share.

    Required during creation of the SMB share.

    For all other operations either *share_name* or *share_id* is required.


  share_id (optional, str, None)
    ID of the SMB share.

    Should not be specified during creation. Id is auto generated.

    For all other operations either *share_name* or *share_id* is required.

    If *share_id* is used then no need to pass nas_server/filesystem/snapshot/path.


  path (optional, str, None)
    Local path to the file system/Snapshot or any existing sub-folder of the file system/Snapshot that is shared over the network.

    Path is relative to the root of the filesystem.

    Required for creation of the SMB share.


  filesystem_id (optional, str, None)
    The ID of the File System.

    Either *filesystem_name* or *filesystem_id* is required for creation of the SMB share for filesystem.

    If *filesystem_name* is specified, then *nas_server_name*/*nas_server_id* is required to uniquely identify the filesystem.

    Options *filesystem_name* and *filesystem_id* are mutually exclusive parameters.


  snapshot_id (optional, str, None)
    The ID of the Filesystem Snapshot.

    Either *snapshot_name* or *snapshot_id* is required for creation of the SMB share for a snapshot.

    If *snapshot_name* is specified, then *nas_server_name*/*nas_server_id* is required to uniquely identify the snapshot.

    Options *snapshot_name* and *snapshot_id* are mutually exclusive parameters.


  nas_server_id (optional, str, None)
    The ID of the NAS Server.

    It is not required if *share_id* is used.


  filesystem_name (optional, str, None)
    The Name of the File System.

    Either *filesystem_name* or *filesystem_id* is required for creation of the SMB share for filesystem.

    If *filesystem_name* is specified, then *nas_server_name*/*nas_server_id* is required to uniquely identify the filesystem.

    Options *filesystem_name* and *filesytem_id* are mutually exclusive parameters.


  snapshot_name (optional, str, None)
    The Name of the Filesystem Snapshot.

    Either *snapshot_name* or *snapshot_id* is required for creation of the SMB share for a snapshot.

    If *snapshot_name* is specified, then *nas_server_name*/*nas_server_id* is required to uniquely identify the snapshot.

    Options *snapshot_name* and *snapshot_id* are mutually exclusive parameters.


  nas_server_name (optional, str, None)
    The Name of the NAS Server.

    It is not required if *share_id* is used.

    Options *nas_server_name* and *nas_server_id* are mutually exclusive parameters.


  description (optional, str, None)
    Description for the SMB share.

    Optional parameter when creating a share.

    To modify, pass the new value in description field.


  is_abe_enabled (optional, bool, None)
    Indicates whether Access-based Enumeration (ABE) for SMB share is enabled.

    During creation, if not mentioned then default is ``false``.


  is_branch_cache_enabled (optional, bool, None)
    Indicates whether Branch Cache optimization for SMB share is enabled.

    During creation, if not mentioned then default is ``false``.


  is_continuous_availability_enabled (optional, bool, None)
    Indicates whether continuous availability for SMB 3.0 is enabled.

    During creation, if not mentioned then default is ``false``.


  is_encryption_enabled (optional, bool, None)
    Indicates whether encryption for SMB 3.0 is enabled at the shared folder level.

    During creation, if not mentioned then default is ``false``.


  offline_availability (optional, str, None)
    Defines valid states of Offline Availability.

    ``MANUAL``- Only specified files will be available offline.

    ``DOCUMENTS``- All files that users open will be available offline.

    ``PROGRAMS``- Program will preferably run from the offline cache even when connected to the network. All files that users open will be available offline.

    ``NONE``- Prevents clients from storing documents and programs in offline cache.


  umask (optional, str, None)
    The default UNIX umask for new files created on the SMB Share.


  state (True, str, None)
    Define whether the SMB share should exist or not.

    Value ``present`` indicates that the share should exist on the system.

    Value ``absent`` indicates that the share should not exist on the system.


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
   - When ID/Name of the filesystem/snapshot is passed then *nas_server* is not required. If passed, then filesystem/snapshot should exist for the mentioned *nas_server*, else the task will fail.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create SMB share for a filesystem
      smbshare:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        share_name: "sample_smb_share"
        filesystem_name: "sample_fs"
        nas_server_id: "NAS_11"
        path: "/sample_fs"
        description: "Sample SMB share created"
        is_abe_enabled: True
        is_branch_cache_enabled: True
        offline_availability: "DOCUMENTS"
        is_continuous_availability_enabled: True
        is_encryption_enabled: True
        umask: "777"
        state: "present"
    - name: Modify Attributes of SMB share for a filesystem
      smbshare:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        share_name: "sample_smb_share"
        nas_server_name: "sample_nas_server"
        description: "Sample SMB share attributes updated"
        is_abe_enabled: False
        is_branch_cache_enabled: False
        offline_availability: "MANUAL"
        is_continuous_availability_enabled: "False"
        is_encryption_enabled: "False"
        umask: "022"
        state: "present"
    - name: Create SMB share for a snapshot
      smbshare:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        share_name: "sample_snap_smb_share"
        snapshot_name: "sample_snapshot"
        nas_server_id: "NAS_11"
        path: "/sample_snapshot"
        description: "Sample SMB share created for snapshot"
        is_abe_enabled: True
        is_branch_cache_enabled: True
        is_continuous_availability_enabled: True
        is_encryption_enabled: True
        umask: "777"
        state: "present"
    - name: Modify Attributes of SMB share for a snapshot
      smbshare:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        share_name: "sample_snap_smb_share"
        snapshot_name: "sample_snapshot"
        description: "Sample SMB share attributes updated for snapshot"
        is_abe_enabled: False
        is_branch_cache_enabled: False
        offline_availability: "MANUAL"
        is_continuous_availability_enabled: "False"
        is_encryption_enabled: "False"
        umask: "022"
        state: "present"
    - name: Get details of SMB share
      smbshare:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        share_id: "{{smb_share_id}}"
        state: "present"
    - name: Delete SMB share
      smbshare:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        share_id: "{{smb_share_id}}"
        state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


smb_share_details (When share exists., dict, {'creation_time': '2022-03-17 11:56:54.867000+00:00', 'description': '', 'existed': True, 'export_paths': ['\\\\multi-prot-pie.extreme1.com\\multi-prot-hui', '\\\\10.230.24.26\\multi-prot-hui'], 'filesystem': {'UnityFileSystem': {'hash': 8748426746492}}, 'filesystem_id': 'fs_140', 'filesystem_name': 'multi-prot-hui', 'hash': 8748426746588, 'id': 'SMBShare_20', 'is_abe_enabled': False, 'is_ace_enabled': False, 'is_branch_cache_enabled': False, 'is_continuous_availability_enabled': False, 'is_dfs_enabled': False, 'is_encryption_enabled': False, 'is_read_only': None, 'modified_time': '2022-03-17 11:56:54.867000+00:00', 'name': 'multi-prot-hui', 'nas_server_id': 'nas_5', 'nas_server_name': 'multi-prot', 'offline_availability': 'CifsShareOfflineAvailabilityEnum.NONE', 'path': '/', 'snap': None, 'type': 'CIFSTypeEnum.CIFS_SHARE', 'umask': '022'})
  The SMB share details.


  id (, str, )
    The ID of the SMB share.


  name (, str, sample_smb_share)
    Name of the SMB share.


  filesystem_id (, str, )
    The ID of the Filesystem.


  filesystem_name (, str, )
    The Name of the filesystem


  snapshot_id (, str, )
    The ID of the Snapshot.


  snapshot_name (, str, )
    The Name of the Snapshot.


  nas_server_id (, str, )
    The ID of the nas_server.


  nas_server_name (, str, )
    The Name of the nas_server.


  description (, str, This share is created for demo purpose only.)
    Additional information about the share.


  is_abe_enabled (, bool, False)
    Whether Access Based enumeration is enforced or not.


  is_branch_cache_enabled (, bool, False)
    Whether branch cache is enabled or not.


  is_continuous_availability_enabled (, bool, False)
    Whether the share will be available continuously or not.


  is_encryption_enabled (, bool, False)
    Whether encryption is enabled or not.


  umask (, str, )
    Unix mask for the SMB share.






Status
------





Authors
~~~~~~~

- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

