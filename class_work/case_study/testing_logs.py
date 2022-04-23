import syslog
from sys import argv
from os import system
#syslog.openlog(argv[0])
syslog.syslog(syslog.LOG_NOTICE, "bro bro bro bro This is another Log Notice")
#syslog.openlog()
try:
    system("sudo cat /private/var/log/system.log")
except PermissionError:
    print("Missing perms")
except Exception as error:
    print(error)