import logging
import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import ansible.playbook

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# Create a connection to the server:
connection = sdk.Connection(
  url='https://plirhapli01/ovirt-engine/api',
  username='admin@internal',
  password='Andorra2016',
  ca_file='/tmp/ca.pem',
)


# Get the reference to the root service:
system_service = connection.system_service()

# Find all the virtual machines and store the id and name in a
# dictioanry, so that looking them up later will be faster:
vms_service = system_service.vms_service()
vms_map = {
    vm.id: vm.name
    for vm in vms_service.list()
}

# Same for storage domains:
sds_service = system_service.storage_domains_service()
sds_map = {
    sd.id: sd.name
    for sd in sds_service.list()
}

# For each virtual machine find its snapshots, then for each snapshot
# find its disks:
for vm_id, vm_name in vms_map.iteritems():
    vm_service = vms_service.vm_service(vm_id)
    snaps_service = vm_service.snapshots_service()
    snaps_map = {
        snap.id: snap.description
        for snap in snaps_service.list()
    }
    for snap_id, snap_description in snaps_map.iteritems():
        snap_service = snaps_service.snapshot_service(snap_id)
        disks_service = snap_service.disks_service()
# Describimos para que solo salga un snapshots
        active = 0
	for disk in disks_service.list():
            if len(disk.storage_domains) > 0:
                sd_id = disk.storage_domains[0].id
                sd_name = sds_map[sd_id]
		active = 1
        if (active) > 0: 
                print("Nombre Maquina:{vm},Snapshot_ID:{snap},Descripcion_Snap:{num}".format(
                        vm=vm_name,
                        snap=snap_description,
	                num=snap_id, 
                        
                ))
	        active = 0 # ponemos la variable a 0





# Close the connection to the server:
connection.close()
