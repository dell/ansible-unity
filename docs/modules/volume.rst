.. _volume_module:


volume -- Manage volume on Unity storage system
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing volume on Unity storage system includes- Create new volume, Modify volume attributes, Map Volume to host, Unmap volume to host, Display volume details, Delete volume.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  vol_name (optional, str, None)
    The name of the volume. Mandatory only for create operation.


  vol_id (optional, str, None)
    The id of the volume.

    It can be used only for get, modify, map/unmap host, or delete operation.


  pool_name (optional, str, None)
    This is the name of the pool where the volume will be created.

    Either the *pool_name* or *pool_id* must be provided to create a new volume.


  pool_id (optional, str, None)
    This is the id of the pool where the volume will be created.

    Either the *pool_name* or *pool_id* must be provided to create a new volume.


  size (optional, int, None)
    The size of the volume.


  cap_unit (optional, str, None)
    The unit of the volume size. It defaults to ``GB``, if not specified.


  description (optional, str, None)
    Description about the volume.

    Description can be removed by passing empty string ("").


  snap_schedule (optional, str, None)
    Snapshot schedule assigned to the volume.

    Add/Remove/Modify the snapshot schedule for the volume.


  compression (optional, bool, None)
    Boolean variable, Specifies whether or not to enable compression. Compression is supported only for thin volumes.


  advanced_dedup (optional, bool, None)
    Boolean variable, Indicates whether or not to enable advanced deduplication.

    Compression should be enabled to enable advanced deduplication.

    It can only be enabled on the all flash high end platforms.

    Deduplicated data will remain as is even after advanced deduplication is disabled.


  is_thin (optional, bool, None)
    Boolean variable, Specifies whether or not it is a thin volume.

    The value is set as ``true`` by default if not specified.


  sp (optional, str, None)
    Storage Processor for this volume.


  io_limit_policy (optional, str, None)
    IO limit policy associated with this volume. Once it is set, it cannot be removed through ansible module but it can be changed.


  host_name (optional, str, None)
    Name of the host to be mapped/unmapped with this volume.

    Either *host_name* or *host_id* can be specified in one task along with *mapping_state*.


  host_id (optional, str, None)
    ID of the host to be mapped/unmapped with this volume.

    Either *host_name* or *host_id* can be specified in one task along with *mapping_state*.


  hlu (optional, int, None)
    Host Lun Unit to be mapped/unmapped with this volume.

    It is an optional parameter, hlu can be specified along with *host_name* or *host_id* and *mapping_state*.

    If *hlu* is not specified, unity will choose it automatically. The maximum value supported is ``255``.


  mapping_state (optional, str, None)
    State of host access for volume.


  new_vol_name (optional, str, None)
    New name of the volume for rename operation.


  tiering_policy (optional, str, None)
    Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.


  state (True, str, None)
    State variable to determine whether volume will exist or not.


  hosts (optional, list, None)
    Name of hosts for mapping to a volume.


    host_name (optional, str, None)
      Name of the host.


    host_id (optional, str, None)
      ID of the host.


    hlu (optional, str, None)
      Host Lun Unit to be mapped/unmapped with this volume.

      It is an optional parameter, *hlu* can be specified along with *host_name* or *host_id* and *mapping_state*.

      If *hlu* is not specified, unity will choose it automatically. The maximum value supported is ``255``.



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

    
    - name: Create Volume
      volume:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vol_name: "{{vol_name}}"
        description: "{{description}}"
        pool_name: "{{pool}}"
        size: 2
        cap_unit: "{{cap_GB}}"
        is_thin: True
        compression: True
        advanced_dedup: True
        state: "{{state_present}}"

    - name: Expand Volume by volume id
      volume:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vol_id: "{{vol_id}}"
        size: 5
        cap_unit: "{{cap_GB}}"
        state: "{{state_present}}"

    - name: Modify Volume, map host by host_name
      volume:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vol_name: "{{vol_name}}"
        host_name: "{{host_name}}"
        hlu: 5
        mapping_state: "{{state_mapped}}"
        state: "{{state_present}}"

    - name: Modify Volume, unmap host mapping by host_name
      volume:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vol_name: "{{vol_name}}"
        host_name: "{{host_name}}"
        mapping_state: "{{state_unmapped}}"
        state: "{{state_present}}"

    - name: Map multiple hosts to a Volume
      volume:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vol_id: "{{vol_id}}"
        hosts:
            - host_name: "10.226.198.248"
              hlu: 1
            - host_id: "Host_929"
              hlu: 2
        mapping_state: "mapped"
        state: "present"

    - name: Modify Volume attributes
      volume:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vol_name: "{{vol_name}}"
        new_vol_name: "{{new_vol_name}}"
        tiering_policy: "AUTOTIER"
        compression: True
        is_thin: True
        advanced_dedup: True
        state: "{{state_present}}"

    - name: Delete Volume by vol name
      volume:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vol_name: "{{vol_name}}"
        state: "{{state_absent}}"

    - name: Delete Volume by vol id
      volume:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        vol_id: "{{vol_id}}"
        state: "{{state_absent}}"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


