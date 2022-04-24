import os
from malicious import Print
hostname = "192.168.1.2" #example
response = os.system("ping -c 1 " + hostname)
#arp = os.system("arp -a")

#and then check the response...
if response == 0:
  print (hostname, 'is up!')
else:
  print (hostname, 'is down!')

#print(arp)

instance = Print()
instance.print_word("my stuff")