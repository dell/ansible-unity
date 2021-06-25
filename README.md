# Ansible Modules for Dell EMC Unity

The Ansible Modules for Dell EMC Unity allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell EMC Unity arrays.

The capabilities of the Ansible modules are managing consistency groups, filesystem, filesystem snapshots, NAS server, NFS export, SMB share, hosts, snapshots, snapshot schedules, storage pools, user quotas, quota trees and volumes; and to gather facts from the array. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.

## Support
Ansible modules for Unity are supported by Dell EMC and are provided under the terms of the license attached to the source code. Dell EMC does not provide support for any source code modifications. For any Ansible module issues, questions or feedback, join the [Dell EMC Automation community](https://www.dell.com/community/Automation/bd-p/Automation).

## Supported Platforms
  * Dell EMC Unity Arrays version 5.0, 5.1.0

## Prerequisites
  * Ansible 2.9, 2.10
  * Python 2.8, 3.5, 3.6, 3.7, 3.8
  * Red Hat Enterprise Linux 7.6, 7.7, 7.8, 8.2
  * Python Library for Unity storops version 1.2.10 or higher

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC Unity
  * Consistency group module
  * Filesystem module
  * Filesystem snapshot module
  * Gather facts module
  * Host module
  * NAS server module
  * NFS export module
  * SMB share module
  * Snapshot module
  * Snapshot schedule module
  * Storage pool module
  * User quota module
  * Quota tree module  
  * Volume module

## Installation of SDK
Install python sdk named 'storops'. It can be installed using pip, based on appropriate python version.

    pip install storops

## Installing Collections
  * Download the tar build and follow the below command to install the collection anywhere in your system:
 
        ansible-galaxy collection install dellemc-unity-1.2.0.tar.gz -p <install_path>
  * Set the environment variable:
  
        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>
 
## Using Collections

  * In order to use any Ansible module, ensure that the importing of proper FQCN(Fully Qualified Collection Name) must be embedded in the playbook.
   Below example can be referred
 
        collections:
        - dellemc.unity

    
  * For generating Ansible documentaion for a specific module, embed the FQCN  before the module name. The below example can be referred.
        
        ansible-doc dellemc.unity.dellemc_unity_gatherfacts

## Running Ansible Modules
The Ansible server must be configured with Python library for Unity to run the Ansible playbooks. The [Documents]( https://github.com/dell/ansible-unity/tree/1.2.0/docs ) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which need to be configured before running the modules.

## SSL Certificate Validation

**NOTE**: These modules are supported through CA certified certificate only, however a self-signed certificate is not supported.

  * Copy the CA certificate to this "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
  * Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the command "export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>"
  * Import the SSL certificate to host using the command "update-ca-trust".

## Results
Each module returns the updated state and details of the entity, For example, if you are using the Volume module, all calls will return the updated details of the volume. Sample result is shown in each module's documentation.