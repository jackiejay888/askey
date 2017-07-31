'''
Created on 2017/06/14
@Author: ron_chen
@Test case T-SVT-2881: Verify the earfcn is matched when set the correct Earfcn number via oam at the Device.Services.FAPService.1.CellConfig.LTE.RAN.RF.EARFCNDL
					   (The value is not dynamic change)
@Precondition:
	Device: Note 4.(Can be used call number *#0011#, and search the cell information)
@Test step:
	1. Login to acs server.
	2. Set the Earfcn via EARFCNDL and EARFCNUL data under the RF folder of Parameter List.
	3. By use to SSH command line to reboot the cell.
	4. Try to registered the cell by mobile, make sure the cell is launched or not.
'''

import sys
sys.path.insert(0, '..\\util')
import os
import time
import string
import unittest
import ConfigParser
from android import Android
from android import AdbClient
from network import SSH
from webcontrol import Webcontrol
from network import RS232_Putty
from uiautomator_control import Uiautomator_Control

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")
config_element = ConfigParser.ConfigParser()
config_element.read(".\..\\..\\ini\\web_control_element.conf")
config_setting = ConfigParser.ConfigParser()
config_setting.read(".\..\\..\\ini\\web_control_setting.conf")


class Earfcn(unittest.TestCase):

	# def __init__(self):
	#   '''
	#   Constructor
	#   '''
	#   pass

	def setUp(self):
		print "Start by Automated execution."

	def tearDown(self):
		print "Stop by Automated execution."

	def test_Earfcn(self):
		android = Android()
		android.Check_Mobile_Note4()
		rs232 = RS232_Putty()
		rs232.RS232_Connect_Putty()
		heMS_SetParameterValues = config_element.get(
			"location", "heMS_SetParameterValues")
		print 'Earfcn\'s testcase...'
		for cycle_times in range(int(config_setting.get("cycle_times", "times"))):
			print 'The Cycle times : ' + str(cycle_times+1)
			earfcn = config_setting.get("setting", "earfcn")
			frequency = config.get("cellmapper_setting", "frequency")
			# Click the EarfcnDL and EarfcnFL via RF folder
			for runtime in range(int(config.get("earfcn_setting", "times"))):
				os.system("taskkill /F /IM iexplore.exe")
				print 'The Run Times : ' + str(runtime+1)
				print 'Earfcn of ACS : ' + earfcn + ' Frequence of mobile : ' + frequency
				# Open the airplane mode
				adbClient = AdbClient()
				adbClient.Start_Airplane()
				# Open the acs website homepage
				webcontrol = Webcontrol()
				webcontrol.Initial()
				webcontrol.Login()
				webcontrol.Clear_All_Data(config_element.get("system", "system_message_queue"), config_element.get(
					"delete_file", "delete_all_message_queue_button"), "Delete Message successfully!")
				webcontrol.Parameter_List_Earfcn(earfcn)
				webcontrol.ACS_Initiate_Connection()
				webcontrol.HeNS_Request_Message_Earfcn(
					earfcn, heMS_SetParameterValues)
				webcontrol.Security_Logout()
				time.sleep(1)
				webcontrol.Exit()
				tc = Uiautomator_Control()
				tc.Switch_Home()
				# Reboot the cell
				rs232 = RS232_Putty()
				rs232.RS232_Connect_Putty()
				time.sleep(2)
				ssh = SSH()
				ssh.SSH_Command('./rsys/scripts/reboot-fap')
				time.sleep(150)
				rs232.RS232_Verify_Message_Putty('Time :')
				# Close the airplane mode
				adbClient.Stop_Airplane()
				# Make sure the cell is launched or not by *#0011#
				tc.Switch_Home()
				tc.Switch_Setting_Note4()
				tc.Switch_More_networks()
				tc.Switch_Mobile_networks()
				tc.Switch_Network_Operators()
				tc.Information_Alert()
				tc.Click_Device_Value1('note4')
				tc.Information_Alert()
				time.sleep(10)
				tc.Switch_Home()
				tc.CellMapper()
				tc.ServiceMode(frequency)
				earfcn = "38750"
				frequency = "38750"
		print '\nThe Cycle time is : ' + config_setting.get("cycle_times", "times") + ' times.\nFinished.'

if __name__ == "__main__":
	unittest.main()
	# testcase = Earfcn()
	# testcase.test_Earfcn()