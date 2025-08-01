.. _replication_session_module:


replication_session -- Manage replication session on Unity storage system
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing replication session on Unity storage system includes getting details, pause, resume, sync, failover, failback and deleting the replication session.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  session_id (optional, str, None)
    ID of replication session.


  session_name (optional, str, None)
    Name of replication session.


  pause (optional, bool, None)
    Pause or resume replication session.


  sync (optional, bool, None)
    Sync a replication session.


  failover_with_sync (optional, bool, None)
    If ``true``, Sync the source and destination resources before failing over the asynchronous replication session or keep them in sync after failing over the synchronous replication session.

    If ``false``, Failover a replication session.


  failback (optional, bool, None)
    Failback a replication session.


  force_full_copy (optional, bool, None)
    Indicates whether to sync back all data from the destination SP to the source SP during the failback session. Needed during resume operation when replication session goes out of sync due to a fault.


  force (optional, bool, None)
    Skip pre-checks on file system(s) replication sessions of a NAS server when a replication failover is issued from the source NAS server.


  state (optional, str, present)
    State variable to determine whether replication session will exist or not.


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
   - The *check_mode* is supported.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get replication session details
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_name: "fs_replication"

    - name: Get replication session details based on session_id
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_id: "103079215114_APM00213404195_0000_103079215274_APM00213404194_0000"

    - name: Pause a replication session
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_name: "fs_replication"
        pause: true

    - name: Resume a replication session
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_name: "fs_replication"
        pause: false
        force_full_copy: true

    - name: Sync a replication session
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_name: "fs_replication"
        sync: true

    - name: Failover with sync a replication session
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_name: "fs_replication"
        failover_with_sync: true
        force: true

    - name: Failover a replication session
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_name: "fs_replication"
        failover_with_sync: false

    - name: Failback a replication session
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_name: "fs_replication"
        failback: true
        force_full_copy: true

    - name: Delete a replication session
      replication_session:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        session_name: "fs_replication"
        state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


replication_session_details (When replication session exists., dict, {'current_transfer_est_remain_time': 0, 'daily_snap_replication_policy': None, 'dst_resource_id': 'nas_8', 'dst_spa_interface': {'UnityRemoteInterface': {'hash': 8771253398547, 'id': 'APM00213404195:if_181'}}, 'dst_spb_interface': {'UnityRemoteInterface': {'hash': 8771253424144, 'id': 'APM00213404195:if_180'}}, 'dst_status': 'ReplicationSessionStatusEnum.OK', 'existed': True, 'hash': 8771259012271, 'health': {'UnityHealth': {'hash': 8771253424168}}, 'hourly_snap_replication_policy': None, 'id': '103079215114_APM00213404195_0000_103079215274_APM00213404194_0000', 'last_sync_time': '2023-04-18 10:35:25+00:00', 'local_role': 'ReplicationSessionReplicationRoleEnum.DESTINATION', 'max_time_out_of_sync': 0, 'members': None, 'name': 'rep_sess_nas', 'network_status': 'ReplicationSessionNetworkStatusEnum.OK', 'remote_system': {'UnityRemoteSystem': {'hash': 8771253380142}}, 'replication_resource_type': 'ReplicationEndpointResourceTypeEnum.NASSERVER', 'src_resource_id': 'nas_213', 'src_spa_interface': {'UnityRemoteInterface': {'hash': 8771253475010, 'id': 'APM00213404194:if_195'}}, 'src_spb_interface': {'UnityRemoteInterface': {'hash': 8771253374169, 'id': 'APM00213404194:if_194'}}, 'src_status': 'ReplicationSessionStatusEnum.OK', 'status': 'ReplicationOpStatusEnum.ACTIVE', 'sync_progress': 0, 'sync_state': 'ReplicationSessionSyncStateEnum.IN_SYNC'})
  Details of the replication session.


  id (, str, )
    Unique identifier of the replicationSession instance.


  name (, str, )
    User-specified replication session name.


  replicationResourceType (, str, )
    Replication resource type of replication session endpoints.


  status (, str, )
    Replication status of the replication session.


  remoteSystem (, dict, )
    Specifies the remote system to use as the destination for the replication session.


    UnityRemoteSystem (, dict, )
      Information about remote storage system.


      id (, str, )
        Unique identifier of the remote system instance.


      serialNumber (, str, )
        Serial number of the remote system.




  maxTimeOutOfSync (, int, )
    Maximum time to wait before the system syncs the source and destination resources.


  srcStatus (, str, )
    Status of the source end of the session.


  networkStatus (, str, )
    Status of the network connection used by the replication session.


  dstStatus (, str, )
    Status of the destination end of the replication session.


  lastSyncTime (, str, )
    Date and time of the last replication synchronization.


  syncState (, str, )
    Synchronization state between source and destination resource of the replication session.


  syncProgress (, int, )
    Synchronization completion percentage between source and destination resources of the replication session.


  dstResourceId (, str, )
    Identifier of the destination resource.


  currentTransferEstRemainTime (, int, )
    Estimated time left for the replication synchronization to complete.






Status
------





Authors
~~~~~~~

- Jennifer John (@Jennifer-John) <ansible.team@dell.com>

