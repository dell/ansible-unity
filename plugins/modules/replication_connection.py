#!/usr/bin/python

"""Ansible module to configure replication connections"""


DOCUMENTATION = r"""
---
module: replication_connection
version_added: '1.0'
short_description: Configure replication connections for Unity
description:
- Configure replication connections on a Unity Unisphere host. For more information on the API go checkout the doc: https://developer.dell.com/apis/3028/versions/5.2.0/models/spec_publish.yml/paths/~1api~1types~1remoteSystem~1instances/post.
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
    force:
        description:
            - Force modify of existing connections even if no drift is detected on comparable fields.
            - Useful because the remote password cannot be read back from the array to verify it still matches, so this guarantees the remote credentials are (re)applied.
        default: false
        type: bool
    replications:
        description: List of replication connections to configure.
        required: true
        type: list
        elements: dict
        suboptions:
            remote_ip_manager:
                description: IP of the remote Unisphere management host.
                required: true
                type: str
            remote_username:
                description: Username to authenticate against the remote host.
                required: true
                type: str
            remote_password:
                description: Password to authenticate against the remote host.
                required: true
                type: str
                no_log: true
            local_username:
                description: Username to authenticate against the local host. By default use the unisphere username.
                required: false
                type: str
            local_password:
                description: Password to authenticate against the local host. By default use the unisphere password.
                required: false
                type: str
                no_log: true
            connection_type:
                description: Type of replication connection (e.g: sync, async, both, none).
                required: true
                type: str
                choices: [sync, async, both, none]
            state:
                description: Whether this replication connection should exist or not.
                type: str
                default: present
                choices: [present, absent]
"""

EXAMPLES = r"""
- name: Configure replication connection
  replication_connection:
    unispherehost: 10.52.20.56
    username: <user>
    password: <password>
    validate_certs: true
    replications:
      - remote_ip_manager: 10.52.20.57
        remote_username: <remote_user>
        remote_password: <remote_password>
        connection_type: async
        state: present

- name: Configure replication connection with special user on local
  replication_connection:
    unispherehost: 10.52.20.56
    username: <user>
    password: <password>
    validate_certs: true
    replications:
      - remote_ip_manager: 10.52.20.57
        remote_username: <remote_user>
        remote_password: <remote_password>
        local_username: <local_user>
        local_password: <local_password>
        connection_type: async
        state: present

- name: Remove replication connection
  replication_connection:
    unispherehost: 10.52.20.56
    username: <user>
    password: <password>
    validate_certs: false
    replications:
      - remote_ip_manager: 10.52.20.57
        remote_username: <remote_user>
        remote_password: <remote_password>
        connection_type: async
        state: absent

- name: Modify replication connection
  replication_connection:
    unispherehost: 10.52.20.56
    username: <user>
    password: <password>
    force: true
    replications:
      - remote_ip_manager: 10.52.20.57
        remote_username: <new_remote_user>
        remote_password: <new_remote_password>
        connection_type: sync
        state: present
"""

