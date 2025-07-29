**Ansible Modules for Dell Technologies Unity** 
=========================================
### Release Notes 2.1.0

>   © 2025 Dell Inc. or its subsidiaries. All rights reserved. Dell
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

| Revision | Date           | Description                                             |
|----------|----------------|---------------------------------------------------------|
| 01       | March 2024     | Current release of Ansible Modules for Dell Unity 2.0.0 |
| 02       | Aug 2025     | Current release of Ansible Modules for Dell Unity 2.1.0 |

Product Description
-------------------
The Ansible modules for Dell Unity are used to automate and orchestrate the deployment, configuration, and management of Dell Unity Family systems, including Unity, Unity XT, and the UnityVSA. The capabilities of Ansible modules are managing host, consistency group, filesystem, filesystem snapshots, CIFS server, NAS servers, NFS server, NFS export, SMB shares, interface, snapshots, snapshot schedules, storage pool, tree quota, user quota, volumes and obtaining Unity system information. The options available for each capability are list, show, create, delete, and modify; except for NAS server for which options available are list & modify and for CIFS server, NFS server the options available are create, list & modify.

New features & enhancements
---------------------------
This release has the following changes -

- Adding support for Unity v5.5.
- Bugfixes and Security Updates.

Known issues
------------
Known issues in this release are listed below:
- Filesystem creation with quota config
    - Setting quota configuration while creating a filesystem may sometimes cause a delay in fetching the details about the quota config of the new filesystem. The module will throw an error to rerun the task to see the expected result.
    
- Mapping and unmapping of hosts for a Consistency group
    - Interoperability between Ansible Unity playbooks and Unisphere REST API is not supported for the mapping and unmapping of hosts for a consistency group.
      > **WORKAROUND:** It is recommended to use Ansible Unity modules consistently for all mapping and unmapping of hosts for a consistency group instead of partially/mutually doing it through Unisphere and Ansible modules.

- Unmapping of LUN's from consistency group after disabling replication fails intermittently
    - Immediate removal/unmapping of LUN's after disabling replication may fail with this error message which indicates that the consistency group has snapshots.

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
The documentation is available on [Ansible Modules for Unity GitHub](https://github.com/dell/ansible-unity/tree/2.1.0/docs)
page. It includes the following:
- README
- Release Notes (this document)
