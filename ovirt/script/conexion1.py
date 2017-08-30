#url ="Your ovirt engine api url"
#username ="user to access the api"
#password ="password of above user"
#ca_file ="location of ca cert file"

# This program can be used to display Vm nic details and IP addresses assigned to them.

from ovirtsdk.api import API
from ovirtsdk.xml import params
import time

try:
    api = API(url="https://myrhevm.humblec.com/api",
              username="admin@internal",
              password="redhat",
              ca_file="/root/ca.crt")
    try:
         vmsList = api.vms.list(max=500)
         for instance in vmsList:
                print '\t \t\t\tVM :%s' % (instance.name.upper())
                address=[]
                if instance.status.state == 'up' and instance.get_guest_info():
                        vmnics= instance.get_nics().list()
                        ips = instance.get_guest_info().get_ips().get_ip()
                        for card in vmnics:
                                print 'Net.ID:%s \t Name:%s \t MacAddress:%s \t Interface:%s \t Plugged:%s \t Linked:%s ' % (card.network.id, card.name, card.mac.address, card.interface, card.plugged, card.linked)
                        for ip in ips:
                                address.append(ip.get_address())
                                print '\t IP : %s' % ( ip.get_address())
    except Exception as e:
        print " Exception:\n%s' % str(e)"


    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex
