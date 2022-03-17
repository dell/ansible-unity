**Ansible Modules for Dell Technologies Unity** 
=========================================
### Release Notes 1.3.0

>   © 2022 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Content
-------
These release notes contain supplemental information about Ansible
Modules for Dell Technologies (Dell) Unity.

-   Revision History
-   Product Description
-   New Features & Enhancements
-   Known Issues
-   Limitations
-   Distribution
-   Documentation

Revision history
----------------
The table in this section lists the revision history of this document.

Table 1. Revision history

| Revision | Date      | Description                                               |
|----------|-----------|-----------------------------------------------------------|
| 01       | March 2022  | Current release of Ansible Modules for Dell Unity 1.3.0 |

Product Description
-------------------
The Ansible modules for Dell Unity are used to automate and orchestrate the deployment, configuration, and management of Dell Unity Family systems, including Unity, Unity XT, and the UnityVSA. The capabilities of Ansible modules are managing host, consistency group, filesystem, filesystem snapshots, NAS servers, NFS export, SMB shares, snapshots, snapshot schedules, storage pool, tree quota, user quota, volumes and obtaining Unity system information. The options available for each capability are list, show, create, delete, and modify; except for NAS server for which options available are list & modify.

New features & enhancements
---------------------------
This release has the following changes -

- Enhanced host module to support listing of network addresses, FC initiators, ISCSI initiators and allocated volumes of a host.
- Enhanced host module to support add/remove network address to/from host.
- Enhanced host module to support both mapping and un-mapping of non-logged-in initiators to host.
- Enhanced Storage Pool module to support listing of drive details of a pool.
- Enhanced consistency group module to support enable/disable replication in consistency group.
- Enhanced storage pool module to support creation of storage pool.
- Renamed gatherfacts module to info module.
- Enhanced info module to list disk groups.
- Added rotating file handler for logging.
- Removed dellemc_unity prefix from module names.
- Bugfixes in volume module to retrieve details of non-thin volumes.

Known issues
------------
Known issues in this release are listed below:
- Filesystem creation with quota config
    - Setting quota configuration while creating a filesystem may sometimes cause a delay in fetching the details about the quota config of the new filesystem. The module will throw an error to rerun the task to see the expected result.
    
- Mapping and unmapping of hosts for a Consistency group
    - Interoperability between Ansible Unity playbooks and Unisphere REST API is not supported for the mapping and unmapping of hosts for a consistency group.
      > **WORKAROUND:** It is recommended to use Ansible Unity modules consistently for all mapping and unmapping of hosts for a consistency group instead of partially/mutually doing it through Unisphere and Ansible modules.

- Unmapping of LUN's from consistency group after disabling replication fails intermittently
    - Immediate removal/unmapping of LUN's after disabling replication may fail with below error message which indicates that the consistency group has snapshots.
        ``` "The LUN cannot be removed from the Consistency group because there are snapshots of the Consistency group that include the selected LUN. Please remove all snapshots containing the selected LUN and try again. (Error Code:0x6000c16)" ```
        > **NOTE:** It is recommended to avoid immediate removal/unmapping of LUN's after disabling replication.


Limitations
-----------
There are no known limitations.

Distribution
----------------
The software package is available for download from the [Ansible Modules
for Unity GitHub](https://github.com/dell/ansible-unity/) page.

Documentation
-------------
The documentation is available on [Ansible Modules for Unity GitHub](https://github.com/dell/ansible-unity/tree/1.3.0/docs)
page. It includes the following:
- README
- Release Notes (this document)
- Product Guide
