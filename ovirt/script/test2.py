from ovirtsdk.api import API
from ovirtsdk.xml import params


try:
    api = API (url="https://plirhapli01/ovirt-engine/api",
               username="admin@internal",
               password="Andorra2016",
               ca_file="/tmp/ca.pem")

    dc_list = api.datacenters.list()

    for dc in dc_list:
        print "%s (%s)" % (dc.get_name(), dc.get_id())

    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex
