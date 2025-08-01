.. _cifsserver_module:


cifsserver -- Manage CIFS server on Unity storage system
========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing the CIFS server on the Unity storage system includes creating CIFS server, getting CIFS server details and deleting CIFS server.



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
    Name of the NAS server on which CIFS server will be hosted.


  nas_server_id (optional, str, None)
    ID of the NAS server on which CIFS server will be hosted.


  netbios_name (optional, str, None)
    The computer name of the SMB server in Windows network.


  workgroup (optional, str, None)
    Standalone SMB server workgroup.


  local_password (optional, str, None)
    Standalone SMB server administrator password.


  domain (optional, str, None)
    The domain name where the SMB server is registered in Active Directory.


  domain_username (optional, str, None)
    Active Directory domain user name.


  domain_password (optional, str, None)
    Active Directory domain password.


  cifs_server_name (optional, str, None)
    The name of the CIFS server.


  cifs_server_id (optional, str, None)
    The ID of the CIFS server.


  interfaces (optional, list, None)
    List of file IP interfaces that service CIFS protocol of SMB server.


  unjoin_cifs_server_account (optional, bool, None)
    Keep SMB server account unjoined in Active Directory after deletion.

    ``false`` specifies keep SMB server account joined after deletion.

    ``true`` specifies unjoin SMB server account from Active Directory before deletion.


  state (True, str, None)
    Define whether the CIFS server should exist or not.


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

    
    - name: Create CIFS server belonging to Active Directory
      cifsserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        nas_server_name: "test_nas1"
        cifs_server_name: "test_cifs"
        domain: "ad_domain"
        domain_username: "domain_username"
        domain_password: "domain_password"
        state: "present"

    - name: Get CIFS server details using CIFS server ID
      cifsserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        cifs_server_id: "cifs_37"
        state: "present"

    - name: Get CIFS server details using NAS server name
      cifsserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        nas_server_name: "test_nas1"
        state: "present"

    - name: Delete CIFS server
      cifsserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        cifs_server_id: "cifs_37"
        unjoin_cifs_server_account: True
        domain_username: "domain_username"
        domain_password: "domain_password"
        state: "absent"

    - name: Create standalone CIFS server
      cifsserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        netbios_name: "ANSIBLE_CIFS"
        workgroup: "ansible"
        local_password: "Password123!"
        nas_server_name: "test_nas1"
        state: "present"

    - name: Get CIFS server details using netbios name
      cifsserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        netbios_name: "ANSIBLE_CIFS"
        state: "present"

    - name: Delete standalone CIFS server
      cifsserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        cifs_server_id: "cifs_40"
        state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


cifs_server_details (When CIFS server exists, dict, {'description': None, 'domain': 'xxx.xxx.xxx.com', 'existed': True, 'file_interfaces': {'UnityFileInterfaceList': [{'UnityFileInterface': {'hash': -9223363258905013637, 'id': 'if_43'}}]}, 'hash': -9223363258905010379, 'health': {'UnityHealth': {'hash': 8777949765559}}, 'id': 'cifs_40', 'is_standalone': False, 'last_used_organizational_unit': 'ou=Computers,ou=Dell NAS servers', 'name': 'ansible_cifs', 'nas_server': {'UnityNasServer': {'hash': 8777949765531, 'id': 'nas_18'}}, 'netbios_name': 'ANSIBLE_CIFS', 'smb_multi_channel_supported': True, 'smb_protocol_versions': ['1.0', '2.0', '2.1', '3.0'], 'smbca_supported': True, 'workgroup': None})
  Details of the CIFS server.


  id (, str, )
    Unique identifier of the CIFS server instance.


  name (, str, )
    User-specified name for the SMB server.


  netbios_name (, str, )
    Computer Name of the SMB server in windows network.


  description (, str, )
    Description of the SMB server.


  domain (, str, )
    Domain name where SMB server is registered in Active Directory.


  workgroup (, str, )
    Windows network workgroup for the SMB server.


  is_standalone (, bool, )
    Indicates whether the SMB server is standalone.


  nasServer (, dict, )
    Information about the NAS server in the storage system.


    UnityNasServer (, dict, )
      Information about the NAS server in the storage system.


      id (, str, )
        Unique identifier of the NAS server instance.




  file_interfaces (, dict, )
    The file interfaces associated with the NAS server.


    UnityFileInterfaceList (, list, )
      List of file interfaces associated with the NAS server.


      UnityFileInterface (, dict, )
        Details of file interface associated with the NAS server.


        id (, str, )
          Unique identifier of the file interface.





  smb_multi_channel_supported (, bool, )
    Indicates whether the SMB 3.0+ multichannel feature is supported.


  smb_protocol_versions (, list, )
    Supported SMB protocols, such as 1.0, 2.0, 2.1, 3.0, and so on.


  smbca_supported (, bool, )
    Indicates whether the SMB server supports continuous availability.






Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

