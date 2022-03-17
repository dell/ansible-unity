# Ansible Modules for Dell Technologies Unity

The Ansible Modules for Dell Technologies (Dell) Unity allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell Unity arrays.

The capabilities of the Ansible modules are managing consistency groups, filesystem, filesystem snapshots, NAS server, NFS export, SMB share, hosts, snapshots, snapshot schedules, storage pools, user quotas, quota trees and volumes; and to gather facts from the array. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.

## License
The Ansible collection for Unity is released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-unity/blob/1.3.0/LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for Unity are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](https://github.com/dell/ansible-unity/blob/1.3.0/MODULE-LICENSE) for the full terms.

## Support
The Ansible collection for Unity are supported by Dell and are provided under the terms of the license attached to the collection. Please see the [LICENSE](#license) section for the full terms. Dell does not provide any support for the source code modifications. For any Ansible modules issues, questions or feedback, join the [Dell Automation Community](https://www.dell.com/community/Automation/bd-p/Automation).

## Supported Platforms
  * Dell Unity Arrays version 5.0, 5.1 ,5.2

## Prerequisites
This table provides information about the software prerequisites for the Ansible Modules for Dell Unity.

| **Ansible Modules** | **Red Hat Enterprise Linux** | **Python version** | **Python library version** | **Ansible** |
|---------------------|------------------------------|--------------------|----------------------------|-------------|
| v1.3.0 | 8.4 <br> 8.5| 3.7 <br> 3.8 <br> 3.9 | 1.2.10 | 2.10 <br> 2.11 <br> 2.12| 

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell Unity
  * [Consistency group module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#consistency-group-module)
  * [Filesystem module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#file-system-module)
  * [Filesystem snapshot module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#filesystem-snapshot-module)
  * [Info module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#info-module)
  * [Host module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#host-module)
  * [NAS server module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#nas-server-module)
  * [NFS export module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md##nfs-module)
  * [SMB share module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#smb-share-module)
  * [Snapshot module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#snapshot-module)
  * [Snapshot schedule module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#snapshot-schedule-module)
  * [Storage pool module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#storage-pool-module)
  * [User quota module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#user-quota-module)
  * [Quota tree module ](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#quota-tree-module)
  * [Volume module](https://github.com/dell/ansible-unity/blob/1.3.0/docs/Product%20Guide.md#volume-module)

## Installation of SDK
Install python sdk named 'storops'. It can be installed using pip, based on appropriate python version.

    pip install storops

## Building Collections
  1. Use the following command to build the collection from source code:
    
    ansible-galaxy collection build

   For more details on how to build a tar ball, refer: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)

## Installing Collections
#### Online Installation of Collections 
  1. Use the following command to install the latest collection hosted in galaxy:

	ansible-galaxy collection install dellemc.unity -p <install_path>

#### Offline Installation of Collections
  1. Download the latest tar build from any of the available distribution channel [Ansible Galaxy](https://galaxy.ansible.com/dellemc/unity) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/unity) and use the following command to install the collection anywhere in your system:

	ansible-galaxy collection install dellemc-unity-1.3.0.tar.gz -p <install_path>

  2. Set the environment variable:

	export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

 
## Using Collections

  1. In order to use any Ansible module, ensure that the importing of a proper FQCN (Fully Qualified Collection Name) must be embedded in the playbook. Refer to the following example:

	collections:
	- dellemc.unity

  2. In order to use an installed collection specific to the task use a proper FQCN (Fully Qualified Collection Name). Refer to the following example:

	tasks:
    - name: Get Volume details
         dellemc.unity.volume

  3. For generating Ansible documentation for a specific module, embed the FQCN  before the module name. Refer to the following example:

	ansible-doc dellemc.unity.info

## Running Ansible Modules
The Ansible server must be configured with Python library for Unity to run the Ansible playbooks. The [Documents]( https://github.com/dell/ansible-unity/tree/1.3.0/docs ) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which need to be configured before running the modules.

## SSL Certificate Validation

**NOTE**: These modules are supported through CA certified certificate only, however a self-signed certificate is not supported.

  * Copy the CA certificate to this "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
  * Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the command "export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>"
  * Import the SSL certificate to host using the command "update-ca-trust".

## Results
Each module returns the updated state and details of the entity, For example, if you are using the Volume module, all calls will return the updated details of the volume. Sample result is shown in each module's documentation.
