import logging
import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# Create a connection to the server:
connection = sdk.Connection(
  url='https://plirhapli01/ovirt-engine/api',
  username='admin@internal',
  password='Andorra2016',
  ca_file='/tmp/ca.pem',
)



# Get the reference to the root of the tree of services:
system_service = connection.system_service()



#Find the virtual machine:
vms_service = system_service.vms_service()
vm = vms_service.list(search='name=dliansibletower')[0]

# Find the service that manages the virtual machine:
vm_service = vms_service.vm_service(vm.id)

# Find the snapshot. Note that the snapshots collection doesn't support
# search, so we need to retrieve the complete list and the look for the
# snapshot that has the description that we are looking for.

snaps_service = vm_service.snapshots_service()
snaps = snaps_service.list()
#nap = next(
#  (s for s in snaps if s.description == 'dliansibletower'),
#  None
#)
#d = snap.id

snaps_map = {
        snap.id: snap.description
        for snap in snaps_service.list()
    }


for snap_id, snap_description in snaps_map.iteritems():
        snap_service = snaps_service.snapshot_service(snap_id)
        disks_service = snap_service.disks_service()
        for disk in disks_service.list():
            if len(disk.storage_domains) > 0:
                sd_id = disk.storage_domains[0].id
                sd_name = sds_map[sd_id]
                print("{vm}:{snap}:{disk}:{sd}".format(
                    vm=vm_name,
                    snap=snap_description,
                    disk=disk.alias,
                    sd=sd_name,
                ))






# Close the connection to the server

connection.close()
