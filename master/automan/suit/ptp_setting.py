'''
Created on 2017/06/30
@author: ron_chen
@title: Coding the customer.ptp by sublime.
'''
import sys
import os
import time
sys.path.insert(0, '..\\util')
import unittest
from network import SCP
from network import RS232_Putty
from network import SSH
from android import Android
from android import AdbClient
from uiautomator_control import Uiautomator_Control

class PTP_Setting(unittest.TestCase):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print 'Start by Automated execution.'
		global scp, ssh, rs232_putty
		global android, adbClient, uiautomator_control
		global reboot_command, customer_ptp_local, customer_remote
		global plmn
		global boolean
		scp = SCP()
		ssh = SSH()
		rs232_putty = RS232_Putty()
		uiautomator_control = Uiautomator_Control()
		android = Android()
		adbClient = AdbClient()
		reboot_command = './rsys/scripts/reboot-fap'
		customer_ptp_local = 'customer.ptp'
		customer_remote = 'customer.rcS'
		plmn = "123-45"

	def tearDown(self):
		print 'Stop by Automated execution.'

	def test_PTP_Setting(self):
		print 'The test_PTP_Setting function.'
		android.Check_Mobile_Note4()
		adbClient.Start_Airplane()
		rs232_putty.RS232_Disconnect_Putty()
		scp.SCP_Connection()
		scp.SCP_Upload('/mnt/flash/', customer_ptp_local)
		ssh.SSH_Command('mv /mnt/flash/'+customer_ptp_local +
						' '+'/mnt/flash/'+customer_remote)
		ssh.SSH_Command('chmod 777 /mnt/flash/'+customer_remote)
		ssh.SSH_Command(reboot_command)
		rs232_putty.RS232_Connect_Putty()
		time.sleep(140)
		rs232_putty.RS232_Verify_Message_Putty('Time :')
		adbClient.Stop_Airplane()
		uiautomator_control.Switch_Home()
		uiautomator_control.Switch_Setting_Note4()
		uiautomator_control.Switch_More_networks()
		uiautomator_control.Switch_Mobile_networks()
		uiautomator_control.Access_Point_Names()
		uiautomator_control.Remove_APN_Note4()
		uiautomator_control.Add_APN('QCI9')
		time.sleep(5)
		uiautomator_control.Switch_Home()
		uiautomator_control.CellMapper()
		boolean = uiautomator_control.ServiceMode_Verify_PLMN(plmn)
		if boolean == True:
			print 'Catch the correct PLMN.'
		if boolean == False:
			print 'Cannot Catch correct PLMN.'
			uiautomator_control.Switch_Home()
			uiautomator_control.Switch_Setting_Note4()
			uiautomator_control.Switch_More_networks()
			uiautomator_control.Switch_Mobile_networks()
			uiautomator_control.Switch_Network_Operators()
			uiautomator_control.Information_Alert()
			uiautomator_control.Click_Device_Value1('note4')
			uiautomator_control.Information_Alert()
			time.sleep(20)
			uiautomator_control.Switch_Home()

if __name__ == "__main__":
	unittest.main()
	# testcase = PTP_Setting()
	# testcase.test_PTP_Setting()
