.. _filesystem_module:


filesystem -- Manage filesystem on Unity storage system
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing filesystem on Unity storage system includes Create new filesystem, Modify snapschedule attribute of filesystem, Modify filesystem attributes, Display filesystem details, Display filesystem snapshots, Display filesystem snapschedule, Delete snapschedule associated with the filesystem, Delete filesystem, Create new filesystem with quota configuration, Enable, modify and disable replication.



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
    The name of the filesystem. Mandatory only for the create operation. All the operations are supported through *filesystem_name*.

    It is mutually exclusive with *filesystem_id*.


  filesystem_id (optional, str, None)
    The id of the filesystem.

    It can be used only for get, modify, or delete operations.

    It is mutually exclusive with *filesystem_name*.


  pool_name (optional, str, None)
    This is the name of the pool where the filesystem will be created.

    Either the *pool_name* or *pool_id* must be provided to create a new filesystem.


  pool_id (optional, str, None)
    This is the ID of the pool where the filesystem will be created.

    Either the *pool_name* or *pool_id* must be provided to create a new filesystem.


  size (optional, int, None)
    The size of the filesystem.


  cap_unit (optional, str, None)
    The unit of the filesystem size. It defaults to ``GB``, if not specified.


  nas_server_name (optional, str, None)
    Name of the NAS server on which filesystem will be hosted.


  nas_server_id (optional, str, None)
    ID of the NAS server on which filesystem will be hosted.


  supported_protocols (optional, str, None)
    Protocols supported by the file system.

    It will be overridden by NAS server configuration if NAS Server is ``Multiprotocol``.


  description (optional, str, None)
    Description about the filesystem.

    Description can be removed by passing empty string ("").


  smb_properties (optional, dict, None)
    Advance settings for SMB. It contains optional candidate variables.


    is_smb_sync_writes_enabled (optional, bool, None)
      Indicates whether the synchronous writes option is enabled on the file system.


    is_smb_notify_on_access_enabled (optional, bool, None)
      Indicates whether notifications of changes to directory file structure are enabled.


    is_smb_op_locks_enabled (optional, bool, None)
      Indicates whether opportunistic file locking is enabled on the file system.


    is_smb_notify_on_write_enabled (optional, bool, None)
      Indicates whether file write notifications are enabled on the file system.


    smb_notify_on_change_dir_depth (optional, int, None)
      Integer variable, determines the lowest directory level to which the enabled notifications apply.

      Minimum value is ``1``.



  data_reduction (optional, bool, None)
    Boolean variable, specifies whether or not to enable compression. Compression is supported only for thin filesystem.


  is_thin (optional, bool, None)
    Boolean variable, specifies whether or not it is a thin filesystem.


  access_policy (optional, str, None)
    Access policy of a filesystem.


  locking_policy (optional, str, None)
    File system locking policies. These policy choices control whether the NFSv4 range locks must be honored.


  tiering_policy (optional, str, None)
    Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.


  quota_config (optional, dict, None)
    Configuration for quota management. It contains optional parameters.


    grace_period (optional, int, None)
      Grace period set in quota configuration after soft limit is reached.

      If *grace_period* is not set during creation of filesystem, it will be set to ``7 days`` by default.


    grace_period_unit (optional, str, None)
      Unit of grace period.

      Default unit is ``days``.


    default_hard_limit (optional, int, None)
      Default hard limit for user quotas and tree quotas.

      If *default_hard_limit* is not set while creation of filesystem, it will be set to ``0B`` by default.


    default_soft_limit (optional, int, None)
      Default soft limit for user quotas and tree quotas.

      If *default_soft_limit* is not set while creation of filesystem, it will be set to ``0B`` by default.


    is_user_quota_enabled (optional, bool, None)
      Indicates whether the user quota is enabled.

      If *is_user_quota_enabled* is not set while creation of filesystem, it will be set to ``false`` by default.

      Parameters *is_user_quota_enabled* and *quota_policy* are mutually exclusive.


    quota_policy (optional, str, None)
      Quota policy set in quota configuration.

      If *quota_policy* is not set while creation of filesystem, it will be set to ``FILE_SIZE`` by default.

      Parameters *is_user_quota_enabled* and *quota_policy* are mutually exclusive.


    cap_unit (optional, str, None)
      Unit of *default_soft_limit* and *default_hard_limit* size.

      Default unit is ``GB``.



  state (True, str, None)
    State variable to determine whether filesystem will exist or not.


  snap_schedule_name (optional, str, None)
    This is the name of an existing snapshot schedule which is to be associated with the filesystem.

    This is mutually exclusive with *snapshot_schedule_id*.


  snap_schedule_id (optional, str, None)
    This is the id of an existing snapshot schedule which is to be associated with the filesystem.

    This is mutually exclusive with *snapshot_schedule_name*.


  replication_params (optional, dict, None)
    Settings required for enabling or modifying replication.


    replication_name (optional, str, None)
      Name of the replication session.


    new_replication_name (optional, str, None)
      Replication name to rename the session to.


    replication_mode (optional, str, None)
      The replication mode.

      This is a mandatory field while creating a replication session.


    rpo (optional, int, None)
      Maximum time to wait before the system syncs the source and destination LUNs.

      The *rpo* option should be specified if the *replication_mode* is ``asynchronous``.

      The value should be in range of ``5`` to ``1440`` for ``asynchronous``, ``0`` for ``synchronous`` and ``-1`` for ``manual``.


    replication_type (optional, str, None)
      Type of replication.


    remote_system (optional, dict, None)
      Details of remote system to which the replication is being configured.

      The *remote_system* option should be specified if the *replication_type* is ``remote``.


      remote_system_host (True, str, None)
        IP or FQDN for remote Unity unisphere Host.


      remote_system_username (True, str, None)
        User name of remote Unity unisphere Host.


      remote_system_password (True, str, None)
        Password of remote Unity unisphere Host.


      remote_system_verifycert (optional, bool, True)
        Boolean variable to specify whether or not to validate SSL certificate of remote Unity unisphere Host.

        ``true`` - Indicates that the SSL certificate should be verified.

        ``false`` - Indicates that the SSL certificate should not be verified.


      remote_system_port (optional, int, 443)
        Port at which remote Unity unisphere is hosted.



    destination_pool_id (optional, str, None)
      ID of pool to allocate destination filesystem.


    destination_pool_name (optional, str, None)
      Name of pool to allocate destination filesystem.



  replication_state (optional, str, None)
    State of the replication.


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
   - SMB shares, NFS exports, and snapshots associated with filesystem need to be deleted prior to deleting a filesystem.
   - The *quota_config* parameter can be used to update default hard limit and soft limit values to limit the maximum space that can be used. By default they both are set to 0 during filesystem creation which means unlimited.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create FileSystem
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_name: "ansible_test_fs"
        nas_server_name: "lglap761"
        pool_name: "pool_1"
        size: 5
        state: "present"

    - name: Create FileSystem with quota configuration
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_name: "ansible_test_fs"
        nas_server_name: "lglap761"
        pool_name: "pool_1"
        size: 5
        quota_config:
            grace_period: 8
            grace_period_unit: "days"
            default_soft_limit: 10
            is_user_quota_enabled: False
        state: "present"

    - name: Expand FileSystem size
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_name: "ansible_test_fs"
        nas_server_name: "lglap761"
        size: 10
        state: "present"

    - name: Expand FileSystem size
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_name: "ansible_test_fs"
        nas_server_name: "lglap761"
        size: 10
        state: "present"

    - name: Modify FileSystem smb_properties
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_name: "ansible_test_fs"
        nas_server_name: "lglap761"
        smb_properties:
          is_smb_op_locks_enabled: True
          smb_notify_on_change_dir_depth: 5
          is_smb_notify_on_access_enabled: True
        state: "present"

    - name: Modify FileSystem Snap Schedule
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_id: "fs_141"
        snap_schedule_id: "{{snap_schedule_id}}"
        state: "{{state_present}}"

    - name: Get details of FileSystem using id
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_id: "rs_405"
        state: "present"

    - name: Delete a FileSystem using id
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_id: "rs_405"
        state: "absent"

    - name: Enable replication on the fs
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_id: "rs_405"
        replication_params:
          replication_name: "test_repl"
          replication_type: "remote"
          replication_mode: "asynchronous"
          rpo: 60
          remote_system:
            remote_system_host: '0.1.2.3'
            remote_system_verifycert: False
            remote_system_username: 'username'
            remote_system_password: 'password'
          destination_pool_name: "pool_test_1"
        replication_state: "enable"
        state: "present"

    - name: Modify replication on the fs
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_id: "rs_405"
        replication_params:
          replication_name: "test_repl"
          new_replication_name: "test_repl_updated"
          replication_mode: "asynchronous"
          rpo: 50
        replication_state: "enable"
        state: "present"

    - name: Disable replication on the fs
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_id: "rs_405"
        replication_state: "disable"
        state: "present"

    - name: Disable replication by specifying replication_name on the fs
      filesystem:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        filesystem_id: "rs_405"
        replication_params:
            replication_name: "test_replication"
        replication_state: "disable"
        state: "present"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


