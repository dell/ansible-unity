.. _dellemc.unity.initiator_module:

initiator
========

.. contents::
   :local:
   :depth: 1

Synopsis
--------

- Manage Initiator operations on Unity storage system.
- Create an Initiator (even if not zoned).
- Add initiators to Host.
- Remove initiators from Host.
- Get details of Initiators.
- Delete an Initiator.
- Automatically create host if it doesn't exist when adding initiators.

Requirements
------------

The below requirements are needed on the host that executes this module.

- python >= 3.11
- storops >= 1.2.12
- ansible-core >= 2.17

Parameters
----------

.. include:: ../../plugins/modules/initiator.py
   :start-after: DOCUMENTATION = r'''
   :end-before: EXAMPLES = r'''

Notes
-----

.. include:: ../../plugins/modules/initiator.py
   :start-after: notes:
   :end-before: examples:

Examples
--------

.. include:: ../../plugins/modules/initiator.py
   :start-before: EXAMPLES = r'''
   :start-after: EXAMPLES = r'''
   :end-before: RETURN = r'''

Return Values
--------------

.. include:: ../../plugins/modules/initiator.py
   :start-before: RETURN = r'''
   :start-after: RETURN = r'''
