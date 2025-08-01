.. _nfsserver_module:


nfsserver -- Manage NFS server on Unity storage system
======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing the NFS server on the Unity storage system includes creating NFS server, getting NFS server details and deleting NFS server attributes.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  nas_server_name (optional, str, None)
    Name of the NAS server on which NFS server will be hosted.


  nas_server_id (optional, str, None)
    ID of the NAS server on which NFS server will be hosted.


  nfs_server_id (optional, str, None)
    ID of the NFS server.


  host_name (optional, str, None)
    Host name of the NFS server.


  nfs_v4_enabled (optional, bool, None)
    Indicates whether the NFSv4 is enabled on the NAS server.


  is_secure_enabled (optional, bool, None)
    Indicates whether the secure NFS is enabled.


  kerberos_domain_controller_type (optional, str, None)
    Type of Kerberos Domain Controller used for secure NFS service.


  kerberos_domain_controller_username (optional, str, None)
    Kerberos Domain Controller administrator username.


  kerberos_domain_controller_password (optional, str, None)
    Kerberos Domain Controller administrator password.


  is_extended_credentials_enabled (optional, bool, None)
    Indicates whether support for more than 16 unix groups in a Unix credential.


  remove_spn_from_kerberos (optional, bool, True)
    Indicates whether to remove the SPN from Kerberos Domain Controller.


  state (True, str, None)
    Define whether the NFS server should exist or not.


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
   - Modify operation for NFS Server is not supported.
   - When *kerberos_domain_controller_type* is ``UNIX``, *kdc_type* in *nfs_server_details* output is displayed as ``null``.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

        - name: Create NFS server with kdctype as Windows
          nfsserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            host_name: "dummy_nas23"
            is_secure_enabled: True
            kerberos_domain_controller_type: "WINDOWS"
            kerberos_domain_controller_username: "administrator"
            kerberos_domain_controller_password: "Password123!"
            is_extended_credentials_enabled: True
            nfs_v4_enabled: True
            state: "present"

        - name: Create NFS server with kdctype as Unix
          nfsserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            host_name: "dummy_nas23"
            is_secure_enabled: True
            kerberos_domain_controller_type: "UNIX"
            is_extended_credentials_enabled: True
            nfs_v4_enabled: True
            state: "present"

        - name: Get NFS server details
          nfsserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            state: "present"

        - name: Delete NFS server
          nfsserver:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            kerberos_domain_controller_username: "administrator"
            kerberos_domain_controller_password: "Password123!"
            unjoin_server_account: False
            state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


nfs_server_details (When NFS server exists, dict, {'credentials_cache_ttl': '0:15:00', 'existed': True, 'file_interfaces': {'UnityFileInterfaceList': [{'UnityFileInterface': {'hash': 8778980109421, 'id': 'if_37'}}]}, 'hash': 8778980109388, 'host_name': 'dummy_nas23.pie.lab.emc.com', 'id': 'nfs_51', 'is_extended_credentials_enabled': True, 'is_secure_enabled': True, 'kdc_type': 'KdcTypeEnum.WINDOWS', 'nas_server': {'UnityNasServer': {'hash': 8778980109412}}, 'nfs_v4_enabled': True, 'servicee_principal_name': None})
  Details of the NFS server.


  credentials_cache_ttl (, str, )
    Credential cache refresh timeout. Resolution is in minutes. Default value is 15 minutes.


  existed (, bool, )
    Indicates if NFS Server exists.


  host_name (, str, )
    Host name of the NFS server.


  id (, str, )
    Unique identifier of the NFS Server instance.


  is_extended_credentials_enabled (, bool, )
    Indicates whether the NFS server supports more than 16 Unix groups in a Unix credential.


  is_secure_enabled (, bool, )
    Indicates whether secure NFS is enabled on the NFS server.


  kdc_type (, str, )
    Type of Kerberos Domain Controller used for secure NFS service.


  nfs_v4_enabled (, bool, )
    Indicates whether NFSv4 is enabled on the NAS server.


  servicee_principal_name (, str, )
    The Service Principal Name (SPN) for the NFS Server.






Status
------





Authors
~~~~~~~

- Meenakshi Dembi (@dembim) <ansible.team@dell.com>

