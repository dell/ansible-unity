.. _nasserver_module:


nasserver -- Manage NAS servers on Unity storage system
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing NAS servers on Unity storage system includes get, modification to the NAS servers.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  nas_server_id (optional, str, None)
    The ID of the NAS server.

    Either *nas_server_name* or *nas_server_id* is required to perform the task.

    The parameters *nas_server_name* and *nas_server_id* are mutually exclusive.


  nas_server_name (optional, str, None)
    The Name of the NAS server.

    Either *nas_server_name* or *nas_server_id*  is required to perform the task.

    The parameters *nas_server_name* and *nas_server_id* are mutually exclusive.


  nas_server_new_name (optional, str, None)
    The new name of the NAS server.

    It can be mentioned during modification of the NAS server.


  is_replication_destination (optional, bool, None)
    It specifies whether the NAS server is a replication destination.

    It can be mentioned during modification of the NAS server.


  is_backup_only (optional, bool, None)
    It specifies whether the NAS server is used as backup only.

    It can be mentioned during modification of the NAS server.


  is_multiprotocol_enabled (optional, bool, None)
    This parameter indicates whether multiprotocol sharing mode is enabled.

    It can be mentioned during modification of the NAS server.


  allow_unmapped_user (optional, bool, None)
    This flag is used to mandatorily disable access in case of any user mapping failure.

    If ``true``, then enable access in case of any user mapping failure.

    If ``false``, then disable access in case of any user mapping failure.

    It can be mentioned during modification of the NAS server.


  default_windows_user (optional, str, None)
    Default windows user name used for granting access in the case of Unix to Windows user mapping failure.

    It can be mentioned during modification of the NAS server.


  default_unix_user (optional, str, None)
    Default Unix user name used for granting access in the case of Windows to Unix user mapping failure.

    It can be mentioned during modification of the NAS server.


  enable_windows_to_unix_username_mapping (optional, bool, None)
    This parameter indicates whether a Unix to/from Windows user name mapping is enabled.

    It can be mentioned during modification of the NAS server.


  is_packet_reflect_enabled (optional, bool, None)
    If the packet has to be reflected, then this parameter has to be set to ``true``.

    It can be mentioned during modification of the NAS server.


  current_unix_directory_service (optional, str, None)
    This is the directory service used for querying identity information for UNIX (such as UIDs, GIDs, net groups).

    It can be mentioned during modification of the NAS server.


  replication_params (optional, dict, None)
    Settings required for enabling replication.


    destination_nas_server_name (optional, str, None)
      Name of the destination nas server.

      Default value will be source nas server name prefixed by 'DR_'.


    replication_mode (optional, str, None)
      The replication mode.

      This is mandatory to enable replication.


    rpo (optional, int, None)
      Maximum time to wait before the system syncs the source and destination LUNs.

      The *rpo* option should be specified if the *replication_mode* is ``asynchronous``.

      The value should be in range of ``5`` to ``1440``.


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



    destination_pool_name (optional, str, None)
      Name of pool to allocate destination Luns.

      Mutually exclusive with *destination_pool_id*.


    destination_pool_id (optional, str, None)
      Id of pool to allocate destination Luns.

      Mutually exclusive with *destination_pool_name*.


    destination_sp (optional, str, None)
      Storage process of destination nas server


    is_backup (optional, bool, None)
      Indicates if the destination nas server is backup.


    replication_name (optional, str, None)
      User defined name for replication session.


    new_replication_name (optional, str, None)
      Replication name to rename the session to.



  replication_state (optional, str, None)
    State of the replication.


  replication_reuse_resource (optional, bool, None)
    This parameter indicates if existing NAS Server is to be used for replication.


  state (True, str, None)
    Define the state of NAS server on the array.

    The value present indicates that NAS server should exist on the system after the task is executed.

    In this release deletion of NAS server is not supported. Hence, if state is set to ``absent`` for any existing NAS server then error will be thrown.

    For any non-existing NAS server, if state is set to ``absent`` then it will return None.


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

    

        - name: Get Details of NAS Server
          nasserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "{{nas_server_name}}"
            state: "present"

        - name: Modify Details of NAS Server
          nasserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "{{nas_server_name}}"
            nas_server_new_name: "updated_sample_nas_server"
            is_replication_destination: False
            is_backup_only: False
            is_multiprotocol_enabled: True
            allow_unmapped_user: True
            default_unix_user: "default_unix_sample_user"
            default_windows_user: "default_windows_sample_user"
            enable_windows_to_unix_username_mapping: True
            current_unix_directory_service: "LDAP"
            is_packet_reflect_enabled: True
            state: "present"

        - name: Enable replication for NAS Server on Local System
          nasserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_id: "nas_10"
            replication_reuse_resource: False
            replication_params:
              replication_name: "test_replication"
              destination_nas_server_name: "destination_nas"
              replication_mode: "asynchronous"
              rpo: 60
              replication_type: "local"
              destination_pool_name: "Pool_Ansible_Neo_DND"
              destination_sp: "SPA"
              is_backup: True
            replication_state: "enable"
            state: "present"

        - name: Enable replication for NAS Server on Remote System
          nasserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            replication_reuse_resource: False
            replication_params:
              replication_name: "test_replication"
              destination_nas_server_name: "destination_nas"
              replication_mode: "asynchronous"
              rpo: 60
              replication_type: "remote"
              remote_system:
                remote_system_host: '10.10.10.10'
                remote_system_verifycert: False
                remote_system_username: 'test1'
                remote_system_password: 'test1!'
              destination_pool_name: "fastVP_pool"
              destination_sp: "SPA"
              is_backup: True
            replication_state: "enable"
            state: "present"

        - name: Enable replication for NAS Server on Remote System in existing NAS Server
          nasserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            replication_reuse_resource: True
            replication_params:
              destination_nas_server_name: "destination_nas"
              replication_mode: "asynchronous"
              rpo: 60
              replication_type: "remote"
              replication_name: "test_replication"
              remote_system:
                remote_system_host: '10.10.10.10'
                remote_system_verifycert: False
                remote_system_username: 'test1'
                remote_system_password: 'test1!'
              destination_pool_name: "fastVP_pool"
            replication_state: "enable"
            state: "present"

        - name: Modify replication on the nasserver
          nasserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            replication_params:
                replication_name: "test_repl"
                new_replication_name: "test_repl_updated"
                replication_mode: "asynchronous"
                rpo: 50
            replication_state: "enable"
            state: "present"

        - name: Disable replication on the nasserver
          nasserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            replication_state: "disable"
            state: "present"

        - name: Disable replication by specifying replication_name on the nasserver
          nasserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            replication_params:
                replication_name: "test_replication"
            replication_state: "disable"
            state: "present"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


