.. _info_module:


info -- Gathering information about Unity
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Gathering information about Unity storage system includes Get the details of Unity array, Get list of Hosts in Unity array, Get list of FC initiators in Unity array, Get list of iSCSI initiators in Unity array, Get list of Consistency groups in Unity array, Get list of Storage pools in Unity array, Get list of Volumes in Unity array, Get list of Snapshot schedules in Unity array, Get list of NAS servers in Unity array, Get list of File systems in Unity array, Get list of Snapshots in Unity array, Get list of SMB shares in Unity array, Get list of NFS exports in Unity array, Get list of User quotas in Unity array, Get list of Quota tree in Unity array, Get list of NFS Servers in Unity array, Get list of CIFS Servers in Unity array. Get list of Ethernet ports in Unity array. Get list of File interfaces used in Unity array.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  gather_subset (optional, list, None)
    List of string variables to specify the Unity storage system entities for which information is required.


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

    
     - name: Get detailed list of Unity entities
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - host
           - fc_initiator
           - iscsi_initiator
           - cg
           - storage_pool
           - vol
           - snapshot_schedule
           - nas_server
           - file_system
           - snapshot
           - nfs_export
           - smb_share
           - user_quota
           - tree_quota
           - disk_group
           - nfs_server
           - cifs_server
           - ethernet_port
           - file_interface

     - name: Get information of Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"

     - name: Get list of hosts on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - host

     - name: Get list of FC initiators on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - fc_initiator

     - name: Get list of ISCSI initiators on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - iscsi_initiator

     - name: Get list of consistency groups on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - cg

     - name: Get list of storage pools on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - storage_pool

     - name: Get list of volumes on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - vol

     - name: Get list of snapshot schedules on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - snapshot_schedule

     - name: Get list of NAS Servers on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - nas_server

     - name: Get list of File Systems on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - file_system

     - name: Get list of Snapshots on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - snapshot

     - name: Get list of NFS exports on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - nfs_export

     - name: Get list of SMB shares on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - smb_share

     - name: Get list of user quotas on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - user_quota

     - name: Get list of quota trees on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - tree_quota

     - name: Get list of disk groups on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - disk_group

     - name: Get list of NFS Servers on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - nfs_server

     - name: Get list of CIFS Servers on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - cifs_server

     - name: Get list of ethernet ports on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - ethernet_port

     - name: Get list of file interfaces on Unity array
       info:
         unispherehost: "{{unispherehost}}"
         username: "{{username}}"
         password: "{{password}}"
         validate_certs: "{{validate_certs}}"
         gather_subset:
           - file_interface



Return Values
-------------

Array_Details (always, dict, {'api_version': '12.0', 'earliest_api_version': '4.0', 'existed': True, 'hash': 8766644083532, 'id': '0', 'model': 'Unity 480', 'name': 'APM00213404195', 'software_version': '5.2.1'})
  Details of the Unity Array.


  api_version (, str, )
    The current api version of the Unity Array.


  earliest_api_version (, str, )
    The earliest api version of the Unity Array.


  model (, str, )
    The model of the Unity Array.


  name (, str, )
    The name of the Unity Array.


  software_version (, str, )
    The software version of the Unity Array.



Hosts (When hosts exist., list, [{'auto_manage_type': 'HostManageEnum.UNKNOWN', 'datastores': None, 'description': '', 'existed': True, 'fc_host_initiators': None, 'hash': 8762200072289, 'health': {'UnityHealth': {'hash': 8762200072352}}, 'host_container': None, 'host_ip_ports': {'UnityHostIpPortList': [{'UnityHostIpPort': {'hash': 8762200072361}}]}, 'host_luns': None, 'host_polled_uuid': None, 'host_pushed_uuid': None, 'host_uuid': None, 'host_v_vol_datastore': None, 'id': 'Host_2191', 'iscsi_host_initiators': None, 'last_poll_time': None, 'name': '10.225.2.153', 'os_type': 'Linux', 'registration_type': None, 'storage_resources': None, 'tenant': None, 'type': 'HostTypeEnum.HOST_MANUAL', 'vms': None}])
  Details of the hosts.


  id (, str, )
    The ID of the host.


  name (, str, )
    The name of the host.



