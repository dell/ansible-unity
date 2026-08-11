#!/usr/bin/python

"""Ansible module to configure replication interfaces"""


DOCUMENTATION = r"""
---
module: replication_connection
version_added: '1.0'
short_description: Configure replication interfaces for Unity
description:
- Configure replication interfaces on a Unity Unisphere host. For more information on the API go checkout the doc: https://developer.dell.com/apis/3028/versions/5.2.0/models/spec_publish.yml/paths/~1api~1types~1replicationInterface~1instances/post.
author:
- Guillaume DORSCHNER (GuillaumeDorschner)
options:
    unispherehost:
        description: IP or hostname of the target Unisphere management host.
        required: true
        type: str
    username:
        description: Username to authenticate against Unisphere.
        required: true
        type: str
    password:
        description: Password to authenticate against Unisphere.
        required: true
        type: str
        no_log: true
    validate_certs:
        description: Whether to validate SSL certificates for the Unisphere connection.
        default: false
        type: bool
    interfaces:
        description: List of replication interface to configure.
        required: true
        type: list
        elements: dict
        suboptions:
            sp:
                description: Unique id storage processor on which the replication interface is running.
                required: true
                type: str
            ipPort:
                description: Unique id Physical port or link aggregation on the storage processor on which the interface is running, as defined by the ethernetPort resource type.
                required: true
                type: str
            ipAddress:
                description: IP address of the replication interface.
                required: true
                type: str
            netmask:
                description: IPv4 netmask for the replication interface, if it uses an IPv4 address.
                required: false
                type: str
            state:
                description: Whether this replication interface should exist or not.
                required: false
                type: str
                default: present
                choices: [present, absent]
            vlanId:
                description: Virtual Local Area Network (VLAN) identifier for the interface. The interface uses the identifier to accept packets that have matching VLAN tags. Values are between 0 - 4094.
                required: false
                type: str
            gateway:
                description: IPv4 or IPv6 gateway address for the replication interface.
                required: false
                type: str
            v6PrefixLength:
                description: IPv6 prefix length for the interface, if it uses an IPv6 address.
                required: false
                type: int
                default: 0
"""

EXAMPLES = r"""
- name: Configure replication interface
  replication_interface:
    unispherehost: 10.52.20.56
    username: <user>
    password: <password>
    validate_certs: true
    interfaces:
      - sp: spa
        ipPort: spa_fsn_4
        ipAddress: 15.67.519.21
        netmask: 255.255.255.0
        gateway: 15.67.519.254
        state: present

- name: Remove replication interface
  replication_interface:
    unispherehost: 10.52.20.56
    username: <user>
    password: <password>
    validate_certs: true
    interfaces:
      - sp: spa
        ipPort: spb_fsn_4
        state: absent

- name: Modify replication interface
  replication_interface:
    unispherehost: 10.52.20.56
    username: <user>
    password: <password>
    validate_certs: true
    interfaces:
      - sp: spa
        ipPort: spa_fsn_4
        netmask: <new_netmask>
"""

RETURN = r"""
ok: [MCSTOUNITDPE01 -> localhost] => {
    "changed": false,
    "invocation": {
        "module_args": {
            "interfaces": [
                {
                    "gateway": "192.168.100.254",
                    "ip_address": "192.168.100.10",
                    "ip_port": "spa_fsn_0",
                    "netmask": "255.255.255.0",
                    "sp": "spa",
                    "state": "present",
                    "v6_prefix_length": null,
                    "vlan_id": 100
                },
                {
                    "gateway": "192.168.101.254",
                    "ip_address": "192.168.101.10",
                    "ip_port": "spb_fsn_0",
                    "netmask": "255.255.255.0",
                    "sp": "spb",
                    "state": "present",
                    "v6_prefix_length": null,
                    "vlan_id": 101
                }
            ],
            "password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
            "state": "present",
            "unispherehost": "192.168.1.100",
            "username": "admin",
            "validate_certs": false
        }
    },
    "replications_added": 0,
    "replications_changed": 0,
    "replications_removed": 0,
    "result": {
        "spa_fsn_0": {
            "id": "if_1001",
            "ip_address": "192.168.100.10",
            "ip_port": "spa_fsn_0",
            "ip_protocol_version": "IPv4",
            "mac_address": "00:60:48:AA:BB:CC",
            "name": "storage_spa_vlan100",
            "netmask": "255.255.255.0",
            "vlan_id": 100
        },
        "spb_fsn_0": {
            "id": "if_1002",
            "ip_address": "192.168.101.10",
            "ip_port": "spb_fsn_0",
            "ip_protocol_version": "IPv4",
            "mac_address": "00:60:48:DD:EE:FF",
            "name": "storage_spb_vlan101",
            "netmask": "255.255.255.0",
            "vlan_id": 101
        }
    }
}
"""

from ansible.module_utils.basic import AnsibleModule

try:
    from storops import UnitySystem
    HAS_STOROPS = True
except ImportError:
    HAS_STOROPS = False


