import sys
import getopt
import optparse
import os
import time

from ovirtsdk.api import API
from ovirtsdk.xml import params
from random import choice

baseurl = "https://plirhapli01/ovirt-engine/api"
api = API(url=baseurl, username="admin@internal",password="Andorra2016",insecure=True)
vms = api.vms.list()

#ms_service = system
#for vm  in vms:
#   print vm.id
#    print("%s: %s" % (vm.name, vm.id))


vms_service = api.vms.list()
vms_map = {
   vm.id: vm.name
   for vm in vms_service.list()

}


sds_service = api.storagedomains.list()
sds_map = {
   sd.id: sd.name
  for sd in api.storagedomains.list()

}    

#for vm_id, vm_name in vms_map.iteritems():
#    vm_service = vms_service.vm_service(vm_id)
#    snaps_service = vm_service.snapshots_service()
#    snaps_map = {
#        snap.id: snap.description
#        for snap in api.snap.list()
#    }
#    for snap_id, snap_description in snaps_map.iteritems():
#        snap_service = snaps_service.snapshot_service(snap_id)
#        disks_service = snap_service.disks_service()
#        for disk in api.disks.list():
#            if len(disk.storage_domains) > 0:
#                sd_id = disk.storage_domains[0].id
#                sd_name = sds_map[sd_id]
#                print("{vm}:{snap}:{disk}:{sd}".format(
#                    vm=vm_name,
#                    snap=snap_description,
#                    disk=disk.alias,
#                    sd=sd_name,
#                ))

