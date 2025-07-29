.. _consistencygroup_module:


consistencygroup -- Manage consistency groups on Unity storage system
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing the consistency group on the Unity storage system includes creating new consistency group, adding volumes to consistency group, removing volumes from consistency group, mapping hosts to consistency group, unmapping hosts from consistency group, renaming consistency group, modifying attributes of consistency group, enabling replication in consistency group, disabling replication in consistency group and deleting consistency group.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  cg_name (optional, str, None)
    The name of the consistency group.

    It is mandatory for the create operation.

    Specify either *cg_name* or *cg_id* (but not both) for any operation.


  cg_id (optional, str, None)
    The ID of the consistency group.

    It can be used only for get, modify, add/remove volumes, or delete operations.


  volumes (optional, list, None)
    This is a list of volumes.

    Either the volume ID or name must be provided for adding/removing existing volumes from consistency group.

    If *volumes* are given, then *vol_state* should also be specified.

    Volumes cannot be added/removed from consistency group, if the consistency group or the volume has snapshots.


    vol_id (optional, str, None)
      The ID of the volume.


    vol_name (optional, str, None)
      The name of the volume.



  vol_state (optional, str, None)
    String variable, describes the state of volumes inside consistency group.

    If *volumes* are given, then *vol_state* should also be specified.


  new_cg_name (optional, str, None)
    The new name of the consistency group, used in rename operation.


  description (optional, str, None)
    Description of the consistency group.


  snap_schedule (optional, str, None)
    Snapshot schedule assigned to the consistency group.

    Specifying an empty string "" removes the existing snapshot schedule from consistency group.


  tiering_policy (optional, str, None)
    Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.


  hosts (optional, list, None)
    This is a list of hosts.

    Either the host ID or name must be provided for mapping/unmapping hosts for a consistency group.

    If *hosts* are given, then *mapping_state* should also be specified.

    Hosts cannot be mapped to a consistency group, if the consistency group has no volumes.

    When a consistency group is being mapped to the host, users should not use the volume module to map the volumes in the consistency group to hosts.


    host_id (optional, str, None)
      The ID of the host.


    host_name (optional, str, None)
      The name of the host.



  mapping_state (optional, str, None)
    String variable, describes the state of hosts inside the consistency group.

    If *hosts* are given, then *mapping_state* should also be specified.


  replication_params (optional, dict, None)
    Settings required for enabling replication.


    destination_cg_name (optional, str, None)
      Name of the destination consistency group.

      Default value will be source consistency group name prefixed by 'DR_'.


    replication_mode (True, str, None)
      The replication mode.


    rpo (optional, int, None)
      Maximum time to wait before the system syncs the source and destination LUNs.

      Option *rpo* should be specified if the *replication_mode* is ``asynchronous``.

      The value should be in range of ``5`` to ``1440``.


    replication_type (optional, str, local)
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



    destination_pool_name (optional, str, None)
      Name of pool to allocate destination Luns.

      Mutually exclusive with *destination_pool_id*.


    destination_pool_id (optional, str, None)
      Id of pool to allocate destination Luns.

      Mutually exclusive with *destination_pool_name*.



  replication_state (optional, str, None)
    State of the replication.


  state (True, str, None)
    Define whether the consistency group should exist or not.


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

    
    - name: Create consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          cg_name: "{{cg_name}}"
          description: "{{description}}"
          snap_schedule: "{{snap_schedule1}}"
          state: "present"

    - name: Get details of consistency group using id
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_id: "{{cg_id}}"
          state: "present"

    - name: Add volumes to consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_id: "{{cg_id}}"
          volumes:
              - vol_name: "Ansible_Test-3"
              - vol_id: "sv_1744"
          vol_state: "{{vol_state_present}}"
          state: "present"

    - name: Rename consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_name: "{{cg_name}}"
          new_cg_name: "{{new_cg_name}}"
          state: "present"

    - name: Modify consistency group details
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_name: "{{new_cg_name}}"
          snap_schedule: "{{snap_schedule2}}"
          tiering_policy: "{{tiering_policy1}}"
          state: "present"

    - name: Map hosts to a consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_id: "{{cg_id}}"
          hosts:
            - host_name: "10.226.198.248"
            - host_id: "Host_511"
          mapping_state: "mapped"
          state: "present"

    - name: Unmap hosts from a consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_id: "{{cg_id}}"
          hosts:
            - host_id: "Host_511"
            - host_name: "10.226.198.248"
          mapping_state: "unmapped"
          state: "present"

    - name: Remove volumes from consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_name: "{{new_cg_name}}"
          volumes:
            - vol_name: "Ansible_Test-3"
            - vol_id: "sv_1744"
          vol_state: "{{vol_state_absent}}"
          state: "present"

    - name: Delete consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_name: "{{new_cg_name}}"
          state: "absent"

    - name: Enable replication for consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_id: "cg_id_1"
          replication_params:
            destination_cg_name: "destination_cg_1"
            replication_mode: "asynchronous"
            rpo: 60
            replication_type: "remote"
            remote_system:
              remote_system_host: '10.1.2.3'
              remote_system_verifycert: False
              remote_system_username: 'username'
              remote_system_password: 'password'
            destination_pool_name: "pool_test_1"
          replication_state: "enable"
          state: "present"

    - name: Disable replication for consistency group
      consistencygroup:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          cg_name: "dis_repl_ans_source"
          replication_state: "disable"
          state: "present"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