class UnityReplicationInterface():
    def __init__(self):
        self.module_params = get_replication_interface_parameters()
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )

        if not HAS_STOROPS:
            self.module.fail_json(msg="Module require the python storops library")

        self.unity_system = UnitySystem(
            self.module.params['unispherehost'],
            username = self.module.params['username'],
            password = self.module.params['password'],
            verify = self.module.params['validate_certs']
        )
        # This allow us to get the hidden children class with useful methode
        self.unity_client = self.unity_system._cli

    def get_current_interfaces(self):
        """
        Return a dict of remote system currently on the Unity, the dict is keyed by the remote management_address
        """
        curr = {}

        for interface in self.unity_system.get_replication_interface():
            curr[str(interface.ip_port.id)] = interface

        return curr

    def diff(self, curr, wanted):
        """
        Compare current remote system connections against the wanted state.

        Returns three lists:
            to_add:    wanted items with no matching current connection
            to_remove: current items (live objects) not present (or state=absent) in wanted
            to_modify: list of dicts {"current": <UnityRemoteSystem>, "wanted": <dict>}
                       for connections that exist on both sides but differ
        """
        to_add = []
        to_remove = []
        to_modify = []

        wanted_by_ip_port = {item['ip_port']: item for item in wanted}

        for ip_port, current_item in curr.items():
            wanted_item = wanted_by_ip_port.get(ip_port)
            if wanted_item is None:
                continue
            if wanted_item.get('state', 'present') == 'absent':
                to_remove.append(current_item)

        for ip_port, wanted_item in wanted_by_ip_port.items():
            state = wanted_item.get('state', 'present')
            current_item = curr.get(ip_port)

            if state == 'absent':
                continue

            if current_item is None:
                to_add.append(wanted_item)
                continue

            if self._interface_differs(current_item, wanted_item):
                to_modify.append({"current": current_item, "wanted": wanted_item})

        return to_add, to_remove, to_modify

    @staticmethod
    def _interface_differs(current_item, wanted_item):
        if str(current_item.ip_address) != str(wanted_item['ip_address']):
            return True
        if str(current_item.netmask) != str(wanted_item['netmask']):
            return True
        if int(current_item.vlan_id) != int(wanted_item['vlan_id']):
            return True
        if str(current_item.gateway) != str(wanted_item['gateway']):
            return True

        return False


    @staticmethod
    def _serialize_interface(interface):
        return {
            "id": str(interface.id),
            "name": str(interface.name),
            "ip_port": str(interface.ip_port.id),
            "ip_address": str(interface.ip_address),
            "ip_protocol_version": str(interface.ip_protocol_version.name),
            "mac_address": str(interface.mac_address),
            "netmask": str(interface.netmask),
            "vlan_id": int(interface.vlan_id),
        }

    def add(self, item):
        kwargs = dict(
            sp={'id': item['sp']},
            ip_port={'id': item['ip_port']},
            ip_address=item['ip_address'],
            netmask=item.get('netmask'),
            gateway=item.get('gateway'),
        )
        if item.get('vlan_id') is not None:
            kwargs['vlan_id'] = item['vlan_id']
        if item.get('v6_prefix_length') is not None:
            kwargs['v6_prefix_length'] = item['v6_prefix_length']
        try:
            self.unity_system.create_replication_interface(**kwargs)
        except Exception as e:
            self.module.fail_json(msg=f"Error during creation of {item['ip_port']}: {e}")

    def modify(self, item):
        current_item = item['current']
        wanted_item = item['wanted']
        replication_interface_id = current_item.id

        changes = dict(
            ipAddress = wanted_item['ip_address'],
        )
        if wanted_item.get('netmask') is not None:
            changes['netmask'] = wanted_item['netmask']
        if wanted_item.get('gateway') is not None:
            changes['gateway'] = wanted_item['gateway']
        if wanted_item.get('vlan_id') is not None:
            changes['vlanId'] = wanted_item['vlan_id']
        if wanted_item.get('v6_prefix_length') is not None:
            changes['v6PrefixLength'] = wanted_item['v6_prefix_length']

        try:
            res = self.unity_client.modify('replicationInterface', replication_interface_id, **changes)
            if isinstance(res, dict) and 'error' in res:
                self.module.fail_json(
                    msg=f"Error during modification of {replication_interface_id}: {res['error']}",
                    result=res,
                )
            self.unity_client.action('replicationInterface', replication_interface_id, 'verify')
            return res
        except Exception as e:
            self.module.fail_json(msg=f"Error during modification of {replication_interface_id}: {e}")


    def remove(self, item):
        id = item.id
        try:
            return self.unity_client.delete('replicationInterface', id)
        except Exception as e:
            self.module.fail_json(msg=f"Error during deletion of {id}: {e}")

    def run(self):
        """
        Perfome the ansible self.module diff and changes.
        """
        unity_curr_state = self.get_current_interfaces()
        unity_wanted_state = self.module.params['interfaces']

        to_add, to_remove, to_modify = self.diff(unity_curr_state, unity_wanted_state)

        changed = bool(to_add or to_remove or to_modify)

        if (not self.module.check_mode) and changed:
            for item in to_add:
                self.add(item)
            for item in to_modify:
                self.modify(item)
            for item in to_remove:
                self.remove(item)

        unity_result_state = {}

        for key, value in self.get_current_interfaces().items():
            unity_result_state[key] = self._serialize_interface(value)

        self.module.exit_json(changed=changed, replications_added=len(to_add), replications_removed=len(to_remove), replications_changed=len(to_modify), result=unity_result_state)

def get_replication_interface_parameters():
    return dict(
        unispherehost=dict(required=True, type='str'),
        username=dict(required=True, type='str'),
        password=dict(required=True, type='str', no_log=True),
        validate_certs=dict(required=False, type='bool', default=False),
        state=dict(required=False, type='str', default='present', choices=['present', 'absent']),
        interfaces=dict(
            required=True, type='list', elements='dict',
            options=dict(
                sp=dict(required=True, type='str'),
                ip_port=dict(required=True, type='str', ),
                ip_address=dict(required=True, type='str'),
                netmask=dict(required=False, type='str', ),
                state=dict(required=False, type='str', default='present', choices=['present', 'absent']),
                vlan_id=dict(required=False, type='int'),
                gateway=dict(required=False, type='str'),
                v6_prefix_length=dict(required=False, type='int'),
            ),
        ),
    )

def main():
    obj = UnityReplicationInterface()
    obj.run()

if __name__ == "__main__":
    main()
