'''
Created on 2017/02/08
@author: wayne_teng
'''
#-*- coding: utf-8 -*-

import os
import time
import sys
import string
import datetime
import subprocess
import ConfigParser
import unittest
from unittest import TestCase, main as unittest_main

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Path.conf") #C:\automation\ini\Path.conf


# filename = config.get("System_Setting", "filename")
# old_string = config.get("System_Setting", "old_string")
# new_string = config.get("System_Setting", "new_string")
# Server_host = config.get("System_Setting", "Server_host")
# Server_user = config.get("System_Setting", "Server_user")
# Server_passwd = config.get("System_Setting", "Server_passwd")
# host = config.get("Femtocell", "host")
# user = config.get("Femtocell", "user")
# passwd = config.get("Femtocell", "passwd")


class client(object):

	def __init__(self):
		'''
		Constructor
		'''
		pass

	global newfile

	def exec_command(self, exec_com):
		# change Server_host, Server_user, Server_passwd
		PlinkCommand = "plink.exe -ssh " + config.get("Femtocell", "host") + " " + "-l " + config.get(
			"Femtocell", "user") + " " + "-pw " + config.get("Femtocell", "passwd") + " " + exec_com
		print "Plink command is = " + PlinkCommand
		pipe = subprocess.Popen(
			PlinkCommand,
			shell=True,
			stdout=subprocess.PIPE).stdout
		out = pipe.read()
		f = open('log.txt', 'w')
		f.write(out)
		f.close

	def verify_result(self, exec_com):
		mystring = exec_com
		with open('log.txt', 'r') as searchfile:

			for line in searchfile:
				if mystring in line:
					print "Found String is : ", (mystring)
					# raise EOFError
					break
				else:
					#raise AssertionError,"The string could not be found"
					print "The string could not be found"
					# break

	def exec_server_command(self, exec_com):
		PlinkCommand = "plink.exe -ssh " + \
			config.get("Epc", "server") + " " + "-l root " + "-pw root " + exec_com
		print "Plink command is = " + PlinkCommand
		pipe = subprocess.Popen(
			PlinkCommand,
			shell=True,
			stdout=subprocess.PIPE).stdout
		out = pipe.read()
		f = open('Server_log.txt', 'w')
		f.write(out)
		f.close

	def verify_server_result(self, exec_com):
		mystring = exec_com
		with open('Server_log.txt', 'r') as searchfile:
			print searchfile

			for line in searchfile:
				if mystring in line:
					print "Found String is : ", (mystring)
					break
				else:
					#raise AssertionError,"The string could not be found"
					print "The string could not be found"
					# break

	def exec_mint_command(self, exec_com):
		global newfile
		PlinkCommand = "plink.exe -ssh " + config.get("Mint", "host") + " " + "-l " + config.get(
			"Mint", "user") + " " + "-pw " + config.get("Mint", "passwd") + " " + exec_com
		# print "plink.exe -ssh "+config.get("Femtocell", "host")+" "+"-l
		# "+config.get("Femtocell", "user")+" "+"-pw "+config.get("Femtocell",
		# "passwd")+'" " '+exec_com
		print "Plink command is = " + PlinkCommand
		pipe = subprocess.Popen(
			PlinkCommand,
			shell=True,
			stdout=subprocess.PIPE).stdout
		out = pipe.read()
		f = open('mintlog.txt', 'w')
		f.write(out)
		f.close

	def verify_mint_result(self, exec_com):
		mystring = exec_com
		with open('mintlog.txt', 'r') as searchfile:

			for line in searchfile:
				if mystring in line:
					print "Found String is : ", (mystring)
					# raise EOFError
					break
				else:
					#raise AssertionError,"The string could not be found"
					print "The string could not be found"

	def set_parameter(self, infile, old_word, new_word):
		if not os.path.isfile(infile):
			print ("Error on replace_word, not a regular file: " + infile)
			sys.exit(1)
		f1 = open(infile, 'r').read()
		f2 = open(infile, 'w')
		m = f1.replace(old_word, new_word)
		f2.write(m)

	def verify_ip_status(self):
		ip_file = open("ip.txt", "r")
		ip_lines = ip_file.readlines()
		ip_file.close()

		for ip_line in ip_lines:
			ip = ip_line.strip("\n")

			r = pyping.ping(ip, timeout=200, count=2)

			if r.ret_code == 0:
				print "ping %s is ok" % ip,
				print ": rtt time is", r.avg_rtt
			else:
				print "ping %s is failed" % ip
				#raise SystemExit
		# sys.exit(0)

	def run_server_ipsec(self, ipsec_type):
		self.exec_server_command("rm /etc/ipsec.conf")
		self.exec_server_command(
			"cp /etc/" +
			str(ipsec_type) +
			"_ipsec.conf /etc/ipsec.conf")
		self.exec_server_command("sync")
		time.sleep(1)
		self.exec_server_command("/usr/sbin/ipsec stop")
		self.exec_server_command("/usr/sbin/ipsec restart")
		time.sleep(3)

	def run_ipsec_times(self, times, ipsec_type):
		for i in range(0, times):
			self.exec_command(
				"rm " +
				config.get(
					"Femtocell",
					"ipsec_folder") +
				"ipsec.conf")
			self.exec_command(
				"cp " +
				config.get(
					"Femtocell",
					"ipsec_folder") +
				str(ipsec_type) +
				"_ipsec.conf " +
				config.get(
					"Femtocell",
					"ipsec_folder") +
				"ipsec.conf")
			self.exec_command("sync")
			time.sleep(1)
			self.exec_command("/usr/sbin/ipsec stop")
			self.exec_command("/usr/sbin/ipsec restart")
			time.sleep(2)
			self.exec_command("/usr/sbin/ipsec statusall")

			if ipsec_type == "128_0":
				self.verify_result("IKE proposal: AES_CBC_128/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_128_0.txt")
				self.verify_result("conn-1{1}:  NULL/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_128, ESP: NULL/HMAC_SHA1_96"
				f = open("count_128_0.txt", 'a')
				f.write(a + "\n")
				f.close
			elif ipsec_type == "128_128":
				self.verify_result("IKE proposal: AES_CBC_128/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_128_128.txt")
				self.verify_result("conn-1{1}:  AES_CBC_128/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_128, ESP: AES_CBC_128/HMAC_SHA1_96"
				f = open("count_128_128.txt", 'a')
				f.write(a + "\n")
				f.close

			elif ipsec_type == "128_256":
				self.verify_result("IKE proposal: AES_CBC_128/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_128_256.txt")
				self.verify_result("conn-1{1}:  AES_CBC_256/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_128, ESP: AES_CBC_256/HMAC_SHA1_96"
				# a = "Successful and a tunnel is created with AES-256 type"
				f = open("count_128_256.txt", 'a')
				f.write(a + "\n")
				f.close

			elif ipsec_type == "256_0":
				#self.verify_result("SC-SecGW{1}:  AES_CBC_256/HMAC_SHA1_96,")
				self.verify_result("IKE proposal: AES_CBC_256/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_256_0.txt")
				self.verify_result("conn-1{1}:  NULL/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_256, ESP: NULL/HMAC_SHA1_96"
				# a = "Successful and a tunnel is created with AES-256 type"
				f = open("count_256_0.txt", 'a')
				f.write(a + "\n")
				f.close

			elif ipsec_type == "256_256":
				#self.verify_result("SC-SecGW{1}:  AES_CBC_256/HMAC_SHA1_96,")
				self.verify_result("IKE proposal: AES_CBC_256/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_256_256.txt")
				self.verify_result("conn-1{1}:  AES_CBC_256/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_256, ESP: AES_CBC_256/HMAC_SHA1_96"
				# a = "Successful and a tunnel is created with AES-256 type"
				f = open("count_256_256.txt", 'a')
				f.write(a + "\n")
				f.close

			elif ipsec_type == "256_128":
				#self.verify_result("SC-SecGW{1}:  AES_CBC_256/HMAC_SHA1_96,")
				self.verify_result("IKE proposal: AES_CBC_256/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_256_128.txt")
				self.verify_result("conn-1{1}:  AES_CBC_128/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_256, ESP: AES_CBC_128/HMAC_SHA1_96"
				# a = "Successful and a tunnel is created with AES-256 type"
				f = open("count_256_128.txt", 'a')
				f.write(a + "\n")
				f.close

			else:
				print "Can not caeate a ipesc tunnel"
				break

	def run_iperf_times(self, times, ipsec_type, iperf_time, ip):
		for i in range(0, times):
			# self.exec_command("pwd")
			# time.sleep(1)
			# self.verify_result("/root")
			self.exec_command(
				"rm " +
				config.get(
					"Femtocell",
					"ipsec_folder") +
				"ipsec.conf")
			self.exec_command(
				"cp " +
				config.get(
					"Femtocell",
					"ipsec_folder") +
				str(ipsec_type) +
				"_ipsec.conf " +
				config.get(
					"Femtocell",
					"ipsec_folder") +
				"ipsec.conf")
			#self.exec_command("cp /opt/strongswan/etc/"+str(ipsec_type)+"_ipsec.conf /opt/strongswan/etc/ipsec.conf")
			self.exec_command("sync")
			time.sleep(1)
			self.exec_command("/usr/sbin/ipsec stop")
			self.exec_command("/usr/sbin/ipsec restart")
			time.sleep(2)
			self.exec_command("/usr/sbin/ipsec statusall")

			if ipsec_type == "128_0":
				#self.verify_result("SC-SecGW{1}:  NULL/HMAC_SHA1_96,")
				self.verify_result("IKE proposal: AES_CBC_128/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_128_0.txt")
				self.verify_result("conn-1{1}:  NULL/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_128, ESP: NULL/HMAC_SHA1_96"
				f = open("count_128_0.txt", 'a')
				f.write(a + "\n")
				f.close
			elif ipsec_type == "128_128":
				self.verify_result("IKE proposal: AES_CBC_128/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_128_128.txt")
				self.verify_result("conn-1{1}:  AES_CBC_128/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_128, ESP: AES_CBC_128/HMAC_SHA1_96"
				f = open("count_128_128.txt", 'a')
				f.write(a + "\n")
				f.close

			elif ipsec_type == "128_256":
				self.verify_result("IKE proposal: AES_CBC_128/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_128_256.txt")
				self.verify_result("conn-1{1}:  AES_CBC_256/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_128, ESP: AES_CBC_256/HMAC_SHA1_96"
				# a = "Successful and a tunnel is created with AES-256 type"
				f = open("count_128_256.txt", 'a')
				f.write(a + "\n")
				f.close
	
			elif ipsec_type == "256_0":
				#self.verify_result("SC-SecGW{1}:  AES_CBC_256/HMAC_SHA1_96,")
				self.verify_result("IKE proposal: AES_CBC_256/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_256_0.txt")
				self.verify_result("conn-1{1}:  NULL/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_256, ESP: NULL/HMAC_SHA1_96"
				# a = "Successful and a tunnel is created with AES-256 type"
				f = open("count_256_0.txt", 'a')
				f.write(a + "\n")
				f.close

			elif ipsec_type == "256_256":
				#self.verify_result("SC-SecGW{1}:  AES_CBC_256/HMAC_SHA1_96,")
				self.verify_result("IKE proposal: AES_CBC_256/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_256_256.txt")
				self.verify_result("conn-1{1}:  AES_CBC_256/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_256, ESP: AES_CBC_256/HMAC_SHA1_96"
				# a = "Successful and a tunnel is created with AES-256 type"
				f = open("count_256_256.txt", 'a')
				f.write(a + "\n")
				f.close

			elif ipsec_type == "256_128":
				#self.verify_result("SC-SecGW{1}:  AES_CBC_256/HMAC_SHA1_96,")
				self.verify_result("IKE proposal: AES_CBC_256/HMAC_SHA1_96")
				self.verify_result("INSTALLED, TUNNEL, reqid 1, ESP SPIs")
				os.system("del count_256_128.txt")
				self.verify_result("conn-1{1}:  AES_CBC_128/HMAC_SHA1_96")
				a = "Successful and a tunnel, IKE proposal: AES_CBC_256, ESP: AES_CBC_128/HMAC_SHA1_96"
				# a = "Successful and a tunnel is created with AES-256 type"
				f = open("count_256_128.txt", 'a')
				f.write(a + "\n")
				f.close

			else:
				print "Can not caeate a ipesc tunnel"
				break

			# self.srop_iferf_process(server)
			# self.srop_iferf_process(config.get("Femtocell", "host"))  ## change config
			# time.sleep(2)
			# self.exec_server_command("/root/iperf-server &")

			# self.exec_iferf_command("iperf -c 10.102.81.100 -t "+str(iperf_time)+" -i 5")
			# time.sleep(int(iperf_time))
			self.iferf_process(ip)

			time.sleep(3)
			if iperf_time < 10:
				self.verify_iperf_result("0.0- " + str(iperf_time) + ".0 sec")
			elif iperf_time >= 10:
				self.verify_iperf_result("0.0-" + str(iperf_time) + ".0 sec")
			else:
				print "Please input iper"

	def srop_iferf_process(self, ip):
		iperf_stop = "ps aux | grep -i iperf | awk {'print $2'} | xargs kill -9"
		PlinkCommand = "plink.exe -ssh " + ip + " " + \
			"-l root " + "-pw root " + '"' + iperf_stop + '"'
		print "Plink command is = " + PlinkCommand
		os.system(PlinkCommand)
		time.sleep(3)

	def iferf_process(self, ip):
		if ip == "10.102.81.100":  # femto to epc
			self.exec_iferf_femto(
				"iperf -c " +
				ip +
				" -t " +
				str(iperf_time) +
				" -i 5")
		elif ip == "10.102.81.11":  # epc to femto
			self.exec_iferf_epc(
				"iperf -c " +
				ip +
				" -t " +
				str(iperf_time) +
				" -i 5")
		else:
			pass

	def exec_iferf_femto(self, exec_com):
		#change host config
		PlinkCommand = "plink.exe -ssh " + config.get("System_Setting", "Server_host") + " " + \
			"-l " + user + " " + "-pw" + ' "" ' + exec_com
		print "Plink command is = " + PlinkCommand
		pipe = subprocess.Popen(
			PlinkCommand,
			shell=True,
			stdout=subprocess.PIPE).stdout
		out = pipe.read()
		f = open('iferf_temp.txt', 'w')
		f.write(out)
		f.close

	def exec_iferf_epc(self, exec_com):
		PlinkCommand = "plink.exe -ssh " + server + \
			" " + "-l root " + "-pw root " + exec_com
		print "Plink command is = " + PlinkCommand
		pipe = subprocess.Popen(
			PlinkCommand,
			shell=True,
			stdout=subprocess.PIPE).stdout
		out = pipe.read()
		f = open('iferf_temp.txt', 'w')
		f.write(out)
		f.close

	def verify_iperf_result(self, exec_com):
		mystring = exec_com
		with open('iferf_temp.txt', 'r') as searchfile:
			# print searchfile

			for line in searchfile:
				if mystring in line:
					# print "Found String is : ",(mystring)
					print line
					f = open('iferf_result.txt', 'a')
					f.write(line + "\n")
					f.close
					#os.system ("echo "+str(line)+ ">> result.txt")
				else:
					print "The string could not be found"

	def clean_log(self):
		os.system("del iferf_result.txt")
		os.system("del 0*_iferf_result.txt")
		os.system("del 128*_iferf_result.txt")
		os.system("del 256*_iferf_result.txt")
		os.system("del count_*txt")
		os.system("del result.txt")
		os.system("del Client\\*.txt")
		os.system("del Server\\*.txt")

	def write_log(self, filename):
		f = open(filename + '.txt', 'a')
		f.write(a + "\n")
		f.close

	def count_result(self, times, filename, ipsec_type):
		f = open(filename + ".txt", 'r')
		fileExt = (ipsec_type)
		line = f.read()
		a = string.count(line, fileExt)
		f.close()
		failcount = float(a)
		result = float(failcount / times)
		err_result = float(times - failcount) / times
		# result = float(failcount / times)
		# err_result = float(times - failcount) / times

		a = filename + ", try to connection " + \
			str(times) + ", successful percent is  " + "{0:.0f}%".format(float(result) * 100)
		b = "try to connection " + \
			str(times) + ",err_result percent is  " + "{0:.0f}%".format(float(err_result) * 100)
		print a
		print b
	#os.system("del result.txt")
		os.system("echo " + str(a) + " >> " + filename + "_result.txt")
		os.system("echo " + str(b) + " >> " + filename + "_result.txt")

	def CheckStatus(self, ipsec_type_set):
		fileName = "count_" + ipsec_type_set + ".txt"
		if os.path.exists(fileName):
			pass
		else:
			raise IOError

	def wireshark(self):
		os.system("cmd.exe /c C:\Sikuli-IDE\Sikuli-IDE.bat -r wireshark.skl")
		os.system("taskkill /f /im wireshark.exe")
		os.system("taskkill /f /im cmd.exe")

	def replace_config(self):
		# os.system("copy c:\\remote\\ini\\configFile c:\\remote\\configFile /Y")
		os.system("copy ..\\..\\automation\\ini\\configFile ..\\..\\automation\\configFile /Y")

	def replace_change(self, filename, old_string, new_string):
		with open(filename) as f:
			s = f.read()
			print s, "sss============================="
			if old_string not in s:
				print '"{old_string}" not found in {filename}.'.format(**locals())
				return

		with open(filename, 'w') as f:
			print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
			s = s.replace(old_string, new_string)
			f.write(s)

	def putfile_command(self):  # put file to Ubuntu
		local_file = ".\ini\configFile"
		remote_file = "/home/test/configFile"

		PscpCommand = "pscp.exe -pw " + config.get("System_Setting", "Server_passwd") + " " + local_file + \
			" " + config.get("System_Setting", "Server_user") + "@" + config.get("System_Setting", "Server_host") + ":" + remote_file
		print "Pscp command is = " + PscpCommand
		os.system(PscpCommand)

	def converter_start(self):
		subprocess.Popen(
			# 'cmd.exe /c "C:\\remote\dos2unix.exe configFile configFile"')
			'cmd.exe /c "..\\..\\automation\\tools\dos2unix.exe configFile configFile"')
		print ("exec converter configFile")

	def putconfigFile_femto(self):
		self.converter_start()
		os.system(
			# "C:\\remote\Winscp\winscp.com /command"
			"..\\..\\automation\\tools\\Winscp\winscp.com /command"
			' "open scp://root:root@' +
			# change host config
			config.get("System_Setting", "Server_host") +
			'/"' +
			' "put configFile  /opt/.data/config/mnt/tmp/configFile" "exit"')
		print (
			# "C:\\remote\Winscp\winscp.com /command"
			"..\\..\\automation\\tools\\Winscp\winscp.com /command"
			' "open scp://root:root@' +
			# change host config
			config.get("System_Setting", "Server_host") +
			'/"' +
			' "put configFile  /opt/.data/config/mnt/tmp/configFile" "exit"')

	def getlog_femto(self):

		print('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /root/rsys/setup/trace//dbgLog*" "exit"')
		os.system('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /root/rsys/setup/trace//dbgLog*" "exit"')
		print('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /var/log//message*" "exit"')
		os.system('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /var/log//message*" "exit"')
		print('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /mnt/flash/coredumps//core*" "exit"')
		os.system('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /mnt/flash/coredumps//core*" "exit"')            
		print('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /mnt/flash/halt_event/ENGINEERING/* ..\\..\\Result\\femtolog\\ENGINEERING" "exit"')
		os.system('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.242/" "get /mnt/flash/halt_event/ENGINEERING/* ..\\..\\Result\\femtolog\\ENGINEERING" "exit"')  
		os.system("rd ..\\..\\automation\\Result\\femtolog\\ /s /q")
		os.system("mkdir ..\\..\\automation\\Result\\femtolog\\ENGINEERING") 
		os.system("mkdir ..\\..\\automation\\Result\\femtolog\\")
		os.system("move dbgLog* ..\\..\\automation\\Result\\femtolog")
		os.system("move message* ..\\..\\automation\\Result\\femtolog")
		os.system("move core*  ..\\..\\automation\\Result\\femtolog")
		os.system("move ..\\..\\automation\\Result\\femtolog\\\ENGINEERING\\*.* ..\\..\\automation\\Result\\femtolog\\ENGINEERING")
		
	def Start_ePerView(self):
		subprocess.Popen(
			'cmd.exe /c "D:\Program Files (x86)\Broadcom\ePerView\ePerView.exe"')
		print ("exec ePerView.exe")
		time.sleep(10)

	def Sop_ePerView(self):
		time.sleep(2)
		os.system("taskkill /F /IM ePerView.exe")
		print ("Stop ePerView.exe")

	def Select_femtocell(self, ip, val):
		# os.system("copy c:\\remote\ini\power_org.conf c:\\remote\ini\power.conf /Y")
		# print ("copy c:\\remote\ini\power_org.conf c:\\remote\ini\power.conf /Y")
		os.system("copy ..\\..\\automation\ini\power_org.conf ..\\..\\automation\ini\power.conf /Y")
		print ("copy ..\\..\\automation\ini\power_org.conf ..\\..\\automation\ini\power.conf /Y")
		self.replace_change(
			".\ini\power.conf",
			"femto_ip=10.1.106.144",
			"femto_ip=" + ip)
		self.replace_change(
			".\ini\power.conf",
			"Max_Power=230",
			"Max_Power=" + val)

	def set_power_value(self):
		os.system("cmd.exe /c C:\Sikuli-IDE\Sikuli-IDE.bat -r ePerView.skl")
		os.system("taskkill /f /im cmd.exe")

	def verify_deblog(self, exec_com):
		mystring = exec_com
		with open('log.txt', 'r') as searchfile:
			os.system("del datatmp.txt")

			for line in searchfile:
				if mystring in line:
					# print "Found String is : ",line
					os.system(
						"echo " +
						str(line).rstrip('\n') +
						" >> datatmp.txt")
					# raise EOFError
				else:
					#raise AssertionError,"The string could not be found"
					print "The string could not be found"

	def compare_newfile(self):
		global newfile
		f = open("datatmp.txt")
		lines = f.readlines()
		# sorted(lines)
		# print lines
		newfile = sorted(lines)[-1]

		print "Download filename is : ", newfile

	def converter_log(self):  # put file to Ubuntu
		self.exec_mint_command("-m converter.txt")

	def trans_handover(self):
		mystring = "MSG: [S1ap: eNB->MME] HANDOVER NTFY"

		# with open('mintlog.txt', 'r') as searchfile:

		#   for line in searchfile:
		#       if mystring in line:
		#           print "Handover Success : ",(mystring)
		#       else:
		#           #raise AssertionError,"The string could not be found"
		#           print "Mobile not handover"

	# def trans_count(self):
		global success_count
	#   mystring = "MSG: [S1ap: eNB->MME] HANDOVER NTFY"
		f = open('mintlog.txt', 'r')
		line = f.read()
		success_count = string.count(line, mystring)
		f.close()
		print "success_count is :", success_count
		# os.system ("echo "+str(success_count)+ " > cont.txt")

	def compare_trans(self):
		global success_count
		mystring = "MSG: [S1ap: eNB->MME] HANDOVER NTFY"
		f = open('mintlog.txt', 'r')
		line = f.read()
		compare_count = string.count(line, mystring)
		f.close()
		# print "compare_count is :",compare_count
		if compare_count >> success_count:
			print "Mobile Handover Sucess"
		elif compare_count <= success_count:
			print "Mobile not Handover Sucess"
		else:
			print " not compare"

	def receive_handover(self):
		global a_success_count
		global b_success_count
		global c_success_count
		a = "MSG: [S1ap: eNB->MME] ENB STATUS TRFR"
		b = "MSG: [S1ap: eNB<-MME] UE CONTEXT REL CMD"
		c = "MSG: [S1ap: eNB->MME] UE CONTEXT REL CMPL"

		f = open('mintlog.txt', 'r')
		line = f.read()
		a_success_count = string.count(line, a)
		b_success_count = string.count(line, b)
		c_success_count = string.count(line, c)
		f.close()
		print "a_success_count is :", a_success_count
		print "b_success_count is :", b_success_count
		print "c_success_count is :", c_success_count

	def compare_receive(self):
		global a_success_count
		global b_success_count
		global c_success_count
		a = "MSG: [S1ap: eNB->MME] ENB STATUS TRFR"
		b = "MSG: [S1ap: eNB<-MME] UE CONTEXT REL CMD"
		c = "MSG: [S1ap: eNB->MME] UE CONTEXT REL CMPL"
		f = open('mintlog.txt', 'r')
		line = f.read()
		a_compare_count = string.count(line, a)
		b_compare_count = string.count(line, b)
		c_compare_count = string.count(line, c)
		f.close()

		print "a_success_count is :", a_compare_count
		print "b_success_count is :", b_compare_count
		print "c_success_count is :", c_compare_count

		if a_compare_count > a_success_count and b_compare_count > b_success_count and c_compare_count > c_success_count:
			print "1+++++++++++++++++++++++"
		elif a_compare_count <= a_success_count or b_compare_count <= b_success_count or c_compare_count <= c_success_count:
			print "2+++++++++++++++++++++++"
		else:
			print " not compare"

	def getlog_femto(self,femce_ip):

		print('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@'+femce_ip+'/" "get /root/rsys/setup/trace//dbgLog*" "exit"')
		os.system('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@'+femce_ip+'/" "get /root/rsys/setup/trace//dbgLog*" "exit"')
		print('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@'+femce_ip+'/" "get /var/log//message*" "exit"')
		os.system('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@'+femce_ip+'/" "get /var/log//message*" "exit"')
		print('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@'+femce_ip+'/" "get /mnt/flash/coredumps//core*" "exit"')
		os.system('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@'+femce_ip+'/" "get /mnt/flash/coredumps//core*" "exit"')            
		print('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@'+femce_ip+'/" "get /mnt/flash/halt_event/ENGINEERING/* ..\\..\\Result\\femtolog\\ENGINEERING" "exit"')
		os.system('..\\..\\automation\\tools\\WinSCP\winscp.com /command "open scp://root:root@'+femce_ip+'/" "get /mnt/flash/halt_event/ENGINEERING/* ..\\..\\Result\\femtolog\\ENGINEERING" "exit"')  
		os.system("rd ..\\..\\automation\\Result\\femtolog\\ /s /q")
		os.system("mkdir ..\\..\\automation\\Result\\femtolog\\ENGINEERING") 
		os.system("mkdir c..\\..\\automation\\Result\\femtolog\\")
		os.system("move dbgLog* c..\\..\\automation\\Result\\femtolog")
		os.system("move message* c..\\..\\automation\\Result\\femtolog")
		os.system("move core*  ..\\..\\automation\\Result\\femtolog")
		os.system("move .\\..\\automation\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\automation\\Result\\femtolog\\ENGINEERING")


	def test(self):
		# gap = 8
		# now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
		# hr= now.split("-")[3]
		# print int(hr)-8
		utc_datetime = datetime.datetime.utcnow()
		# 9-8-2016 1:55:55.000
		femto_time = utc_datetime.strftime("%m-%d-%Y %H:%M:%S")
		# hr= femto_time.split("-")[3]
		# print hr
	#   while True:

	#       os.system("del mintlog.txt")
	#       self.getfile_command()

	#       f = open("mintlog.log", 'r')
	#       fileString = f.read()
	#       f.close()

	#       if mystring != -1:
	#           # Not reached.
	#           print("String found")
	#           break
	#       else:
	#           time.sleep(20)
	#           print("String not found")


class TestStringMethods(unittest.TestCase, client):

	def test_upper(self):
		TC = client()
		self.clean_log()
		repeat_Times = 1
		ipsec_type_set = "128_128"
#       self.exec_command("rm -rf /root/OAM/setup/trace")
# -------------------mark-----------
#       self.run_server_ipsec(ipsec_type_set)
#       self.run_ipsec_times(repeat_Times,ipsec_type_set)
# ----------------------------------------
#                   #Should be follow verify type setting
		self.CheckStatus(ipsec_type_set)
		self.count_result(
			repeat_Times,
			"count_" + ipsec_type_set,
			"IKE proposal: AES_CBC_128, ESP: AES_CBC_128/HMAC_SHA1_96")

		# self.wireshark()

if __name__ == "__main__":
	# TC = client()  # Run_Test  = class name
	# # self.exec_mint_command("-m converter.txt")
	# # TC.exec_command("-m 123.txt")  

	# TC.exec_command("/root/rsys/scripts/reboot-fap")
	# time.sleep(130)


	# Server_host = config.get("System_Setting", "Server_host")
	print config.get("System_Setting", "Server_host")
	# TC.getlog_femto("10.1.106.242")

	#TC.verify_deblog("dbglog")
	# TC.compare_newfile()
	# TC.exec_mint_command("/root/Public/rlogapp/femto 10.1.106.144 "+ newfile)
	# TC.converter_log()
	# TC.exec_mint_command("cat /root/Public/rlogapp/log.txt")
	# time.sleep(10)

	# TC.trans_handover()

	# TC.Sop_ePerView()
	# TC.Select_femtocell("10.1.106.144","100")
	# TC.Start_ePerView()
	# TC.set_power_value()
	# TC.Sop_ePerView()

	# TC.exec_command("ls /root/rsys/setup/trace/")
	# TC.verify_deblog("dbglog")
	# TC.compare_newfile()
	# TC.exec_mint_command("/root/Public/rlogapp/femto 10.1.106.144 "+ newfile)
	# TC.converter_log()
	# TC.exec_mint_command("cat /root/Public/rlogapp/144.log")

	# TC.compare_trans()

	# TC.Select_femtocell("10.1.106.144","100")
	# TC.Start_ePerView()
	# TC.set_power_value()  /root/Public/rlogapp/
	# TC.Sop_ePerView()
	# time.sleep(10)

	# TC.exec_command("ls /root/rsys/setup/trace/")
	# TC.verify_deblog("dbglog")
	# TC.compare_newfile()
	# TC.exec_mint_command("/root/Public/rlogapp/femto 10.1.106.144 "+ newfile)
	# TC.converter_log()
	# TC.exec_mint_command("cat /root/Public/rlogapp/log.txt")

	# TC.compare_trans()

	# TC.receive_handover()
	# # TC.trans_handover()

	# # time.sleep(20)
	# # TC.compare_handover()

	# TC.receive_handover()
	# time.sleep(20)
	# TC.compare_receive()
	# TC.getlog_femto()

	# TC.replace_change("configFile","LTE_DL_BANDWIDTH 100","LTE_DL_BANDWIDTH 150")
	# TC.replace_change("configFile","LTE_UL_BANDWIDTH 100","LTE_UL_BANDWIDTH 250")
	# TC.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n100","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n150")

	# reboot

	# TC.replace_change("configFile","LTE_DL_BANDWIDTH 75","LTE_DL_BANDWIDTH 75")
	# TC.replace_change("configFile","LTE_UL_BANDWIDTH 75","LTE_UL_BANDWIDTH 75")
	# TC.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n75","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n75")
	# reboot

	# TC.replace_change("configFile","LTE_DL_BANDWIDTH 50","LTE_DL_BANDWIDTH 50")
	# TC.replace_change("configFile","LTE_UL_BANDWIDTH 50","LTE_UL_BANDWIDTH 50")
	# TC.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n50","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n50")
# reboot
	# TC.replace_change("configFile","LTE_DL_BANDWIDTH 25","LTE_DL_BANDWIDTH 25")
	# TC.replace_change("configFile","LTE_UL_BANDWIDTH 25","LTE_UL_BANDWIDTH 25")
	# TC.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n25","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n25")
# reboot

	# TC.replace_change("configFile",'LTE_CIPHERING_ALGO_LIST "128-EEA1"','LTE_CIPHERING_ALGO_LIST "128-EEA2"')
	# TC.replace_change("configFile",'LTE_INTEGRITY_ALGO_LIST "128-EIA1"','LTE_INTEGRITY_ALGO_LIST "128-EIA2"')
#   TC.replace_change("configFile","LTE_DL_BANDWIDTH 100","LTE_DL_BANDWIDTH 150")
#   TC.replace_change("configFile","LTE_UL_BANDWIDTH 100","LTE_UL_BANDWIDTH 150")
#   TC.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n100","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n150")

# reboot

	# TC.replace_change("configFile",'LTE_CIPHERING_ALGO_LIST "128-EEA1"','LTE_CIPHERING_ALGO_LIST "128-EEA2"')
	# TC.replace_change("configFile",'LTE_INTEGRITY_ALGO_LIST "128-EIA1"','LTE_INTEGRITY_ALGO_LIST "128-EIA2"')
#   TC.replace_change("configFile","LTE_DL_BANDWIDTH 75","LTE_DL_BANDWIDTH 75")
#   TC.replace_change("configFile","LTE_UL_BANDWIDTH 75","LTE_UL_BANDWIDTH 75")
#   TC.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n75","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n75")
# reboot

	# TC.replace_change("configFile",'LTE_CIPHERING_ALGO_LIST "128-EEA1"','LTE_CIPHERING_ALGO_LIST "128-EEA2"')
	# TC.replace_change("configFile",'LTE_INTEGRITY_ALGO_LIST "128-EIA1"','LTE_INTEGRITY_ALGO_LIST "128-EIA2"')
#   TC.replace_change("configFile","LTE_DL_BANDWIDTH 50","LTE_DL_BANDWIDTH 50")
#   TC.replace_change("configFile","LTE_UL_BANDWIDTH 50","LTE_UL_BANDWIDTH 50")
#   TC.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n50","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n50")
# reboot

	# TC.replace_change("configFile",'LTE_CIPHERING_ALGO_LIST "128-EEA1"','LTE_CIPHERING_ALGO_LIST "128-EEA2"')
	# TC.replace_change("configFile",'LTE_INTEGRITY_ALGO_LIST "128-EIA1"','LTE_INTEGRITY_ALGO_LIST "128-EIA2"')
#   TC.replace_change("configFile","LTE_DL_BANDWIDTH 25","LTE_DL_BANDWIDTH 25")
#   TC.replace_change("configFile","LTE_UL_BANDWIDTH 25","LTE_UL_BANDWIDTH 25")
#   TC.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n25","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n25")
# reboot