RETURN = r"""
changed: [Unity -> localhost] => {
    "changed": true,
    "invocation": {
        "module_args": {
            "force": false,
            "password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
            "replications": [
                {
                    "connection_type": "async",
                    "remote_ip_manager": "128.222.11.12",
                    "remote_password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
                    "remote_username": "your_user",
                    "state": "present"
                }
            ],
            "state": "present",
            "unispherehost": "128.221.10.12",
            "username": "your_user",
            "validate_certs": false
        }
    },
    "replications_added": 1,
    "replications_changed": 0,
    "replications_removed": 0,
    "result": {
        "128.222.11.12": {
            "connection_type": "async",
            "id": "RS_33",
            "local_spa_interfaces": "['128.221.255.12']",
            "local_spb_interfaces": "['128.221.256.12']",
            "management_address": "128.222.11.12",
            "model": "Unity 380",
            "name": "MCSTOUNITDPE01",
            "remote_spa_interfaces": "['128.222.255.13']",
            "remote_spb_interfaces": "['128.222.256.13']",
            "serial_number": "CRK00242108243",
            "username": "your_user"
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


class UnityReplicationConnection():
    def __init__(self):
        self.module_params = get_replication_connection_parameters()
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )

        if not HAS_STOROPS:
            self.module.fail_json(msg="Module requires the python storops library")

        self.unity_system = UnitySystem(
            self.module.params['unispherehost'],
            username = self.module.params['username'],
            password = self.module.params['password'],
            verify = self.module.params['validate_certs']
        )
        # This allow us to get the hidden children class with useful methode
        self.unity_client = self.unity_system._cli
        self.force = self.module.params['force']

    def get_current_connections(self):
        """
        Return a dict of remote systems currently on the Unity, the dict is keyed by the remote management_address
        """
        curr = {}

        for connection in self.unity_system.get_remote_system():
            curr[connection.management_address] = connection

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

        wanted_by_ip = {item['remote_ip_manager']: item for item in wanted}

        for ip, current_item in curr.items():
            wanted_item = wanted_by_ip.get(ip)
            if wanted_item is None:
                continue
            if wanted_item.get('state', 'present') == 'absent':
                to_remove.append(current_item)

        for ip, wanted_item in wanted_by_ip.items():
            state = wanted_item.get('state', 'present')
            current_item = curr.get(ip)

            if state == 'absent':
                continue

            if current_item is None:
                to_add.append(wanted_item)
                continue

            if self.force or self._connection_differs(current_item, wanted_item):
                to_modify.append({"current": current_item, "wanted": wanted_item})

        return to_add, to_remove, to_modify

    @staticmethod
    def _connection_differs(current_item, wanted_item):
        if current_item.username != wanted_item['remote_username']:
            return True

        current_type = str(current_item.connection_type.name).lower()
        wanted_type = str(wanted_item['connection_type']).lower()
        if current_type != wanted_type:
            return True

        return False

    @staticmethod
    def _serialize_connection(connection):
        return {
            "id": str(connection.id),
            "name": str(connection.name),
            "management_address": str(connection.management_address),
            "connection_type": str(connection.connection_type.name).lower(),
            "username": str(connection.username),
            "model": str(connection.model),
            "remote_spa_interfaces": str(connection.remote_spa_interfaces),
            "remote_spb_interfaces": str(connection.remote_spb_interfaces),
            "local_spa_interfaces": str(connection.local_spa_interfaces),
            "local_spb_interfaces": str(connection.local_spb_interfaces),
            "serial_number": str(connection.serial_number),
        }

    def connection_refacto(self, connection):
        match connection:
            case 'sync':
                return 0
            case 'async':
                return 1
            case 'both':
                return 2
            case 'none':
                return 3

    def add(self, item):
        default_local_user = item.get('local_username') or self.module.params['username']
        default_local_pass = item.get('local_password') or self.module.params['password']

        try:
            self.unity_system.create_remote_system(
                management_address=item['remote_ip_manager'],
                local_username= default_local_user,
                local_password=default_local_pass,
                remote_username=item['remote_username'],
                remote_password=item['remote_password'],
                connection_type=self.connection_refacto(item['connection_type'])
            )
        except Exception as e:
            self.module.fail_json(msg=f"Error during creation of {item['remote_ip_manager']}: {e}")

    def modify(self, item):
        current_item = item['current']
        wanted_item = item['wanted']
        remote_system_id = current_item.id


        changes = {
            'username': wanted_item['remote_username'],
            'password': wanted_item['remote_password'],
            'connectionType': self.connection_refacto(wanted_item['connection_type']),
        }

        try:
            res = self.unity_client.modify('remoteSystem', remote_system_id, **changes).body
            if isinstance(res, dict) and 'error' in res:
                self.module.fail_json(
                    msg=f"Error during modification of {remote_system_id}: {res['error']}",
                    result=res,
                )

            self.unity_client.action('remoteSystem', remote_system_id, 'verify')
            return res
        except Exception as e:
            self.module.fail_json(msg=f"Error during modification of {remote_system_id}: {e}")


    def remove(self, item):
        id = item.id
        try:
            return self.unity_client.delete('remoteSystem', id)
        except Exception as e:
            self.module.fail_json(msg=f"Error during deletion of {id}: {e}")

    def run(self):
        """
        Perform the ansible self.module diff and changes.
        """
        unity_curr_state = self.get_current_connections()
        unity_wanted_state = self.module.params['replications']

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

        for key, value in self.get_current_connections().items():
            if str(key) != self.module.params['unispherehost']:
                unity_result_state[key] = self._serialize_connection(value)

        self.module.exit_json(changed=changed, replications_added=len(to_add), replications_removed=len(to_remove), replications_changed=len(to_modify), result=unity_result_state)

def get_replication_connection_parameters():
    return dict(
        unispherehost=dict(required=True, type='str'),
        username=dict(required=True, type='str'),
        password=dict(required=True, type='str', no_log=True),
        validate_certs=dict(required=False, type='bool', default=False),
        state=dict(required=False, type='str', default='present', choices=['present', 'absent']),
        force=dict(required=False, type='bool', default=False),
        replications=dict(
            required=True, type='list', elements='dict',
            options=dict(
                remote_ip_manager=dict(required=True, type='str'),
                remote_username=dict(required=True, type='str'),
                remote_password=dict(required=True, type='str', no_log=True),
                local_username=dict(required=False, type='str'),
                local_password=dict(required=False, type='str', no_log=True),
                connection_type=dict(required=True, type='str', choices=['sync', 'async', 'both', 'none']),
                state=dict(required=False, type='str', default='present', choices=['present', 'absent']),
            ),
        ),
    )

def main():
    obj = UnityReplicationConnection()
    obj.run()

if __name__ == "__main__":
    main()
