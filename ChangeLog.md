# ansible-unity Change Log
## Version 1.2.0 - released on 25/06/21
- Added support for Application tagging.
- Added CRUD operations support for User Quota on Filesystem/Quota tree.
- Added CRUD operations support for Quota tree.
- Consistency group module is enhanced to map/unmap hosts to/from a new or existing consistency group.
- Filesystem module is enhanced to update default quota configuration during create operation.
- Filesystem module is enhanced to associate/dissociate snapshot schedule to/from a Filesystem.
- Volume module is enhanced to support map/unmap multiple hosts from a volume.
- Gather facts module is enhanced to list User Quota and Quota tree components.

## Version 1.1.0 - released on 02/12/20
- Gather facts module is enhanced to list Filesystem snapshots, NAS servers, File systems, NFS exports, SMB shares.
- Added CRUD operations support for NFS export.
- Added CRUD operations support for SMB share.
- Added support to get/modify operations on NAS server.
- Added CRUD operations support for Filesystem.
- Added CRUD operations support for Filesystem snapshot.

## Version 1.0.0 - released on 22/06/20
- Gather facts module is enhanced to list volumes, consistency groups, FC initiators, iSCSI initiators, hosts, snapshot schedules.
- Added CRUD operations support for Volume.
- Added CRUD operations support for Consistency group.
- Added support for adding/removing volumes to/from a consistency group.
- Added support to get/modify operations on storage pool.
- Added support for CRUD operations on a host with FC/iSCSI initiators.
- Added support to add/remove FC/iSCSI initiators to/from a host.
- Added support for CRUD operations on a snapshot of a volume.
- Added support to create a snapshot for a consistency group.
- Added support to map/unmap a host to/from a snapshot.
- Added CRUD operations support for a snapshot schedule.