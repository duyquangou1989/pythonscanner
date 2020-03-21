#!/usr/bin/env python
###Scanner Python QuangTD
from socket import *

if __name__ == '__main__':
	target = input('IP: ')
	targetIP = gethostbyname(target)

	arr_open = []

	for i in range (20,2025):
		s = socket(AF_INET, SOCK_STREAM)
		s.settimeout(2)
		result = s.connect_ex((targetIP,i))
		print('Scanning Port : %d' % i )
		if result == 0 :
			arr_open.append(i)
			#print('--> Port %d Open' % i)
		#else:
		#	print('--> Port %d Closed' % i)
		s.close()
	print(*arr_open)