import paramiko
import telnetlib
import sys
import ConfigParser
import os
import time
from paramiko import SSHClient
from scp import SCPClient
import serial
import subprocess

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\network.conf")

ser = serial.Serial()
ser.port = config.get("RS232_setting", "ser.port")
ser.baudrate = config.get("RS232_setting", "ser.baudrate")
ser.writeTimeout = int(config.get("RS232_setting", "ser.writeTimeout"))
ser.timeout = int(config.get("RS232_setting", "ser.timeout"))
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False

# host = sys.argv[1]


class RS232(object):

	def RS232_Connect(self):
		try:
			ser.open()
		except Exception, e:
			print "error open serial port: " + str(e)
			exit()

	def RS232_Command(self, command):

		if ser.isOpen():

			try:
				ser.flushInput()
				ser.flushOutput()
				# ser.write("root\r\n")
				# time.sleep(1)
				ser.write(command+"\r\n")
				time.sleep(1)
			except Exception, e1:
				print "error communicating...: " + str(e1)
		else:
			print "cannot open serial port "

	def RS232_Response(self):
		numOfLines = 0
		global response
		while True:
			response = ser.readline()

			f = open('..\\..\\temp\\RS232_log.txt', 'a')
			print("read data: " + response)
			f.write(response)
			f.close()

			numOfLines = numOfLines + 1
			if numOfLines >= 2:
				break
				
	def RS232_Verify_Message(self,message):
		if message in response:
			print 'found respone message - PASS'
			print message
		else:
			raise Exception ('not found respone message - FAIL')

	def RS232_Disonnect(self):
		ser.close()

class RS232_Putty(object):
	
	def RS232_Connect_Putty(self):
		os.system("taskkill /F /IM putty.exe")
		print 'The putty.exe is shutdown!'
		time.sleep(1)
		os.system("del ..\\..\\temp\\putty.log")
		print 'The putty.log is killed!'
		time.sleep(1)
		subprocess.Popen('..\\..\\tools\\putty.exe -load '+'"'+ser.port+'"')
		print '..\\..\\tools\\putty.exe -load '+'"'+ser.port+'"'

	def RS232_Verify_Message_Putty(self,message):
		try:
			time.sleep(2)
			f = open("..\\..\\temp\\putty.log", 'r')
			fileString = f.read()
			f.close()
			if message in fileString:
				print 'Found respone message \''+ message +'\' - PASS'
			else:
				raise Exception ('The message is not found - FAIL')
		except:
			raise Exception("The message is not found - FAIL")

	def RS232_Disconnect_Putty(self):
		print "taskkill /F /IM putty.exe"
		os.system("taskkill /F /IM putty.exe")

class Telnet(object):

	def Telnet_Connection(self):
		global telnet

		host = config.get("Telnet_setting", "host")
		port = int(config.get("Telnet_setting", "port"))

		telnet = telnetlib.Telnet(host, port)
		time.sleep(1)

	def Telnet_Command(self, commandline):
		self.Telnet_Connection()
		telnet.write(commandline + "\r\n")
		print "exec telnet command - " + '"' + commandline + '"'

	def Telnet_Respone(self, message):
		time.sleep(int(config.get("Telnet_setting", "respone_wait_time")))
		content = telnet.read_very_eager().decode('big5', 'ignore')

		if message in content:
			print 'found respone message - PASS'
			print message
		else:
			raise Exception('not found respone message - FAIL')


class SSH(object):

	def SSH_Connection(self):
		global s
		host = config.get("SSH_setting", "host")
		name = config.get("SSH_setting", "name")
		passwd = config.get("SSH_setting", "passwd")
		port = int(config.get("SSH_setting", "port"))

		s = paramiko.SSHClient()
		s.load_system_host_keys()
		s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		s.connect(host, port, name, passwd, timeout=8)

	def SSH_Command(self, commandline):
		self.SSH_Connection()
		global stdin, stdout, stderr
		stdin, stdout, stderr = s.exec_command(commandline)
		print "exec SSH command - " + '"' + commandline + '"'

	def SSH_Respone(self, message):
		cmd_result = stdout.read(), stderr.read()
		result = ' '.join(map(str, cmd_result))
		respone_result = result.strip()

		if message in respone_result:
			print 'found respone message - PASS'
			# print message
		else:
			raise Exception('not found respone message - FAIL')
		s.close()

class SFTP(object):

	def SFTP_Connection(self):
		global sftp, transport

		host = config.get("SFTP_setting", "host")
		name = config.get("SFTP_setting", "name")
		passwd = config.get("SFTP_setting", "passwd")

		transport = paramiko.Transport((host, 22))
		transport.connect(username=name, password=passwd)
		sftp = paramiko.SFTPClient.from_transport(transport)

	def SFTP_Download(self, reomte_path, filename):
		self.SFTP_Connection()
		sftp.get(reomte_path + filename, '..\\..\\temp\\' + filename)
		print('Download '+reomte_path + filename +
			  " from " + '..\\..\\temp\\' + filename)
		transport.close()

	def SFTP_Upload(self, reomte_path, filename):
		self.SFTP_Connection()
		sftp.put('..\\..\\temp\\' + filename, reomte_path + filename)
		print('Upload ' + '..\\..\\temp\\' +
			  filename + " to "+reomte_path + filename)
		transport.close()