FC_initiators (When FC initiator exist., list, [{'WWN': '20:00:00:0E:1E:E9:B8:FC:21:00:00:0E:1E:E9:B8:FC', 'id': 'HostInitiator_3'}, {'WWN': '20:00:00:0E:1E:E9:B8:F7:21:00:00:0E:1E:E9:B8:F7', 'id': 'HostInitiator_4'}])
  Details of the FC initiators.


  WWN (, str, )
    The WWN of the FC initiator.


  id (, str, )
    The id of the FC initiator.



ISCSI_initiators (When ISCSI initiators exist., list, [{'IQN': 'iqn.1994-05.com.redhat:634d768090f', 'id': 'HostInitiator_1'}, {'IQN': 'iqn.1994-05.com.redhat:2835ba62cc6d', 'id': 'HostInitiator_2'}])
  Details of the ISCSI initiators.


  IQN (, str, )
    The IQN of the ISCSI initiator.


  id (, str, )
    The id of the ISCSI initiator.



Consistency_Groups (When Consistency Groups exist., list, [{'advanced_dedup_status': 'DedupStatusEnum.DISABLED', 'block_host_access': {'UnityBlockHostAccessList': [{'UnityBlockHostAccess': {'hash': 8745385821206}}, {'UnityBlockHostAccess': {'hash': 8745386530115}}, {'UnityBlockHostAccess': {'hash': 8745386530124}}]}, 'data_reduction_percent': 0, 'data_reduction_ratio': 1.0, 'data_reduction_size_saved': 0, 'data_reduction_status': 'DataReductionStatusEnum.DISABLED', 'datastores': None, 'dedup_status': None, 'description': 'CG has created with all parametres.', 'esx_filesystem_block_size': None, 'esx_filesystem_major_version': None, 'existed': True, 'filesystem': None, 'hash': 8745385801328, 'health': {'UnityHealth': {'hash': 8745386647098}}, 'host_v_vol_datastore': None, 'id': 'res_93', 'is_replication_destination': False, 'is_snap_schedule_paused': False, 'luns': {'UnityLunList': [{'UnityLun': {'hash': 8745389830024, 'id': 'sv_64'}}, {'UnityLun': {'hash': 8745386526751, 'id': 'sv_63'}}]}, 'metadata_size': 8858370048, 'metadata_size_allocated': 7516192768, 'name': 'CG1_Ansible_Test_SS', 'per_tier_size_used': [11811160064, 0, 0], 'pools': {'UnityPoolList': [{'UnityPool': {'hash': 8745386552375, 'id': 'pool_3'}}]}, 'relocation_policy': 'TieringPolicyEnum.AUTOTIER', 'replication_type': 'ReplicationTypeEnum.NONE', 'size_allocated': 99418112, 'size_total': 268435456000, 'size_used': None, 'snap_count': 1, 'snap_schedule': {'UnitySnapSchedule': {'hash': 8745386550224, 'id': 'snapSch_66'}}, 'snaps_size_allocated': 8888320, 'snaps_size_total': 108675072, 'thin_status': 'ThinStatusEnum.TRUE', 'type': 'StorageResourceTypeEnum.CONSISTENCY_GROUP', 'virtual_volumes': None, 'vmware_uuid': None}])
  Details of the Consistency Groups.


  id (, str, )
    The ID of the Consistency Group.


  name (, str, )
    The name of the Consistency Group.