consistency_group_details (When consistency group exists, dict, {'advanced_dedup_status': 'DedupStatusEnum.DISABLED', 'block_host_access': None, 'cg_replication_enabled': False, 'data_reduction_percent': 0, 'data_reduction_ratio': 1.0, 'data_reduction_size_saved': 0, 'data_reduction_status': 'DataReductionStatusEnum.DISABLED', 'datastores': None, 'dedup_status': None, 'description': 'Ansible testing', 'esx_filesystem_block_size': None, 'esx_filesystem_major_version': None, 'existed': True, 'filesystem': None, 'hash': 8776023812033, 'health': {'UnityHealth': {'hash': 8776023811889}}, 'host_v_vol_datastore': None, 'id': 'res_7477', 'is_replication_destination': False, 'is_snap_schedule_paused': None, 'luns': None, 'metadata_size': 0, 'metadata_size_allocated': 0, 'name': 'Ansible_CG_Testing', 'per_tier_size_used': None, 'pools': None, 'relocation_policy': 'TieringPolicyEnum.MIXED', 'replication_type': 'ReplicationTypeEnum.NONE', 'size_allocated': 0, 'size_total': 0, 'size_used': None, 'snap_count': 0, 'snap_schedule': None, 'snaps_size_allocated': 0, 'snaps_size_total': 0, 'snapshots': [], 'thin_status': 'ThinStatusEnum.FALSE', 'type': 'StorageResourceTypeEnum.CONSISTENCY_GROUP', 'virtual_volumes': None, 'vmware_uuid': None})
  Details of the consistency group.


  id (, str, )
    The system ID given to the consistency group.


  relocation_policy (, str, )
    FAST VP tiering policy for the consistency group.


  cg_replication_enabled (, bool, )
    Whether or not the replication is enabled..


  snap_schedule (, dict, )
    Snapshot schedule applied to consistency group.


    UnitySnapSchedule (, dict, )
      Snapshot schedule applied to consistency group.


      id (, str, )
        The system ID given to the snapshot schedule.


      name (, str, )
        The name of the snapshot schedule.




  luns (, dict, )
    Details of volumes part of consistency group.


    UnityLunList (, list, )
      List of volumes part of consistency group.


      UnityLun (, dict, )
        Detail of volume.


        id (, str, )
          The system ID given to volume.


        name (, str, )
          The name of the volume.





  snapshots (, list, )
    List of snapshots of consistency group.


    name (, str, )
      Name of the snapshot.


    creation_time (, str, )
      Date and time on which the snapshot was taken.


    expirationTime (, str, )
      Date and time after which the snapshot will expire.


    storageResource (, dict, )
      Storage resource for which the snapshot was taken.


      UnityStorageResource (, dict, )
        Details of the storage resource.


        id (, str, )
          The id of the storage resource.





  block_host_access (, dict, )
    Details of hosts mapped to the consistency group.


    UnityBlockHostAccessList (, list, )
      List of hosts mapped to consistency group.


      UnityBlockHostAccess (, dict, )
        Details of host.


        id (, str, )
          The ID of the host.


        name (, str, )
          The name of the host.









Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

