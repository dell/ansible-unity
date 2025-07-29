.. _storagepool_module:


storagepool -- Manage storage pool on Unity
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing storage pool on Unity storage system contains the operations Get details of storage pool, Create a storage pool, Modify storage pool.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  pool_name (optional, str, None)
    Name of the storage pool, unique in the storage system.


  pool_id (optional, str, None)
    Unique identifier of the pool instance.


  new_pool_name (optional, str, None)
    New name of the storage pool, unique in the storage system.


  pool_description (optional, str, None)
    The description of the storage pool.


  fast_cache (optional, str, None)
    Indicates whether the fast cache is enabled for the storage pool.

    ``Enabled`` - FAST Cache is enabled for the pool.

    ``Disabled`` - FAST Cache is disabled for the pool.


  fast_vp (optional, str, None)
    Indicates whether to enable scheduled data relocations for the pool.

    ``Enabled`` - Enabled scheduled data relocations for the pool.

    ``Disabled`` - Disabled scheduled data relocations for the pool.


  raid_groups (optional, dict, None)
    Parameters to create RAID group from the disks and add it to the pool.


    disk_group_id (optional, str, None)
      Id of the disk group.


    disk_num (optional, int, None)
      Number of disks.


    raid_type (optional, str, None)
      RAID group types or RAID levels.


    stripe_width (optional, str, None)
      RAID group stripe widths, including parity or mirror disks.



  alert_threshold (optional, int, None)
    Threshold at which the system will generate alerts about the free space in the pool, specified as a percentage.

    Minimum threshold limit is 50.

    Maximum threshold limit is 84.


  is_harvest_enabled (optional, bool, None)
    Enable/Disable automatic deletion of snapshots based on pool space usage.


  pool_harvest_high_threshold (optional, float, None)
    Max threshold for space used in pool beyond which the system automatically starts deleting snapshots in the pool.

    Applies when the automatic deletion of snapshots based on pool space usage is enabled for the system and pool.

    Minimum pool harvest high threshold value is 1.

    Maximum pool harvest high threshold value is 99.


  pool_harvest_low_threshold (optional, float, None)
    Min threshold for space used in pool below which the system automatically stops deletion of snapshots in the pool.

    Applies when the automatic deletion of snapshots based on pool space usage is enabled for the system and pool.

    Minimum pool harvest low threshold value is 0.

    Maximum pool harvest low threshold value is 98.


  is_snap_harvest_enabled (optional, bool, None)
    Enable/Disable automatic deletion of snapshots based on pool space usage.


  snap_harvest_high_threshold (optional, float, None)
    Max threshold for space used in snapshot beyond which the system automatically starts deleting snapshots in the pool.

    Applies when the automatic deletion of snapshots based on pool space usage is enabled for the pool.

    Minimum snap harvest high threshold value is 1.

    Maximum snap harvest high threshold value is 99.


  snap_harvest_low_threshold (optional, float, None)
    Min threshold for space used in snapshot below which the system will stop automatically deleting snapshots in the pool.

    Applies when the automatic deletion of snapshots based on pool space usage is enabled for the pool.

    Minimum snap harvest low threshold value is 0.

    Maximum snap harvest low threshold value is 98.


  pool_type (optional, str, None)
    Indicates storage pool type.


  state (True, str, None)
    Define whether the storage pool should exist or not.

    ``Present`` - indicates that the storage pool should exist on the system.

    ``Absent`` - indicates that the storage pool should not exist on the system.


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
   - Deletion of storage pool is not allowed through Ansible module.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get Storage pool details using pool_name
      storagepool:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        pool_name: "{{pool_name}}"
        state: "present"

    - name: Get Storage pool details using pool_id
      storagepool:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        pool_id: "{{pool_id}}"
        state: "present"

    - name: Modify Storage pool attributes using pool_name
      storagepool:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        pool_name: "{{pool_name}}"
        new_pool_name: "{{new_pool_name}}"
        pool_description: "{{pool_description}}"
        fast_cache: "{{fast_cache_enabled}}"
        fast_vp: "{{fast_vp_enabled}}"
        state: "present"

    - name: Modify Storage pool attributes using pool_id
      storagepool:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        pool_id: "{{pool_id}}"
        new_pool_name: "{{new_pool_name}}"
        pool_description: "{{pool_description}}"
        fast_cache: "{{fast_cache_enabled}}"
        fast_vp: "{{fast_vp_enabled}}"
        state: "present"

    - name: Create a StoragePool
      storagepool:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        pool_name: "Test"
        pool_description: "test pool"
        raid_groups:
          disk_group_id : "dg_16"
          disk_num : 2
          raid_type : "RAID10"
          stripe_width : "BEST_FIT"
        alert_threshold : 50
        is_harvest_enabled : True
        pool_harvest_high_threshold : 60
        pool_harvest_low_threshold : 40
        is_snap_harvest_enabled : True
        snap_harvest_high_threshold : 70
        snap_harvest_low_threshold : 50
        fast_vp: "enabled"
        fast_cache: "enabled"
        pool_type : "DYNAMIC"
        state: "present"




Return Values
-------------

