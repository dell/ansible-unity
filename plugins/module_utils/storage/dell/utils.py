# Copyright: (c) 2020, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import logging
from ansible_collections.dellemc.unity.plugins.module_utils.storage.dell.logging_handler \
    import CustomRotatingFileHandler
import math
from decimal import Decimal
import re

try:
    import urllib3

    urllib3.disable_warnings()
    HAS_URLLIB3 = True
except ImportError:
    HAS_URLLIB3 = False

"""import storops lib"""
try:
    from storops import UnitySystem
    from storops.unity.client import UnityClient
    from storops.unity.resource import host, cg, snap_schedule, snap, \
        cifs_share, nas_server
    from storops.unity.resource.lun import UnityLun
    from storops.unity.resource.pool import UnityPool, UnityPoolList, RaidGroupParameter
    from storops.unity.resource.filesystem import UnityFileSystem, \
        UnityFileSystemList
    from storops.unity.resource.nas_server import UnityNasServer
    from storops.unity.resource.nfs_share import UnityNfsShare, \
        UnityNfsShareList
    from storops.unity.resource.snap_schedule import UnitySnapScheduleList, \
        UnitySnapSchedule
    from storops.unity.resource.replication_session import UnityReplicationSession
    from storops.unity.enums import HostInitiatorTypeEnum, \
        TieringPolicyEnum, ScheduleTypeEnum, DayOfWeekEnum, NodeEnum, \
        HostLUNAccessEnum, HostTypeEnum, AccessPolicyEnum, \
        FilesystemTypeEnum, FSSupportedProtocolEnum, FSFormatEnum, \
        NFSTypeEnum, NFSShareDefaultAccessEnum, NFSShareSecurityEnum, \
        FilesystemSnapAccessTypeEnum, FSLockingPolicyEnum, \
        CifsShareOfflineAvailabilityEnum, NasServerUnixDirectoryServiceEnum, \
        KdcTypeEnum, NodeEnum, FileInterfaceRoleEnum
    from storops.exception import UnityResourceNotFoundError, \
        StoropsConnectTimeoutError, UnityNfsShareNameExistedError
    from storops.connection.exceptions import HttpError, HTTPClientError
    from storops.unity.resource.user_quota import UnityUserQuota, \
        UnityUserQuotaList
    from storops.unity.resource.tree_quota import UnityTreeQuota, \
        UnityTreeQuotaList
    from storops.unity.resource.quota_config import UnityQuotaConfig, \
        UnityQuotaConfigList
    from storops.unity.resource.storage_resource import UnityStorageResource
    from storops.unity.enums import QuotaPolicyEnum, RaidTypeEnum, \
        RaidStripeWidthEnum, StoragePoolTypeEnum
    from storops.unity.resource.disk import UnityDisk, \
        UnityDiskList, UnityDiskGroup, UnityDiskGroupList
    from storops.unity.resource.cifs_server import UnityCifsServer
    from storops.unity.resource.nfs_server import UnityNfsServer
    from storops.unity.resource.interface import UnityFileInterface
    HAS_UNITY_SDK = True
except ImportError:
    HAS_UNITY_SDK = False

try:
    from pkg_resources import parse_version
    import pkg_resources

    PKG_RSRC_IMPORTED = True
except ImportError:
    PKG_RSRC_IMPORTED = False


'''Check required libraries'''


def get_unity_sdk():
    return HAS_UNITY_SDK


'''
This method provides common access parameters required for the ansible
modules on Unity StorageSystem
options:
  management_host:
    description:
    - IP/FQDN of Unity unisphere host.
    required: true
  port:
    description:
    - port at which Unity unisphere api is listening.
    required: false
  verifycert:
    description:
    - Whether or not to verify client SSL certificate.
    required: false
  username:
    description:
    - User name to access on to unity unisphere host.
    required: true
  password:
    description:
    - password to access on to unity unispherehost
    required: true
'''


