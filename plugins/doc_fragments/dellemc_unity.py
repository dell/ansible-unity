# -*- coding: utf-8 -*-
# Copyright: (c) 2020, DellEMC.
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r'''
options:
  - See respective platform section for more details
requirements:
  - See respective platform section for more details
notes:
  - Ansible modules are available for DellEMC Unity Storage Platform
'''

    # Documentation fragment for Unity (unity)
    UNITY = r'''
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
        verifycert:
            type: bool
            default: True
            required: False
            description:
            - Boolean variable to specify whether or not to validate SSL
              certificate.
            - True - Indicates that the SSL certificate should be verified.
            - False - Indicates that the SSL certificate should not be
              verified.
        port:
            description:
            - Port number through which communication happens with Unity
              management server.
            type: int
            required: False
            default: 443
    requirements:
      - A Dell EMC Unity Storage device.
      - Ansible 2.10, 2.11 or 2.12.
    notes:
      - The modules present in this collection named as 'dellemc.unity'
        are built to support the Dell EMC Unity storage platform.
'''