class SCP(object):

	def SCP_Connection(self):
		global ssh, scp, SCPClient

		host = config.get("SCP_setting", "host")
		name = config.get("SCP_setting", "name")
		passwd = config.get("SCP_setting", "passwd")

		ssh = SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.load_system_host_keys()
		ssh.connect(host, username=name, password=passwd)

	def SCP_Download(self, reomte_path, filename):
		self.SCP_Connection()
		global scp
		with SCPClient(ssh.get_transport()) as scp:
			scp.get(reomte_path + filename, '..\\..\\temp\\' + filename)
			print('Download '+reomte_path + " from " +
				  filename + '..\\..\\temp\\' + filename)
			scp.close()

	def SCP_Download_Folder(self, ip, reomte_path, local_path):
		os.system('..\\..\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.' +
				  ip + '/" "get ' + reomte_path + ' ..\\..\\Result\\' + local_path + '\\" "exit"')
		print 'The log in the Z:\\automation\\Result\\femtolog'

	def SCP_Upload(self, reomte_path, filename):
		self.SCP_Connection()
		global scp
		with SCPClient(ssh.get_transport()) as scp:
			scp.put('..\\..\\temp\\' + filename, reomte_path + filename)
			print('Upload ' + '..\\..\\temp\\' +
				  filename + " to "+reomte_path + filename)
			scp.close()

	def SCP_Upload_Folder(self, ip, local_path, reomte_path):
		os.system('..\\..\\tools\\WinSCP\winscp.com /command "open scp://root:root@10.1.106.' +
				  ip + '/" "put ..\\..\\temp\\' + local_path + "\ " + reomte_path + '/" "exit"')

if __name__ == "__main__":
	print 'The Network.py code.'
	# Ron
	# ssh = SSH()
	# ssh.SSH_Command("./rsys/scripts/reboot-fap")
	# rs232 = RS232_Putty()
	# rs232.RS232_Connect()
	# time.sleep(140)
	# rs232.RS232_Disconnect()
	# rs232.RS232_Verify_Message("Time : 0 sec")
	# ssh = SSH()
	# ssh.SSH_Command('rm -rf trace')
	# ssh.SSH_Respone('')
	# print 'The file was deleted.'
	# ssh.SSH_Command('cp -r /tmp/trace .')
	# ssh.SSH_Respone('')
	# print 'The file was Copied.'
	# scp = SCP()
	# scp.SCP_Download_Folder('242', '/tmp/trace/', 'femtolog')
	##########################################################################
	# TC = RS232()
	# os.system("del ..\\..\\temp\\RS232_log.txt")
	# TC.RS232_Connect()
	# for i in range(0,101):
	# 	print i,"times"
	# 	TC.RS232_Command("root")
	# 	TC.RS232_Response()
	# 	TC.RS232_Command("root")
	# 	TC.RS232_Response()
	# 	TC.RS232_Command("/sbin/reboot")
	# 	time.sleep(3)
	# 	TC.RS232_Response()
	# 	time.sleep(20)

	# TC = SSH()  # Run_Test  = class name
	# TC.Telnet_Command('#$$CONNECT')
	# TC.Telnet_Respone('C: CONNECT 0x00 ok. Waiting for User to Configure Test Mobile')
	# TC.SSH_Command('pwd')
	# TC.SSH_Respone('/mnt/flash/root')
	# TC.SFTP_Upload('/root/','23')
	# TC.SFTP_Download('/root/','23')
	# TC.SCP_Download('/root/','23')
	# TC.SSH_Command('ls /root/askey-test')
	# TC.SCP_Download_Folder('242','/tmp/trace/','femtolog')
	# TC.SCP_Upload_Folder('242','1.txt','/tmp/trace/')
	# TC.SCP_Upload('/root/','23')

	# TC.RS232_Connect()
	# TC.RS232_Command("pwd")
	# TC.RS232_Response()
	# TC.RS232_Disonnect()
#	LED1_Green_ON
	# TC.SSH_Command('cat /sys/class/leds/led_1_R/brightness')
	# TC.SSH_Respone('1')
	# TC.SSH_Command('cat /sys/class/leds/led_1_G/brightness')
	# TC.SSH_Respone('1')
	# TC.SSH_Command('cat /sys/class/leds/led_1_B/brightness')
	# TC.SSH_Respone('0')
#	LED1_RED_ON
	# TC.SSH_Command('cat /sys/class/leds/led_1_R/brightness')
	# TC.SSH_Respone('0')
	# TC.SSH_Command('cat /sys/class/leds/led_1_G/brightness')
	# TC.SSH_Respone('0')
	# TC.SSH_Command('cat /sys/class/leds/led_1_B/brightness')
	# TC.SSH_Respone('0')