changed (always, bool, True)
  Whether or not the storage pool has changed.


storage_pool_details (When storage pool exists., dict, {'alert_threshold': 50, 'creation_time': '2022-03-08 14:05:32+00:00', 'description': '', 'drives': [{'disk_technology': 'SAS', 'id': 'dpe_disk_22', 'name': 'DPE Drive 22', 'size': 590860984320, 'tier_type': 'PERFORMANCE'}, {'disk_technology': 'SAS', 'id': 'dpe_disk_23', 'name': 'DPE Drive 23', 'size': 590860984320, 'tier_type': 'PERFORMANCE'}, {'disk_technology': 'SAS', 'id': 'dpe_disk_24', 'name': 'DPE Drive 24', 'size': 590860984320, 'tier_type': 'PERFORMANCE'}], 'existed': True, 'harvest_state': 'UsageHarvestStateEnum.IDLE', 'hash': 8744642897210, 'health': {'UnityHealth': {'hash': 8744642799842}}, 'id': 'pool_280', 'is_all_flash': False, 'is_empty': False, 'is_fast_cache_enabled': False, 'is_fast_vp_enabled': False, 'is_harvest_enabled': True, 'is_snap_harvest_enabled': True, 'metadata_size_subscribed': 105763569664, 'metadata_size_used': 57176752128, 'name': 'test_pool', 'object_id': 12884902146, 'pool_fast_vp': {'UnityPoolFastVp': {'hash': 8744647518980}}, 'pool_space_harvest_high_threshold': 59.0, 'pool_space_harvest_low_threshold': 40.0, 'pool_type': 'StoragePoolTypeEnum.DYNAMIC', 'raid_type': 'RaidTypeEnum.RAID10', 'rebalance_progress': None, 'size_free': 470030483456, 'size_free_with_unit': '437.75 GB', 'size_subscribed': 447215820800, 'size_subscribed_with_unit': '416.5 GB', 'size_total': 574720311296, 'size_total_with_unit': '535.25 GB', 'size_used': 76838068224, 'size_used_with_unit': '71.56 GB', 'snap_size_subscribed': 128851369984, 'snap_size_subscribed_with_unit': '120.0 GB', 'snap_size_used': 2351104, 'snap_size_used_with_unit': '2.24 MB', 'snap_space_harvest_high_threshold': 80.0, 'snap_space_harvest_low_threshold': 60.0, 'tiers': {'UnityPoolTierList': [{'disk_count': [0, 3, 0], 'existed': True, 'hash': 8744643017382, 'name': ['Extreme Performance', 'Performance', 'Capacity'], 'pool_units': [None, {'UnityPoolUnitList': [{'UnityPoolUnit': {'hash': 8744642786759, 'id': 'rg_4'}}, {'UnityPoolUnit': {'hash': 8744642786795, 'id': 'rg_5'}}]}, None], 'raid_type': ['RaidTypeEnum.NONE', 'RaidTypeEnum.RAID10', 'RaidTypeEnum.NONE'], 'size_free': [0, 470030483456, 0], 'size_moving_down': [0, 0, 0], 'size_moving_up': [0, 0, 0], 'size_moving_within': [0, 0, 0], 'size_total': [0, 574720311296, 0], 'size_used': [0, 104689827840, 0], 'stripe_width': [None, 'RaidStripeWidthEnum._2', None], 'tier_type': ['TierTypeEnum.EXTREME_PERFORMANCE', 'TierTypeEnum.PERFORMANCE', 'TierTypeEnum.CAPACITY']}]}})
  The storage pool details.


  id (, str, )
    Pool id, unique identifier of the pool.


  name (, str, )
    Pool name, unique in the storage system.


  is_fast_cache_enabled (, bool, )
    Indicates whether the fast cache is enabled for the storage pool. true - FAST Cache is enabled for the pool. false - FAST Cache is disabled for the pool.


  is_fast_vp_enabled (, bool, )
    Indicates whether to enable scheduled data relocations for the storage pool. true - Enabled scheduled data relocations for the pool. false - Disabled scheduled data relocations for the pool.


  size_free_with_unit (, str, )
    Indicates size_free with its appropriate unit in human readable form.


  size_subscribed_with_unit (, str, )
    Indicates size_subscribed with its appropriate unit in human readable form.


  size_total_with_unit (, str, )
    Indicates size_total with its appropriate unit in human readable form.


  size_used_with_unit (, str, )
    Indicates size_used with its appropriate unit in human readable form.


  snap_size_subscribed_with_unit (, str, )
    Indicates snap_size_subscribed with its appropriate unit in human readable form.


  snap_size_used_with_unit (, str, )
    Indicates snap_size_used with its appropriate unit in human readable form.


  drives (, list, )
    Indicates information about the drives associated with the storage pool.


    id (, str, )
      Unique identifier of the drive.


    name (, str, )
      Indicates name of the drive.


    size (, str, )
      Indicates size of the drive.


    disk_technology (, str, )
      Indicates disk technology of the drive.


    tier_type (, str, )
      Indicates tier type of the drive.







Status
------





Authors
~~~~~~~

- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>

