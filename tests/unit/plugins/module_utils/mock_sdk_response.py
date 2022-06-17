# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Mock SDKResponse for Unit tests for Unity modules"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSDKObject:
    def __init__(self, data):
        self.skip_list = ['skip_list']
        for key, value in data.items():
            setattr(self, key, value)

    def add_to_skip_list(self, key):
        self.skip_list.append(key)

    def _get_properties(self):
        data = {}
        for attr, value in self.__dict__.items():
            if attr not in self.skip_list:
                data[attr] = value
        return data

    def get_id(self):
        return "res_0"

    def name(self):
        return "res_0"