def get_unity_management_host_parameters():
    return dict(
        unispherehost=dict(type='str', required=True, no_log=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        verifycert=dict(type='bool', required=False,
                        default=True),
        port=dict(type='int', required=False, default=443, no_log=True)
    )


'''
This method is to establish connection with Unity array using storops SDK.
parameters:
  module_params - Ansible module parameters which contain below unity
                  unisphere details to establish connection.
                - unispherehost: IP/FQDN of unity unisphere host.
                - port: port at which Unity unisphere api is hosted.
                - verifycert: Boolean value to inform system whether to
                  verify client certificate or not.
                - username:  User name to access on to unity management host
                - password: Password to access unity management host
  application_type - Specifies details of the calling application
returns connection object to access Unity Unisphere using storops SDK
'''


def get_unity_unisphere_connection(module_params, application_type=None):

    if HAS_UNITY_SDK:
        conn = UnitySystem(host=module_params['unispherehost'],
                           port=module_params['port'],
                           verify=module_params['verifycert'],
                           username=module_params['username'],
                           password=module_params['password'],
                           application_type=application_type)
        return conn


'''
This method checks if supported version of storops SDK installed.
'''


def storops_version_check():
    try:
        supported_version = False

        if not HAS_URLLIB3:
            unsupported_version_message = "Unable to import Urllib3," \
                                          " please install necessary package"
        elif PKG_RSRC_IMPORTED is False:
            unsupported_version_message = "Unable to import " \
                                          "'pkg_resources', please install" \
                                          " the required package"
        else:
            min_ver = '1.2.10'
            curr_version = pkg_resources.require("storops")[0].version
            unsupported_version_message = "Storops {0} is not supported " \
                                          "by this module. Minimum " \
                                          "supported version is :" \
                                          "{1}".format(curr_version, min_ver)

            supported_version = parse_version(curr_version) >= parse_version(
                min_ver)

        storops_version = dict(
            supported_version=supported_version,
            unsupported_version_message=unsupported_version_message)

        return storops_version

    except Exception as e:
        unsupported_version_message = "Getting Storops SDK version, failed" \
                                      " with Error {0}".format(str(e))

        storops_version = dict(
            supported_version=False,
            unsupported_version_message=unsupported_version_message)
        return storops_version


'''
This method is to initialize logger and return the logger object
parameters:
     - module_name: Name of module to be part of log message.
     - log_file_name: Name of file in which the log messages get appended.
     - log_devel: log level.
returns logger object
'''


def get_logger(module_name, log_file_name='ansible_unity.log',
               log_devel=logging.INFO):
    FORMAT = '%(asctime)-15s %(filename)s %(levelname)s : %(message)s'
    max_bytes = 5 * 1024 * 1024
    logging.basicConfig(filename=log_file_name, format=FORMAT)
    LOG = logging.getLogger(module_name)
    LOG.setLevel(log_devel)
    handler = CustomRotatingFileHandler(log_file_name,
                                        maxBytes=max_bytes,
                                        backupCount=5)
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)
    LOG.addHandler(handler)
    LOG.propagate = False
    return LOG


'''
Convert the given size to bytes
'''
KB_IN_BYTES = 1024
MB_IN_BYTES = 1024 * 1024
GB_IN_BYTES = 1024 * 1024 * 1024
TB_IN_BYTES = 1024 * 1024 * 1024 * 1024


def get_size_bytes(size, cap_units):
    if size is not None and size > 0:
        if cap_units in ('kb', 'KB'):
            return size * KB_IN_BYTES
        elif cap_units in ('mb', 'MB'):
            return size * MB_IN_BYTES
        elif cap_units in ('gb', 'GB'):
            return size * GB_IN_BYTES
        elif cap_units in ('tb', 'TB'):
            return size * TB_IN_BYTES
        else:
            return size
    else:
        return 0


'''
Convert size in byte with actual unit like KB,MB,GB,TB,PB etc.
'''


def convert_size_with_unit(size_bytes):
    if not isinstance(size_bytes, int):
        raise ValueError('This method takes Integer type argument only')
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


'''
Convert the given size to size in GB, size is restricted to 2 decimal places
'''


def get_size_in_gb(size, cap_units):
    size_in_bytes = get_size_bytes(size, cap_units)
    size = Decimal(size_in_bytes / GB_IN_BYTES)
    size_in_gb = round(size)
    return size_in_gb


'''
Check whether input string is empty
'''


def is_input_empty(item):
    if item == "" or item.isspace():
        return True
    else:
        return False


'''
Check whether size is negative
'''


def is_size_negative(size):
    if size and size < 0:
        return True
    else:
        return False


'''
Check whether the string has any special character
It allows '_' character
'''


def has_special_char(value):
    regex = re.compile(r'[@!#$%^&*()<>?/\|}{~:]')
    if regex.search(value) is None:
        return False
    else:
        return True


'''
Validate format of the FC or iSCSI initiator
'''


def is_initiator_valid(value):
    if value.startswith('iqn') or re.match(r"([A-Fa-f0-9]{2}:){15}[A-Fa-f0-9]{2}", value, re.I) is not None:
        return True
    else:
        return False


'''
Validates if ip is valid subnet mask
'''


def is_valid_netmask(netmask):
    if netmask:
        regexp = re.compile(r'^((128|192|224|240|248|252|254)\.0\.0\.0)|'
                            r'(255\.(((0|128|192|224|240|248|252|254)\.0\.0)|'
                            r'(255\.(((0|128|192|224|240|248|252|254)\.0)|'
                            r'255\.(0|128|192|224|240|248|252|254)))))$')
        if not regexp.search(netmask):
            return False
        return True
