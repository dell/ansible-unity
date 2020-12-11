# -*- coding: utf-8 -*-
# Copyright: (c) 2020, DellEMC.

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
            choices: [True, False]
        port:
            description:
            - Port number through which communication happens with Unity
              management server.
            type: int
            required: False
            default: 443
    requirements:
      - A DellEMC Unity Storage device.
      - Ansible 2.9 or higher.
    notes:
      - The modules prefixed with dellemc_unity are built to support the
        DellEMC Unity storage platform.
'''