filesystem_details (When filesystem exists, dict, {'access_policy': 'AccessPolicyEnum.UNIX', 'cifs_notify_on_change_dir_depth': 512, 'cifs_share': None, 'data_reduction_percent': 0, 'data_reduction_ratio': 1.0, 'data_reduction_size_saved': 0, 'description': '', 'existed': True, 'folder_rename_policy': 'FSRenamePolicyEnum.SMB_RENAME_FORBIDDEN', 'format': 'FSFormatEnum.UFS64', 'hash': 8735427610152, 'health': {'UnityHealth': {'hash': 8735427614928}}, 'host_io_size': 'HostIOSizeEnum.GENERAL_8K', 'id': 'fs_65916', 'is_advanced_dedup_enabled': False, 'is_cifs_notify_on_access_enabled': False, 'is_cifs_notify_on_write_enabled': False, 'is_cifs_op_locks_enabled': False, 'is_cifs_sync_writes_enabled': False, 'is_data_reduction_enabled': False, 'is_read_only': False, 'is_smbca': False, 'is_thin_enabled': True, 'locking_policy': 'FSLockingPolicyEnum.MANDATORY', 'metadata_size': 11274289152, 'metadata_size_allocated': 4294967296, 'min_size_allocated': 0, 'name': 'test_fs', 'nas_server': {'id': 'nas_18', 'name': 'test_nas1'}, 'nfs_share': None, 'per_tier_size_used': [6979321856, 0, 0], 'pool': {'id': 'pool_7', 'name': 'pool 7'}, 'pool_full_policy': 'ResourcePoolFullPolicyEnum.FAIL_WRITES', 'quota_config': {'default_hard_limit': '0B', 'default_soft_limit': '0B', 'grace_period': '7.0 days', 'id': 'quotaconfig_171798760421_0', 'is_user_quota_enabled': False, 'quota_policy': 'QuotaPolicyEnum.FILE_SIZE'}, 'replication_sessions': {'current_transfer_est_remain_time': 0, 'id': '***', 'last_sync_time': '2022-05-12 11:20:38+00:00', 'local_role': 'ReplicationSessionReplicationRoleEnum.SOURCE', 'max_time_out_of_sync': 60, 'members': None, 'name': 'local_repl_new', 'network_status': 'ReplicationSessionNetworkStatusEnum.OK', 'remote_system': {'UnityRemoteSystem': {'hash': 8735426929707}}, 'replication_resource_type': 'ReplicationEndpointResourceTypeEnum.FILESYSTEM', 'src_resource_id': 'res_66444', 'src_status': 'ReplicationSessionStatusEnum.OK', 'status': 'ReplicationOpStatusEnum.AUTO_SYNC_CONFIGURED', 'sync_progress': 0, 'sync_state': 'ReplicationSessionSyncStateEnum.IDLE'}, 'size_allocated': 283148288, 'size_allocated_total': 4578148352, 'size_preallocated': 2401173504, 'size_total': 10737418240, 'size_total_with_unit': '10.0 GB', 'size_used': 1620312064, 'snap_count': 2, 'snaps_size': 21474869248, 'snaps_size_allocated': 32768, 'snapshots': [], 'supported_protocols': 'FSSupportedProtocolEnum.NFS', 'tiering_policy': 'TieringPolicyEnum.AUTOTIER_HIGH', 'type': 'FilesystemTypeEnum.FILESYSTEM'})
  Details of the filesystem.


  id (, str, )
    The system generated ID given to the filesystem.


  name (, str, )
    Name of the filesystem.


  description (, str, )
    Description about the filesystem.


  is_data_reduction_enabled (, bool, )
    Whether or not compression enabled on this filesystem.


  size_total_with_unit (, str, )
    Size of the filesystem with actual unit.


  tiering_policy (, str, )
    Tiering policy applied to this filesystem.


  is_cifs_notify_on_access_enabled (, bool, )
    Indicates whether the system generates a notification when a user accesses the file system.


  is_cifs_notify_on_write_enabled (, bool, )
    Indicates whether the system generates a notification when the file system is written to.


  is_cifs_op_locks_enabled (, bool, )
    Indicates whether opportunistic file locks are enabled for the file system.


  is_cifs_sync_writes_enabled (, bool, )
    Indicates whether the CIFS synchronous writes option is enabled for the file system.


  cifs_notify_on_change_dir_depth (, int, )
    Indicates the lowest directory level to which the enabled notifications apply, if any.


  pool (, dict, )
    The pool in which this filesystem is allocated.


    id (, str, )
      The system ID given to the pool.


    name (, str, )
      The name of the storage pool.



  nas_server (, dict, )
    The NAS Server details on which this filesystem is hosted.


    id (, str, )
      The system ID given to the NAS Server.


    name (, str, )
      The name of the NAS Server.



  snapshots (, list, )
    The list of snapshots of this filesystem.


    id (, str, )
      The system ID given to the filesystem snapshot.


    name (, str, )
      The name of the filesystem snapshot.



  is_thin_enabled (, bool, )
    Indicates whether thin provisioning is enabled for this filesystem.


  snap_schedule_id (, str, )
    Indicates the id of the snap schedule associated with the filesystem.


  snap_schedule_name (, str, )
    Indicates the name of the snap schedule associated with the filesystem.


  quota_config (, dict, )
    Details of quota configuration of the filesystem created.


    grace_period (, str, )
      Grace period set in quota configuration after soft limit is reached.


    default_hard_limit (, int, )
      Default hard limit for user quotas and tree quotas.


    default_soft_limit (, int, )
      Default soft limit for user quotas and tree quotas.


    is_user_quota_enabled (, bool, )
      Indicates whether the user quota is enabled.


    quota_policy (, str, )
      Quota policy set in quota configuration.



  replication_sessions (, dict, )
    List of replication sessions if replication is enabled.


    id (, str, )
      ID of replication session


    name (, str, )
      Name of replication session


    remote_system (, dict, )
      Remote system


      id (, str, )
        ID of remote system








Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Meenakshi Dembi (@dembim) <ansible.team@dell.com>
- Spandita Panigrahi (@panigs7) <ansible.team@dell.com>

