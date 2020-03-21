#!/usr/bin/env python
###Scanner Python QuangTD
from socket import *

def scan(ip,start,end):
	ports_open = []
	for i in range(start,end):
		s = socket(AF_INET,SOCK_STREAM)
		s.settimeout(1)
		result = s.connect_ex((ip,i))
		print('Scanning Port: %d' % i)
		if result == 0:
			print('Gottcha --> %d' % i)
			ports_open.append(i)
		s.close()
	return ports_open

if __name__ == '__main__':
	target = input('IP: ')
	targetIP = gethostbyname(target)

	print(scan(targetIP,80,445))
