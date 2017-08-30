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

# Get the reference to the "vms" service:
vms_service = connection.system_service().vms_service()

# Use the "list" method of the "vms" service to list all the virtual machines of the system:
vms = vms_service.list()

# Print the virtual machine names and identifiers:
for vm in vms:
  print("%s: %s" % (vm.name, vm.id))


# Close the connection to the server

connection.close()