volume_details (When volume exists, dict, {'current_node': 'NodeEnum.SPB', 'data_reduction_percent': 0, 'data_reduction_ratio': 1.0, 'data_reduction_size_saved': 0, 'default_node': 'NodeEnum.SPB', 'description': None, 'effective_io_limit_max_iops': None, 'effective_io_limit_max_kbps': None, 'existed': True, 'family_base_lun': {'UnityLun': {'hash': 8774954523796, 'id': 'sv_27'}}, 'family_clone_count': 0, 'hash': 8774954522426, 'health': {'UnityHealth': {'hash': 8774954528278}}, 'host_access': [{'accessMask': 'PRODUCTION', 'hlu': 0, 'id': 'Host_75', 'name': '10.226.198.250'}], 'id': 'sv_27', 'io_limit_policy': None, 'is_advanced_dedup_enabled': False, 'is_compression_enabled': None, 'is_data_reduction_enabled': False, 'is_replication_destination': False, 'is_snap_schedule_paused': False, 'is_thin_clone': False, 'is_thin_enabled': False, 'metadata_size': 4294967296, 'metadata_size_allocated': 4026531840, 'name': 'VSI-UNITY-test-task', 'per_tier_size_used': [111400714240, 0, 0], 'pool': {'id': 'pool_3', 'name': 'Extreme_Perf_tier'}, 'size_allocated': 107374182400, 'size_total': 107374182400, 'size_total_with_unit': '100.0 GB', 'size_used': None, 'snap_count': 0, 'snap_schedule': None, 'snap_wwn': '60:06:01:60:5C:F0:50:00:94:3E:91:4D:51:5A:4F:97', 'snaps_size': 0, 'snaps_size_allocated': 0, 'storage_resource': {'UnityStorageResource': {'hash': 8774954518887}}, 'tiering_policy': 'TieringPolicyEnum.AUTOTIER_HIGH', 'type': 'LUNTypeEnum.VMWARE_ISCSI', 'wwn': '60:06:01:60:5C:F0:50:00:00:B5:95:61:2E:34:DB:B2'})
  Details of the volume.


  id (, str, )
    The system generated ID given to the volume.


  name (, str, )
    Name of the volume.


  description (, str, )
    Description about the volume.


  is_data_reduction_enabled (, bool, )
    Whether or not compression enabled on this volume.


  size_total_with_unit (, str, )
    Size of the volume with actual unit.


  snap_schedule (, dict, )
    Snapshot schedule applied to this volume.


  tiering_policy (, str, )
    Tiering policy applied to this volume.


  current_sp (, str, )
    Current storage processor for this volume.


  pool (, dict, )
    The pool in which this volume is allocated.


  host_access (, list, )
    Host mapped to this volume.


  io_limit_policy (, dict, )
    IO limit policy associated with this volume.


  wwn (, str, )
    The world wide name of this volume.


  is_thin_enabled (, bool, )
    Indicates whether thin provisioning is enabled for this volume.






Status
------





Authors
~~~~~~~

- Arindam Datta (@arindam-emc) <ansible.team@dell.com>
- Pavan Mudunuri(@Pavan-Mudunuri) <ansible.team@dell.com>

