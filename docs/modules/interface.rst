.. _interface_module:


interface -- Manage Interfaces on Unity storage system
======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing the Interfaces on the Unity storage system includes adding Interfaces to NAS Server, getting details of interface and deleting configured interfaces.



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
    Name of the NAS server for which interface will be configured.


  nas_server_id (optional, str, None)
    ID of the NAS server for which interface will be configured.


  ethernet_port_name (optional, str, None)
    Name of the ethernet port.


  ethernet_port_id (optional, str, None)
    ID of the ethernet port.


  role (optional, str, None)
    Indicates whether interface is configured as production or backup.


  interface_ip (True, str, None)
    IP of network interface.


  netmask (optional, str, None)
    Netmask of network interface.


  prefix_length (optional, int, None)
    Prefix length is mutually exclusive with *netmask*.


  gateway (optional, str, None)
    Gateway of network interface.


  vlan_id (optional, int, None)
    Vlan id of the interface.


  state (True, str, None)
    Define whether the interface should exist or not.


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
   - Modify operation for interface is not supported.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

        - name: Add Interface as Backup to NAS Server
          interface:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            ethernet_port_name: "SP A 4-Port Card Ethernet Port 0"
            role: "BACKUP"
            interface_ip: "xx.xx.xx.xx"
            netmask: "xx.xx.xx.xx"
            gateway: "xx.xx.xx.xx"
            vlan_id: 324
            state: "present"

        - name: Add Interface as Production to NAS Server
          interface:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            ethernet_port_name: "SP A 4-Port Card Ethernet Port 0"
            role: "PRODUCTION"
            interface_ip: "xx.xx.xx.xx"
            netmask: "xx.xx.xx.xx"
            gateway: "xx.xx.xx.xx"
            vlan_id: 324
            state: "present"

        - name: Get interface details
          interface:
            unispherehost: "{{unispherehost}}"
            username: "{{username}}"
            password: "{{password}}"
            validate_certs: "{{validate_certs}}"
            nas_server_name: "dummy_nas"
            interface_ip: "xx.xx.xx.xx"
            state: "present"

        - name: Delete Interface
          interface:
          unispherehost: "{{unispherehost}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          nas_server_name: "dummy_nas"
          interface_ip: "xx.xx.xx.xx"
          state: "absent"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


interface_details (When interface is configured for NAS Server., dict, {'existed': True, 'gateway': 'xx.xx.xx.xx', 'hash': 8785300560421, 'health': {'UnityHealth': {'hash': 8785300565468}}, 'id': 'if_69', 'ip_address': '10.10.10.10', 'ip_port': {'UnityIpPort': {'hash': 8785300565300, 'id': 'spb_ocp_0_eth0'}}, 'ip_protocol_version': 'IpProtocolVersionEnum.IPv4', 'is_disabled': False, 'is_preferred': True, 'mac_address': '0C:48:C6:9F:57:BF', 'name': '36_APM00213404194', 'nas_server': {'UnityNasServer': {'hash': 8785300565417, 'id': 'nas_10'}}, 'netmask': '10.10.10.10', 'replication_policy': None, 'role': 'FileInterfaceRoleEnum.PRODUCTION', 'source_parameters': None, 'v6_prefix_length': None, 'vlan_id': 324})
  Details of the interface.


  existed (, bool, )
    Indicates if interface exists.


  gateway (, str, )
    Gateway of network interface.


  id (, str, )
    Unique identifier interface.


  ip_address (, str, )
    IP address of interface.


  ip_port (, dict, )
    Port on which network interface is configured.


    id (, str, )
      ID of ip_port.



  ip_protocol_version (, str, )
    IP protocol version.


  is_disabled (, bool, )
    Indicates whether interface is disabled.


  is_preferred (, bool, )
    Indicates whether interface is preferred.


  mac_address (, bool, )
    Mac address of ip_port.


  name (, bool, )
    System configured name of interface.


  nas_server (, dict, )
    Details of NAS server where interface is configured.


    id (, str, )
      ID of NAS Server.







Status
------





Authors
~~~~~~~

- Meenakshi Dembi (@dembim) <ansible.team@dell.com>

