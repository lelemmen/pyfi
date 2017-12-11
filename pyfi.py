import nmap

import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Your hostname is: {}".format(hostname))
print("Your IPv4 address is: {}".format(ip_address))
