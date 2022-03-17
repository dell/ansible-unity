# ansible-unity Change Log
## Version 1.3.0 - released on 25/03/22
- Enhanced host module to support listing of network addresses, FC initiators, ISCSI initiators and allocated volumes of a host
- Enhance host module to support add/remove network address to/from a host.
- Enhanced host module to support both mapping and un-mapping of non-logged-in initiators to host.
- Enhanced consistency group module to support enable/disable replication in consistency group
- Enhanced Storage pool module to support creation of storage pool
- Enhanced Storage Pool module to support listing of drive details of a pool
- Renamed gatherfacts module to info module
- Enhanced Info module to list disk groups.
- Removed dellemc.unity prefix from module names.
- Added rotating file handler for logging.
- Bugfix in volume module to retrieve details of non-thin volumes.

## Version 1.2.1 - released on 28/09/21
- Fixed typo in galaxy.yml
- Updated few samples in modules
- Added dual licensing
- Documentation updates

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