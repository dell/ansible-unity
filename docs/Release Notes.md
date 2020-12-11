**Ansible Modules for Dell EMC Unity** 
=========================================
### Release Notes 1.1

>   © 2020 Dell Inc. or its subsidiaries. All rights reserved. Dell,
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
| 01       | Nov 2020  | Current release of Ansible Modules for Dell EMC Unity 1.1 |

Product Description
-------------------
The Ansible modules for Dell EMC Unity are used to automate and orchestrate the deployment, configuration, and management of Dell EMC Unity Family systems, including Unity, Unity XT, and the UnityVSA. The capabilities of Ansible modules are managing NFS exports, SMB shares, NAS server, File Systems, File System Snapshots and obtaining Unity system information. The options available for each capability are list, show, create, delete, and modify; except for NAS server for which options available are list & modify.

New features & enhancements
---------------------------
This release supports the following tasks/operations -

-   Gather Facts Module
    -  List of File system snapshots 
    -  List of NAS servers
    -  List of File systems
    -  List of NFS exports
    -  List of SMB shares

-   NFS export module
    -   Create a NFS export for a Filesystem/snapshot 
    -   Get NFS export details    
    -   Modify attributes of NFS export
    -   Delete a NFS export

-   SMB share module
    -   Create a SMB Share for a Filesystem/snapshot 
    -   Get SMB share details    
    -   Modify attributes of SMB share
    -   Delete a SMB share

-   NAS server module
    -   Get NAS server details    
    -   Modify NAS server details

-   Filesystem module
    -   Create a Filesystem 
    -   Get Filesystem details    
    -   Modify attributes of Filesystem
    -   Delete a Filesystem 

-   Filesystem snapshot module
    -   Create a Filesystem snapshot
    -   Get Filesystem Snapshot details    
    -   Modify attributes of Filesystem Snapshot
    -   Delete a Filesystem Snapshot

Known issues
------------
There are no known issues.

Limitations
-----------
There are no known limitations.

Distribution
----------------
The software package is available for download from the [Ansible Modules
for Unity GitHub](https://github.com/dell/ansible-unity/) page.

Documentation
-------------
The documentation is available on [Ansible Modules for Unity GitHub](https://github.com/dell/ansible-unity/tree/1.1.0/dellemc_ansible/docs)
page. It includes the following:
- README
- Release Notes (this document)
- Product Guide
