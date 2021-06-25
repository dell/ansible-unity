**Ansible Modules for Dell EMC Unity** 
=========================================
### Release Notes 1.2.0

>   © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell,
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Content
-------
These release notes contain supplemental information about Ansible
Modules for Dell EMC Unity.

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
| 01       | June 2021  | Current release of Ansible Modules for Dell EMC Unity 1.2.0 |

Product Description
-------------------
The Ansible modules for Dell EMC Unity are used to automate and orchestrate the deployment, configuration, and management of Dell EMC Unity Family systems, including Unity, Unity XT, and the UnityVSA. The capabilities of Ansible modules are managing NFS exports, SMB shares, NAS server, File Systems, File System Snapshots, Quota tree, User quotas for filesystem and quota tree and obtaining Unity system information. The options available for each capability are list, show, create, delete, and modify; except for NAS server for which options available are list & modify.

New features & enhancements
---------------------------
This release supports the following features -


- Application Tagging:
    - A new HTTP header (Application-Type) is added in Unity REST API in Goshawk release which is used to set REST client name and its version and this information is recorded in Unity logs
    - Ansible modules support application tagging which is used to identify the REST application that makes the request to Unisphere
    - The value of application type parameter from Ansible module is set to Ansible/1.2.0

-   User quota module supports the following functionalities:
    -   Create User quota for a Filesystem/Quota tree 
    -   Get User quota details    
    -   Modify attributes of User quota
    -   Delete User quota

-   Quota tree module supports the following functionalities:
    -   Create Quota tree for a Filesystem 
    -   Get Quota tree details    
    -   Modify attributes of Quota tree
    -   Delete Quota tree

-   Consistency group module has the following enhancements:
    -   Map hosts to a new or an existing Consistency group    
    -   Unmap hosts from a Consistency group 

-   Filesystem module has the following enhancements:
    -   Set the attributes of Quota config while Filesystem creation
    -   Associate an existing snapshot schedule to existing or new Filesystem
    -   Remove snapshot schedule from a Filesystem

-   Volume module has the following enhancements:
    -   Map multiple hosts to a new or existing volume
    -   Unmap multiple hosts from a volume
    
-   Gather Facts Module has the following enhancements:
    -  List of User quota 
    -  List of Quota tree

Known issues
------------
Known issues in this release are listed below:
- Filesystem creation with quota config
    - Setting quota configuration while creating a filesystem may sometime observe delay in fetching the details about the quota config of the new filesystem. The module will throw an error to rerun the task to see expected result.
    
- Mapping and unmapping of hosts for a Consistency group
    - Interoperability between Ansible Unity playbooks and Unisphere REST API is not supported for mapping and unmapping of hosts for a consistency group.
      > **WORKAROUND:** It is recommended to use Ansible Unity modules consistently for all mapping and unmapping of hosts for a consistency group instead of partially/mutually doing it through Unisphere and Ansible modules.

Limitations
-----------
There are no known limitations.

Distribution
----------------
The software package is available for download from the [Ansible Modules
for Unity GitHub](https://github.com/dell/ansible-unity/) page.

Documentation
-------------
The documentation is available on [Ansible Modules for Unity GitHub](https://github.com/dell/ansible-unity/tree/1.2.0/docs)
page. It includes the following:
- README
- Release Notes (this document)
- Product Guide