nas_server_details (When NAS server exists., dict, {'allow_unmapped_user': None, 'cifs_server': {'UnityCifsServerList': [{'UnityCifsServer': {'hash': 8761756885270, 'id': 'cifs_34'}}]}, 'current_sp': {'UnityStorageProcessor': {'hash': 8761756885273, 'id': 'spb'}}, 'current_unix_directory_service': 'NasServerUnixDirectoryServiceEnum.NIS', 'default_unix_user': None, 'default_windows_user': None, 'existed': True, 'file_dns_server': {'UnityFileDnsServer': {'hash': 8761756885441, 'id': 'dns_12'}}, 'file_interface': {'UnityFileInterfaceList': [{'UnityFileInterface': {'hash': 8761756889908, 'id': 'if_37'}}]}, 'filesystems': None, 'hash': 8761757005084, 'health': {'UnityHealth': {'hash': 8761756867588}}, 'home_sp': {'UnityStorageProcessor': {'hash': 8761756867618, 'id': 'spb'}}, 'id': 'nas_10', 'is_backup_only': False, 'is_multi_protocol_enabled': False, 'is_packet_reflect_enabled': False, 'is_replication_destination': False, 'is_replication_enabled': True, 'is_windows_to_unix_username_mapping_enabled': None, 'name': 'dummy_nas', 'pool': {'UnityPool': {'hash': 8761756885360, 'id': 'pool_7'}}, 'preferred_interface_settings': {'UnityPreferredInterfaceSettings': {'hash': 8761756885438, 'id': 'preferred_if_10'}}, 'replication_type': 'ReplicationTypeEnum.REMOTE', 'size_allocated': 3489660928, 'tenant': None, 'virus_checker': {'UnityVirusChecker': {'hash': 8761756885426, 'id': 'cava_10'}}})
  The NAS server details.


  name (, str, )
    Name of the NAS server.


  id (, str, )
    ID of the NAS server.


  allow_unmapped_user (, bool, )
    Enable/disable access status in case of any user mapping failure.


  current_unix_directory_service (, str, )
    Directory service used for querying identity information for UNIX (such as UIDs, GIDs, net groups).


  default_unix_user (, str, )
    Default Unix user name used for granting access in the case of Windows to Unix user mapping failure.


  default_windows_user (, str, )
    Default windows user name used for granting access in the case of Unix to Windows user mapping failure.


  is_backup_only (, bool, )
    Whether the NAS server is used as backup only.


  is_multi_protocol_enabled (, bool, )
    Indicates whether multiprotocol sharing mode is enabled.


  is_packet_reflect_enabled (, bool, )
    If the packet reflect has to be enabled.


  is_replication_destination (, bool, )
    If the NAS server is a replication destination then True.


  is_windows_to_unix_username_mapping_enabled (, bool, )
    Indicates whether a Unix to/from Windows user name mapping is enabled.






Status
------





Authors
~~~~~~~

- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