Storage_Pools (When Storage Pools exist., list, [{'alert_threshold': 70, 'creation_time': '2021-10-18 12:45:12+00:00', 'description': '', 'existed': True, 'harvest_state': 'UsageHarvestStateEnum.PAUSED_COULD_NOT_REACH_HWM', 'hash': 8741501012399, 'health': {'UnityHealth': {'hash': 8741501012363}}, 'id': 'pool_2', 'is_all_flash': False, 'is_empty': False, 'is_fast_cache_enabled': False, 'is_harvest_enabled': True, 'is_snap_harvest_enabled': False, 'metadata_size_subscribed': 312458870784, 'metadata_size_used': 244544700416, 'name': 'fastVP_pool', 'object_id': 12884901891, 'pool_fast_vp': {'UnityPoolFastVp': {'hash': 8741501228023}}, 'pool_space_harvest_high_threshold': 95.0, 'pool_space_harvest_low_threshold': 85.0, 'pool_type': 'StoragePoolTypeEnum.TRADITIONAL', 'raid_type': 'RaidTypeEnum.RAID5', 'rebalance_progress': None, 'size_free': 2709855928320, 'size_subscribed': 2499805044736, 'size_total': 3291018690560, 'size_used': 455513956352, 'snap_size_subscribed': 139720515584, 'snap_size_used': 66002944, 'snap_space_harvest_high_threshold': 25.0, 'snap_space_harvest_low_threshold': 20.0, 'tiers': {'UnityPoolTierList': [{'UnityPoolTier': {'hash': 8741500996410}}, {'UnityPoolTier': {'hash': 8741501009430}}, {'UnityPoolTier': {'hash': 8741501009508}}]}}])
  Details of the Storage Pools.


  id (, str, )
    The ID of the Storage Pool.


  name (, str, )
    The name of the Storage Pool.



Volumes (When Volumes exist., list, [{'current_node': 'NodeEnum.SPB', 'data_reduction_percent': 0, 'data_reduction_ratio': 1.0, 'data_reduction_size_saved': 0, 'default_node': 'NodeEnum.SPB', 'description': None, 'effective_io_limit_max_iops': None, 'effective_io_limit_max_kbps': None, 'existed': True, 'family_base_lun': {'UnityLun': {'hash': 8774260820794, 'id': 'sv_27'}}, 'family_clone_count': 0, 'hash': 8774260854260, 'health': {'UnityHealth': {'hash': 8774260812499}}, 'host_access': {'UnityBlockHostAccessList': [{'UnityBlockHostAccess': {'hash': 8774260826387}}]}, 'id': 'sv_27', 'io_limit_policy': None, 'is_advanced_dedup_enabled': False, 'is_compression_enabled': None, 'is_data_reduction_enabled': False, 'is_replication_destination': False, 'is_snap_schedule_paused': False, 'is_thin_clone': False, 'is_thin_enabled': False, 'metadata_size': 4294967296, 'metadata_size_allocated': 4026531840, 'name': 'VSI-UNITY-test-task', 'per_tier_size_used': [111400714240, 0, 0], 'pool': {'UnityPool': {'hash': 8774260811427}}, 'size_allocated': 107374182400, 'size_total': 107374182400, 'size_used': None, 'snap_count': 0, 'snap_schedule': None, 'snap_wwn': '60:06:01:60:5C:F0:50:00:94:3E:91:4D:51:5A:4F:97', 'snaps_size': 0, 'snaps_size_allocated': 0, 'storage_resource': {'UnityStorageResource': {'hash': 8774267822228}}, 'tiering_policy': 'TieringPolicyEnum.AUTOTIER_HIGH', 'type': 'LUNTypeEnum.VMWARE_ISCSI', 'wwn': '60:06:01:60:5C:F0:50:00:00:B5:95:61:2E:34:DB:B2'}])
  Details of the Volumes.


  id (, str, )
    The ID of the Volume.


  name (, str, )
    The name of the Volume.



Snapshot_Schedules (When Snapshot Schedules exist., list, [{'existed': True, 'hash': 8775599492651, 'id': 'snapSch_1', 'is_default': True, 'is_modified': None, 'is_sync_replicated': False, 'luns': None, 'modification_time': '2021-08-18 19:10:33.774000+00:00', 'name': 'CEM_DEFAULT_SCHEDULE_DEFAULT_PROTECTION', 'rules': {'UnitySnapScheduleRuleList': [{'UnitySnapScheduleRule': {'hash': 8775599498593}}]}, 'storage_resources': {'UnityStorageResourceList': [{'UnityStorageResource': {'hash': 8775599711597, 'id': 'res_88'}}, {'UnityStorageResource': {'hash': 8775599711528, 'id': 'res_3099'}}]}, 'version': 'ScheduleVersionEnum.LEGACY'}])
  Details of the Snapshot Schedules.


  id (, str, )
    The ID of the Snapshot Schedule.


  name (, str, )
    The name of the Snapshot Schedule.



