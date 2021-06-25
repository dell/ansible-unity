# Ansible Modules for Dell EMC Unity
## Product Guide 1.2.0
© 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

--------------
## Contents
*   [NFS Module](#nfs-module)
    *   [Synopsis](#synopsis)
    *   [Parameters](#parameters)
    *   [Examples](#examples)
    *   [Return Values](#return-values)
    *   [Authors](#authors)
*   [Volume Module](#volume-module)
    *   [Synopsis](#synopsis-1)
    *   [Parameters](#parameters-1)
    *   [Examples](#examples-1)
    *   [Return Values](#return-values-1)
    *   [Authors](#authors-1)
*   [NAS Server Module](#nas-server-module)
    *   [Synopsis](#synopsis-2)
    *   [Parameters](#parameters-2)
    *   [Examples](#examples-2)
    *   [Return Values](#return-values-2)
    *   [Authors](#authors-2)
*   [Quota Tree Module](#quota-tree-module)
    *   [Synopsis](#synopsis-3)
    *   [Parameters](#parameters-3)
    *   [Examples](#examples-3)
    *   [Return Values](#return-values-3)
    *   [Authors](#authors-3)
*   [File System Module](#file-system-module)
    *   [Synopsis](#synopsis-4)
    *   [Parameters](#parameters-4)
    *   [Notes](#notes-4)
    *   [Examples](#examples-4)
    *   [Return Values](#return-values-4)
    *   [Authors](#authors-4)
*   [Storage Pool Module](#storage-pool-module)
    *   [Synopsis](#synopsis-5)
    *   [Parameters](#parameters-5)
    *   [Notes](#notes-5)
    *   [Examples](#examples-5)
    *   [Return Values](#return-values-5)
    *   [Authors](#authors-5)
*   [Gatherfacts Module](#gatherfacts-module)
    *   [Synopsis](#synopsis-6)
    *   [Parameters](#parameters-6)
    *   [Examples](#examples-6)
    *   [Return Values](#return-values-6)
    *   [Authors](#authors-6)
*   [User Quota Module](#user-quota-module)
    *   [Synopsis](#synopsis-7)
    *   [Parameters](#parameters-7)
    *   [Examples](#examples-7)
    *   [Return Values](#return-values-7)
    *   [Authors](#authors-7)
*   [Filesystem Snapshot Module](#filesystem-snapshot-module)
    *   [Synopsis](#synopsis-8)
    *   [Parameters](#parameters-8)
    *   [Notes](#notes-8)
    *   [Examples](#examples-8)
    *   [Return Values](#return-values-8)
    *   [Authors](#authors-8)
*   [Snapshot Module](#snapshot-module)
    *   [Synopsis](#synopsis-9)
    *   [Parameters](#parameters-9)
    *   [Examples](#examples-9)
    *   [Return Values](#return-values-9)
    *   [Authors](#authors-9)
*   [SMB Share Module](#smb-share-module)
    *   [Synopsis](#synopsis-10)
    *   [Parameters](#parameters-10)
    *   [Notes](#notes-10)
    *   [Examples](#examples-10)
    *   [Return Values](#return-values-10)
    *   [Authors](#authors-10)
*   [Host Module](#host-module)
    *   [Synopsis](#synopsis-11)
    *   [Parameters](#parameters-11)
    *   [Examples](#examples-11)
    *   [Return Values](#return-values-11)
    *   [Authors](#authors-11)
*   [Consistency Group Module](#consistency-group-module)
    *   [Synopsis](#synopsis-12)
    *   [Parameters](#parameters-12)
    *   [Examples](#examples-12)
    *   [Return Values](#return-values-12)
    *   [Authors](#authors-12)
*   [Snapshot Schedule Module](#snapshot-schedule-module)
    *   [Synopsis](#synopsis-13)
    *   [Parameters](#parameters-13)
    *   [Notes](#notes-13)
    *   [Examples](#examples-13)
    *   [Return Values](#return-values-13)
    *   [Authors](#authors-13)

--------------

# NFS Module

Manage NFS export on Unity storage system

### Synopsis
 Managing NFS export on Unity storage system includes- Create new NFS export, Modify NFS export attributes, Display NFS export details, Delete NFS export

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=2 > nfs_export_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the nfs export.  <br> Mandatory for create operation.  <br> Specify either nfs_export_name or nfs_export_id(but not both) for any operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > nfs_export_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the nfs export.  <br> This is a unique ID generated by Unity storage system. </td>
        </tr>
                    <tr>
            <td colspan=2 > filesystem_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the filesystem for which NFS export will be created.  <br> Either filesystem or snapshot is required for creation of the NFS.  <br> If filesystem name is specified, then nas_server is required to uniquely identify the filesystem  <br> If filesystem parameter is provided, then snapshot cannot be specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > filesystem_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the filesystem  <br> This is a unique ID generated by Unity storage system. </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the snapshot for which NFS export will be created.  <br> Either filesystem or snapshot is required for creation of the NFS export.  <br> If snapshot parameter is provided, then filesystem cannot be specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the snapshot.  <br> This is a unique ID generated by Unity storage system. </td>
        </tr>
                    <tr>
            <td colspan=2 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the NAS server on which filesystem will be hosted. </td>
        </tr>
                    <tr>
            <td colspan=2 > nas_server_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the NAS server on which filesystem will be hosted. </td>
        </tr>
                    <tr>
            <td colspan=2 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Local path to export relative to the NAS server root.  <br> With NFS, each export of a file_system or file_snap must have a unique local path.  <br> Mandatory while creating NFS export. </td>
        </tr>
                    <tr>
            <td colspan=2 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description of the NFS export.  <br> Optional parameter when creating a NFS export.  <br> To modify description, pass the new value in description field.  <br> To remove description, pass the empty value in description field. </td>
        </tr>
                    <tr>
            <td colspan=2 > host_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-export</li>  <li>absent-in-export</li> </ul></td>
            <td> <br> Define whether the hosts can access the NFS export.  <br> Required when adding or removing access of hosts from the export. </td>
        </tr>
                    <tr>
            <td colspan=2 > anonymous_uid</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies the user ID of the anonymous account.  <br> If not specified at the time of creation, it will be set to 4294967294. </td>
        </tr>
                    <tr>
            <td colspan=2 > anonymous_gid</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies the group ID of the anonymous account.  <br> If not specified at the time of creation, it will be set to 4294967294. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> State variable to determine whether NFS export will exist or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > default_access</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NO_ACCESS</li>  <li>READ_ONLY</li>  <li>READ_WRITE</li>  <li>ROOT</li>  <li>READ_ONLY_ROOT</li> </ul></td>
            <td> <br> Default access level for all hosts that can access the NFS export.  <br> For hosts that need different access than the default, they can be configured by adding to the list.  <br> If default_access is not mentioned during creation, then NFS export will be created with NO_ACCESS. </td>
        </tr>
                    <tr>
            <td colspan=2 > min_security</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>SYS</li>  <li>KERBEROS</li>  <li>KERBEROS_WITH_INTEGRITY</li>  <li>KERBEROS_WITH_ENCRYPTION</li> </ul></td>
            <td> <br> NFS enforced security type for users accessing a NFS export.  <br> If not specified at the time of creation, it will be set to SYS. </td>
        </tr>
                    <tr>
            <td colspan=2 > no_access_hosts</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with no access to the NFS export.  <br> List of dictionaries. Each dictionary will have any of the keys from host_name, host_id,  and ip_address. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_name </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Name of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_id </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> ID of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > ip_address </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> IP address of the host.  </td>
            </tr>
                            <tr>
            <td colspan=2 > read_only_hosts</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read-only access to the NFS export.  <br> List of dictionaries. Each dictionary will have any of the keys from host_name, host_id, and ip_address </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_name </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Name of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_id </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> ID of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > ip_address </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> IP address of the host.  </td>
            </tr>
                            <tr>
            <td colspan=2 > read_only_root_hosts</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read-only for root user access to the NFS export.  <br> List of dictionaries. Each dictionary will have any of the keys from host_name, host_id, and ip_address </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_name </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Name of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_id </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> ID of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > ip_address </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> IP address of the host.  </td>
            </tr>
                            <tr>
            <td colspan=2 > read_write_hosts</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read and write access to the NFS export.  <br> List of dictionaries. Each dictionary will have any of the keys from host_name, host_id, and ip_address. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_name </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Name of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_id </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> ID of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > ip_address </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> IP address of the host.  </td>
            </tr>
                            <tr>
            <td colspan=2 > read_write_root_hosts</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hosts with read and write for root user access to the NFS export.  <br> List of dictionaries. Each dictionary will have any of the keys from host_name, host_id, and ip_address. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_name </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> Name of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_id </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> ID of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > ip_address </td>
                <td> str  </td>
                <td> False </td>
                <td></td>
                <td></td>
                <td>  <br> IP address of the host.  </td>
            </tr>
                            <tr>
            <td colspan=2 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create nfs export from filesystem
  dellemc_unity_nfs:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    nfs_export_name: "ansible_nfs_from_fs"
    path: '/'
    filesystem_id: "fs_377"
    state: "present"

- name: Create nfs export from snapshot
  dellemc_unity_nfs:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    nfs_export_name: "ansible_nfs_from_snap"
    path: '/'
    snapshot_name: "ansible_fs_snap"
    state: "present"

- name: Modify nfs export
  dellemc_unity_nfs:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    nfs_export_name: "ansible_nfs_from_fs"
    nas_server_id: "nas_3"
    description: ""
    default_access: "READ_ONLY_ROOT"
    anonymous_gid: 4294967290
    anonymous_uid: 4294967290
    state: "present"

- name: Add host in nfs export
  dellemc_unity_nfs:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    nfs_export_name: "ansible_nfs_from_fs"
    filesystem_id: "fs_377"
    no_access_hosts:
      - host_id: "Host_1"
    read_only_hosts:
      - host_id: "Host_2"
    read_only_root_hosts:
      - host_name: "host_name1"
    read_write_hosts:
      - host_name: "host_name2"
    read_write_root_hosts:
      - ip_address: "1.1.1.1"
    host_state: "present-in-export"
    state: "present"

- name: Remove host in nfs export
  dellemc_unity_nfs:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    nfs_export_name: "ansible_nfs_from_fs"
    filesystem_id: "fs_377"
    no_access_hosts:
      - host_id: "Host_1"
    read_only_hosts:
      - host_id: "Host_2"
    read_only_root_hosts:
      - host_name: "host_name1"
    read_write_hosts:
      - host_name: "host_name2"
    read_write_root_hosts:
      - ip_address: "1.1.1.1"
    host_state: "absent-in-export"
    state: "present"

- name: Get nfs details
  dellemc_unity_nfs:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    nfs_export_id: "NFSShare_291"
    state: "present"

- name: Delete nfs export by nfs name
  dellemc_unity_nfs:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    nfs_export_name: "ansible_nfs_name"
    nas_server_name: "ansible_nas_name"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=6>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=6 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=6 > nfs_share_details </td>
            <td>  complex </td>
            <td> When nfs export exists. </td>
            <td> Details of the nfs export. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > anonymous_gid </td>
                <td> int </td>
                <td>success</td>
                <td> Group ID of the anonymous account </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > anonymous_uid </td>
                <td> int </td>
                <td>success</td>
                <td> User ID of the anonymous account </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > default_access </td>
                <td> str </td>
                <td>success</td>
                <td> Default access level for all hosts that can access export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the nfs export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > export_paths </td>
                <td> list </td>
                <td>success</td>
                <td> Export paths that can be used to mount and access export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > filesystem </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of the filesystem on which nfs export is present </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > UnityFileSystem </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> filesystem details </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> ID of the filesystem </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > name </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Name of the filesystem </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the nfs export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > min_security </td>
                <td> str </td>
                <td>success</td>
                <td> NFS enforced security type for users accessing an export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the nfs export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > nas_server </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of the nas server </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > UnityNasServer </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> NAS server details </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> ID of the nas server </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > name </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Name of the nas server </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > no_access_hosts_string </td>
                <td> str </td>
                <td>success</td>
                <td> Hosts with no access to the nfs export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > read_only_hosts_string </td>
                <td> str </td>
                <td>success</td>
                <td> Hosts with read-only access to the nfs export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > read_only_root_hosts_string </td>
                <td> str </td>
                <td>success</td>
                <td> Hosts with read-only for root user access to the nfs export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > read_write_hosts_string </td>
                <td> str </td>
                <td>success</td>
                <td> Hosts with read and write access to the nfs export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > read_write_root_hosts_string </td>
                <td> str </td>
                <td>success</td>
                <td> Hosts with read and write for root user access to export </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > type </td>
                <td> str </td>
                <td>success</td>
                <td> NFS export type. i.e. filesystem or snapshot </td>
            </tr>
                                        </table>

### Authors
* Vivek Soni (@v-soni11) <ansible.team@dell.com>

--------------------------------
# Volume Module

Manage volume on Unity storage system

### Synopsis
 Managing volume on Unity storage system includes- Create new volume, Modify volume attributes, Map Volume to host, Unmap volume to host, Display volume details, Delete volume

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=2 > vol_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the volume. Mandatory only for create operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > vol_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The id of the volume.  <br> It can be used only for get, modify, map/unmap host, or delete operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > pool_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is the name of the pool where the volume will be created.  <br> Either the pool_name or pool_id must be provided to create a new volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > pool_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is the id of the pool where the volume will be created.  <br> Either the pool_name or pool_id must be provided to create a new volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > size</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The size of the volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> The unit of the volume size. It defaults to 'GB', if not specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description about the volume.  <br> Description can be removed by passing empty string (""). </td>
        </tr>
                    <tr>
            <td colspan=2 > snap_schedule</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Snapshot schedule assigned to the volume.  <br> Add/Remove/Modify the snapshot schedule for the volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > compression</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Boolean variable , specifies whether or not to enable compression. Compression is supported only for thin volumes </td>
        </tr>
                    <tr>
            <td colspan=2 > is_thin</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td></td>
            <td> <br> Boolean variable , specifies whether or not it's a thin volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > sp</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>SPA</li>  <li>SPB</li> </ul></td>
            <td> <br> Storage Processor for this volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > io_limit_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> IO limit policy associated with this volume. Once it's set, it cannot be removed through ansible module but it can be changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > host_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the host to be mapped/unmapped with this volume.  <br> Either host_name or host_id can be specified in one task along with mapping_state. </td>
        </tr>
                    <tr>
            <td colspan=2 > host_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the host to be mapped/unmapped with this volume.  <br> Either host_name or host_id can be specified in one task along with mapping_state. </td>
        </tr>
                    <tr>
            <td colspan=2 > hlu</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Host Lun Unit to be mapped/unmapped with this volume.  <br> It's an optional parameter, hlu can be specified along with host_name or host_id and mapping_state.  <br> If hlu is not specified, unity will choose it automatically. The maximum value supported is 255. </td>
        </tr>
                    <tr>
            <td colspan=2 > mapping_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>mapped</li>  <li>unmapped</li> </ul></td>
            <td> <br> State of host access for volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > new_vol_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the volume for rename operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > tiering_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>AUTOTIER_HIGH</li>  <li>AUTOTIER</li>  <li>HIGHEST</li>  <li>LOWEST</li> </ul></td>
            <td> <br> Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> State variable to determine whether volume will exist or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > hosts</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of hosts for mapping to a volume </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_name </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Name of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_id </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> ID of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hlu </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Host Lun Unit to be mapped/unmapped with this volume.  <br> It's an optional parameter, hlu can be specified along with host_name or host_id and mapping_state.  <br> If hlu is not specified, unity will choose it automatically. The maximum value supported is 255.  </td>
            </tr>
                            <tr>
            <td colspan=2 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create Volume
  dellemc_unity_volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    vol_name: "{{vol_name}}"
    description: "{{description}}"
    pool_name: "{{pool}}"
    size: 2
    cap_unit: "{{cap_GB}}"
    state: "{{state_present}}"

- name: Expand Volume by volume id
  dellemc_unity_volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    vol_id: "{{vol_id}}"
    size: 5
    cap_unit: "{{cap_GB}}"
    state: "{{state_present}}"

- name: Modify Volume, map host by host_name
  dellemc_unity_volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    vol_name: "{{vol_name}}"
    host_name: "{{host_name}}"
    hlu: 5
    mapping_state: "{{state_mapped}}"
    state: "{{state_present}}"

- name: Modify Volume, unmap host mapping by host_name
  dellemc_unity_volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    vol_name: "{{vol_name}}"
    host_name: "{{host_name}}"
    mapping_state: "{{state_unmapped}}"
    state: "{{state_present}}"

- name: Map multiple hosts to a Volume
  dellemc_unity_volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    vol_id: "{{vol_id}}"
    hosts:
        - host_name: "10.226.198.248"
          hlu: 1
        - host_id: "Host_929"
          hlu: 2
    mapping_state: "mapped"
    state: "present"

- name: Modify Volume attributes
  dellemc_unity_volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    vol_name: "{{vol_name}}"
    new_vol_name: "{{new_vol_name}}"
    tiering_policy: "AUTOTIER"
    compression: True
    state: "{{state_present}}"

- name: Delete Volume by vol name
  dellemc_unity_volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    vol_name: "{{vol_name}}"
    state: "{{state_absent}}"

- name: Delete Volume by vol id
  dellemc_unity_volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    vol_id: "{{vol_id}}"
    state: "{{state_absent}}"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > volume_details </td>
            <td>  complex </td>
            <td> When volume exists </td>
            <td> Details of the volume </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > current_sp </td>
                <td> str </td>
                <td>success</td>
                <td> Current storage processor for this volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_access </td>
                <td> list </td>
                <td>success</td>
                <td> Host mapped to this volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system generated ID given to the volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > io_limit_policy </td>
                <td> dict </td>
                <td>success</td>
                <td> IO limit policy associated with this volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_data_reduction_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether or not compression enabled on this volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_thin_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether thin provisioning is enabled for this volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > pool </td>
                <td> dict </td>
                <td>success</td>
                <td> The pool in which this volume is allocated. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size_total_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Size of the volume with actual unit. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snap_schedule </td>
                <td> dict </td>
                <td>success</td>
                <td> Snapshot schedule applied to this volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > tiering_policy </td>
                <td> str </td>
                <td>success</td>
                <td> Tiering policy applied to this volume </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > wwn </td>
                <td> str </td>
                <td>success</td>
                <td> The world wide name of this volume </td>
            </tr>
                                        </table>

### Authors
* Arindam Datta (@arindam-emc) <ansible.team@dell.com>

--------------------------------
# NAS Server Module

Manage NAS servers on Unity storage system

### Synopsis
 Managing NAS servers on Unity storage system includes get, modification to the NAS servers.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > nas_server_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the NAS server.  <br> nas_server_name and nas_server_id are mutually exclusive parameters.  <br> Either one is required to perform the task. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The Name of the NAS server.  <br> nas_server_name and nas_server_id are mutually exclusive parameters.  <br> Either one  is required to perform the task. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of the NAS server.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_replication_destination</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> It specifies whether the NAS server is a replication destination.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_backup_only</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> It specifies whether the NAS server is used as backup only.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_multiprotocol_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This parameter indicates whether multiprotocol sharing mode is enabled.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > allow_unmapped_user</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This flag is used to mandatorily disable access in case of any user mapping failure.  <br> If true, then enable access in case of any user mapping failure.  <br> If false, then disable access in case of any user mapping failure.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > default_windows_user</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Default windows user name used for granting access in the case of Unix to Windows user mapping failure.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > default_unix_user</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Default Unix user name used for granting access in the case of Windows to Unix user mapping failure.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > enable_windows_to_unix_username_mapping</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This parameter indicates whether a Unix to/from Windows user name mapping is enabled.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_packet_reflect_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> If the packet has to be reflected, then this parameter has to be set to True.  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > current_unix_directory_service</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NONE</li>  <li>NIS</li>  <li>LOCAL</li>  <li>LDAP</li>  <li>LOCAL_THEN_NIS</li>  <li>LOCAL_THEN_LDAP</li> </ul></td>
            <td> <br> This is the directory service used for querying identity information for UNIX (such as UIDs, GIDs, net groups).  <br> It can be mentioned during modification of the NAS server. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> Define the state of NAS server on the array.  <br> present indicates that NAS server should exist on the system after the task is executed.  <br> Right now deletion of NAS server is not supported. Hence, if state is set to absent for any existing NAS server then error will be thrown.  <br> For any non-existing NAS server, if state is set to absent then it will return None. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
    - name: Get Details of NAS Server
      dellemc_unity_nasserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        verifycert: "{{verifycert}}"
        nas_server_name: "{{nas_server_name}}"
        state: "present"

    - name: Modify Details of NAS Server
      dellemc_unity_nasserver:
        unispherehost: "{{unispherehost}}"
        username: "{{username}}"
        password: "{{password}}"
        verifycert: "{{verifycert}}"
        nas_server_name: "{{nas_server_name}}"
        nas_server_new_name: "updated_sample_nas_server"
        is_replication_destination: False
        is_backup_only: False
        is_multiprotocol_enabled: True
        allow_unmapped_user: True
        default_unix_user: "default_unix_sample_user"
        default_windows_user: "default_windows_sample_user"
        enable_windows_to_unix_username_mapping: True
        current_unix_directory_service: "LDAP"
        is_packet_reflect_enabled: True
        state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > nas_server_details </td>
            <td>  complex </td>
            <td> When NAS server exists. </td>
            <td> The NAS server details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > allow_unmapped_user </td>
                <td> bool </td>
                <td>success</td>
                <td> enable/disable access status in case of any user mapping failure </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > current_unix_directory_service </td>
                <td> str </td>
                <td>success</td>
                <td> Directory service used for querying identity information for UNIX (such as UIDs, GIDs, net groups). </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_unix_user </td>
                <td> str </td>
                <td>success</td>
                <td> Default Unix user name used for granting access in the case of Windows to Unix user mapping failure. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_windows_user </td>
                <td> str </td>
                <td>success</td>
                <td> Default windows user name used for granting access in the case of Unix to Windows user mapping failure </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the NAS server </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_backup_only </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether the NAS server is used as backup only. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_multi_protocol_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether multiprotocol sharing mode is enabled </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_packet_reflect_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> If the packet reflect has to be enabled </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_replication_destination </td>
                <td> bool </td>
                <td>success</td>
                <td> If the NAS server is a replication destination then True. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_windows_to_unix_username_mapping_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether a Unix to/from Windows user name mapping is enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the NAS server </td>
            </tr>
                                        </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Quota Tree Module

Manage quota tree on the Unity storage system

### Synopsis
 Managing Quota tree on the Unity storage system includes Create quota tree, Get quota tree, Modify quota tree and Delete quota tree

### Parameters
                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > filesystem_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the filesystem for which quota tree is created.  <br> For creation or modification of a quota tree either filesystem_name or filesystem_id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the filesystem for which the quota tree is created.  <br> For creation of a quota tree either filesystem_id or filesystem_name is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the NAS server in which the filesystem is created.  <br> For creation of a quota tree either nas_server_name or nas_server_id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the NAS server in which the filesystem is created.  <br> For creation of a quota tree either filesystem_id or filesystem_name is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > tree_quota_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the quota tree.  <br> Either tree_quota_id or path to quota tree is required to view/modify/delete quota tree. </td>
        </tr>
                    <tr>
            <td colspan=1 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The path to the quota tree.  <br> Either tree_quota_id or path to quota tree is required to create/view/modify/delete a quota tree.  <br> Path must start with a forward slash '/'. </td>
        </tr>
                    <tr>
            <td colspan=1 > hard_limit</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hard limitation for a quota tree on the total space available. If exceeded, users in quota tree cannot write data.  <br> Value 0 implies no limit.  <br> One of the values of soft_limit and hard_limit can be 0, however, both cannot be both 0 during creation of a quota tree. </td>
        </tr>
                    <tr>
            <td colspan=1 > soft_limit</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Soft limitation for a quota tree on the total space available. If exceeded, notification will be sent to users in the quota tree for the grace period mentioned, beyond which users cannot use space.  <br> Value 0 implies no limit.  <br> Both soft_limit and hard_limit cannot be 0 during creation of quota tree. </td>
        </tr>
                    <tr>
            <td colspan=1 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>MB</li>  <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> Unit of soft_limit and hard_limit size.  <br> It defaults to 'GB' if not specified. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description of a quota tree. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> The state option is used to mention the existence of the filesystem quota tree. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
  - name: Get quota tree details by quota tree id
    dellemc_unity_tree_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      quota_tree_id: "treequota_171798700679_10"
      state: "present"

  - name: Get quota tree details by quota tree path
    dellemc_unity_tree_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_name: "fs_2171"
      nas_server_id: "nas_21"
      path: "/test"
      state: "present"

  - name: Create quota tree for a filesystem with filesystem id
    dellemc_unity_tree_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      hard_limit: 6
      cap_unit: "TB"
      soft_limit: 5
      path: "/test_new"
      state: "present"

  - name: Create quota tree for a filesystem with filesystem name
    dellemc_unity_tree_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_name: "Test_filesystem"
      nas_server_name: "lglad068"
      hard_limit: 6
      cap_unit: "TB"
      soft_limit:  5
      path: "/test_new"
      state: "present"

  - name: Modify quota tree limit usage by quota tree path
    dellemc_unity_tree_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      path: "/test_new"
      hard_limit: 10
      cap_unit: "TB"
      soft_limit: 8
      state: "present"

  - name: Modify quota tree by quota tree id
    dellemc_unity_tree_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      quota_tree_id: "treequota_171798700679_10"
      hard_limit: 12
      cap_unit: "TB"
      soft_limit: 10
      state: "present"

  - name: Delete quota tree by quota tree id
    dellemc_unity_tree_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      quota_tree_id: "treequota_171798700679_10"
      state: "absent"

  - name: Delete quota tree by path
    dellemc_unity_tree_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      path: "/test_new"
      state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=4 > get_quota_tree_details </td>
            <td>  complex </td>
            <td> When quota tree exists </td>
            <td> Details of the quota tree. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description of the quota tree. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > filesystem </td>
                <td> complex </td>
                <td>success</td>
                <td> Filesystem details for which the quota tree is created. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > UnityFileSystem </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> Filesystem details for which the quota tree is created. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> ID of the filesystem for which the quota tree is create. </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > gp_left </td>
                <td> int </td>
                <td>success</td>
                <td> The grace period left after the soft limit for the user quota is exceeded. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > hard_limit </td>
                <td> int </td>
                <td>success</td>
                <td> Hard limit of quota tree. If the quota tree's space usage exceeds the hard limit, users in quota tree cannot write data. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Quota tree ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > path </td>
                <td> str </td>
                <td>success</td>
                <td> Path to quota tree. A valid path must start with a forward slash '/'. It is mandatory while creating a quota tree. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > size_used </td>
                <td> int </td>
                <td>success</td>
                <td> Size of used space in the filesystem by the user files. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > soft_limit </td>
                <td> int </td>
                <td>success</td>
                <td> Soft limit of the quota tree. If the quota tree's space usage exceeds the soft limit, the storage system starts to count down based on the specified grace period. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > state </td>
                <td> int </td>
                <td>success</td>
                <td> State of the quota tree. </td>
            </tr>
                                        </table>

### Authors
* Spandita Panigrahi (@panigs7) <ansible.team@dell.com>

--------------------------------
# File System Module

Manage filesystem on Unity storage system

### Synopsis
 Managing filesystem on Unity storage system includes- Create new filesystem, Modify snapschedule attribute of filesystem Modify filesystem attributes, Display filesystem details, Display filesystem snapshots, Display filesystem snapschedule, Delete snapschedule associated with the filesystem, Delete filesystem, Create new filesystem with quota configuration

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=2 > filesystem_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the filesystem. Mandatory only for the create operation. All the operations are supported through 'filesystem_name'  <br> It's mutually exclusive with 'filesystem_id'. </td>
        </tr>
                    <tr>
            <td colspan=2 > filesystem_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The id of the filesystem.It's mutually exclusive with 'filesystem_name'  <br> It can be used only for get, modify, or delete operations. </td>
        </tr>
                    <tr>
            <td colspan=2 > pool_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is the name of the pool where the filesystem will be created.  <br> Either the pool_name or pool_id must be provided to create a new filesystem. </td>
        </tr>
                    <tr>
            <td colspan=2 > pool_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is the ID of the pool where the filesystem will be created.  <br> Either the pool_name or pool_id must be provided to create a new filesystem. </td>
        </tr>
                    <tr>
            <td colspan=2 > size</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The size of the filesystem. </td>
        </tr>
                    <tr>
            <td colspan=2 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> The unit of the filesystem size. It defaults to 'GB', if not specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the NAS server on which filesystem will be hosted. </td>
        </tr>
                    <tr>
            <td colspan=2 > nas_server_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the NAS server on which filesystem will be hosted. </td>
        </tr>
                    <tr>
            <td colspan=2 > supported_protocols</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NFS</li>  <li>CIFS</li>  <li>MULTIPROTOCOL</li> </ul></td>
            <td> <br> Protocols supported by the file system.  <br> It will be overridden by NAS server configuration if NAS Server is Multiprotocol </td>
        </tr>
                    <tr>
            <td colspan=2 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description about the filesystem.  <br> Description can be removed by passing empty string (""). </td>
        </tr>
                    <tr>
            <td colspan=2 > smb_properties</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Advance settings for SMB. It contains optional candidate variables </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_sync_writes_enabled </td>
                <td> bool  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether the synchronous writes option is enabled on the file system.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_notify_on_access_enabled </td>
                <td> bool  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether notifications of changes to directory file structure are enabled.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_op_locks_enabled </td>
                <td> bool  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether opportunistic file locking is enabled on the file system.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_smb_notify_on_write_enabled </td>
                <td> bool  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether file write notifications are enabled on the file system.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > smb_notify_on_change_dir_depth </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Integer variable, determines the lowest directory level to which the enabled notifications apply.  <br> Minimum value is 1.  </td>
            </tr>
                            <tr>
            <td colspan=2 > data_reduction</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Boolean variable, specifies whether or not to enable compression. Compression is supported only for thin filesystem </td>
        </tr>
                    <tr>
            <td colspan=2 > is_thin</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Boolean variable, specifies whether or not it's a thin filesystem. </td>
        </tr>
                    <tr>
            <td colspan=2 > access_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NATIVE</li>  <li>UNIX</li>  <li>WINDOWS</li> </ul></td>
            <td> <br> Access policy of a filesystem. </td>
        </tr>
                    <tr>
            <td colspan=2 > locking_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>ADVISORY</li>  <li>MANDATORY</li> </ul></td>
            <td> <br> File system locking policies. These policy choices control whether the NFSv4 range locks must be honored. </td>
        </tr>
                    <tr>
            <td colspan=2 > tiering_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>AUTOTIER_HIGH</li>  <li>AUTOTIER</li>  <li>HIGHEST</li>  <li>LOWEST</li> </ul></td>
            <td> <br> Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool. </td>
        </tr>
                    <tr>
            <td colspan=2 > quota_config</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Configuration for quota management. It contains optional parameters. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > grace_period </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Grace period set in quota configuration after soft limit is reached.  <br> If grace_period is not set during creation of filesystem, it will be set to '7 days' by default.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > grace_period_unit </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td> <ul> <li>minutes</li>  <li>hours</li>  <li>days</li> </ul></td>
                <td>  <br> Unit of grace period.  <br> Default unit is 'days'.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_hard_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Default hard limit for user quotas and tree quotas.  <br> If default_hard_limit is not set while creation of filesystem, it will be set to 0B by default.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > default_soft_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Default soft limit for user quotas and tree quotas.  <br> If default_soft_limit is not set while creation of filesystem, it will be set to 0B by default.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_user_quota_enabled </td>
                <td> bool  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Indicates whether the user quota is enabled.  <br> Parameters 'is_user_quota_enabled' and 'quota_policy' are mutually exclusive.  <br> If is_user_quota_enabled is not set while creation of filesystem, it will be set to false by default.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > quota_policy </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td> <ul> <li>FILE_SIZE</li>  <li>BLOCKS</li> </ul></td>
                <td>  <br> Quota policy set in quota configuration.  <br> Parameters 'is_user_quota_enabled' and 'quota_policy' are mutually exclusive.  <br> If quota_policy is not set while creation of filesystem, it will be set to "FILE_SIZE" by default.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > cap_unit </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td> <ul> <li>MB</li>  <li>GB</li>  <li>TB</li> </ul></td>
                <td>  <br> Unit of default_soft_limit and default_hard_limit size.  <br> Default unit is 'GB'.  </td>
            </tr>
                            <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> State variable to determine whether filesystem will exist or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > snap_schedule_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is the name of an existing snapshot schedule which is to be associated with the filesystem. This is mutually exclusive with snapshot schedule id. </td>
        </tr>
                    <tr>
            <td colspan=2 > snap_schedule_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is the id of an existing snapshot schedule which is to be associated with the filesystem. This is mutually exclusive with snapshot schedule name. filesystem. </td>
        </tr>
                    <tr>
            <td colspan=2 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                                    </table>

### Notes
* SMB shares, NFS exports, and snapshots associated with filesystem need to be deleted prior to deleting a filesystem.
* quota_config parameter can be used to update default hard limit and soft limit values to limit the maximum space that can be used. By default they both are set to 0 during filesystem creation which means unlimited.

### Examples
```
- name: Create FileSystem
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    pool_name: "pool_1"
    size: 5
    state: "present"

- name: Create FileSystem with quota configuration
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    pool_name: "pool_1"
    size: 5
    quota_config:
        grace_period: 8
        grace_period_unit: "days"
        default_soft_limit: 10
        is_user_quota_enabled: False
    state: "present"

- name: Expand FileSystem size
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    size: 10
    state: "present"

- name: Expand FileSystem size
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    size: 10
    state: "present"

- name: Modify FileSystem smb_properties
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_name: "ansible_test_fs"
    nas_server_name: "lglap761"
    smb_properties:
      is_smb_op_locks_enabled: True
      smb_notify_on_change_dir_depth: 5
      is_smb_notify_on_access_enabled: True
    state: "present"

- name: Modify FileSystem Snap Schedule
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_id: "fs_141"
    snap_schedule_id: "{{snap_schedule_id}}"
    state: "{{state_present}}"

- name: Get details of FileSystem using id
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_id: "rs_405"
    state: "present"

- name: Delete a FileSystem using id
  dellemc_unity_filesystem:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    filesystem_id: "rs_405"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > filesystem_snapshot_details </td>
            <td>  complex </td>
            <td> When filesystem snapshot exists </td>
            <td> Details of the filesystem snapshot. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > access_type </td>
                <td> str </td>
                <td>success</td>
                <td> Access type of filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > attached_wwn </td>
                <td> str </td>
                <td>success</td>
                <td> Attached WWN details. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > creation_time </td>
                <td> str </td>
                <td>success</td>
                <td> Creation time of filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > creator_schedule </td>
                <td> str </td>
                <td>success</td>
                <td> Creator schedule of filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > creator_type </td>
                <td> str </td>
                <td>success</td>
                <td> Creator type for filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > creator_user </td>
                <td> str </td>
                <td>success</td>
                <td> Creator user for filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description of the filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > expiration_time </td>
                <td> str </td>
                <td>success</td>
                <td> Date and time after which the filesystem snapshot will expire. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filesystem_id </td>
                <td> str </td>
                <td>success</td>
                <td> Id of the filesystem for which the snapshot exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filesystem_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the filesystem for which the snapshot exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the filesystem snapshot instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_auto_delete </td>
                <td> bool </td>
                <td>success</td>
                <td> Is the filesystem snapshot is auto deleted or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > nas_server_id </td>
                <td> str </td>
                <td>success</td>
                <td> Id of the NAS server on which filesystem exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > nas_server_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the NAS server on which filesystem exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size </td>
                <td> int </td>
                <td>success</td>
                <td> Size of the filesystem snapshot. </td>
            </tr>
                                        </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>
* Meenakshi Dembi (@dembim) <ansible.team@dell.com>
* Spandita Panigrahi (@panigs7) <ansible.team@dell.com>

--------------------------------
# Storage Pool Module

Manage storage pool on Unity

### Synopsis
 Managing storage pool on Unity storage system contains the following operations
 Get details of storage pool
 Modify storage pool

### Parameters
                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > pool_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the storage pool, unique in the storage system. </td>
        </tr>
                    <tr>
            <td colspan=1 > pool_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the pool instance. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_pool_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the storage pool, unique in the storage system. </td>
        </tr>
                    <tr>
            <td colspan=1 > pool_description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The description of the storage pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > fast_cache</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>enabled</li>  <li>disabled</li> </ul></td>
            <td> <br> Indicates whether the fast cache is enabled for the storage pool.  <br> enabled - FAST Cache is enabled for the pool.  <br> disabled - FAST Cache is disabled for the pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > fast_vp</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>enabled</li>  <li>disabled</li> </ul></td>
            <td> <br> Indicates whether to enable scheduled data relocations for the pool.  <br> enabled - Enabled scheduled data relocations for the pool.  <br> disabled - Disabled scheduled data relocations for the pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the storage pool should exist or not.  <br> present - indicates that the storage pool should exist on the system.  <br> absent - indicates that the storage pool should not exist on the system. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                                    </table>

### Notes
* Creation/Deletion of storage pool is not allowed through Ansible module.

### Examples
```
- name: Get Storage pool details using pool_name
  dellemc_unity_storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    pool_name: "{{pool_name}}"
    state: "present"

- name: Get Storage pool details using pool_id
  dellemc_unity_storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    pool_id: "{{pool_id}}"
    state: "present"

- name: Modify Storage pool attributes using pool_name
  dellemc_unity_storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    pool_name: "{{pool_name}}"
    new_pool_name: "{{new_pool_name}}"
    pool_description: "{{pool_description}}"
    fast_cache: "{{fast_cache_enabled}}"
    fast_vp: "{{fast_vp_enabled}}"
    state: "present"

- name: Modify Storage pool attributes using pool_id
  dellemc_unity_storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    pool_id: "{{pool_id}}"
    new_pool_name: "{{new_pool_name}}"
    pool_description: "{{pool_description}}"
    fast_cache: "{{fast_cache_enabled}}"
    fast_vp: "{{fast_vp_enabled}}"
    state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the storage pool has changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > storage_pool_details </td>
            <td>  complex </td>
            <td> When storage pool exists. </td>
            <td> The storage pool details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Pool id, unique identifier of the pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_fast_cache_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether the fast cache is enabled for the storage pool. true - FAST Cache is enabled for the pool. false - FAST Cache is disabled for the pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_fast_vp_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether to enable scheduled data relocations for the storage pool. true - Enabled scheduled data relocations for the pool. false - Disabled scheduled data relocations for the pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Pool name, unique in the storage system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size_free_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates size_free with its appropriate unit in human readable form. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size_subscribed_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates size_subscribed with its appropriate unit in human readable form. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size_total_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates size_total with its appropriate unit in human readable form. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size_used_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates size_used with its appropriate unit in human readable form. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snap_size_subscribed_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates snap_size_subscribed with its appropriate unit in human readable form. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snap_size_used_with_unit </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates snap_size_used with its appropriate unit in human readable form. </td>
            </tr>
                                        </table>

### Authors
* Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>

--------------------------------
# Gatherfacts Module

Gathering information about DellEMC Unity

### Synopsis
 Gathering information about DellEMC Unity storage system includes Get the details of Unity array, Get list of Hosts in Unity array, Get list of FC initiators in Unity array, Get list of iSCSI initiators in Unity array, Get list of Consistency groups in Unity array, Get list of Storage pools in Unity array, Get list of Volumes in Unity array, Get list of Snapshot schedules in Unity array, Get list of NAS servers in Unity array, Get list of File systems in Unity array, Get list of Snapshots in Unity array, Get list of SMB shares in Unity array, Get list of NFS exports in Unity array, Get list of User quotas in Unity array, Get list of Quota tree in Unity array

### Parameters
                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > gather_subset</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td> <ul> <li>host</li>  <li>fc_initiator</li>  <li>iscsi_initiator</li>  <li>cg</li>  <li>storage_pool</li>  <li>vol</li>  <li>snapshot_schedule</li>  <li>nas_server</li>  <li>file_system</li>  <li>snapshot</li>  <li>nfs_export</li>  <li>smb_share</li>  <li>user_quota</li>  <li>tree_quota</li> </ul></td>
            <td> <br> List of string variables to specify the Unity storage system entities for which information is required.  <br> host  <br> fc_initiator  <br> iscsi_initiator  <br> cg  <br> storage_pool  <br> vol  <br> snapshot_schedule  <br> nas_server  <br> file_system  <br> snapshot  <br> nfs_export  <br> smb_share  <br> user_quota  <br> tree_quota </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
 - name: Get detailed list of Unity entities.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - host
       - fc_initiator
       - iscsi_initiator
       - cg
       - storage_pool
       - vol
       - snapshot_schedule
       - nas_server
       - file_system
       - snapshot
       - nfs_export
       - smb_share
       - user_quota
       - tree_quota

 - name: Get information of Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"

 - name: Get list of hosts on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - host

 - name: Get list of FC initiators on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - fc_initiator

 - name: Get list of ISCSI initiators on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - iscsi_initiator

 - name: Get list of consistency groups on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - cg

 - name: Get list of storage pools on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - storage_pool

 - name: Get list of volumes on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - vol

 - name: Get list of snapshot schedules on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - snapshot_schedule

 - name: Get list of NAS Servers on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - nas_server

 - name: Get list of File Systems on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - file_system

 - name: Get list of Snapshots on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - snapshot

 - name: Get list of NFS exports on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - nfs_export

 - name: Get list of SMB shares on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - smb_share

 - name: Get list of user quotas on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - user_quota

 - name: Get list of quota trees on Unity array.
   dellemc_unity_gatherfacts:
     unispherehost: "{{unispherehost}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - tree_quota
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > Array_Details </td>
            <td>  complex </td>
            <td> always </td>
            <td> Details of the Unity Array. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > api_version </td>
                <td> str </td>
                <td>success</td>
                <td> The current api version of the Unity Array. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > earliest_api_version </td>
                <td> str </td>
                <td>success</td>
                <td> The earliest api version of the Unity Array. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > model </td>
                <td> str </td>
                <td>success</td>
                <td> The model of the Unity Array. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the Unity Array. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > software_version </td>
                <td> str </td>
                <td>success</td>
                <td> The software version of the Unity Array. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Consistency_Groups </td>
            <td>  complex </td>
            <td> When Consistency Groups exist. </td>
            <td> Details of the Consistency Groups. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Consistency Group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the Consistency Group. </td>
            </tr>
                                        <tr>
            <td colspan=2 > FC_initiators </td>
            <td>  complex </td>
            <td> When FC initiator exist. </td>
            <td> Details of the FC initiators. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > WWN </td>
                <td> str </td>
                <td>success</td>
                <td> The WWN of the FC initiator. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The id of the FC initiator. </td>
            </tr>
                                        <tr>
            <td colspan=2 > File_Systems </td>
            <td>  complex </td>
            <td> When File Systems exist. </td>
            <td> Details of the File Systems. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the File System. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the File System. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Hosts </td>
            <td>  complex </td>
            <td> When hosts exist. </td>
            <td> Details of the hosts. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the host. </td>
            </tr>
                                        <tr>
            <td colspan=2 > ISCSI_initiators </td>
            <td>  complex </td>
            <td> When ISCSI initiators exist. </td>
            <td> Details of the ISCSI initiators. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > IQN </td>
                <td> str </td>
                <td>success</td>
                <td> The IQN of the ISCSI initiator. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The id of the ISCSI initiator. </td>
            </tr>
                                        <tr>
            <td colspan=2 > NAS_Servers </td>
            <td>  complex </td>
            <td> When NAS Servers exist. </td>
            <td> Details of the NAS Servers. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the NAS Server. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the NAS Server. </td>
            </tr>
                                        <tr>
            <td colspan=2 > NFS_Exports </td>
            <td>  complex </td>
            <td> When NFS Exports exist. </td>
            <td> Details of the NFS Exports. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the NFS Export. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the NFS Export. </td>
            </tr>
                                        <tr>
            <td colspan=2 > SMB_Shares </td>
            <td>  complex </td>
            <td> When SMB Shares exist. </td>
            <td> Details of the SMB Shares. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the SMB Share. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the SMB Share. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Snapshot_Schedules </td>
            <td>  complex </td>
            <td> When Snapshot Schedules exist. </td>
            <td> Details of the Snapshot Schedules. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Snapshot Schedule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the Snapshot Schedule. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Snapshots </td>
            <td>  complex </td>
            <td> When Snapshots exist. </td>
            <td> Details of the Snapshots. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the Snapshot. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Storage_Pools </td>
            <td>  complex </td>
            <td> When Storage Pools exist. </td>
            <td> Details of the Storage Pools. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Storage Pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the Storage Pool. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Tree_Quotas </td>
            <td>  complex </td>
            <td> When quota trees exist. </td>
            <td> Details of the quota trees. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the quota tree. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > path </td>
                <td> str </td>
                <td>success</td>
                <td> The path of the quota tree. </td>
            </tr>
                                        <tr>
            <td colspan=2 > User_Quotas </td>
            <td>  complex </td>
            <td> When user quotas exist. </td>
            <td> Details of the user quotas. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the user quota. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > uid </td>
                <td> str </td>
                <td>success</td>
                <td> The UID of the user quota. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Volumes </td>
            <td>  complex </td>
            <td> When Volumes exist. </td>
            <td> Details of the Volumes. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the Volume. </td>
            </tr>
                                        </table>

### Authors
* Rajshree Khare (@kharer5) <ansible.team@dell.com>
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# User Quota Module

Manage user quota on the Unity storage system

### Synopsis
 Managing User Quota on the Unity storage system includes Create user quota, Get user quota, Modify user quota, Delete user quota, Create user quota for quota tree, Modify user quota for quota tree and Delete user quota for quota tree.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > filesystem_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the filesystem for which the user quota is created.  <br> For creation of a user quota either filesystem_name or filesystem_id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the filesystem for which the user quota is created.  <br> For creation of a user quota either filesystem_id or filesystem_name is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the NAS server in which the filesystem is created.  <br> For creation of a user quota either nas_server_name or nas_server_id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the NAS server in which the filesystem is created.  <br> For creation of a user quota either filesystem_id or filesystem_name is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > hard_limit</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hard limitation for a user on the total space available. If exceeded, user cannot write data.  <br> Value 0 implies no limit.  <br> One of the values of soft_limit and hard_limit can be 0, however, both cannot be 0 during creation or modification of user quota. </td>
        </tr>
                    <tr>
            <td colspan=1 > soft_limit</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Soft limitation for a user on the total space available. If exceeded, notification will be sent to the user for the grace period mentioned, beyond which the user cannot use space.  <br> Value 0 implies no limit.  <br> Both soft_limit and hard_limit cannot be 0 during creation or modification of user quota. </td>
        </tr>
                    <tr>
            <td colspan=1 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>MB</li>  <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> Unit of soft_limit and hard_limit size.  <br> It defaults to 'GB' if not specified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Unix</li>  <li>Windows</li> </ul></td>
            <td> <br> Type of user creating a user quota.  <br> Mandatory while creating or modifying user quota. </td>
        </tr>
                    <tr>
            <td colspan=1 > win_domain</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Fully qualified or short domain name for Windows user type.  <br> Mandatory when user_type is 'Windows'. </td>
        </tr>
                    <tr>
            <td colspan=1 > user_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> User name of the user quota when user_type is 'Windows' or 'Unix'.  <br> user_name must be specified along with win_domain when user_type is 'Windows'. </td>
        </tr>
                    <tr>
            <td colspan=1 > uid</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> User ID of the user quota. </td>
        </tr>
                    <tr>
            <td colspan=1 > user_quota_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> User quota ID generated after creation of a user quota. </td>
        </tr>
                    <tr>
            <td colspan=1 > tree_quota_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the quota tree.  <br> Either tree_quota_id or path to quota tree is required to create/modify/delete user quota for a quota tree. </td>
        </tr>
                    <tr>
            <td colspan=1 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The path to the quota tree.  <br> Either tree_quota_id or path to quota tree is required to create/modify/delete user quota for a quota tree.  <br> Path must start with a forward slash '/'. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> The state option is used to mention the existence of the user quota. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
  - name: Get user quota details by user quota id
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      user_quota_id: "userquota_171798700679_0_123"
      state: "present"

  - name: Get user quota details by user quota uid/user name
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_name: "fs_2171"
      nas_server_id: "nas_21"
      user_name: "test"
      state: "present"

  - name: Create user quota for a filesystem with filesystem id
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      hard_limit: 6
      cap_unit: "TB"
      soft_limit: 5
      user_type: "UID"
      uid: "111"
      state: "present"

  - name: Create user quota for a filesystem with filesystem name
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_name: "Test_filesystem"
      nas_server_name: "lglad068"
      hard_limit: 6
      cap_unit: "TB"
      soft_limit:  5
      user_type: "UID"
      uid: "111"
      state: "present"

  - name: Modify user quota limit usage by user quota id
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      user_quota_id: "userquota_171798700679_0_123"
      hard_limit: 10
      cap_unit: "TB"
      soft_limit: 8
      state: "present"

  - name: Modify user quota by filesystem id and user quota uid/user_name
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      user_type: "Windows"
      win_domain: "prod"
      user_name: "sample"
      hard_limit: 12
      cap_unit: "TB"
      soft_limit: 10
      state: "present"

  - name: Delete user quota
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      win_domain: "prod"
      user_name: "sample"
      state: "absent"

  - name: Create user quota of a quota tree
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      tree_quota_id: "treequota_171798700679_4"
      user_type: "Windows"
      win_domain: "prod"
      user_name: "sample"
      soft_limit: 9
      cap_unit: "TB"
      state: "present"

  - name: Create user quota of a quota tree by quota tree path
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      path: "/sample"
      user_type: "Unix"
      user_name: "test"
      hard_limit: 2
      cap_unit: "TB"
      state: "present"

  - name: Modify user quota of a quota tree
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      tree_quota_id: "treequota_171798700679_4"
      user_type: "Windows"
      win_domain: "prod"
      user_name: "sample"
      soft_limit: 10
      cap_unit: "TB"
      state: "present"

  - name: Modify user quota of a quota tree by quota tree path
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      path: "/sample"
      user_type: "Windows"
      win_domain: "prod"
      user_name: "sample"
      hard_limit: 12
      cap_unit: "TB"
      state: "present"

  - name: Delete user quota of a quota tree by quota tree path
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      filesystem_id: "fs_2171"
      path: "/sample"
      win_domain: "prod"
      user_name: "sample"
      state: "absent"

  - name: Delete user quota of a quota tree by quota tree id
    dellemc_unity_user_quota:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      tree_quota_id: "treequota_171798700679_4"
      win_domain: "prod"
      user_name: "sample"
      state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=6>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=6 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=6 > get_user_quota_details </td>
            <td>  complex </td>
            <td> When user quota exists </td>
            <td> Details of the user quota. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > filesystem </td>
                <td> complex </td>
                <td>success</td>
                <td> Filesystem details for which the user quota is created. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > UnityFileSystem </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> Filesystem details for which the user quota is created. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> ID of the filesystem for which the user quota is created. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > name </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Name of filesystem. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > nas_server </td>
                        <td> complex </td>
                        <td>success</td>
                        <td> Nasserver details where filesystem is created. </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > gp_left </td>
                <td> int </td>
                <td>success</td>
                <td> The grace period left after the soft limit for the user quota is exceeded. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > hard_limit </td>
                <td> int </td>
                <td>success</td>
                <td> Hard limitation for a user on the total space available. If exceeded, user cannot write data. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > hard_ratio </td>
                <td> str </td>
                <td>success</td>
                <td> The hard ratio is the ratio between the hard limit size of the user quota and the amount of storage actually consumed. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > id </td>
                <td> str </td>
                <td>success</td>
                <td> User quota ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > size_used </td>
                <td> int </td>
                <td>success</td>
                <td> Size of used space in the filesystem by the user files. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > soft_limit </td>
                <td> int </td>
                <td>success</td>
                <td> Soft limitation for a user on the total space available. If exceeded, notification will be sent to user for the grace period mentioned, beyond which user cannot use space. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > soft_ratio </td>
                <td> str </td>
                <td>success</td>
                <td> The soft ratio is the ratio between the soft limit size of the user quota and the amount of storage actually consumed. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > state </td>
                <td> int </td>
                <td>success</td>
                <td> State of the user quota. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > tree_quota </td>
                <td> complex </td>
                <td>success</td>
                <td> Quota tree details for which the user quota is created. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > UnityTreeQuota </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> Quota tree details for which the user quota is created. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> ID of the quota tree. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=3 > path </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Path to quota tree </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > uid </td>
                <td> int </td>
                <td>success</td>
                <td> User ID of the user. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > unix_name </td>
                <td> str </td>
                <td>success</td>
                <td> Unix user name for this user quota's uid. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > windows_names </td>
                <td> str </td>
                <td>success</td>
                <td> Windows user name that maps to this quota's uid. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > windows_sids </td>
                <td> str </td>
                <td>success</td>
                <td> Windows SIDs that maps to this quota's uid </td>
            </tr>
                                        </table>

### Authors
* Spandita Panigrahi (@panigs7) <ansible.team@dell.com>

--------------------------------
# Filesystem Snapshot Module

Manage filesystem snapshot on the Unity storage system

### Synopsis
 Managing Filesystem Snapshot on the Unity storage system includes create filesystem snapshot, get filesystem snapshot, modify filesystem snapshot and delete filesystem snapshot.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the filesystem snapshot.  <br> Mandatory parameter for creating a filesystem snapshot.  <br> For all other operations either snapshot_name or snapshot_id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> During creation snapshot_id is auto generated.  <br> For all other operations either snapshot_id or snapshot_name is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the Filesystem for which snapshot is created.  <br> For creation of filesystem snapshot either filesystem_name or filesystem_id is required.  <br> Not required for other operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the Filesystem for which snapshot is created.  <br> For creation of filesystem snapshot either filesystem_id or filesystem_name is required.  <br> Not required for other operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the NAS server in which the Filesystem is created.  <br> For creation of filesystem snapshot either nas_server_name or nas_server_id is required.  <br> Not required for other operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the NAS server in which the Filesystem is created.  <br> For creation of filesystem snapshot either filesystem_id or filesystem_name is required.  <br> Not required for other operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > auto_delete</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This option specifies whether or not the filesystem snapshot will be automatically deleted.  <br> If set to true, the filesystem snapshot will expire based on the pool auto deletion policy.  <br> If set to false, the filesystem snapshot will not be auto deleted based on the pool auto deletion policy.  <br> auto_delete can not be set to True, if expiry_time is specified.  <br> If during creation neither auto_delete nor expiry_time is mentioned then the filesystem snapshot will be created keeping auto_delete as True.  <br> Once the expiry_time is set, then the filesystem snapshot cannot be assigned to the auto delete policy. </td>
        </tr>
                    <tr>
            <td colspan=1 > expiry_time</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This option is for specifying the date and time after which the filesystem snapshot will expire.  <br> The time is to be mentioned in UTC timezone.  <br> The format is "MM/DD/YYYY HH:MM". Year must be in 4 digits. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The additional information about the filesystem snapshot can be provided using this option.  <br> The description can be removed by passing an empty string. </td>
        </tr>
                    <tr>
            <td colspan=1 > fs_access_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Checkpoint</li>  <li>Protocol</li> </ul></td>
            <td> <br> Access type of the filesystem snapshot.  <br> Required only during creation of filesystem snapshot.  <br> If not given, snapshot's access type will be 'Checkpoint'. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> The state option is used to mention the existence of the filesystem snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                                    </table>

### Notes
* Filesystem snapshot cannot be deleted, if it has nfs or smb share.

### Examples
```
  - name: Create Filesystem Snapshot
    dellemc_unity_filesystem_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_name: "ansible_test_FS_snap"
      filesystem_name: "ansible_test_FS"
      nas_server_name: "lglad069"
      description: "Created using playbook"
      auto_delete: True
      fs_access_type: "Protocol"
      state: "present"

  - name: Create Filesystem Snapshot with expiry time.
    dellemc_unity_filesystem_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_name: "ansible_test_FS_snap_1"
      filesystem_name: "ansible_test_FS_1"
      nas_server_name: "lglad069"
      description: "Created using playbook"
      expiry_time: "04/15/2021 2:30"
      fs_access_type: "Protocol"
      state: "present"

  - name: Get Filesystem Snapshot Details using Name
    dellemc_unity_filesystem_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_name: "ansible_test_FS_snap"
      state: "present"

  - name: Get Filesystem Snapshot Details using ID
    dellemc_unity_filesystem_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_id: "10008000403"
      state: "present"

  - name: Update Filesystem Snapshot attributes
    dellemc_unity_filesystem_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_name: "ansible_test_FS_snap"
      description: "Description updated"
      auto_delete: False
      expiry_time: "04/15/2021 5:30"
      state: "present"

  - name: Update Filesystem Snapshot attributes using ID
    dellemc_unity_filesystem_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_id: "10008000403"
      expiry_time: "04/18/2021 8:30"
      state: "present"

  - name: Delete Filesystem Snapshot using Name
    dellemc_unity_filesystem_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_name: "ansible_test_FS_snap"
      state: "absent"

  - name: Delete Filesystem Snapshot using ID
    dellemc_unity_filesystem_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_id: "10008000403"
      state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > filesystem_snapshot_details </td>
            <td>  complex </td>
            <td> When filesystem snapshot exists </td>
            <td> Details of the filesystem snapshot. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > access_type </td>
                <td> str </td>
                <td>success</td>
                <td> Access type of filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > attached_wwn </td>
                <td> str </td>
                <td>success</td>
                <td> Attached WWN details. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > creation_time </td>
                <td> str </td>
                <td>success</td>
                <td> Creation time of filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > creator_schedule </td>
                <td> str </td>
                <td>success</td>
                <td> Creator schedule of filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > creator_type </td>
                <td> str </td>
                <td>success</td>
                <td> Creator type for filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > creator_user </td>
                <td> str </td>
                <td>success</td>
                <td> Creator user for filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description of the filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > expiration_time </td>
                <td> str </td>
                <td>success</td>
                <td> Date and time after which the filesystem snapshot will expire. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filesystem_id </td>
                <td> str </td>
                <td>success</td>
                <td> Id of the filesystem for which the snapshot exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filesystem_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the filesystem for which the snapshot exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the filesystem snapshot instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_auto_delete </td>
                <td> bool </td>
                <td>success</td>
                <td> Is the filesystem snapshot is auto deleted or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the filesystem snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > nas_server_id </td>
                <td> str </td>
                <td>success</td>
                <td> Id of the NAS server on which filesystem exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > nas_server_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the NAS server on which filesystem exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > size </td>
                <td> int </td>
                <td>success</td>
                <td> Size of the filesystem snapshot. </td>
            </tr>
                                        </table>

### Authors
* Rajshree Khare (@kharer5) <ansible.team@dell.com>

--------------------------------
# Snapshot Module

Manage snapshots on the Unity storage system.

### Synopsis
 Managing snapshots on the Unity storage system includes create snapshot, delete snapshot, update snapshot, get snapshot, map host and unmap host.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the snapshot.  <br> Mandatory parameter for creating a snapshot.  <br> For all other operations either snapshot name or snapshot id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > vol_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the volume for which snapshot is created.  <br> For creation of a snapshot either vol_name or cg_name is required.  <br> Not required for other operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > cg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the Consistency Group for which snapshot is created.  <br> For creation of a snapshot either vol_name or cg_name is required.  <br> Not required for other operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The id of the snapshot.  <br> For all operations other than creation either snapshot name or snapshot id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > auto_delete</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This option specifies whether the snapshot is auto deleted or not.  <br> If set to true, snapshot will expire based on the pool auto deletion policy.  <br> If set to false, snapshot will not be auto deleted based on the pool auto deletion policy.  <br> auto_delete can not be set to True, if expiry_time is specified.  <br> If during creation neither auto_delete nor expiry_time is mentioned then snapshot will be created keeping auto_delete as True.  <br> Once the expiry_time is set then snapshot cannot be assigned to the auto delete policy. </td>
        </tr>
                    <tr>
            <td colspan=1 > expiry_time</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This option is for specifying the date and time after which the snapshot will expire.  <br> The time is to be mentioned in UTC timezone.  <br> The format is "MM/DD/YYYY HH:MM". Year must be in 4 digits. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The additional information about the snapshot can be provided using this option. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name for the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> The state option is used to mention the existence of the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the host.  <br> Either host_name or host_id is required to map or unmap a snapshot from a host.  <br> Snapshot can be attached to multiple hosts. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The id of the host.  <br> Either host_name or host_id is required to map or unmap a snapshot from a host  <br> Snapshot can be attached to multiple hosts. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>mapped</li>  <li>unmapped</li> </ul></td>
            <td> <br> The host_state option is used to mention the existence of the host for snapshot.  <br> It is required when a snapshot is mapped or unmapped from host. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
  - name: Create a Snapshot for a CG
    dellemc_unity_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      port: "{{port}}"
      cg_name: "{{cg_name}}"
      snapshot_name: "{{cg_snapshot_name}}"
      description: "{{description}}"
      auto_delete: False
      state: "present"

  - name: Create a Snapshot for a volume with Host attached.
    dellemc_unity_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      port: "{{port}}"
      vol_name: "{{vol_name}}"
      snapshot_name: "{{vol_snapshot_name}}"
      description: "{{description}}"
      expiry_time: "04/15/2025 16:30"
      host_name: "{{host_name}}"
      host_state: "mapped"
      state: "present"

  - name: Unmap a host for a Snapshot
    dellemc_unity_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      port: "{{port}}"
      snapshot_name: "{{vol_snapshot_name}}"
      host_name: "{{host_name}}"
      host_state: "unmapped"
      state: "present"

  - name: Map snapshot to a host
    dellemc_unity_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      port: "{{port}}"
      snapshot_name: "{{vol_snapshot_name}}"
      host_name: "{{host_name}}"
      host_state: "mapped"
      state: "present"

  - name: Update attributes of a Snapshot for a volume
    dellemc_unity_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_name: "{{vol_snapshot_name}}"
      new_snapshot_name: "{{new_snapshot_name}}"
      description: "{{new_description}}"
      host_name: "{{host_name}}"
      host_state: "unmapped"
      state: "present"

  - name: Delete Snapshot of CG.
    dellemc_unity_snapshot:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      snapshot_name: "{{cg_snapshot_name}}"
      state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_details </td>
            <td>  complex </td>
            <td> When snapshot exists </td>
            <td> Details of the snapshot. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > expiration_time </td>
                <td> str </td>
                <td>success</td>
                <td> Date and time after which the snapshot will expire. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hosts_list </td>
                <td> dict </td>
                <td>success</td>
                <td> Contains the name and id of the associated hosts. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the snapshot instance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_auto_delete </td>
                <td> str </td>
                <td>success</td>
                <td> Additional information mentioned for snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storage_resource_id </td>
                <td> str </td>
                <td>success</td>
                <td> Id of the storage resource for which the snapshot exists. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storage_resource_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the storage resource for which the snapshot exists. </td>
            </tr>
                                        </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# SMB Share Module

Manage SMB shares on Unity storage system.

### Synopsis
 Managing SMB Shares on Unity storage system includes create, get, modify, and delete the smb shares.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > share_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the SMB share.  <br> Required during creation of the SMB share.  <br> For all other operations either share_name or share_id is required. </td>
        </tr>
                    <tr>
            <td colspan=1 > share_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the SMB share.  <br> Should not be specified during creation. Id is auto generated.  <br> For all other operations either share_name or share_id is required.  <br> If share_id is used then no need to pass nas_server/filesystem/snapshot/path. </td>
        </tr>
                    <tr>
            <td colspan=1 > path</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Local path to the file system/Snapshot or any existing sub-folder of the file system/Snapshot that is shared over the network.  <br> Path is relative to the root of the filesystem.  <br> Required for creation of the SMB share. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the File System.  <br> Either filesystem_name or filesystem_id is required for creation of the SMB share for filesystem.  <br> If filesystem name is specified, then nas_server_name/nas_server_id is required to uniquely identify the filesystem.  <br> filesystem_name and filesystem_id are mutually exclusive parameters. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the Filesystem Snapshot.  <br> Either snapshot_name or snapshot_id is required for creation of the SMB share for a snapshot.  <br> If snapshot name is specified, then nas_server_name/nas_server_id is required to uniquely identify the snapshot.  <br> snapshot_name and snapshot_id are mutually exclusive parameters. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the NAS Server.  <br> It is not required if share_id is used. </td>
        </tr>
                    <tr>
            <td colspan=1 > filesystem_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The Name of the File System.  <br> Either filesystem_name or filesystem_id is required for creation of the SMB share for filesystem.  <br> If filesystem name is specified, then nas_server_name/nas_server_id is required to uniquely identify the filesystem.  <br> filesystem_name and filesytem_id are mutually exclusive parameters. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The Name of the Filesystem Snapshot.  <br> Either snapshot_name or snapshot_id is required for creation of the SMB share for a snapshot.  <br> If snapshot name is specified, then nas_server_name/nas_server_id is required to uniquely identify the snapshot.  <br> snapshot_name and snapshot_id are mutually exclusive parameters. </td>
        </tr>
                    <tr>
            <td colspan=1 > nas_server_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The Name of the NAS Server.  <br> It is not required if share_id is used.  <br> nas_server_name and nas_server_id are mutually exclusive parameters. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description for the SMB share.  <br> Optional parameter when creating a share.  <br> To modify, pass the new value in description field. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_abe_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether Access-based Enumeration (ABE) for SMB share is enabled.  <br> During creation, if not mentioned then default is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_branch_cache_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether Branch Cache optimization for SMB share is enabled.  <br> During creation, if not mentioned then default is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_continuous_availability_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether continuous availability for SMB 3.0 is enabled.  <br> During creation, if not mentioned then default is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > is_encryption_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether encryption for SMB 3.0 is enabled at the shared folder level.  <br> During creation, if not mentioned then default is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > offline_availability</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>MANUAL</li>  <li>DOCUMENTS</li>  <li>PROGRAMS</li>  <li>NONE</li> </ul></td>
            <td> <br> Defines valid states of Offline Availability.  <br> MANUAL- Only specified files will be available offline.  <br> DOCUMENTS- All files that users open will be available offline.  <br> PROGRAMS- Program will preferably run from the offline cache even when connected to the network. All files that users open will be available offline.  <br> NONE- Prevents clients from storing documents and programs in offline cache. </td>
        </tr>
                    <tr>
            <td colspan=1 > umask</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The default UNIX umask for new files created on the SMB Share. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the SMB share should exist or not.  <br> present  indicates that the share should exist on the system.  <br> absent  indicates that the share should not exist on the system. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                                    </table>

### Notes
* When ID/Name of the filesystem/snapshot is passed then nas_server is not required. If passed, then filesystem/snapshot should exist for the mentioned nas_server, else the task will fail.

### Examples
```
- name: Create SMB share for a filesystem
  dellemc_unity_smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    share_name: "sample_smb_share"
    filesystem_name: "sample_fs"
    nas_server_id: "NAS_11"
    path: "/sample_fs"
    description: "Sample SMB share created"
    is_abe_enabled: True
    is_branch_cache_enabled: True
    offline_availability: "DOCUMENTS"
    is_continuous_availability_enabled: True
    is_encryption_enabled: True
    umask: "777"
    state: "present"
- name: Modify Attributes of SMB share for a filesystem
  dellemc_unity_smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    share_name: "sample_smb_share"
    nas_server_name: "sample_nas_server"
    description: "Sample SMB share attributes updated"
    is_abe_enabled: False
    is_branch_cache_enabled: False
    offline_availability: "MANUAL"
    is_continuous_availability_enabled: "False"
    is_encryption_enabled: "False"
    umask: "022"
    state: "present"
- name: Create SMB share for a snapshot
  dellemc_unity_smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    share_name: "sample_snap_smb_share"
    snapshot_name: "sample_snapshot"
    nas_server_id: "NAS_11"
    path: "/sample_snapshot"
    description: "Sample SMB share created for snapshot"
    is_abe_enabled: True
    is_branch_cache_enabled: True
    is_continuous_availability_enabled: True
    is_encryption_enabled: True
    umask: "777"
    state: "present"
- name: Modify Attributes of SMB share for a snapshot
  dellemc_unity_smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    share_name: "sample_snap_smb_share"
    snapshot_name: "sample_snapshot"
    description: "Sample SMB share attributes updated for snapshot"
    is_abe_enabled: False
    is_branch_cache_enabled: False
    offline_availability: "MANUAL"
    is_continuous_availability_enabled: "False"
    is_encryption_enabled: "False"
    umask: "022"
    state: "present"
- name: Get details of SMB share
  dellemc_unity_smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    share_id: "{{smb_share_id}}"
    state: "present"
- name: Delete SMB share
  dellemc_unity_smbshare:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    share_id: "{{smb_share_id}}"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=2 > smb_share_details </td>
            <td>  complex </td>
            <td> When share exists. </td>
            <td> The SMB share details. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Additional information about the share. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filesystem_id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Filesystem. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filesystem_name </td>
                <td> str </td>
                <td>success</td>
                <td> The Name of the filesystem </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the SMB share. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_abe_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether Access Based enumeration is enforced or not </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_branch_cache_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether branch cache is enabled or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_continuous_availability_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether the share will be available continuously or not </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_encryption_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether encryption is enabled or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the SMB share. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > nas_server_id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the nas_server. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > nas_server_name </td>
                <td> str </td>
                <td>success</td>
                <td> The Name of the nas_server. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snapshot_id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snapshot_name </td>
                <td> str </td>
                <td>success</td>
                <td> The Name of the Snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > umask </td>
                <td> str </td>
                <td>success</td>
                <td> Unix mask for the SMB share </td>
            </tr>
                                        </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Host Module

Manage Host operations on Unity.

### Synopsis
 The Host module contains the following operations Creation of a Host. Addition of initiators to Host. Removal of initiators from Host. Modification of host attributes. Get details of a Host. Deletion of a Host.

### Parameters
                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > host_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the host.  <br> Mandatory for host creation. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique identifier of the host.  <br> host_id is auto generated during creation.  <br> Except create, all other operations require either host_id or host_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Host description. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_os</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>AIX</li>  <li>Citrix XenServer</li>  <li>HP-UX</li>  <li>IBM VIOS</li>  <li>Linux</li>  <li>Mac OS</li>  <li>Solaris</li>  <li>VMware ESXi</li>  <li>Windows Client</li>  <li>Windows Server</li> </ul></td>
            <td> <br> Operating system running on the host. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_host_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name for the host.  <br> Only required in rename host operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > initiators</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of initiators to be added/removed to/from host. </td>
        </tr>
                    <tr>
            <td colspan=1 > initiator_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-host</li>  <li>absent-in-host</li> </ul></td>
            <td> <br> State of the initiator. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> State of the host. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create empty Host.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host"
    host_os: "Linux"
    description: "ansible-test-host"
    state: "present"

- name: Create Host with Initiators.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host-1"
    host_os: "Linux"
    description: "ansible-test-host-1"
    initiators:
      - "iqn.1994-05.com.redhat:c38e6e8cfd81"
      - "20:00:00:90:FA:13:81:8D:10:00:00:90:FA:13:81:8D"
    initiator_state: "present-in-host"
    state: "present"

- name: Modify Host using host_id.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_id: "Host_253"
    new_host_name: "ansible-test-host-2"
    host_os: "Mac OS"
    description: "Ansible tesing purpose"
    state: "present"

- name: Add Initiators to Host.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host-2"
    initiators:
      - "20:00:00:90:FA:13:81:8C:10:00:00:90:FA:13:81:8C"
    initiator_state: "present-in-host"
    state: "present"

- name: Get Host details using host_name.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host-2"
    state: "present"

- name: Get Host details using host_id.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_id: "Host_253"
    state: "present"

- name: Delete Host.
  dellemc_unity_host:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    host_name: "ansible-test-host-2"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=4 > host_details </td>
            <td>  complex </td>
            <td> When host exists. </td>
            <td> Details of the host. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > fc_host_initiators </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of the FC initiators associated with the host. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > UnityHostInitiatorList </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> FC initiators with system generated unique hash value. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system ID given to the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > iscsi_host_initiators </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of the ISCSI initiators associated with the host. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > UnityHostInitiatorList </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> ISCSI initiators with sytem genrated unique hash value. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > os_type </td>
                <td> str </td>
                <td>success</td>
                <td> Operating system running on the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > type </td>
                <td> str </td>
                <td>success</td>
                <td> HostTypeEnum of the host. </td>
            </tr>
                                        </table>

### Authors
* Rajshree Khare (@kharer5) <ansible.team@dell.com>

--------------------------------
# Consistency Group Module

Manage consistency groups on Unity storage system

### Synopsis
 Managing the consistency group on the Unity storage system includes creating new consistency group, adding volumes to consistency group, removing volumes from consistency group, mapping hosts to consistency group, unmapping hosts from consistency group, renaming consistency group, modifying attributes of consistency group and deleting consistency group.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=2 > cg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the consistency group.  <br> It is mandatory for the create operation.  <br> Specify either cg_name or cg_id (but not both) for any operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > cg_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the consistency group.  <br> It can be used only for get, modify, add/remove volumes, or delete operations. </td>
        </tr>
                    <tr>
            <td colspan=2 > volumes</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is a list of volumes.  <br> Either the volume ID or name must be provided for adding/removing existing volumes from consistency group.  <br> If volumes are given, then vol_state should also be specified.  <br> Volumes cannot be added/removed from consistency group, if the consistency group or the volume has snapshots. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > vol_id </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> The ID of the volume.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > vol_name </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> The name of the volume.  </td>
            </tr>
                            <tr>
            <td colspan=2 > vol_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> String variable, describes the state of volumes inside consistency group.  <br> If volumes are given, then vol_state should also be specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > new_cg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of the consistency group, used in rename operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > description</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Description of the consistency group. </td>
        </tr>
                    <tr>
            <td colspan=2 > snap_schedule</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Snapshot schedule assigned to the consistency group.  <br> Specifying an empty string "" removes the existing snapshot schedule from consistency group. </td>
        </tr>
                    <tr>
            <td colspan=2 > tiering_policy</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>AUTOTIER_HIGH</li>  <li>AUTOTIER</li>  <li>HIGHEST</li>  <li>LOWEST</li> </ul></td>
            <td> <br> Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool. </td>
        </tr>
                    <tr>
            <td colspan=2 > hosts</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is a list of hosts.  <br> Either the host ID or name must be provided for mapping/unmapping hosts for a consistency group.  <br> If hosts are given, then mapping_state should also be specified.  <br> Hosts cannot be mapped to a consistency group, if the consistency group has no volumes.  <br> When a consistency group is being mapped to the host, users should not use the volume module to map the volumes in the consistency group to hosts. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_id </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> The ID of the host.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > host_name </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> The name of the host.  </td>
            </tr>
                            <tr>
            <td colspan=2 > mapping_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>mapped</li>  <li>unmapped</li> </ul></td>
            <td> <br> String variable, describes the state of hosts inside the consistency group.  <br> If hosts are given, then mapping_state should also be specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the consistency group should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create consistency group
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      cg_name: "{{cg_name}}"
      description: "{{description}}"
      snap_schedule: "{{snap_schedule1}}"
      state: "present"

- name: Get details of consistency group using id
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      cg_id: "{{cg_id}}"
      state: "present"

- name: Add volumes to consistency group
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      cg_id: "{{cg_id}}"
      volumes:
          - vol_name: "Ansible_Test-3"
          - vol_id: "sv_1744"
      vol_state: "{{vol_state_present}}"
      state: "present"

- name: Rename consistency group
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      cg_name: "{{cg_name}}"
      new_cg_name: "{{new_cg_name}}"
      state: "present"

- name: Modify consistency group details
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      cg_name: "{{new_cg_name}}"
      snap_schedule: "{{snap_schedule2}}"
      tiering_policy: "{{tiering_policy1}}"
      state: "present"

- name: Map hosts to a consistency group
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      cg_id: "{{cg_id}}"
      hosts:
        - host_name: "10.226.198.248"
        - host_id: "Host_511"
      mapping_state: "mapped"
      state: "present"

- name: Unmap hosts from a consistency group
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      cg_id: "{{cg_id}}"
      hosts:
        - host_id: "Host_511"
        - host_name: "10.226.198.248"
      mapping_state: "unmapped"
      state: "present"

- name: Remove volumes from consistency group
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      cg_name: "{{new_cg_name}}"
      volumes:
        - vol_name: "Ansible_Test-3"
        - vol_id: "sv_1744"
      vol_state: "{{vol_state_absent}}"
      state: "present"

- name: Delete consistency group
  dellemc_unity_consistencygroup:
      unispherehost: "{{unispherehost}}"
      username: "{{username}}"
      password: "{{password}}"
      verifycert: "{{verifycert}}"
      cg_name: "{{new_cg_name}}"
      state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=10>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=10 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed </td>
        </tr>
                    <tr>
            <td colspan=10 > consistency_group_details </td>
            <td>  complex </td>
            <td> When consistency group exists </td>
            <td> Details of the consistency group </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=9 > block_host_access </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of hosts mapped to the consistency group </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=8 > UnityBlockHostAccessList </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> List of hosts mapped to consistency group </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=7 > UnityBlockHostAccess </td>
                        <td> complex </td>
                        <td>success</td>
                        <td> Details of host </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=9 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system ID given to the consistency group </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=9 > luns </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of volumes part of consistency group </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=8 > UnityLunList </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> List of volumes part of consistency group </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=7 > UnityLun </td>
                        <td> complex </td>
                        <td>success</td>
                        <td> Detail of volume </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=9 > relocation_policy </td>
                <td> str </td>
                <td>success</td>
                <td> FAST VP tiering policy for the consistency group </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=9 > snap_schedule </td>
                <td> complex </td>
                <td>success</td>
                <td> Snapshot schedule applied to consistency group </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=8 > UnitySnapSchedule </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> Snapshot schedule applied to consistency group </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=7 > id </td>
                        <td> str </td>
                        <td>success</td>
                        <td> The system ID given to the snapshot schedule </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=7 > name </td>
                        <td> str </td>
                        <td>success</td>
                        <td> The name of the snapshot schedule </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=9 > snapshots </td>
                <td> complex </td>
                <td>success</td>
                <td> List of snapshots of consistency group </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=8 > creation_time </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Date and time on which the snapshot was taken </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=8 > expirationTime </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Date and time after which the snapshot will expire </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=8 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the snapshot </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=8 > storageResource </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> Storage resource for which the snapshot was taken </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=7 > UnityStorageResource </td>
                        <td> complex </td>
                        <td>success</td>
                        <td> Details of the storage resource </td>
                    </tr>
                                                                                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# Snapshot Schedule Module

Manage snapshot schedules on Unity storage system

### Synopsis
 Managing snapshot schedules on Unity storage system includes creating new snapshot schedule, getting details of snapshot schedule, modifying attributes of snapshot schedule, and deleting snapshot schedule.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the snapshot schedule.  <br> Name is mandatory for a create operation.  <br> Specify either name or id (but not both) for any operation. </td>
        </tr>
                    <tr>
            <td colspan=1 > id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the snapshot schedule. </td>
        </tr>
                    <tr>
            <td colspan=1 > type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>every_n_hours</li>  <li>every_day</li>  <li>every_n_days</li>  <li>every_week</li>  <li>every_month</li> </ul></td>
            <td> <br> Type of the rule to be included in snapshot schedule.  <br> Type is mandatory for any create or modify operation.  <br> Once the snapshot schedule is created with one type it can be modified. </td>
        </tr>
                    <tr>
            <td colspan=1 > interval</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Number of hours between snapshots.  <br> Applicable only when rule type is 'every_n_hours'. </td>
        </tr>
                    <tr>
            <td colspan=1 > hours_of_day</td>
            <td> list   <br> elements: int </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Hours of the day when the snapshot will be taken.  <br> Applicable only when rule type is 'every_day'. </td>
        </tr>
                    <tr>
            <td colspan=1 > day_interval</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Number of days between snapshots.  <br> Applicable only when rule type is 'every_n_days'. </td>
        </tr>
                    <tr>
            <td colspan=1 > days_of_week</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td> <ul> <li>SUNDAY</li>  <li>MONDAY</li>  <li>TUESDAY</li>  <li>WEDNESDAY</li>  <li>THURSDAY</li>  <li>FRIDAY</li>  <li>SATURDAY</li> </ul></td>
            <td> <br> Days of the week for which the snapshot schedule rule applies.  <br> Applicable only  when rule type is 'every_week'. </td>
        </tr>
                    <tr>
            <td colspan=1 > day_of_month</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Day of the month for which the snapshot schedule rule applies.  <br> Applicable only when rule type is 'every_month'.  <br> Value should be [1, 31]. </td>
        </tr>
                    <tr>
            <td colspan=1 > hour</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> the hour when the snapshot will be taken.  <br> Applicable for 'every_n_days', 'every_week', 'every_month' rule types.  <br> For create operation, if 'hour' parameter is not specified, value will be taken as 0.  <br> Value should be [0, 23]. </td>
        </tr>
                    <tr>
            <td colspan=1 > minute</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Minute offset from the hour when the snapshot will be taken.  <br> Applicable for all rule types.  <br> For a create operation, if 'minute' parameter is not specified, value will be taken as 0.  <br> Value should be [0, 59]. </td>
        </tr>
                    <tr>
            <td colspan=1 > desired_retention</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The number of days/hours for which snapshot will be retained.  <br> When auto_delete is True, desired_retention cannot be specified.  <br> Maximum desired retention supported is 31 days or 744 hours. </td>
        </tr>
                    <tr>
            <td colspan=1 > retention_unit</td>
            <td> str  </td>
            <td></td>
            <td> hours </td>
            <td> <ul> <li>hours</li>  <li>days</li> </ul></td>
            <td> <br> The retention unit for the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > auto_delete</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Indicates whether the system can automatically delete the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the snapshot schedule should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unity management server. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with Unity management server. </td>
        </tr>
                                                    </table>

### Notes
* Snapshot schedule created via Ansible will have only one rule.
* Modification of rule type is not allowed. Within the same type, other parameters can be modified.
* If an existing snapshot schedule has more than 1 rule in it, only get and delete operation is allowed.

### Examples
```
- name: Create snapshot schedule (Rule Type - every_n_hours)
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_N_Hours_Testing"
      type: "every_n_hours"
      interval: 6
      desired_retention: 24
      state: "{{state_present}}"

- name: Create snapshot schedule (Rule Type - every_day)
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Day_Testing"
      type: "every_day"
      hours_of_day:
        - 8
        - 14
      auto_delete: True
      state: "{{state_present}}"

- name: Create snapshot schedule (Rule Type - every_n_days)
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_N_Day_Testing"
      type: "every_n_days"
      day_interval: 2
      desired_retention: 16
      retention_unit: "days"
      state: "{{state_present}}"

- name: Create snapshot schedule (Rule Type - every_week)
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Week_Testing"
      type: "every_week"
      days_of_week:
        - MONDAY
        - FRIDAY
      hour: 12
      minute: 30
      desired_retention: 200
      state: "{{state_present}}"

- name: Create snapshot schedule (Rule Type - every_month)
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Month_Testing"
      type: "every_month"
      day_of_month: 17
      auto_delete: True
      state: "{{state_present}}"

- name: Get snapshot schedule details using name
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_N_Hours_Testing"
      state: "{{state_present}}"

- name: Get snapshot schedule details using id
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      id: "{{id}}"
      state: "{{state_present}}"

- name: Modify snapshot schedule details id
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      id: "{{id}}"
      type: "every_n_hours"
      interval: 8
      state: "{{state_present}}"

- name: Modify snapshot schedule using name
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Day_Testing"
      type: "every_day"
      desired_retention: 200
      auto_delete: False
      state: "{{state_present}}"

- name: Delete snapshot schedule using id
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      id: "{{id}}"
      state: "{{state_absent}}"

- name: Delete snapshot schedule using name
  dellemc_unity_snapshotschedule:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Day_Testing"
      state: "{{state_absent}}"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=8>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=8 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=8 > snapshot_schedule_details </td>
            <td>  complex </td>
            <td> When snapshot schedule exists </td>
            <td> Details of the snapshot schedule. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=7 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The system ID given to the snapshot schedule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=7 > luns </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of volumes for which snapshot schedule applied. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > UnityLunList </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> List of volumes for which snapshot schedule applied. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=5 > UnityLun </td>
                        <td> complex </td>
                        <td>success</td>
                        <td> Detail of volume. </td>
                    </tr>
                                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=7 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the snapshot schedule. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=7 > rules </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of rules that apply to snapshot schedule. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > days_of_month </td>
                    <td> list </td>
                    <td>success</td>
                    <td> Days of the month for which the snapshot schedule rule applies. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > days_of_week </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> Days of the week for which the snapshot schedule rule applies. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=5 > DayOfWeekEnumList </td>
                        <td> list </td>
                        <td>success</td>
                        <td> Enumeration of days of the week. </td>
                    </tr>
                                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > hours </td>
                    <td> list </td>
                    <td>success</td>
                    <td> Hourly frequency for the snapshot schedule rule. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The system ID of the rule. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > interval </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Number of days or hours between snaps, depending on the rule type. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > is_auto_delete </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the system can automatically delete the snapshot based on pool automatic-deletion thresholds. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > minute </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Minute frequency for the snapshot schedule rule. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > retention_time </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Period of time in seconds for which to keep the snapshot. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > retention_time_in_hours </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Period of time in hours for which to keep the snapshot. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > rule_type </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Type of the rule applied to snapshot schedule. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=7 > storage_resources </td>
                <td> complex </td>
                <td>success</td>
                <td> Details of storage resources for which snapshot schedule applied. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=6 > UnityStorageResourceList </td>
                    <td> complex </td>
                    <td>success</td>
                    <td> List of storage resources for which snapshot schedule applied. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=5 > UnityStorageResource </td>
                        <td> complex </td>
                        <td>success</td>
                        <td> Detail of storage resource. </td>
                    </tr>
                                                                                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
