<!--
Copyright (c) 2022-2025 Dell Inc., or its subsidiaries. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
-->

# Installation and execution of Ansible modules for Dell Unity

## Installation of SDK
* Install the python SDK named [Storops](https://pypi.org/project/storops/). It can be installed using pip, based on appropriate python version. Execute this command:

        pip install storops

* Alternatively, Other installation ways can be found from [SDK](https://github.com/emc-openstack/storops#readme) page

## Building collections
  * Use this command to build the collection from source code:

        ansible-galaxy collection build

   For more details on how to build a tar ball, please refer to: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)

## Installing collections

#### Online installation of collections
  * Use this command to install the latest collection hosted in [galaxy portal](https://galaxy.ansible.com/dellemc/unity):

        ansible-galaxy collection install dellemc.unity -p <install_path>

#### Offline installation of collections

  * Download the latest tar build from any of the available distribution channel [Ansible Galaxy](https://galaxy.ansible.com/dellemc/unity) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/unity) and use this command to install the collection anywhere in your system:

        ansible-galaxy collection install dellemc-unity-2.1.0.tar.gz -p <install_path>

  * Set the environment variable:

        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

## Using collections

  * In order to use any Ansible module, ensure that the importing of proper FQCN (Fully Qualified Collection Name) must be embedded in the playbook.
   This example can be referred to:

        collections:
        - dellemc.unity

  * In order to use installed collection in a specific task use a proper FQCN (Fully Qualified Collection Name). Refer to this example:

        tasks:
        - name: Create volume
          volume

  * For generating Ansible documentation for a specific module, embed the FQCN  before the module name. Refer to this example:

        ansible-doc dellemc.unity.volume


## Ansible modules execution

The Ansible server must be configured with Python library for Unity to run the Ansible playbooks. The [Documents](https://github.com/dell/ansible-unity/blob/2.1.0/docs/) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

## SSL certificate validation

* Copy the CA certificate to the "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
* Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the command:

        export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>
* Import the SSL certificate to host using the command:

        update-ca-trust extract
* If "TLS CA certificate bundle error" occurs, then follow these steps:

        cd /etc/pki/tls/certs/
        openssl x509 -in ca-bundle.crt -text -noout

## Results
Each module returns the updated state and details of the entity, For example, if you are using the Volume module, all calls will return the updated details of the volume. Sample result is shown in each module's documentation.

## Ansible execution environment
Ansible can also be installed in a container environment. Ansible Builder provides the ability to create reproducible, self-contained environments as container images that can be run as Ansible execution environments.
* Install the ansible builder package using:

      pip3 install ansible-builder
* Ensure the execution-environment.yml is at the root of collection and create the execution environment using:

      ansible-builder build --tag <tag_name> --container-runtime docker
* After the image is built, run the container using:

      docker run -it <tag_name> /bin/bash
* Verify collection installation using command:

      ansible-galaxy collection list
* The playbook can be run on the container using:

      docker run --rm -v $(pwd):/runner <tag_name> ansible-playbook info_test.yml
