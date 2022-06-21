# -*- coding: utf-8 -*-
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
      - A Dell Unity Storage device. Ansible 2.11, 2.12 or 2.13.
    notes:
      - The modules present in this collection named as 'dellemc.unity'
        are built to support the Dell Unity storage platform.
'''
