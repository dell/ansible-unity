
**Ansible Modules for Dell EMC Unity** 
=========================================
### Product Guide 1.1

>   © 2020 Dell Inc. or its subsidiaries. All rights reserved. Dell,
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Content
-------

-   [Common Parameters](#common-parameters)
-   [Consistency Group Module](#consistency-group-module)
    -   [Synopsis](#synopsis)
    -   [Parameters](#parameters)
    -   [Examples](#examples)
    -   [Return Values](#return-values)
    -   [Authors](#authors)
-   [Filesystem Module](#filesystem-module)
    -   [Synopsis](#synopsis-1)
    -   [Parameters](#parameters-1)
    -   [Notes](#notes)
    -   [Examples](#examples-1)
    -   [Return Values](#return-values-1)
    -   [Authors](#authors-1)
-   [Filesystem Snapshot Module](#filesystem-snapshot-module)
    -   [Synopsis](#synopsis-2)
    -   [Parameters](#parameters-2)
    -   [Notes](#notes-1)
    -   [Examples](#examples-2)
    -   [Return Values](#return-values-2)
    -   [Authors](#authors-2)
-   [Gatherfacts Module](#gatherfacts-module)
    -   [Synopsis](#synopsis-3)
    -   [Parameters](#parameters-3)
    -   [Examples](#examples-3)
    -   [Return Values](#return-values-3)
    -   [Authors](#authors-3)
-   [Host Module](#host--module)
    -   [Synopsis](#synopsis-4)
    -   [Parameters](#parameters-4)
    -   [Examples](#examples-4)
    -   [Return Values](#return-values-4)
    -   [Authors](#authors-4)
-   [NAS Server Module](#nas-server-module)
    -   [Synopsis](#synopsis-5)
    -   [Parameters](#parameters-5)
    -   [Examples](#examples-5)
    -   [Return Values](#return-values-5)
    -   [Authors](#authors-5)
-   [NFS Export Module](#nfs-export-module)
    -   [Synopsis](#synopsis-6)
    -   [Parameters](#parameters-6)
    -   [Examples](#examples-6)
    -   [Return Values](#return-values-6)
    -   [Authors](#authors-6)
-   [SMB Share Module](#smb-share-module)
    -   [Synopsis](#synopsis-7)
    -   [Parameters](#parameters-7)
    -   [Notes](#notes-2)
    -   [Examples](#examples-7)
    -   [Return Values](#return-values-7)
    -   [Authors](#authors-7)
-   [Snapshot Module](#snapshot-module)
    -   [Synopsis](#synopsis-8)
    -   [Requirements](#requirements-8)
    -   [Parameters](#parameters-8)
    -   [Notes](#notes-1)
    -   [Examples](#examples-8)
    -   [Return Values](#return-values-8)
    -   [Authors](#authors-8)
-   [Snapshot Schedule Module](#snapshot-schedule-module)
    -   [Synopsis](#synopsis-9)
    -   [Parameters](#parameters-9)
    -   [Notes](#notes-3)
    -   [Examples](#examples-9)
    -   [Return Values](#return-values-9)
    -   [Authors](#authors-9)
-   [Storage Pool Module](#storage-pool-module)
    -   [Synopsis](#synopsis-10)
    -   [Parameters](#parameters-10)
    -   [Notes](#notes-4)
    -   [Examples](#examples-10)
    -   [Return Values](#return-values-10)
    -   [Authors](#authors-10)
-   [Volume Module](volume-module)
    -   [Synopsis](#synopsis-11)
    -   [Parameters](#parameters-11)
    -   [Examples](#examples-11)
    -   [Return Values](#return-values-11)
    -   [Authors](#authors-11)

Common Parameters
=======================
These parameters are applicable to all the modules respectively along with module specific parameters.

**NOTE:** If the parameter is mandatory, then required=true else it is an optional parameter. This is applicable to all the module specific parameters also.
<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-username"></div>
                <b>username</b>
                <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>, <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>username of the Unity management server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-password"></div>
                <b>password</b>
                <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>, <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>the password of the Unity management server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-unispherehost"></div>
                <b>unispherehost</b>
                <a class="ansibleOptionLink" href="#parameter-unispherehost" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP or FQDN of the Unity management server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-port"></div>
                <b>port</b>
                <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">443</div>
                                </td>
                                                            <td>
                                        <div>Port number through which communication happens with Unity management server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-verifycert"></div>
                <b>verifycert</b>
                <a class="ansibleOptionLink" href="#parameter-verifycert" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Boolean variable to specify whether or not to validate SSL certificate.</div>
                                        <div>True - Indicates that the SSL certificate should be verified.</div>
                                        <div>False - Indicates that the SSL certificate should not be verified.</div>
                                                    </td>
        </tr>
                    </table>

Consistency Group Module
=====================================================================================================

Synopsis
--------

-   Managing the consistency group on the Unity storage system includes
    creating new consistency group, adding volumes to consistency group,
    removing volumes from consistency group, renaming consistency group,
    modifying attributes of consistency group and deleting consistency
    group.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-cg_id"></div>
                <b>cg_id</b>
                <a class="ansibleOptionLink" href="#parameter-cg_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the consistency group.</div>
                                        <div>It can be used only for get, modify, add/remove volumes or delete operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-cg_name"></div>
                <b>cg_name</b>
                <a class="ansibleOptionLink" href="#parameter-cg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the consistency group.</div>
                                        <div>It is mandatory for create operation.</div>
                                        <div>Specify either cg_name or cg_id (but not both) for any operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Description of the consistency group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_cg_name"></div>
                <b>new_cg_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_cg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new name of the consistency group, used in rename operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snap_schedule"></div>
                <b>snap_schedule</b>
                <a class="ansibleOptionLink" href="#parameter-snap_schedule" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Snapshot schedule assigned to the consistency group.</div>
                                        <div>Specifying an empty string &quot;&quot; removes the existing snapshot schedule from Consistency Group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>, <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the consistency group should exist or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-tiering_policy"></div>
                <b>tiering_policy</b>
                <a class="ansibleOptionLink" href="#parameter-tiering_policy" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>AUTOTIER_HIGH</li>
                                                                                                                                                                                            <li>AUTOTIER</li>
                                                                                                                                                                                            <li>HIGHEST</li>
                                                                                                                                                                                            <li>LOWEST</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vol_state"></div>
                <b>vol_state</b>
                <a class="ansibleOptionLink" href="#parameter-vol_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present-in-group</li>
                                                                                                                                                                                            <li>absent-in-group</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>String variable, describes the state of volumes inside consistency group.</div>
                                        <div>If volumes are given, then vol_state should also be specified.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-volumes"></div>
                <b>volumes</b>
                <a class="ansibleOptionLink" href="#parameter-volumes" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>, <span style="color: purple">elements: dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This is a list of volumes.</div>
                                        <div>Either the volume ID or name must be provided for adding/removing existing volumes from consistency group.</div>
                                        <div>If volumes are given, then vol_state should also be specified.</div>
                                        <div>Volumes cannot be added/removed from consistency group, if the consistency group or the volume has snapshots.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="5">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="5">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="5">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details"></div>
                <b>consistency_group_details</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When consistency group exists</td>
            <td>
                                        <div>Details of the consistency group</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID given to the consistency group</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/luns"></div>
                <b>luns</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/luns" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of volumes part of consistency group</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/luns/UnityLunList"></div>
                <b>UnityLunList</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/luns/UnityLunList" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of volumes part of consistency group</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/luns/UnityLunList/UnityLun"></div>
                <b>UnityLun</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/luns/UnityLunList/UnityLun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Detail of volume</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/luns/UnityLunList/UnityLun/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/luns/UnityLunList/UnityLun/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID given to volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/luns/UnityLunList/UnityLun/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/luns/UnityLunList/UnityLun/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/relocation_policy"></div>
                <b>relocation_policy</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/relocation_policy" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>FAST VP tiering policy for the consistency group</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snap_schedule"></div>
                <b>snap_schedule</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snap_schedule" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Snapshot schedule applied to consistency group</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snap_schedule/UnitySnapSchedule"></div>
                <b>UnitySnapSchedule</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snap_schedule/UnitySnapSchedule" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Snapshot schedule applied to consistency group</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snap_schedule/UnitySnapSchedule/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snap_schedule/UnitySnapSchedule/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID given to the snapshot schedule</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snap_schedule/UnitySnapSchedule/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snap_schedule/UnitySnapSchedule/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the snapshot schedule</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snapshots"></div>
                <b>snapshots</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snapshots" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of snapshots of consistency group</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snapshots/creation_time"></div>
                <b>creation_time</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snapshots/creation_time" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date and time on which the snapshot was taken</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snapshots/expirationTime"></div>
                <b>expirationTime</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snapshots/expirationTime" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date and time after which the snapshot will expire</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snapshots/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snapshots/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the snapshot</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snapshots/storageResource"></div>
                <b>storageResource</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snapshots/storageResource" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Storage resource for which the snapshot was taken</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snapshots/storageResource/UnityStorageResource"></div>
                <b>UnityStorageResource</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snapshots/storageResource/UnityStorageResource" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of the storage resource</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-consistency_group_details/snapshots/storageResource/UnityStorageResource/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-consistency_group_details/snapshots/storageResource/UnityStorageResource/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The id of the storage resource</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
-------------

-   Akash Shendge (@shenda1) &lt;<ansible.team@dell.com>&gt;

Filesystem Module
=======================================================================================

Synopsis
--------

-   Managing filesystem on Unity storage system includes- Create new
    filesystem, Modify filesystem attributes, Display filesystem
    details, Display filesystem snapshots, Delete filesystem

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-access_policy"></div>
                <b>access_policy</b>
                <a class="ansibleOptionLink" href="#parameter-access_policy" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>NATIVE</li>
                                                                                                                                                                                            <li>UNIX</li>
                                                                                                                                                                                            <li>WINDOWS</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Access policy of a filesystem.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-cap_unit"></div>
                <b>cap_unit</b>
                <a class="ansibleOptionLink" href="#parameter-cap_unit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>GB</li>
                                                                                                                                                                                            <li>TB</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The unit of the filesystem size. It defaults to &#x27;GB&#x27;, if not specified.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-data_reduction"></div>
                <b>data_reduction</b>
                <a class="ansibleOptionLink" href="#parameter-data_reduction" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Boolean variable, specifies whether or not to enable compression. Compression is supported only for thin filesystem</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Description about the filesystem.</div>
                                        <div>Description can be removed by passing empty string (&quot;&quot;).</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-filesystem_id"></div>
                <b>filesystem_id</b>
                <a class="ansibleOptionLink" href="#parameter-filesystem_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The id of the filesystem.It&#x27;s mutually exclusive with &#x27;filesystem_name&#x27;</div>
                                        <div>It can be used only for get, modify or delete operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-filesystem_name"></div>
                <b>filesystem_name</b>
                <a class="ansibleOptionLink" href="#parameter-filesystem_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the filesystem. Mandatory only for create operation. All the operations are supported through &#x27;filesystem_name&#x27;</div>
                                        <div>It&#x27;s mutually exclusive with &#x27;filesystem_id&#x27;.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-is_thin"></div>
                <b>is_thin</b>
                <a class="ansibleOptionLink" href="#parameter-is_thin" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Boolean variable, specifies whether or not it&#x27;s a thin filesystem.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-locking_policy"></div>
                <b>locking_policy</b>
                <a class="ansibleOptionLink" href="#parameter-locking_policy" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>ADVISORY</li>
                                                                                                                                                                                            <li>MANDATORY</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>File system locking policies. These policy choices control whether the NFSv4 range locks must be honored.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_id"></div>
                <b>nas_server_id</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the NAS server on which filesystem will be hosted.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_name"></div>
                <b>nas_server_name</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the NAS server on which filesystem will be hosted.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-pool_id"></div>
                <b>pool_id</b>
                <a class="ansibleOptionLink" href="#parameter-pool_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This is the ID of the pool where the filesystem will be created.</div>
                                        <div>Either the pool_name or pool_id must be provided to create a new filesystem.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-pool_name"></div>
                <b>pool_name</b>
                <a class="ansibleOptionLink" href="#parameter-pool_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This is the name of the pool where the filesystem will be created.</div>
                                        <div>Either the pool_name or pool_id must be provided to create a new filesystem.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-size"></div>
                <b>size</b>
                <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The size of the filesystem.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-smb_properties"></div>
                <b>smb_properties</b>
                <a class="ansibleOptionLink" href="#parameter-smb_properties" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=dictionary</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Advance settings for SMB. It contains optional candidate variables</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-smb_properties/is_smb_notify_on_access_enabled"></div>
                <b>is_smb_notify_on_access_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-smb_properties/is_smb_notify_on_access_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether notifications of changes to directory file structure are enabled.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-smb_properties/is_smb_notify_on_write_enabled"></div>
                <b>is_smb_notify_on_write_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-smb_properties/is_smb_notify_on_write_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether file write notifications are enabled on the file system.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-smb_properties/is_smb_op_locks_enabled"></div>
                <b>is_smb_op_locks_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-smb_properties/is_smb_op_locks_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether opportunistic file locking is enabled on the file system.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-smb_properties/is_smb_sync_writes_enabled"></div>
                <b>is_smb_sync_writes_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-smb_properties/is_smb_sync_writes_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether the synchronous writes option is enabled on the file system.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-smb_properties/smb_notify_on_change_dir_depth"></div>
                <b>smb_notify_on_change_dir_depth</b>
                <a class="ansibleOptionLink" href="#parameter-smb_properties/smb_notify_on_change_dir_depth" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Integer variable, determines the lowest directory level to which the enabled notifications apply.</div>
                                        <div>Minimum value is 1.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>, <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State variable to determine whether filesystem will exist or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-supported_protocols"></div>
                <b>supported_protocols</b>
                <a class="ansibleOptionLink" href="#parameter-supported_protocols" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>NFS</li>
                                                                                                                                                                                            <li>CIFS</li>
                                                                                                                                                                                            <li>MULTIPROTOCOL</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Protocols supported by the file system.</div>
                                        <div>It will be overridden by NAS server configuration if NAS Server is Multiprotocol</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-tiering_policy"></div>
                <b>tiering_policy</b>
                <a class="ansibleOptionLink" href="#parameter-tiering_policy" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>AUTOTIER_HIGH</li>
                                                                                                                                                                                            <li>AUTOTIER</li>
                                                                                                                                                                                            <li>HIGHEST</li>
                                                                                                                                                                                            <li>LOWEST</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Notes
-----

- SMB shares, NFS exports and snapshots associated with filesystem
needs to be deleted prior to deleting a filesystem.

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="4">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-filesystem_details"></div>
                <b>filesystem_details</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When filesystem exists</td>
            <td>
                                        <div>Details of the filesystem</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/cifs_notify_on_change_dir_depth"></div>
                <b>cifs_notify_on_change_dir_depth</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/cifs_notify_on_change_dir_depth" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates the lowest directory level to which the enabled notifications apply, if any.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/description" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>description about the filesystem</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system generated ID given to the filesystem</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/is_cifs_notify_on_access_enabled"></div>
                <b>is_cifs_notify_on_access_enabled</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/is_cifs_notify_on_access_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the system generates a notification when a user accesses the file system.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/is_cifs_notify_on_write_enabled"></div>
                <b>is_cifs_notify_on_write_enabled</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/is_cifs_notify_on_write_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the system generates a notification when the file system is written to.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/is_cifs_op_locks_enabled"></div>
                <b>is_cifs_op_locks_enabled</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/is_cifs_op_locks_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether opportunistic file locks are enabled for the file system.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/is_cifs_sync_writes_enabled"></div>
                <b>is_cifs_sync_writes_enabled</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/is_cifs_sync_writes_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the CIFS synchronous writes option is enabled for the file system.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/is_data_reduction_enabled"></div>
                <b>is_data_reduction_enabled</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/is_data_reduction_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether or not compression enabled on this filesystem</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/is_thin_enabled"></div>
                <b>is_thin_enabled</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/is_thin_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether thin provisioning is enabled for this filesystem</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the filesystem</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/nas_server"></div>
                <b>nas_server</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/nas_server" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The NAS Server details on which this filesystem is hosted.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/nas_server/nas_server"></div>
                <b>nas_server</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/nas_server/nas_server" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>nas_server details.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/nas_server/nas_server/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/nas_server/nas_server/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID given to the NAS Server</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/nas_server/nas_server/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/nas_server/nas_server/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the NAS Server</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/pool"></div>
                <b>pool</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/pool" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The pool in which this filesystem is allocated</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/pool/UnityPool"></div>
                <b>UnityPool</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/pool/UnityPool" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unity pool in which this filesystem is allocated</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/pool/UnityPool/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/pool/UnityPool/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID given to the pool</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/pool/UnityPool/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/pool/UnityPool/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the storage pool</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/size_total_with_unit"></div>
                <b>size_total_with_unit</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/size_total_with_unit" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Size of the filesystem with actual unit.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/snap_list"></div>
                <b>snap_list</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/snap_list" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                   / <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The list of snapshots of this filesystem.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/snap_list/snap_list"></div>
                <b>snap_list</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/snap_list/snap_list" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Filesystem snapshots.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/snap_list/snap_list/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/snap_list/snap_list/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID given to the filesystem snapshot</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/snap_list/snap_list/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/snap_list/snap_list/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the filesystem snapshot</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-filesystem_details/tiering_policy"></div>
                <b>tiering_policy</b>
                <a class="ansibleOptionLink" href="#return-filesystem_details/tiering_policy" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Tiering policy applied to this filesystem</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
---------

-   Arindam Datta (@dattaarindam) &lt;<ansible.team@dell.com>&gt;

Filesystem Snapshot Module
==============================================================================================================

Synopsis
--------

-   Managing Filesystem Snapshot on the Unity storage system includes
    create filesystem snapshot, get filesystem snapshot, modify
    filesystem snapshot and delete filesystem snapshot.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-auto_delete"></div>
                <b>auto_delete</b>
                <a class="ansibleOptionLink" href="#parameter-auto_delete" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>This option specifies whether or not the filesystem snapshot will be automatically deleted.</div>
                                        <div>If set to true, the filesystem snapshot will expire based on the pool auto deletion policy.</div>
                                        <div>If set to false, the filesystem snapshot will not be auto deleted based on the pool auto deletion policy.</div>
                                        <div>auto_delete can not be set to True, if expiry_time is specified.</div>
                                        <div>If during creation neither auto_delete nor expiry_time is mentioned then the filesystem snapshot will be created keeping auto_delete as True.</div>
                                        <div>Once the expiry_time is set, then the filesystem snapshot cannot be assigned to the auto delete policy.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The additional information about the filesystem snapshot can be provided using this option.</div>
                                        <div>The description can be removed by passing an empty string.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-expiry_time"></div>
                <b>expiry_time</b>
                <a class="ansibleOptionLink" href="#parameter-expiry_time" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This option is for specifying the date and time after which the filesystem snapshot will expire.</div>
                                        <div>The time is to be mentioned in UTC timezone.</div>
                                        <div>The format is &quot;MM/DD/YYYY HH:MM&quot;. Year must be in 4 digits.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filesystem_id"></div>
                <b>filesystem_id</b>
                <a class="ansibleOptionLink" href="#parameter-filesystem_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the Filesystem for which snapshot is created.</div>
                                        <div>For creation of filesystem snapshot either filesystem_id or filesystem_name is required.</div>
                                        <div>Not required for other operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filesystem_name"></div>
                <b>filesystem_name</b>
                <a class="ansibleOptionLink" href="#parameter-filesystem_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the Filesystem for which snapshot is created.</div>
                                        <div>For creation of filesystem snapshot either filesystem_name or filesystem_id is required.</div>
                                        <div>Not required for other operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-fs_access_type"></div>
                <b>fs_access_type</b>
                <a class="ansibleOptionLink" href="#parameter-fs_access_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>Checkpoint</li>
                                                                                                                                                                                            <li>Protocol</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Access type of the filesystem snapshot.</div>
                                        <div>Required only during creation of filesystem snapshot.</div>
                                        <div>If not given, snapshot&#x27;s access type will be &#x27;Checkpoint&#x27;.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_id"></div>
                <b>nas_server_id</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the NAS server in which the Filesystem is created.</div>
                                        <div>For creation of filesystem snapshot either filesystem_id or filesystem_name is required.</div>
                                        <div>Not required for other operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_name"></div>
                <b>nas_server_name</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the NAS server in which the Filesystem is created.</div>
                                        <div>For creation of filesystem snapshot either nas_server_name or nas_server_id is required.</div>
                                        <div>Not required for other operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>
                <b>snapshot_id</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>During creation snapshot_id is auto generated.</div>
                                        <div>For all other operations either snapshot_id or snapshot_name is required.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>
                <b>snapshot_name</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the filesystem snapshot.</div>
                                        <div>Mandatory parameter for creating a filesystem snapshot.</div>
                                        <div>For all other operations either snapshot_name or snapshot_id is required.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>, <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The state option is used to mention the existence of the filesystem snapshot.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Notes
-----
- Filesystem snapshot cannot be deleted, if it has nfs or smb share.

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details"></div>
                <b>filesystem_snapshot_details</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When filesystem snapshot exists</td>
            <td>
                                        <div>Details of the filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/access_type"></div>
                <b>access_type</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/access_type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Access type of filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/attached_wwn"></div>
                <b>attached_wwn</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/attached_wwn" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Attached WWN details.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/creation_time"></div>
                <b>creation_time</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/creation_time" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Creation time of filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/creator_schedule"></div>
                <b>creator_schedule</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/creator_schedule" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Creator schedule of filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/creator_type"></div>
                <b>creator_type</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/creator_type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Creator type for filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/creator_user"></div>
                <b>creator_user</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/creator_user" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Creator user for filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/description" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Description of the filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/expiration_time"></div>
                <b>expiration_time</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/expiration_time" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date and time after which the filesystem snapshot will expire.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/filesystem_id"></div>
                <b>filesystem_id</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/filesystem_id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Id of the filesystem for which the snapshot exists.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/filesystem_name"></div>
                <b>filesystem_name</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/filesystem_name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the filesystem for which the snapshot exists.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique identifier of the filesystem snapshot instance.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/is_auto_delete"></div>
                <b>is_auto_delete</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/is_auto_delete" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Is the filesystem snapshot is auto deleted or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/nas_server_id"></div>
                <b>nas_server_id</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/nas_server_id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Id of the NAS server on which filesystem exists.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/nas_server_name"></div>
                <b>nas_server_name</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/nas_server_name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the NAS server on which filesystem exists.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-filesystem_snapshot_details/size"></div>
                <b>size</b>
                <a class="ansibleOptionLink" href="#return-filesystem_snapshot_details/size" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Size of the filesystem snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
---------------

-   Rajshree Khare (@kharer5) &lt;<ansible.team@dell.com>&gt;

Gatherfacts Module
========================================================================================

Synopsis
--------

-   Gathering information about DellEMC Unity storage system includes
    Get the details of Unity array, Get list of Hosts in Unity array,
    Get list of FC initiators in Unity array, Get list of iSCSI
    initiators in Unity array, Get list of Consistency groups in Unity
    array, Get list of Storage pools in Unity array, Get list of Volumes
    in Unity array, Get list of Snapshot schedules in Unity array, Get
    list of NAS servers in Unity array, Get list of File systems in
    Unity array, Get list of Snapshots in Unity array, Get list of SMB
    shares in Unity array, Get list of NFS exports in Unity array

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-gather_subset"></div>
                <b>gather_subset</b>
                <a class="ansibleOptionLink" href="#parameter-gather_subset" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>, <span style="color: purple">elements=string</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>host</li>
                                                                                                                                                                                            <li>fc_initiator</li>
                                                                                                                                                                                            <li>iscsi_initiator</li>
                                                                                                                                                                                            <li>cg</li>
                                                                                                                                                                                            <li>storage_pool</li>
                                                                                                                                                                                            <li>vol</li>
                                                                                                                                                                                            <li>snapshot_schedule</li>
                                                                                                                                                                                            <li>nas_server</li>
                                                                                                                                                                                            <li>file_system</li>
                                                                                                                                                                                            <li>snapshot</li>
                                                                                                                                                                                            <li>nfs_export</li>
                                                                                                                                                                                            <li>smb_share</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>List of string variables to specify the Unity storage system entities for which information is required.</div>
                                        <div>host</div>
                                        <div>fc_initiator</div>
                                        <div>iscsi_initiator</div>
                                        <div>cg</div>
                                        <div>storage_pool</div>
                                        <div>vol</div>
                                        <div>snapshot_schedule</div>
                                        <div>nas_server</div>
                                        <div>file_system</div>
                                        <div>snapshot</div>
                                        <div>nfs_export</div>
                                        <div>smb_share</div>
                                                    </td>
        </tr>
         </table>
<br/>

Examples
--------

``` yaml+jinja
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
```

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Array_Details"></div>
                <b>Array_Details</b>
                <a class="ansibleOptionLink" href="#return-Array_Details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Details of the Unity Array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/api_version"></div>
                <b>api_version</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/api_version" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The current api version of the Unity Array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/earliest_api_version"></div>
                <b>earliest_api_version</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/earliest_api_version" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The earliest api version of the Unity Array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/model"></div>
                <b>model</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/model" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The model of the Unity Array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the Unity Array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/software_version"></div>
                <b>software_version</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/software_version" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The software version of the Unity Array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Consistency_Groups"></div>
                <b>Consistency_Groups</b>
                <a class="ansibleOptionLink" href="#return-Consistency_Groups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When Consistency Groups exist.</td>
            <td>
                                        <div>Details of the Consistency Groups.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Consistency_Groups/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Consistency_Groups/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the Consistency Group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Consistency_Groups/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Consistency_Groups/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the Consistency Group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-FC_initiators"></div>
                <b>FC_initiators</b>
                <a class="ansibleOptionLink" href="#return-FC_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When FC initiator exist.</td>
            <td>
                                        <div>Details of the FC initiators.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-FC_initiators/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-FC_initiators/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The id of the FC initiator.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-FC_initiators/WWN"></div>
                <b>WWN</b>
                <a class="ansibleOptionLink" href="#return-FC_initiators/WWN" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The WWN of the FC initiator.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-File_Systems"></div>
                <b>File_Systems</b>
                <a class="ansibleOptionLink" href="#return-File_Systems" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When File Systems exist.</td>
            <td>
                                        <div>Details of the File Systems.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-File_Systems/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-File_Systems/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the File System.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-File_Systems/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-File_Systems/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the File System.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Hosts"></div>
                <b>Hosts</b>
                <a class="ansibleOptionLink" href="#return-Hosts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When hosts exist.</td>
            <td>
                                        <div>Details of the hosts.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Hosts/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Hosts/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Hosts/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Hosts/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-ISCSI_initiators"></div>
                <b>ISCSI_initiators</b>
                <a class="ansibleOptionLink" href="#return-ISCSI_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When ISCSI initiators exist.</td>
            <td>
                                        <div>Details of the ISCSI initiators.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-ISCSI_initiators/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-ISCSI_initiators/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The id of the ISCSI initiator.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-ISCSI_initiators/IQN"></div>
                <b>IQN</b>
                <a class="ansibleOptionLink" href="#return-ISCSI_initiators/IQN" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The IQN of the ISCSI initiator.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-NAS_Servers"></div>
                <b>NAS_Servers</b>
                <a class="ansibleOptionLink" href="#return-NAS_Servers" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When NAS Servers exist.</td>
            <td>
                                        <div>Details of the NAS Servers.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-NAS_Servers/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-NAS_Servers/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the NAS Server.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-NAS_Servers/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-NAS_Servers/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the NAS Server.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-NFS_Exports"></div>
                <b>NFS_Exports</b>
                <a class="ansibleOptionLink" href="#return-NFS_Exports" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When NFS Exports exist.</td>
            <td>
                                        <div>Details of the NFS Exports.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-NFS_Exports/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-NFS_Exports/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the NFS Export.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-NFS_Exports/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-NFS_Exports/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the NFS Export.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-SMB_Shares"></div>
                <b>SMB_Shares</b>
                <a class="ansibleOptionLink" href="#return-SMB_Shares" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When SMB Shares exist.</td>
            <td>
                                        <div>Details of the SMB Shares.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SMB_Shares/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-SMB_Shares/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the SMB Share.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SMB_Shares/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-SMB_Shares/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the SMB Share.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Snapshot_Schedules"></div>
                <b>Snapshot_Schedules</b>
                <a class="ansibleOptionLink" href="#return-Snapshot_Schedules" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When Snapshot Schedules exist.</td>
            <td>
                                        <div>Details of the Snapshot Schedules.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Snapshot_Schedules/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Snapshot_Schedules/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the Snapshot Schedule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Snapshot_Schedules/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Snapshot_Schedules/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the Snapshot Schedule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Snapshots"></div>
                <b>Snapshots</b>
                <a class="ansibleOptionLink" href="#return-Snapshots" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When Snapshots exist.</td>
            <td>
                                        <div>Details of the Snapshots.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Snapshots/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Snapshots/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the Snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Snapshots/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Snapshots/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the Snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Storage_Pools"></div>
                <b>Storage_Pools</b>
                <a class="ansibleOptionLink" href="#return-Storage_Pools" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When Storage Pools exist.</td>
            <td>
                                        <div>Details of the Storage Pools.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Storage_Pools/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Storage_Pools/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the Storage Pool.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Storage_Pools/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Storage_Pools/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the Storage Pool.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Volumes"></div>
                <b>Volumes</b>
                <a class="ansibleOptionLink" href="#return-Volumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When Volumes exist.</td>
            <td>
                                        <div>Details of the Volumes.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Volumes/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Volumes/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the Volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Volumes/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Volumes/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the Volume.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
------------

-   Rajshree Khare (@kharer5) &lt;<ansible.team@dell.com>&gt;
-   Akash Shendge (@shenda1) &lt;<ansible.team@dell.com>&gt;

Host Module
========================================================================

Synopsis
--------

-   Creation of a Host.
-   Addition of initiators to Host.
-   Removal of initiators from Host.
-   Modification of host attributes.
-   Get details of a Host.
-   Deletion of a Host.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Host description.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_id"></div>
                <b>host_id</b>
                <a class="ansibleOptionLink" href="#parameter-host_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Unique identifier of the host.</div>
                                        <div>host_id is auto generated during creation.</div>
                                        <div>Except create, all other operations require either host_id or host_name.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the host.</div>
                                        <div>Mandatory for host creation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_os"></div>
                <b>host_os</b>
                <a class="ansibleOptionLink" href="#parameter-host_os" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>AIX</li>
                                                                                                                                                                                            <li>Citrix XenServer</li>
                                                                                                                                                                                            <li>HP-UX</li>
                                                                                                                                                                                            <li>IBM VIOS</li>
                                                                                                                                                                                            <li>Linux</li>
                                                                                                                                                                                            <li>Mac OS</li>
                                                                                                                                                                                            <li>Solaris</li>
                                                                                                                                                                                            <li>VMware ESXi</li>
                                                                                                                                                                                            <li>Windows Client</li>
                                                                                                                                                                                            <li>Windows Server</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Operating system running on the host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-initiator_state"></div>
                <b>initiator_state</b>
                <a class="ansibleOptionLink" href="#parameter-initiator_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present-in-host</li>
                                                                                                                                                                                            <li>absent-in-host</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State of the initiator.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-initiators"></div>
                <b>initiators</b>
                <a class="ansibleOptionLink" href="#parameter-initiators" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                      <span style="color: purple">elements=string</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>List of initiators to be added/removed to/from host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_host_name"></div>
                <b>new_host_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name for the host.</div>
                                        <div>Only required in rename host operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present</li>
                                                                                                                                                                                            <li>absent</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State of the host.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-host_details"></div>
                <b>host_details</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When host exists.</td>
            <td>
                                        <div>Details of the host.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details/description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-host_details/description" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Description about the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details/fc_host_initiators"></div>
                <b>fc_host_initiators</b>
                <a class="ansibleOptionLink" href="#return-host_details/fc_host_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of the FC initiators associated with the host.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/fc_host_initiators/UnityHostInitiatorList"></div>
                <b>UnityHostInitiatorList</b>
                <a class="ansibleOptionLink" href="#return-host_details/fc_host_initiators/UnityHostInitiatorList" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>FC initiators with system generated unique hash value.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-host_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID given to the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details/iscsi_host_initiators"></div>
                <b>iscsi_host_initiators</b>
                <a class="ansibleOptionLink" href="#return-host_details/iscsi_host_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of the ISCSI initiators associated with the host.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/iscsi_host_initiators/UnityHostInitiatorList"></div>
                <b>UnityHostInitiatorList</b>
                <a class="ansibleOptionLink" href="#return-host_details/iscsi_host_initiators/UnityHostInitiatorList" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ISCSI initiators with sytem genrated unique hash value.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-host_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details/os_type"></div>
                <b>os_type</b>
                <a class="ansibleOptionLink" href="#return-host_details/os_type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Operating system running on the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-host_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>HostTypeEnum of the host.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
----------------

-   Rajshree Khare (@kharer5) &lt;<ansible.team@dell.com>&gt;

NAS Server Module
======================================================================================

Synopsis
--------

-   Managing NAS servers on Unity storage system includes get,
    modification to the NAS servers.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-allow_unmapped_user"></div>
                <b>allow_unmapped_user</b>
                <a class="ansibleOptionLink" href="#parameter-allow_unmapped_user" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>This flag is used to mandatorily disable access in case of any user mapping failure.</div>
                                        <div>If true, then enable access in case of any user mapping failure.</div>
                                        <div>If false, then disable access in case of any user mapping failure.</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-current_unix_directory_service"></div>
                <b>current_unix_directory_service</b>
                <a class="ansibleOptionLink" href="#parameter-current_unix_directory_service" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>NONE</li>
                                                                                                                                                                                            <li>NIS</li>
                                                                                                                                                                                            <li>LOCAL</li>
                                                                                                                                                                                            <li>LDAP</li>
                                                                                                                                                                                            <li>LOCAL_THEN_NIS</li>
                                                                                                                                                                                            <li>LOCAL_THEN_LDAP</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>This is the directory service used for querying identity information for UNIX (such as UIDs, GIDs, net groups).</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-default_unix_user"></div>
                <b>default_unix_user</b>
                <a class="ansibleOptionLink" href="#parameter-default_unix_user" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Default Unix user name used for granting access in the case of Windows to Unix user mapping failure.</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-default_windows_user"></div>
                <b>default_windows_user</b>
                <a class="ansibleOptionLink" href="#parameter-default_windows_user" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Default windows user name used for granting access in the case of Unix to Windows user mapping failure</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-enable_windows_to_unix_username_mapping"></div>
                <b>enable_windows_to_unix_username_mapping</b>
                <a class="ansibleOptionLink" href="#parameter-enable_windows_to_unix_username_mapping" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>This parameter indicates whether a Unix to/from Windows user name mapping is enabled.</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_backup_only"></div>
                <b>is_backup_only</b>
                <a class="ansibleOptionLink" href="#parameter-is_backup_only" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>It specifies whether the NAS server is used as backup only.</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_multiprotocol_enabled"></div>
                <b>is_multiprotocol_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-is_multiprotocol_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>This parameter indicates whether multiprotocol sharing mode is enabled.</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_packet_reflect_enabled"></div>
                <b>is_packet_reflect_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-is_packet_reflect_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>If the packet has to be reflected, then this parameter has to be set to True.</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_replication_destination"></div>
                <b>is_replication_destination</b>
                <a class="ansibleOptionLink" href="#parameter-is_replication_destination" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>It specifies whether the NAS server is a replication destination.</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_id"></div>
                <b>nas_server_id</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the NAS server.</div>
                                        <div>nas_server_name and nas_server_id are mutually exclusive parameters.</div>
                                        <div>Any one of both is required to perform the task.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_name"></div>
                <b>nas_server_name</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The Name of the NAS server.</div>
                                        <div>nas_server_name and nas_server_id are mutually exclusive parameters.</div>
                                        <div>Any one of both is required to perform the task.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_new_name"></div>
                <b>nas_server_new_name</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new name of the NAS server.</div>
                                        <div>It can be mentioned during modification of NAS server.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present</li>
                                                                                                                                                                                            <li>absent</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define the state of NAS server on the array.</div>
                                        <div>present indicates that NAS server should exist on the system after the task is executed.</div>
                                        <div>Right now deletion of NAS server is not supported. Hence, if state is set to absent for any existing nas server then error will be thrown.</div>
                                        <div>For any non existing NAS server if state is set to absent then it will return None.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                        <div style="font-size: smaller"><b>Sample:</b></div>
                                            <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-nas_server_details"></div>
                <b>nas_server_details</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When NAS server exists.</td>
            <td>
                                        <div>The NAS server details.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/allow_unmapped_user"></div>
                <b>allow_unmapped_user</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/allow_unmapped_user" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>enable/disable access status in case of any user mapping failure</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/current_unix_directory_service"></div>
                <b>current_unix_directory_service</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/current_unix_directory_service" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Directory service used for querying identity information for UNIX (such as UIDs, GIDs, net groups).</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/default_unix_user"></div>
                <b>default_unix_user</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/default_unix_user" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Default Unix user name used for granting access in the case of Windows to Unix user mapping failure.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/default_windows_user"></div>
                <b>default_windows_user</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/default_windows_user" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Default windows user name used for granting access in the case of Unix to Windows user mapping failure</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the NAS server</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/is_backup_only"></div>
                <b>is_backup_only</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/is_backup_only" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>whether the NAS server is used as backup only.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/is_multi_protocol_enabled"></div>
                <b>is_multi_protocol_enabled</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/is_multi_protocol_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether multiprotocol sharing mode is enabled</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/is_packet_reflect_enabled"></div>
                <b>is_packet_reflect_enabled</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/is_packet_reflect_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>If the packet reflect has to be enabled</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/is_replication_destination"></div>
                <b>is_replication_destination</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/is_replication_destination" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>If the NAS server is a replication destination then True.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/is_windows_to_unix_username_mapping_enabled"></div>
                <b>is_windows_to_unix_username_mapping_enabled</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/is_windows_to_unix_username_mapping_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether a Unix to/from Windows user name mapping is enabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nas_server_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-nas_server_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the NAS server</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
---------------

-   P Srinivas Rao (@srinivas-rao5) &lt;<ansible.team@dell.com>&gt;

NFS Export Module
================================================================================

Synopsis
--------

-   Managing NFS export on Unity storage system includes- Create new NFS
    export, Modify NFS export attributes, Display NFS export details,
    Delete NFS export

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-anonymous_gid"></div>
                <b>anonymous_gid</b>
                <a class="ansibleOptionLink" href="#parameter-anonymous_gid" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Specifies the group ID of the anonymous account</div>
                                        <div>If not specified at the time of creation, it will be set to 4294967294</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-anonymous_uid"></div>
                <b>anonymous_uid</b>
                <a class="ansibleOptionLink" href="#parameter-anonymous_uid" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Specifies the user ID of the anonymous account</div>
                                        <div>If not specified at the time of creation, it will be set to 4294967294</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-default_access"></div>
                <b>default_access</b>
                <a class="ansibleOptionLink" href="#parameter-default_access" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>NO_ACCESS</li>
                                                                                                                                                                                            <li>READ_ONLY</li>
                                                                                                                                                                                            <li>READ_WRITE</li>
                                                                                                                                                                                            <li>ROOT</li>
                                                                                                                                                                                            <li>READ_ONLY_ROOT</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Default access level for all hosts that can access the NFS export</div>
                                        <div>For hosts that need different access than the default, they can be configured by adding to the list</div>
                                        <div>If default_access is not mentioned during creation, then NFS export will be created with NO_ACCESS</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Description of the NFS export</div>
                                        <div>Optional parameter when creating a NFS export</div>
                                        <div>To modify description, pass the new value in description field</div>
                                        <div>To remove description, pass the empty value in description field</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-filesystem_id"></div>
                <b>filesystem_id</b>
                <a class="ansibleOptionLink" href="#parameter-filesystem_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the filesystem</div>
                                        <div>This is unique ID generated by Unity storage system</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-filesystem_name"></div>
                <b>filesystem_name</b>
                <a class="ansibleOptionLink" href="#parameter-filesystem_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the filesystem for which NFS export will be created.</div>
                                        <div>Either filesystem or snapshot is required for creation of the NFS.</div>
                                        <div>If filesystem name is specified, then nas_server is required to uniquely identify the filesystem</div>
                                        <div>If filesystem parameter is provided, then snapshot cannot be specified</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-host_state"></div>
                <b>host_state</b>
                <a class="ansibleOptionLink" href="#parameter-host_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present-in-export</li>
                                                                                                                                                                                            <li>absent-in-export</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the hosts can access the NFS export</div>
                                        <div>Required when adding or removing access of hosts from the export</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-min_security"></div>
                <b>min_security</b>
                <a class="ansibleOptionLink" href="#parameter-min_security" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SYS</li>
                                                                                                                                                                                            <li>KERBEROS</li>
                                                                                                                                                                                            <li>KERBEROS_WITH_INTEGRITY</li>
                                                                                                                                                                                            <li>KERBEROS_WITH_ENCRYPTION</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>NFS enforced security type for users accessing a NFS export</div>
                                        <div>If not specified at the time of creation, it will be set to SYS</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_id"></div>
                <b>nas_server_id</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the NAS server on which filesystem will be hosted</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_name"></div>
                <b>nas_server_name</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the NAS server on which filesystem will be hosted</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-nfs_export_id"></div>
                <b>nfs_export_id</b>
                <a class="ansibleOptionLink" href="#parameter-nfs_export_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the nfs export</div>
                                        <div>This is unique ID generated by Unity storage system</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-nfs_export_name"></div>
                <b>nfs_export_name</b>
                <a class="ansibleOptionLink" href="#parameter-nfs_export_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the nfs export</div>
                                        <div>Mandatory for create operation</div>
                                        <div>Specify either nfs_export_name or nfs_export_id(but not both) for any operation</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-no_access_hosts"></div>
                <b>no_access_hosts</b>
                <a class="ansibleOptionLink" href="#parameter-no_access_hosts" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                      <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Hosts with no access to the nfs export</div>
                                        <div>List of dictionaries. Each dictionary will have any of the key from host_name, host_id and ip_address</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-no_access_hosts/host_id"></div>
                <b>host_id</b>
                <a class="ansibleOptionLink" href="#parameter-no_access_hosts/host_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-no_access_hosts/host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-no_access_hosts/host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-no_access_hosts/ip_address"></div>
                <b>ip_address</b>
                <a class="ansibleOptionLink" href="#parameter-no_access_hosts/ip_address" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP address of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-path"></div>
                <b>path</b>
                <a class="ansibleOptionLink" href="#parameter-path" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Local path to export relative to the NAS server root</div>
                                        <div>With NFS, each export of a file_system or file_snap must have a unique local path</div>
                                        <div>Mandatory while creating NFS export</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-read_only_hosts"></div>
                <b>read_only_hosts</b>
                <a class="ansibleOptionLink" href="#parameter-read_only_hosts" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                      <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Hosts with read-only access to the NFS export</div>
                                        <div>List of dictionaries. Each dictionary will have any of the key from host_name, host_id and ip_address</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_only_hosts/host_id"></div>
                <b>host_id</b>
                <a class="ansibleOptionLink" href="#parameter-read_only_hosts/host_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_only_hosts/host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-read_only_hosts/host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_only_hosts/ip_address"></div>
                <b>ip_address</b>
                <a class="ansibleOptionLink" href="#parameter-read_only_hosts/ip_address" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP address of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-read_only_root_hosts"></div>
                <b>read_only_root_hosts</b>
                <a class="ansibleOptionLink" href="#parameter-read_only_root_hosts" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                      <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Hosts with read-only for root user access to the nfs export</div>
                                        <div>List of dictionaries. Each dictionary will have any of the key from host_name, host_id and ip_address</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_only_root_hosts/host_id"></div>
                <b>host_id</b>
                <a class="ansibleOptionLink" href="#parameter-read_only_root_hosts/host_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_only_root_hosts/host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-read_only_root_hosts/host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_only_root_hosts/ip_address"></div>
                <b>ip_address</b>
                <a class="ansibleOptionLink" href="#parameter-read_only_root_hosts/ip_address" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP address of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-read_write_hosts"></div>
                <b>read_write_hosts</b>
                <a class="ansibleOptionLink" href="#parameter-read_write_hosts" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                      <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Hosts with read and write access to the nfs export</div>
                                        <div>List of dictionaries. Each dictionary will have any of the key from host_name, host_id and ip_address</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_write_hosts/host_id"></div>
                <b>host_id</b>
                <a class="ansibleOptionLink" href="#parameter-read_write_hosts/host_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_write_hosts/host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-read_write_hosts/host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_write_hosts/ip_address"></div>
                <b>ip_address</b>
                <a class="ansibleOptionLink" href="#parameter-read_write_hosts/ip_address" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP address of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-read_write_root_hosts"></div>
                <b>read_write_root_hosts</b>
                <a class="ansibleOptionLink" href="#parameter-read_write_root_hosts" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                      <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Hosts with read and write for root user access to the nfs export</div>
                                        <div>List of dictionaries. Each dictionary will have any of the key from host_name, host_id and ip_address</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_write_root_hosts/host_id"></div>
                <b>host_id</b>
                <a class="ansibleOptionLink" href="#parameter-read_write_root_hosts/host_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_write_root_hosts/host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-read_write_root_hosts/host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-read_write_root_hosts/ip_address"></div>
                <b>ip_address</b>
                <a class="ansibleOptionLink" href="#parameter-read_write_root_hosts/ip_address" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP address of the host</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>
                <b>snapshot_id</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the snapshot</div>
                                        <div>This is unique ID generated by Unity storage system</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>
                <b>snapshot_name</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the snapshot for which nfs export will be created</div>
                                        <div>Either filesystem or snapshot is required for creation of the nfs export</div>
                                        <div>If snapshot parameter is provided, then filesystem cannot be specified</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State variable to determine whether NFS export will exist or not</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="4">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details"></div>
                <b>nfs_share_details</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When nfs export exists.</td>
            <td>
                                        <div>Details of the nfs export.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/anonymous_gid"></div>
                <b>anonymous_gid</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/anonymous_gid" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Group ID of the anonymous account</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/anonymous_uid"></div>
                <b>anonymous_uid</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/anonymous_uid" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>User ID of the anonymous account</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/default_access"></div>
                <b>default_access</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/default_access" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Default access level for all hosts that can access export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/description" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Description about the nfs export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/export_paths"></div>
                <b>export_paths</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/export_paths" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                   / <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Export paths that can be used to mount and access export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/filesystem"></div>
                <b>filesystem</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/filesystem" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of the filesystem on which nfs export is present</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/filesystem/UnityFileSystem"></div>
                <b>UnityFileSystem</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/filesystem/UnityFileSystem" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>filesystem details</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/filesystem/UnityFileSystem/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/filesystem/UnityFileSystem/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the filesystem</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/filesystem/UnityFileSystem/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/filesystem/UnityFileSystem/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the filesystem</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the nfs export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/min_security"></div>
                <b>min_security</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/min_security" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>NFS enforced security type for users accessing an export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the nfs export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/nas_server"></div>
                <b>nas_server</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/nas_server" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of the nas server</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/nas_server/UnityNasServer"></div>
                <b>UnityNasServer</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/nas_server/UnityNasServer" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>NAS server details</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/nas_server/UnityNasServer/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/nas_server/UnityNasServer/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the nas server</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/nas_server/UnityNasServer/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/nas_server/UnityNasServer/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the nas server</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/no_access_hosts_string"></div>
                <b>no_access_hosts_string</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/no_access_hosts_string" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Hosts with no access to the nfs export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/read_only_hosts_string"></div>
                <b>read_only_hosts_string</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/read_only_hosts_string" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Hosts with read-only access to the nfs export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/read_only_root_hosts_string"></div>
                <b>read_only_root_hosts_string</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/read_only_root_hosts_string" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Hosts with read-only for root user access to the nfs export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/read_write_hosts_string"></div>
                <b>read_write_hosts_string</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/read_write_hosts_string" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Hosts with read and write access to the nfs export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/read_write_root_hosts_string"></div>
                <b>read_write_root_hosts_string</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/read_write_root_hosts_string" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Hosts with read and write for root user access to export</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-nfs_share_details/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-nfs_share_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>NFS export type. i.e. filesystem or snapshot</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
---------------

-   Vivek Soni (@v-soni11) &lt;<ansible.team@dell.com>&gt;

SMB Share Module
=====================================================================================

Synopsis
--------

-   Managing SMB Shares on Unity storage system includes create, get,
    modify and delete the smb shares.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Description for the SMB share.</div>
                                        <div>Optional parameter when creating a share.</div>
                                        <div>To modify, pass the new value in description field.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filesystem_id"></div>
                <b>filesystem_id</b>
                <a class="ansibleOptionLink" href="#parameter-filesystem_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the File System.</div>
                                        <div>Either filesystem_name or filesystem_id is required for creation of the SMB share for filesystem.</div>
                                        <div>If filesystem name is specified, then nas_server_name/nas_server_id is required to uniquely identify the filesystem.</div>
                                        <div>filesystem_name and filesystem_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filesystem_name"></div>
                <b>filesystem_name</b>
                <a class="ansibleOptionLink" href="#parameter-filesystem_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The Name of the File System.</div>
                                        <div>Either filesystem_name or filesystem_id is required for creation of the SMB share for filesystem.</div>
                                        <div>If filesystem name is specified, then nas_server_name/nas_server_id is required to uniquely identify the filesystem.</div>
                                        <div>filesystem_name and filesytem_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_abe_enabled"></div>
                <b>is_abe_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-is_abe_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether Access-based Enumeration (ABE) for SMB share is enabled.</div>
                                        <div>During creation, if not mentioned then default is False.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_branch_cache_enabled"></div>
                <b>is_branch_cache_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-is_branch_cache_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether Branch Cache optimization for SMB share is enabled.</div>
                                        <div>During creation, if not mentioned then default is False.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_continuous_availability_enabled"></div>
                <b>is_continuous_availability_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-is_continuous_availability_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether continuous availability for SMB 3.0 is enabled.</div>
                                        <div>During creation, if not mentioned then default is False.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_encryption_enabled"></div>
                <b>is_encryption_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-is_encryption_enabled" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether encryption for SMB 3.0 is enabled at the shared folder level.</div>
                                        <div>During creation, if not mentioned then default is False.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_id"></div>
                <b>nas_server_id</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the NAS Server.</div>
                                        <div>It is not required if share_id is used.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-nas_server_name"></div>
                <b>nas_server_name</b>
                <a class="ansibleOptionLink" href="#parameter-nas_server_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The Name of the NAS Server.</div>
                                        <div>It is not required if share_id is used.</div>
                                        <div>nas_server_name and nas_server_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-offline_availability"></div>
                <b>offline_availability</b>
                <a class="ansibleOptionLink" href="#parameter-offline_availability" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>MANUAL</li>
                                                                                                                                                                                            <li>DOCUMENTS</li>
                                                                                                                                                                                            <li>PROGRAMS</li>
                                                                                                                                                                                            <li>NONE</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Defines valid states of Offline Availability.</div>
                                        <div>MANUAL- Only specified files will be available offline.</div>
                                        <div>DOCUMENTS- All files that users open will be available offline.</div>
                                        <div>PROGRAMS- Program will preferably run from the offline cache even when connected to the network. All files that users open will be available offline.</div>
                                        <div>NONE- Prevents clients from storing documents and programs in offline cache.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-path"></div>
                <b>path</b>
                <a class="ansibleOptionLink" href="#parameter-path" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Local path to the file system/Snapshot or any existing sub-folder of the file system/Snapshot that is shared over the network.</div>
                                        <div>Path is relative to the root of the filesystem.</div>
                                        <div>Required for creation of the SMB share.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-share_id"></div>
                <b>share_id</b>
                <a class="ansibleOptionLink" href="#parameter-share_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the SMB share.</div>
                                        <div>Should not be specified during creation. Id is auto generated.</div>
                                        <div>For all other operations either share_name or share_id is required.</div>
                                        <div>If share_id is used then no need to pass nas_server/filesystem/snapshot/path.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-share_name"></div>
                <b>share_name</b>
                <a class="ansibleOptionLink" href="#parameter-share_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the SMB share.</div>
                                        <div>Required during creation of the SMB share.</div>
                                        <div>For all other operations either share_name or share_id is required.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>
                <b>snapshot_id</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the Filesystem Snapshot.</div>
                                        <div>Either snapshot_name or snapshot_id is required for creation of the SMB share for a snapshot.</div>
                                        <div>If snapshot name is specified, then nas_server_name/nas_server_id is required to uniquely identify the snapshot.</div>
                                        <div>snapshot_name and snapshot_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>
                <b>snapshot_name</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The Name of the Filesystem Snapshot.</div>
                                        <div>Either snapshot_name or snapshot_id is required for creation of the SMB share for a snapshot.</div>
                                        <div>If snapshot name is specified, then nas_server_name/nas_server_id is required to uniquely identify the snapshot.</div>
                                        <div>snapshot_name and snapshot_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the SMB share should exist or not.</div>
                                        <div>present  indicates that the share should exist on the system.</div>
                                        <div>absent  indicates that the share should not exist on the system.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-umask"></div>
                <b>umask</b>
                <a class="ansibleOptionLink" href="#parameter-umask" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The default UNIX umask for new files created on the SMB Share.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Notes
-----
- When ID/Name of the filesystem/snapshot is passed then nas\_server is
not required. If passed, then filesystem/snapshot should exist for the
mentioned nas\_server, else the task will fail.

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                        <div style="font-size: smaller"><b>Sample:</b></div>
                                            <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-smb_share_details"></div>
                <b>smb_share_details</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When share exists.</td>
            <td>
                                        <div>The SMB share details.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/description" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Additional information about the share.</div>
                                    <br/>
                                        <div style="font-size: smaller"><b>Sample:</b></div>
                                            <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This share is created for demo purpose only.</div>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/filesystem_id"></div>
                <b>filesystem_id</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/filesystem_id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the Filesystem.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/filesystem_name"></div>
                <b>filesystem_name</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/filesystem_name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The Name of the filesystem</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the SMB share.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/is_abe_enabled"></div>
                <b>is_abe_enabled</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/is_abe_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether Access Based enumeration is enforced or not</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/is_branch_cache_enabled"></div>
                <b>is_branch_cache_enabled</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/is_branch_cache_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether branch cache is enabled or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/is_continuous_availability_enabled"></div>
                <b>is_continuous_availability_enabled</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/is_continuous_availability_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether the share will be available continuously or not</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/is_encryption_enabled"></div>
                <b>is_encryption_enabled</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/is_encryption_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether encryption is enabled or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the SMB share.</div>
                                    <br/>
                                        <div style="font-size: smaller"><b>Sample:</b></div>
                                            <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">sample_smb_share</div>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/nas_server_id"></div>
                <b>nas_server_id</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/nas_server_id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the nas_server.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/nas_server_name"></div>
                <b>nas_server_name</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/nas_server_name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The Name of the nas_server.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/snapshot_id"></div>
                <b>snapshot_id</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/snapshot_id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the Snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/snapshot_name"></div>
                <b>snapshot_name</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/snapshot_name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The Name of the Snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-smb_share_details/umask"></div>
                <b>umask</b>
                <a class="ansibleOptionLink" href="#return-smb_share_details/umask" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unix mask for the SMB share</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
---------------

-   P Srinivas Rao (@srinivas-rao5) &lt;<ansible.team@dell.com>&gt;

Snapshot Module
=======================================================================================

Synopsis
--------

-   Manage snapshots on the Unity storage system includes create
    snapshots, delete snapshots, update snapshots, get snapshots, map hosts
    and unmap hosts.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-auto_delete"></div>
                <b>auto_delete</b>
                <a class="ansibleOptionLink" href="#parameter-auto_delete" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>This option specifies whether the snapshot is auto deleted or not.</div>
                                        <div>If set to true, snapshot will expire based on the pool auto deletion policy.</div>
                                        <div>If set to false, snapshot will not be auto deleted based on the pool auto deletion policy.</div>
                                        <div>auto_delete can not be set to True, if expiry_time is specified.</div>
                                        <div>If during creation neither auto_delete nor expiry_time is mentioned then snapshot will be created keeping auto_delete as True.</div>
                                        <div>Once the expiry_time is set then snapshot cannot be assigned to the auto delete policy.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-cg_name"></div>
                <b>cg_name</b>
                <a class="ansibleOptionLink" href="#parameter-cg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the Consistency Group for which snapshot is created.</div>
                                        <div>For creation of snapshot either vol_name or cg_name is required.</div>
                                        <div>Not required for other operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The additional information about the snapshot can be provided using this option.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-expiry_time"></div>
                <b>expiry_time</b>
                <a class="ansibleOptionLink" href="#parameter-expiry_time" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This option is for specifying the date and time after which the snapshot will expire.</div>
                                        <div>The time is to be mentioned in UTC timezone.</div>
                                        <div>The format is &quot;MM/DD/YYYY HH:MM&quot;. Year must be in 4 digits.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_id"></div>
                <b>host_id</b>
                <a class="ansibleOptionLink" href="#parameter-host_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The id of the host.</div>
                                        <div>Either host_name or host_id is required to map or unmap a snapshot from a host</div>
                                        <div>Snapshot can be attached to multiple hosts.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the host.</div>
                                        <div>Either host_name or host_id is required to map or unmap a snapshot from a host</div>
                                        <div>Snapshot can be attached to multiple hosts.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_state"></div>
                <b>host_state</b>
                <a class="ansibleOptionLink" href="#parameter-host_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>mapped</li>
                                                                                                                                                                                            <li>unmapped</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The host_state option is used to mention the existence of the host for snapshot.</div>
                                        <div>It is required when a snapshot is mapped or unmapped from host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_snapshot_name"></div>
                <b>new_snapshot_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_snapshot_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name for the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>
                <b>snapshot_id</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The id of the snapshot.</div>
                                        <div>For all operations other than creation either snapshot name or snapshot id is required.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>
                <b>snapshot_name</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the snapshot.</div>
                                        <div>Mandatory parameter for creating a snapshot.</div>
                                        <div>For all other operations either snapshot name or snapshot id is required.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The state option is used to mention the existence of the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vol_name"></div>
                <b>vol_name</b>
                <a class="ansibleOptionLink" href="#parameter-vol_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the volume for which snapshot is created.</div>
                                        <div>For creation of snapshot either vol_name or cg_name is required.</div>
                                        <div>Not required for other operations.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_details"></div>
                <b>snapshot_details</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When snapshot exists</td>
            <td>
                                        <div>Details of the snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/expiration_time"></div>
                <b>expiration_time</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/expiration_time" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date and time after which the snapshot will expire.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/hosts_list"></div>
                <b>hosts_list</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/hosts_list" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Contains the name and id of the associated hosts.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique identifier of the snapshot instance.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/is_auto_delete"></div>
                <b>is_auto_delete</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/is_auto_delete" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Additional information mentioned for snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/storage_resource_id"></div>
                <b>storage_resource_id</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/storage_resource_id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Id of the storage resource for which the snapshot exists.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/storage_resource_name"></div>
                <b>storage_resource_name</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/storage_resource_name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the storage resource for which the snapshot exists.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
---------------
-   P Srinivas Rao (@srinivas-rao5) &lt;<ansible.team@dell.com>&gt;

Snapshot Schedule Module
====================================================================================================

Synopsis
--------

-   Managing snapshot schedules on Unity storage system includes creating
    new snapshot schedule, getting details of snapshot schedule,
    modifying attributes of snapshot schedule and deleting snapshot
    schedule.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-auto_delete"></div>
                <b>auto_delete</b>
                <a class="ansibleOptionLink" href="#parameter-auto_delete" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether the system can automatically delete the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-day_interval"></div>
                <b>day_interval</b>
                <a class="ansibleOptionLink" href="#parameter-day_interval" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Number of days between snapshots.</div>
                                        <div>Applicable only when rule type is &#x27;every_n_days&#x27;.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-day_of_month"></div>
                <b>day_of_month</b>
                <a class="ansibleOptionLink" href="#parameter-day_of_month" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Day of the month for which the snapshot schedule rule applies.</div>
                                        <div>Applicable only when rule type is &#x27;every_month&#x27;.</div>
                                        <div>Value should be [1, 31].</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-days_of_week"></div>
                <b>days_of_week</b>
                <a class="ansibleOptionLink" href="#parameter-days_of_week" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                      <span style="color: purple">elements=string</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SUNDAY</li>
                                                                                                                                                                                            <li>MONDAY</li>
                                                                                                                                                                                            <li>TUESDAY</li>
                                                                                                                                                                                            <li>WEDNESDAY</li>
                                                                                                                                                                                            <li>THURSDAY</li>
                                                                                                                                                                                            <li>FRIDAY</li>
                                                                                                                                                                                            <li>SATURDAY</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Days of the week for which the snapshot schedule rule applies.</div>
                                        <div>Applicable only  when rule type is &#x27;every_week&#x27;.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-desired_retention"></div>
                <b>desired_retention</b>
                <a class="ansibleOptionLink" href="#parameter-desired_retention" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The number of days/hours for which snapshot will be retained.</div>
                                        <div>When auto_delete is True, desired_retention cannot be specified.</div>
                                        <div>Maximum desired retention supported is 31 days or 744 hours.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-hour"></div>
                <b>hour</b>
                <a class="ansibleOptionLink" href="#parameter-hour" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>the hour when the snapshot will be taken.</div>
                                        <div>Applicable for &#x27;every_n_days&#x27;, &#x27;every_week&#x27;, &#x27;every_month&#x27; rule types.</div>
                                        <div>For create operation, if &#x27;hour&#x27; parameter is not specified, value will be taken as 0.</div>
                                        <div>Value should be [0, 23].</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-hours_of_day"></div>
                <b>hours_of_day</b>
                <a class="ansibleOptionLink" href="#parameter-hours_of_day" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                       <span style="color: purple">elements=integer</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Hours of the day when the snapshot will be taken.</div>
                                        <div>Applicable only when rule type is &#x27;every_day&#x27;.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the snapshot schedule.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-interval"></div>
                <b>interval</b>
                <a class="ansibleOptionLink" href="#parameter-interval" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Number of hours between snapshots.</div>
                                        <div>Applicable only when rule type is &#x27;every_n_hours&#x27;.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-minute"></div>
                <b>minute</b>
                <a class="ansibleOptionLink" href="#parameter-minute" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Minute offset from the hour when the snapshot will be taken.</div>
                                        <div>Applicable for all rule types.</div>
                                        <div>For create operation, if &#x27;minute&#x27; parameter is not specified, value will be taken as 0.</div>
                                        <div>Value should be [0, 59].</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the snapshot schedule.</div>
                                        <div>Name is mandatory for create operation.</div>
                                        <div>Specify either name or id (but not both) for any operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-retention_unit"></div>
                <b>retention_unit</b>
                <a class="ansibleOptionLink" href="#parameter-retention_unit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>hours</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>days</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The retention unit for the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the snapshot schedule should exist or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>every_n_hours</li>
                                                                                                                                                                                            <li>every_day</li>
                                                                                                                                                                                            <li>every_n_days</li>
                                                                                                                                                                                            <li>every_week</li>
                                                                                                                                                                                            <li>every_month</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Type of the rule to be included in snapshot schedule.</div>
                                        <div>Type is mandatory for any create or modify operation.</div>
                                        <div>Once the snapshot schedule is created with one type it can be modified.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Notes
-----

- Snapshot schedule created via Ansible will have only one rule.
- Modification of rule type is not allowed. Within the same type, other
parameters can be modified.
- If an existing snapshot schedule has more than one rule in it, only get and delete operation is allowed.

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="5">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="5">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="5">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details"></div>
                <b>snapshot_schedule_details</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When snapshot schedule exists</td>
            <td>
                                        <div>Details of the snapshot schedule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID given to the snapshot schedule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/luns"></div>
                <b>luns</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/luns" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of volumes for which snapshot schedule applied.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan="3">
        <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/luns/UnityLunList"></div>
        <b>UnityLunList</b>
        <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/luns/UnityLunList" title="Permalink to this return value"></a>
        <div style="font-size: small">
          <span style="color: purple">type=complex</span>
                              </div>
                        </td>
    <td>success</td>
    <td>
                                <div>List of volumes for which snapshot schedule applied.</div>
                            <br/>
                        </td>
</tr>
                            <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan="2">
        <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/luns/UnityLunList/UnityLun"></div>
        <b>UnityLun</b>
        <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/luns/UnityLunList/UnityLun" title="Permalink to this return value"></a>
        <div style="font-size: small">
          <span style="color: purple">type=complex</span>
                              </div>
                        </td>
    <td>success</td>
    <td>
                                <div>Detail of volume.</div>
                            <br/>
                        </td>
</tr>
                            <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan="1">
        <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/luns/UnityLunList/UnityLun/id"></div>
        <b>id</b>
        <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/luns/UnityLunList/UnityLun/id" title="Permalink to this return value"></a>
        <div style="font-size: small">
          <span style="color: purple">type=string</span>
                              </div>
                        </td>
    <td>success</td>
    <td>
                                <div>The system ID given to volume.</div>
                            <br/>
                        </td>
</tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the snapshot schedule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules"></div>
                <b>rules</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of rules that apply to snapshot schedule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/days_of_month"></div>
                <b>days_of_month</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/days_of_month" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                   / <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Days of the month for which the snapshot schedule rule applies.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/days_of_week"></div>
                <b>days_of_week</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/days_of_week" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Days of the week for which the snapshot schedule rule applies.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/days_of_week/DayOfWeekEnumList"></div>
                <b>DayOfWeekEnumList</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/days_of_week/DayOfWeekEnumList" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                   / <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Enumeration of days of the week.</div>
                                    <br/>
                                </td>
</tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/hours"></div>
                <b>hours</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/hours" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                   / <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Hourly frequency for the snapshot schedule rule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system ID of the rule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/interval"></div>
                <b>interval</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/interval" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of days or hours between snaps, depending on the rule type.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/is_auto_delete"></div>
                <b>is_auto_delete</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/is_auto_delete" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the system can automatically delete the snapshot based on pool automatic-deletion thresholds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/minute"></div>
                <b>minute</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/minute" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Minute frequency for the snapshot schedule rule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/retention_time"></div>
                <b>retention_time</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/retention_time" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Period of time in seconds for which to keep the snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/retention_time_in_hours"></div>
                <b>retention_time_in_hours</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/retention_time_in_hours" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Period of time in hours for which to keep the snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/rules/rule_type"></div>
                <b>rule_type</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/rules/rule_type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of the rule applied to snapshot schedule.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/storage_resources"></div>
                <b>storage_resources</b>
                <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/storage_resources" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details of storage resources for which snapshot schedule applied.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan="3">
        <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/storage_resources/UnityStorageResourceList"></div>
        <b>UnityStorageResourceList</b>
        <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/storage_resources/UnityStorageResourceList" title="Permalink to this return value"></a>
        <div style="font-size: small">
          <span style="color: purple">type=complex</span>
                              </div>
                        </td>
    <td>success</td>
    <td>
                                <div>List of storage resources for which snapshot schedule applied.</div>
                            <br/>
                        </td>
</tr>
                            <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan="2">
        <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/storage_resources/UnityStorageResourceList/UnityStorageResource"></div>
        <b>UnityStorageResource</b>
        <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/storage_resources/UnityStorageResourceList/UnityStorageResource" title="Permalink to this return value"></a>
        <div style="font-size: small">
          <span style="color: purple">type=complex</span>
                              </div>
                        </td>
    <td>success</td>
    <td>
                                <div>Detail of storage resource.</div>
                            <br/>
                        </td>
</tr>
                            <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan="1">
        <div class="ansibleOptionAnchor" id="return-snapshot_schedule_details/storage_resources/UnityStorageResourceList/UnityStorageResource/id"></div>
        <b>id</b>
        <a class="ansibleOptionLink" href="#return-snapshot_schedule_details/storage_resources/UnityStorageResourceList/UnityStorageResource/id" title="Permalink to this return value"></a>
        <div style="font-size: small">
          <span style="color: purple">type=string</span>
                              </div>
                        </td>
    <td>success</td>
    <td>
                                <div>The system ID given to storage resource.</div>
                            <br/>
                        </td>
</tr>
                    </table>
<br/><br/>

Authors
-----------------

-   Akash Shendge (@shenda1) &lt;<ansible.team@dell.com>&gt;

Storage Pool Module
===========================================================================

Synopsis
--------

-   Managing storage pool on Unity storage system
-   Get details of storage pool
-   Modify storage pool

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-fast_cache"></div>
                <b>fast_cache</b>
                <a class="ansibleOptionLink" href="#parameter-fast_cache" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>enabled</li>
                                                                                                                                                                                            <li>disabled</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether the fast cache is enabled for the storage pool.</div>
                                        <div>enabled - FAST Cache is enabled for the pool.</div>
                                        <div>disabled - FAST Cache is disabled for the pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-fast_vp"></div>
                <b>fast_vp</b>
                <a class="ansibleOptionLink" href="#parameter-fast_vp" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>enabled</li>
                                                                                                                                                                                            <li>disabled</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Indicates whether to enable scheduled data relocations for the pool.</div>
                                        <div>enabled - Enabled scheduled data relocations for the pool.</div>
                                        <div>disabled - Disabled scheduled data relocations for the pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_pool_name"></div>
                <b>new_pool_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_pool_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name of the storage pool, unique in the storage system.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-pool_description"></div>
                <b>pool_description</b>
                <a class="ansibleOptionLink" href="#parameter-pool_description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The description of the storage pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-pool_id"></div>
                <b>pool_id</b>
                <a class="ansibleOptionLink" href="#parameter-pool_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Unique identifier of the pool instance.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-pool_name"></div>
                <b>pool_name</b>
                <a class="ansibleOptionLink" href="#parameter-pool_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the storage pool, unique in the storage system.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the storage pool should exist or not.</div>
                                        <div>present - indicates that the storage pool should exist on the system.</div>
                                        <div>absent - indicates that the storage pool should not exist on the system.</div>
                                                    </td>
        </tr>
                     </table>
<br/>

Notes
-----

- Creation/Deletion of storage pool is not allowed through Ansible
module.

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the storage pool has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details"></div>
                <b>storage_pool_details</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When storage pool exists.</td>
            <td>
                                        <div>The storage pool details.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Pool id, unique identifier of the pool.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/is_fast_cache_enabled"></div>
                <b>is_fast_cache_enabled</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/is_fast_cache_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the fast cache is enabled for the storage pool.</div>
                                        <div>true - FAST Cache is enabled for the pool.</div>
                                        <div>false - FAST Cache is disabled for the pool.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/is_fast_vp_enabled"></div>
                <b>is_fast_vp_enabled</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/is_fast_vp_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether to enable scheduled data relocations for the storage pool.</div>
                                        <div>true - Enabled scheduled data relocations for the pool.</div>
                                        <div>false - Disabled scheduled data relocations for the pool.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Pool name, unique in the storage system.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/size_free_with_unit"></div>
                <b>size_free_with_unit</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/size_free_with_unit" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates size_free with its appropriate unit in human readable form.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/size_subscribed_with_unit"></div>
                <b>size_subscribed_with_unit</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/size_subscribed_with_unit" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates size_subscribed with its appropriate unit in human readable form.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/size_total_with_unit"></div>
                <b>size_total_with_unit</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/size_total_with_unit" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates size_total with its appropriate unit in human readable form.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/size_used_with_unit"></div>
                <b>size_used_with_unit</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/size_used_with_unit" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates size_used with its appropriate unit in human readable form.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/snap_size_subscribed_with_unit"></div>
                <b>snap_size_subscribed_with_unit</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/snap_size_subscribed_with_unit" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates snap_size_subscribed with its appropriate unit in human readable form.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/snap_size_used_with_unit"></div>
                <b>snap_size_used_with_unit</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/snap_size_used_with_unit" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates snap_size_used with its appropriate unit in human readable form.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

Authors
--------------
-   Ambuj Dubey (@AmbujDube) &lt;<ansible.team@dell.com>&gt;

Volume Module
===============================================================================

Synopsis
--------

-   Managing volume on Unity storage system includes- Create new volume,
    Modify volume attributes, Map Volume to host, Unmap volume to host,
    Display volume details, Delete volume

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-cap_unit"></div>
                <b>cap_unit</b>
                <a class="ansibleOptionLink" href="#parameter-cap_unit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>GB</li>
                                                                                                                                                                                            <li>TB</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The unit of the volume size. It defaults to &#x27;GB&#x27;, if not specified.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-compression"></div>
                <b>compression</b>
                <a class="ansibleOptionLink" href="#parameter-compression" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Boolean variable , specifies whether or not to enable compression. Compression is supported only for thin volumes</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Description about the volume.</div>
                                        <div>Description can be removed by passing empty string (&quot;&quot;).</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-hlu"></div>
                <b>hlu</b>
                <a class="ansibleOptionLink" href="#parameter-hlu" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Host Lun Unit to be mapped/unmapped with this volume.</div>
                                        <div>It&#x27;s an optional parameter, hlu can be specified along with host_name or host_id and mapping_state.</div>
                                        <div>If hlu is not specified, unity will choose it automatically. The maximum value supported is 255.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_id"></div>
                <b>host_id</b>
                <a class="ansibleOptionLink" href="#parameter-host_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the host to be mapped/unmapped with this volume.</div>
                                        <div>Either host_name,host_id can be specified in one task along with mapping_state.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the host to be mapped/unmapped with this volume.</div>
                                        <div>Either host_name,host_id can be specified in one task along with mapping_state.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-io_limit_policy"></div>
                <b>io_limit_policy</b>
                <a class="ansibleOptionLink" href="#parameter-io_limit_policy" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IO limit policy associated with this volume. Once it&#x27;s set cannot be removed through ansible module but it can be changed.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-is_thin"></div>
                <b>is_thin</b>
                <a class="ansibleOptionLink" href="#parameter-is_thin" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Boolean variable , specifies whether or not it&#x27;s a thin volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-mapping_state"></div>
                <b>mapping_state</b>
                <a class="ansibleOptionLink" href="#parameter-mapping_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>mapped</li>
                                                                                                                                                                                            <li>unmapped</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State of host access for volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_vol_name"></div>
                <b>new_vol_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_vol_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name of the volume for rename operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-pool_id"></div>
                <b>pool_id</b>
                <a class="ansibleOptionLink" href="#parameter-pool_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This is the id of the pool where the volume will be created.</div>
                                        <div>Either the pool_name or pool_id must be provided to create a new volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-pool_name"></div>
                <b>pool_name</b>
                <a class="ansibleOptionLink" href="#parameter-pool_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This is the name of the pool where the volume will be created.</div>
                                        <div>Either the pool_name or pool_id must be provided to create a new volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-size"></div>
                <b>size</b>
                <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The size of the volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snap_schedule"></div>
                <b>snap_schedule</b>
                <a class="ansibleOptionLink" href="#parameter-snap_schedule" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Snapshot schedule assigned to the volume.</div>
                                        <div>Add/Remove/Modify the snapshot schedule for the volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sp"></div>
                <b>sp</b>
                <a class="ansibleOptionLink" href="#parameter-sp" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>SPA</li>
                                                                                                                                                                                            <li>SPB</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Storage Processor for this volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=yes</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State variable to determine whether volume will exist or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-tiering_policy"></div>
                <b>tiering_policy</b>
                <a class="ansibleOptionLink" href="#parameter-tiering_policy" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>AUTOTIER_HIGH</li>
                                                                                                                                                                                            <li>AUTOTIER</li>
                                                                                                                                                                                            <li>HIGHEST</li>
                                                                                                                                                                                            <li>LOWEST</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vol_id"></div>
                <b>vol_id</b>
                <a class="ansibleOptionLink" href="#parameter-vol_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The id of the volume.</div>
                                        <div>It can be used only for get, modify, map/unmap host or delete operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vol_name"></div>
                <b>vol_name</b>
                <a class="ansibleOptionLink" href="#parameter-vol_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the volume. Mandatory only for create operation.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details"></div>
                <b>volume_details</b>
                <a class="ansibleOptionLink" href="#return-volume_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=complex</span>
                                      </div>
                                </td>
            <td>When volume exists</td>
            <td>
                                        <div>Details of the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/current_sp"></div>
                <b>current_sp</b>
                <a class="ansibleOptionLink" href="#return-volume_details/current_sp" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Current storage processor for this volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-volume_details/description" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>description about the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/host_access"></div>
                <b>host_access</b>
                <a class="ansibleOptionLink" href="#return-volume_details/host_access" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                   / <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Host mapped to this volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-volume_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The system generated ID given to the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/io_limit_policy"></div>
                <b>io_limit_policy</b>
                <a class="ansibleOptionLink" href="#return-volume_details/io_limit_policy" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>IO limit policy associated with this volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/is_data_reduction_enabled"></div>
                <b>is_data_reduction_enabled</b>
                <a class="ansibleOptionLink" href="#return-volume_details/is_data_reduction_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether or not compression enabled on this volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/is_thin_enabled"></div>
                <b>is_thin_enabled</b>
                <a class="ansibleOptionLink" href="#return-volume_details/is_thin_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether thin provisioning is enabled for this volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-volume_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/pool"></div>
                <b>pool</b>
                <a class="ansibleOptionLink" href="#return-volume_details/pool" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The pool in which this volume is allocated.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/size_total_with_unit"></div>
                <b>size_total_with_unit</b>
                <a class="ansibleOptionLink" href="#return-volume_details/size_total_with_unit" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Size of the volume with actual unit.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/snap_schedule"></div>
                <b>snap_schedule</b>
                <a class="ansibleOptionLink" href="#return-volume_details/snap_schedule" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Snapshot schedule applied to this volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/tiering_policy"></div>
                <b>tiering_policy</b>
                <a class="ansibleOptionLink" href="#return-volume_details/tiering_policy" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Tiering policy applied to this volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/wwn"></div>
                <b>wwn</b>
                <a class="ansibleOptionLink" href="#return-volume_details/wwn" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The world wide name of this volume</div>
                                    <br/>
                                </td>
        </tr>
            </table>
<br/><br/>

Authors
----------------

-   Arindam Datta (@arindam-emc) &lt;<ansible.team@dell.com>&gt;