NAS_Servers (When NAS Servers exist., list, [{'allow_unmapped_user': None, 'cifs_server': None, 'current_sp': {'UnityStorageProcessor': {'hash': 8747629920422, 'id': 'spb'}}, 'current_unix_directory_service': 'NasServerUnixDirectoryServiceEnum.NONE', 'default_unix_user': None, 'default_windows_user': None, 'existed': True, 'file_dns_server': None, 'file_interface': {'UnityFileInterfaceList': [{'UnityFileInterface': {'hash': 8747626606870, 'id': 'if_6'}}]}, 'filesystems': {'UnityFileSystemList': [{'UnityFileSystem': {'hash': 8747625901355, 'id': 'fs_6892'}}]}, 'hash': 8747625900370, 'health': {'UnityHealth': {'hash': 8747625900493}}, 'home_sp': {'UnityStorageProcessor': {'hash': 8747625877420, 'id': 'spb'}}, 'id': 'nas_1', 'is_backup_only': False, 'is_multi_protocol_enabled': False, 'is_packet_reflect_enabled': False, 'is_replication_destination': False, 'is_replication_enabled': False, 'is_windows_to_unix_username_mapping_enabled': None, 'name': 'lglad072', 'pool': {'UnityPool': {'hash': 8747629920479, 'id': 'pool_3'}}, 'preferred_interface_settings': {'UnityPreferredInterfaceSettings': {'hash': 8747626625166, 'id': 'preferred_if_1'}}, 'replication_type': 'ReplicationTypeEnum.NONE', 'size_allocated': 2952790016, 'tenant': None, 'virus_checker': {'UnityVirusChecker': {'hash': 8747626604144, 'id': 'cava_1'}}}])
  Details of the NAS Servers.


  id (, str, )
    The ID of the NAS Server.


  name (, str, )
    The name of the NAS Server.



File_Systems (When File Systems exist., list, [{'access_policy': 'AccessPolicyEnum.UNIX', 'cifs_notify_on_change_dir_depth': 512, 'cifs_share': None, 'data_reduction_percent': 0, 'data_reduction_ratio': 1.0, 'data_reduction_size_saved': 0, 'description': '', 'existed': True, 'folder_rename_policy': 'FSRenamePolicyEnum.SMB_RENAME_FORBIDDEN', 'format': 'FSFormatEnum.UFS64', 'hash': 8786518053735, 'health': {'UnityHealth': {'hash': 8786518049091}}, 'host_io_size': 'HostIOSizeEnum.GENERAL_8K', 'id': 'fs_12', 'is_advanced_dedup_enabled': False, 'is_cifs_notify_on_access_enabled': False, 'is_cifs_notify_on_write_enabled': False, 'is_cifs_op_locks_enabled': True, 'is_cifs_sync_writes_enabled': False, 'is_data_reduction_enabled': False, 'is_read_only': False, 'is_smbca': False, 'is_thin_enabled': True, 'locking_policy': 'FSLockingPolicyEnum.MANDATORY', 'metadata_size': 4294967296, 'metadata_size_allocated': 3758096384, 'min_size_allocated': 0, 'name': 'vro-daniel-test', 'nas_server': {'UnityNasServer': {'hash': 8786517296113, 'id': 'nas_1'}}, 'nfs_share': None, 'per_tier_size_used': [6442450944, 0, 0], 'pool': {'UnityPool': {'hash': 8786518259493, 'id': 'pool_3'}}, 'pool_full_policy': 'ResourcePoolFullPolicyEnum.FAIL_WRITES', 'size_allocated': 283148288, 'size_allocated_total': 4041244672, 'size_preallocated': 2401206272, 'size_total': 107374182400, 'size_used': 1620312064, 'snap_count': 0, 'snaps_size': 0, 'snaps_size_allocated': 0, 'storage_resource': {'UnityStorageResource': {'hash': 8786518044167, 'id': 'res_20'}}, 'supported_protocols': 'FSSupportedProtocolEnum.NFS', 'tiering_policy': 'TieringPolicyEnum.AUTOTIER_HIGH', 'type': 'FilesystemTypeEnum.FILESYSTEM'}])
  Details of the File Systems.


  id (, str, )
    The ID of the File System.


  name (, str, )
    The name of the File System.



