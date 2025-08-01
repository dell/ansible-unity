.. _host_module:


host -- Manage Host operations on Unity
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The Host module contains the operations Creation of a Host, Addition of initiators to Host, Removal of initiators from Host, Modification of host attributes, Get details of a Host, Deletion of a Host, Addition of network address to Host, Removal of network address from Host.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  host_name (optional, str, None)
    Name of the host.

    Mandatory for host creation.


  host_id (optional, str, None)
    Unique identifier of the host.

    Host Id is auto generated during creation.

    Except create, all other operations require either *host_id* or Ihost_name).


  description (optional, str, None)
    Host description.


  host_os (optional, str, None)
    Operating system running on the host.


  new_host_name (optional, str, None)
    New name for the host.

    Only required in rename host operation.


  initiators (optional, list, None)
    List of initiators to be added/removed to/from host.


  initiator_state (optional, str, None)
    State of the initiator.


  network_address (optional, str, None)
    Network address to be added/removed to/from the host.

    Enter valid IPV4 or host name.


  network_address_state (optional, str, None)
    State of the Network address.


  state (True, str, None)
    State of the host.


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

    
    - name: Create empty Host
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_name: "ansible-test-host"
        host_os: "Linux"
        description: "ansible-test-host"
        state: "present"

    - name: Create Host with Initiators
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_name: "ansible-test-host-1"
        host_os: "Linux"
        description: "ansible-test-host-1"
        initiators:
          - "iqn.1994-05.com.redhat:c38e6e8cfd81"
          - "20:00:00:90:FA:13:81:8D:10:00:00:90:FA:13:81:8D"
        initiator_state: "present-in-host"
        state: "present"

    - name: Modify Host using host_id
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_id: "Host_253"
        new_host_name: "ansible-test-host-2"
        host_os: "Mac OS"
        description: "Ansible tesing purpose"
        state: "present"

    - name: Add Initiators to Host
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_name: "ansible-test-host-2"
        initiators:
          - "20:00:00:90:FA:13:81:8C:10:00:00:90:FA:13:81:8C"
        initiator_state: "present-in-host"
        state: "present"

    - name: Get Host details using host_name
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_name: "ansible-test-host-2"
        state: "present"

    - name: Get Host details using host_id
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_id: "Host_253"
        state: "present"

    - name: Delete Host
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_name: "ansible-test-host-2"
        state: "absent"

    - name: Add network address to Host
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_name: "{{host_name}}"
        network_address: "192.168.1.2"
        network_address_state: "present-in-host"
        state: "present"

    - name: Delete network address from Host
      host:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        host_name: "{{host_name}}"
        network_address: "192.168.1.2"
        network_address_state: "absent-in-host"
        state: "present"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


host_details (When host exists., dict, {'auto_manage_type': 'HostManageEnum.UNKNOWN', 'datastores': None, 'description': 'ansible-test-host-1', 'existed': True, 'fc_host_initiators': [{'id': 'HostInitiator_1', 'name': 'HostName_1', 'paths': [{'id': 'HostInitiator_1_Id1', 'is_logged_in': True}, {'id': 'HostInitiator_1_Id2', 'is_logged_in': True}]}], 'hash': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER', 'health': {'UnityHealth': {'hash': 8764429420954}}, 'host_container': None, 'host_luns': [], 'host_polled_uuid': None, 'host_pushed_uuid': None, 'host_uuid': None, 'host_v_vol_datastore': None, 'id': 'Host_2198', 'iscsi_host_initiators': [{'id': 'HostInitiator_2', 'name': 'HostName_2', 'paths': [{'id': 'HostInitiator_2_Id1', 'is_logged_in': True}, {'id': 'HostInitiator_2_Id2', 'is_logged_in': True}]}], 'last_poll_time': None, 'name': 'ansible-test-host-1', 'network_addresses': [], 'os_type': 'Linux', 'registration_type': None, 'storage_resources': None, 'tenant': None, 'type': 'HostTypeEnum.HOST_MANUAL', 'vms': None})
  Details of the host.


  id (, str, )
    The system ID given to the host.


  name (, str, )
    The name of the host.


  description (, str, )
    Description about the host.


  fc_host_initiators (, list, )
    Details of the FC initiators associated with the host.


    id (, str, )
      Unique identifier of the FC initiator path.


    name (, str, )
      FC Qualified Name (WWN) of the initiator.


    paths (, list, )
      Details of the paths associated with the FC initiator.


      id (, str, )
        Unique identifier of the path.


      is_logged_in (, bool, )
        Indicates whether the host initiator is logged into the storage system.




  iscsi_host_initiators (, list, )
    Details of the ISCSI initiators associated with the host.


    id (, str, )
      Unique identifier of the ISCSI initiator path.


    name (, str, )
      ISCSI Qualified Name (IQN) of the initiator.


    paths (, list, )
      Details of the paths associated with the ISCSI initiator.


      id (, str, )
        Unique identifier of the path.


      is_logged_in (, bool, )
        Indicates whether the host initiator is logged into the storage system.




  network_addresses (, list, )
    List of network addresses mapped to the host.


  os_type (, str, )
    Operating system running on the host.


  type (, str, )
    HostTypeEnum of the host.


  host_luns (, list, )
    Details of luns attached to host.






Status
------





Authors
~~~~~~~

- Rajshree Khare (@kharer5) <ansible.team@dell.com>

