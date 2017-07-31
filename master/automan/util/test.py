import netifaces
netifaces.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[2][0]['addr']
print ip  # should print "192.168.100.37"