Snapshots (When Snapshots exist., list, [{'access_type': 'FilesystemSnapAccessTypeEnum.CHECKPOINT', 'attached_wwn': None, 'creation_time': '2022-04-06 11:19:26.818000+00:00', 'creator_schedule': None, 'creator_type': 'SnapCreatorTypeEnum.REP_V2', 'creator_user': None, 'description': '', 'existed': True, 'expiration_time': None, 'hash': 8739100256648, 'host_access': None, 'id': '38654716464', 'io_limit_policy': None, 'is_auto_delete': False, 'is_modifiable': False, 'is_modified': False, 'is_read_only': True, 'is_system_snap': True, 'last_writable_time': None, 'lun': {'UnityLun': {'hash': 8739100148962, 'id': 'sv_301'}}, 'name': '42949677504_APM00213404195_0000.ckpt000_9508038064690266.2_238', 'parent_snap': None, 'size': 3221225472, 'snap_group': None, 'state': 'SnapStateEnum.READY', 'storage_resource': {'UnityStorageResource': {'hash': 8739100173002, 'id': 'sv_301'}}}])
  Details of the Snapshots.


  id (, str, )
    The ID of the Snapshot.


  name (, str, )
    The name of the Snapshot.



NFS_Exports (When NFS Exports exist., list, [{'anonymous_gid': 4294967294, 'anonymous_uid': 4294967294, 'creation_time': '2021-12-01 06:21:48.381000+00:00', 'default_access': 'NFSShareDefaultAccessEnum.NO_ACCESS', 'description': '', 'existed': True, 'export_option': 1, 'export_paths': ['10.230.24.20:/zack_nfs_01'], 'filesystem': {'UnityFileSystem': {'hash': 8747298565566, 'id': 'fs_67'}}, 'hash': 8747298565548, 'host_accesses': None, 'id': 'NFSShare_29', 'is_read_only': None, 'min_security': 'NFSShareSecurityEnum.SYS', 'modification_time': '2022-04-01 11:44:17.553000+00:00', 'name': 'zack_nfs_01', 'nfs_owner_username': None, 'no_access_hosts': None, 'no_access_hosts_string': '10.226.198.207,10.226.198.25,10.226.198.44,10.226.198.85,Host1, Host2,Host4,Host5,Host6,10.10.0.0/255.255.240.0', 'path': '/', 'read_only_hosts': None, 'read_only_hosts_string': '', 'read_only_root_access_hosts': None, 'read_only_root_hosts_string': '', 'read_write_hosts': None, 'read_write_hosts_string': '', 'read_write_root_hosts_string': '', 'role': 'NFSShareRoleEnum.PRODUCTION', 'root_access_hosts': None, 'snap': None, 'type': 'NFSTypeEnum.NFS_SHARE'}])
  Details of the NFS Exports.


  id (, str, )
    The ID of the NFS Export.


  name (, str, )
    The name of the NFS Export.



