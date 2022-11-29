# Copyright: (c) 2020, Dell Technologies.
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    # Documentation fragment for Unity (unity)
    DOCUMENTATION = r'''
    options:
        unispherehost:
            required: True
            description:
            - IP or FQDN of the Unity management server.
            type: str
        username:
            type: str
            required: True
            description:
            - The username of the Unity management server.
        password:
            type: str
            required: True
            description:
            - The password of the Unity management server.
        validate_certs:
            type: bool
            default: True
            aliases:
            - verifycert
            description:
            - Boolean variable to specify whether or not to validate SSL
              certificate.
            - C(true) - Indicates that the SSL certificate should be verified.
            - C(false) - Indicates that the SSL certificate should not be
              verified.
        port:
            description:
            - Port number through which communication happens with Unity
              management server.
            type: int
            default: 443
    requirements:
      - A Dell Unity Storage device version 5.1 or later.
      - Ansible-core 2.11 or later.
      - Python 3.8, 3.9 or 3.10.
      - Storops Python SDK 1.2.11.
    notes:
      - The modules present in this collection named as 'dellemc.unity'
        are built to support the Dell Unity storage platform.
'''
