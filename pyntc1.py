#get ios facts and basic basic config
import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='192.168.122.72', username='carlo', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

ios_output = iosvl2.facts
print (json.dumps(ios_output, indent=4))

iosvl2.config_list(['hostname s1', 'router ospf 1', 'network 0.0.0.0 255.255.255.255 area 0'])

iosvl2.close()


#different method for config list
import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='192.168.122.72', username='carlo', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

ios_output = iosvl2.facts
print (ios_output)

#iosvl2.config_list(['hostname s1', 'router ospf 1', 'network 0.0.0.0 255.255.255.255 area 0'])
iosvl2.config_list(['hostname s1',
                    'router ospf 1',
                    'no network 0.0.0.0 255.255.255.255 area 0',
                    'network 10.1.1.0 0.0.0.255 area 0',
                    'network 10.1.2.0 0.0.0.255 area 1'])

iosvl2.close()


#backup configs
import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='192.168.122.72', username='carlo', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

ios_run = iosvl2.running_config
print (ios_run)

iosvl2.close()

#backup configs and save to a file
import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='192.168.122.72', username='carlo', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

ios_run = iosvl2.running_config

HOST = '192.169.122.72'
saveoutput = open('switch' + HOST, 'w')
saveoutput.write(ios_run)
saveoutput.close

#backup configs better script
import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='192.168.122.72', username='carlo', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

ios_run = iosvl2.backup_running_config('iosvl2-1.cfg')

iosvl2.close()