.. _snapshotschedule_module:


snapshotschedule -- Manage snapshot schedules on Unity storage system
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing snapshot schedules on Unity storage system includes creating new snapshot schedule, getting details of snapshot schedule, modifying attributes of snapshot schedule, and deleting snapshot schedule.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.17 or later.
- Python 3.11, or 3.12.
- Storops Python SDK 1.2.12.



Parameters
----------

  name (optional, str, None)
    The name of the snapshot schedule.

    Name is mandatory for a create operation.

    Specify either *name* or *id* (but not both) for any operation.


  id (optional, str, None)
    The ID of the snapshot schedule.


  type (optional, str, None)
    Type of the rule to be included in snapshot schedule.

    Type is mandatory for any create or modify operation.

    Once the snapshot schedule is created with one type it can be modified.


  interval (optional, int, None)
    Number of hours between snapshots.

    Applicable only when rule type is ``every_n_hours``.


  hours_of_day (optional, list, None)
    Hours of the day when the snapshot will be taken.

    Applicable only when rule type is ``every_day``.


  day_interval (optional, int, None)
    Number of days between snapshots.

    Applicable only when rule type is ``every_n_days``.


  days_of_week (optional, list, None)
    Days of the week for which the snapshot schedule rule applies.

    Applicable only when rule type is ``every_week``.


  day_of_month (optional, int, None)
    Day of the month for which the snapshot schedule rule applies.

    Applicable only when rule type is ``every_month``.

    Value should be [1, 31].


  hour (optional, int, None)
    The hour when the snapshot will be taken.

    Applicable for ``every_n_days``, ``every_week``, ``every_month`` rule types.

    For create operation, if *hour* parameter is not specified, value will be taken as ``0``.

    Value should be [0, 23].


  minute (optional, int, None)
    Minute offset from the hour when the snapshot will be taken.

    Applicable for all rule types.

    For a create operation, if *minute* parameter is not specified, value will be taken as ``0``.

    Value should be [0, 59].


  desired_retention (optional, int, None)
    The number of days/hours for which snapshot will be retained.

    When *auto_delete* is ``true``, *desired_retention* cannot be specified.

    Maximum desired retention supported is 31 days or 744 hours.


  retention_unit (optional, str, hours)
    The retention unit for the snapshot.


  auto_delete (optional, bool, None)
    Indicates whether the system can automatically delete the snapshot.


  state (True, str, None)
    Define whether the snapshot schedule should exist or not.


  unispherehost (True, str, None)
    IP or FQDN of the Unity management server.


  username (True, str, None)
    The username of the Unity management server.


  password (True, str, None)
    The password of the Unity management server.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether or not to validate SSL certificate.

    ``true`` - Indicates that the SSL certificate should be verified.

    ``false`` - Indicates that the SSL certificate should not be verified.


  port (optional, int, 443)
    Port number through which communication happens with Unity management server.





Notes
-----

.. note::
   - Snapshot schedule created through Ansible will have only one rule.
   - Modification of rule type is not allowed. Within the same type, other parameters can be modified.
   - If an existing snapshot schedule has more than 1 rule in it, only get and delete operation is allowed.
   - The *check_mode* is not supported.
   - The modules present in this collection named as 'dellemc.unity' are built to support the Dell Unity storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create snapshot schedule (Rule Type - every_n_hours)
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          name: "Ansible_Every_N_Hours_Testing"
          type: "every_n_hours"
          interval: 6
          desired_retention: 24
          state: "{{state_present}}"

    - name: Create snapshot schedule (Rule Type - every_day)
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
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
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          name: "Ansible_Every_N_Day_Testing"
          type: "every_n_days"
          day_interval: 2
          desired_retention: 16
          retention_unit: "days"
          state: "{{state_present}}"

    - name: Create snapshot schedule (Rule Type - every_week)
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
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
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          name: "Ansible_Every_Month_Testing"
          type: "every_month"
          day_of_month: 17
          auto_delete: True
          state: "{{state_present}}"

    - name: Get snapshot schedule details using name
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          name: "Ansible_Every_N_Hours_Testing"
          state: "{{state_present}}"

    - name: Get snapshot schedule details using id
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          id: "{{id}}"
          state: "{{state_present}}"

    - name: Modify snapshot schedule details id
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          id: "{{id}}"
          type: "every_n_hours"
          interval: 8
          state: "{{state_present}}"

    - name: Modify snapshot schedule using name
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          name: "Ansible_Every_Day_Testing"
          type: "every_day"
          desired_retention: 200
          auto_delete: False
          state: "{{state_present}}"

    - name: Delete snapshot schedule using id
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          id: "{{id}}"
          state: "{{state_absent}}"

    - name: Delete snapshot schedule using name
      snapshotschedule:
          unispherehost: "{{unispherehost}}"
          validate_certs: "{{validate_certs}}"
          username: "{{username}}"
          password: "{{password}}"
          name: "Ansible_Every_Day_Testing"
          state: "{{state_absent}}"



Return Values
-------------

changed (always, bool, True)
  Whether or not the resource has changed.


snapshot_schedule_details (When snapshot schedule exists, dict, {'existed': True, 'hash': 8742032390151, 'id': 'snapSch_63', 'is_default': False, 'is_modified': None, 'is_sync_replicated': False, 'luns': None, 'modification_time': '2021-12-14 21:37:47.905000+00:00', 'name': 'SS7_empty_hour_SS', 'rules': [{'access_type': 'FilesystemSnapAccessTypeEnum.CHECKPOINT', 'days_of_month': None, 'days_of_week': {'DayOfWeekEnumList': []}, 'existed': True, 'hash': 8742032280772, 'hours': [0], 'id': 'SchedRule_109', 'interval': 2, 'is_auto_delete': False, 'minute': 0, 'retention_time': 86400, 'retention_time_in_hours': 24, 'rule_type': 'every_n_days', 'type': 'ScheduleTypeEnum.N_DAYS_AT_HHMM'}], 'storage_resources': None, 'version': 'ScheduleVersionEnum.LEGACY'})
  Details of the snapshot schedule.


  id (, str, )
    The system ID given to the snapshot schedule.


  name (, str, )
    The name of the snapshot schedule.


  luns (, dict, )
    Details of volumes for which snapshot schedule applied.


    UnityLunList (, list, )
      List of volumes for which snapshot schedule applied.


      UnityLun (, dict, )
        Detail of volume.


        id (, str, )
          The system ID given to volume.





  rules (, list, )
    Details of rules that apply to snapshot schedule.


    id (, str, )
      The system ID of the rule.


    interval (, int, )
      Number of days or hours between snaps, depending on the rule type.


    hours (, list, )
      Hourly frequency for the snapshot schedule rule.


    minute (, int, )
      Minute frequency for the snapshot schedule rule.


    days_of_week (, dict, )
      Days of the week for which the snapshot schedule rule applies.


      DayOfWeekEnumList (, list, )
        Enumeration of days of the week.



    days_of_month (, list, )
      Days of the month for which the snapshot schedule rule applies.


    retention_time (, int, )
      Period of time in seconds for which to keep the snapshot.


    retention_time_in_hours (, int, )
      Period of time in hours for which to keep the snapshot.


    rule_type (, str, )
      Type of the rule applied to snapshot schedule.


    is_auto_delete (, bool, )
      Indicates whether the system can automatically delete the snapshot based on pool automatic-deletion thresholds.



  storage_resources (, dict, )
    Details of storage resources for which snapshot. schedule applied.


    UnityStorageResourceList (, list, )
      List of storage resources for which snapshot schedule applied.


      UnityStorageResource (, dict, )
        Detail of storage resource.


        id (, str, )
          The system ID given to storage resource.









Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