SMB_Shares (When SMB Shares exist., list, [{'creation_time': '2022-03-17 11:56:54.867000+00:00', 'description': '', 'existed': True, 'export_paths': ['\\\\multi-prot-pie.extreme1.com\\multi-prot-hui', '\\\\10.230.24.26\\multi-prot-hui'], 'filesystem': {'UnityFileSystem': {'hash': 8741295638110, 'id': 'fs_140'}}, 'hash': 8741295638227, 'id': 'SMBShare_20', 'is_abe_enabled': False, 'is_ace_enabled': False, 'is_branch_cache_enabled': False, 'is_continuous_availability_enabled': False, 'is_dfs_enabled': False, 'is_encryption_enabled': False, 'is_read_only': None, 'modified_time': '2022-03-17 11:56:54.867000+00:00', 'name': 'multi-prot-hui', 'offline_availability': 'CifsShareOfflineAvailabilityEnum.NONE', 'path': '/', 'snap': None, 'type': 'CIFSTypeEnum.CIFS_SHARE', 'umask': '022'}])
  Details of the SMB Shares.


  id (, str, )
    The ID of the SMB Share.


  name (, str, )
    The name of the SMB Share.



User_Quotas (When user quotas exist., list, [{'id': 'userquota_171798694698_0_60000', 'uid': 60000}, {'id': 'userquota_171798694939_0_5001', 'uid': 5001}])
  Details of the user quotas.


  id (, str, )
    The ID of the user quota.


  uid (, str, )
    The UID of the user quota.



Tree_Quotas (When quota trees exist., list, [{'id': 'treequota_171798709589_1', 'path': '/vro-ui-fs-rkKfimmN'}, {'id': 'treequota_171798709590_1', 'path': '/vro-ui-fs-mGYXAMqk'}])
  Details of the quota trees.


  id (, str, )
    The ID of the quota tree.


  path (, str, )
    The path of the quota tree.



Disk_Groups (When disk groups exist., list, [{'id': 'dg_3', 'name': '400 GB SAS Flash 2', 'tier_type': 'EXTREME_PERFORMANCE'}, {'id': 'dg_16', 'name': '600 GB SAS 10K', 'tier_type': 'PERFORMANCE'}])
  Details of the disk groups.


  id (, str, )
    The ID of the disk group.


  name (, str, )
    The name of the disk group.


  tier_type (, str, )
    The tier type of the disk group.



NFS_Servers (When NFS Servers exist., list, [{'id': 'nfs_3'}, {'id': 'nfs_4'}, {'id': 'nfs_9'}])
  Details of the NFS Servers.


  id (, str, )
    The ID of the NFS Servers.



CIFS_Servers (When CIFS Servers exist., list, [{'id': 'cifs_3', 'name': 'test_cifs_1'}, {'id': 'cifs_4', 'name': 'test_cifs_2'}, {'id': 'cifs_9', 'name': 'test_cifs_3'}])
  Details of the CIFS Servers.


  id (, str, )
    The ID of the CIFS Servers.


  name (, str, )
    The name of the CIFS server.



Ethernet_ports (When ethernet ports exist., list, [{'id': 'spa_mgmt', 'name': 'SP A Management Port'}, {'id': 'spa_ocp_0_eth0', 'name': 'SP A 4-Port Card Ethernet Port 0'}, {'id': 'spa_ocp_0_eth1', 'name': 'SP A 4-Port Card Ethernet Port 1'}])
  Details of the ethernet ports.


  id (, str, )
    The ID of the ethernet port.


  name (, str, )
    The name of the ethernet port.



File_interfaces (When file inetrface exist., list, [{'id': 'if_3', 'ip_address': 'xx.xx.xx.xx', 'name': '1_APMXXXXXXXXXX'}, {'id': 'if_3', 'ip_address': 'xx.xx.xx.xx', 'name': '2_APMXXXXXXXXXX'}, {'id': 'if_3', 'ip_address': 'xx.xx.xx.xx', 'name': '3_APMXXXXXXXXXX'}])
  Details of the file inetrfaces.


  id (, str, )
    The ID of the file inetrface.


  name (, str, )
    The name of the file inetrface.


  ip_address (, str, )
    IP address of the file inetrface.






Status
------





Authors
~~~~~~~

- Rajshree Khare (@kharer5) <ansible.team@dell.com>
- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Meenakshi Dembi (@dembim) <ansible.team@dell.com>

