'''
Created on 2017/07/11
@Author: ron_chen
@Test case T-SVT-2827: Verify the plmn is matched when set the correct plmn number via oam at the Device.Services.FAPService.1.CellConfig.LTE.EPC.PLMNList
					   (The value is not dynamic change)
@Precondition:
	Device: Note 4.(Can be used call number *#0011#, and search the cell information)
@Test step:
	1. Login to acs server.
	2. Set the plmn via PLMNID under the PLMNList folder of Parameter List.
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


class PLMN(unittest.TestCase):

	# def __init__(self):
	#   '''
	#   Constructor
	#   '''
	#   pass

	def setUp(self):
		print "Start by Automated execution."

	def tearDown(self):
		print "Stop by Automated execution."

	def test_PLMN(self):
		rs232 = RS232_Putty()
		rs232.RS232_Connect_Putty()
		android = Android()
		android.Check_Mobile_Note4()
		heMS_SetParameterValues = config_element.get(
			"location", "heMS_SetParameterValues")
		heNB_SetParameterValuesResponse = config_element.get(
			"location", "heNB_SetParameterValuesResponse")
		print 'PLMN\'s testcase...'
		for cycle_times in range(int(config_setting.get("cycle_times", "times"))):
			print 'The Cycle times : ' + str(cycle_times+1)
			plmn = config_setting.get("setting", "PLMN")
			merge_plmn = plmn.split(" ")[0]+plmn.split(" ")[1]
			cellmapper_plmn = config.get("cellmapper_setting", "PLMN")
			# Click the PLMNID via PLMNList folder
			for runtime in range(int(config.get("plmn_setting", "times"))):
				status = config_setting.get("setting", "status")
				os.system("taskkill /F /IM iexplore.exe")
				print 'The Run Times : ' + str(runtime+1)
				print 'PLMN of ACS : ' + merge_plmn + ' Frequence of mobile : ' + cellmapper_plmn
				# Open the airplane mode
				adbClient = AdbClient()
				adbClient.Start_Airplane()
				# Open the acs website homepage
				webcontrol = Webcontrol()
				webcontrol.Initial()
				webcontrol.Login()
				webcontrol.Clear_All_Data(config_element.get("system", "system_message_queue"), config_element.get(
					"delete_file", "delete_all_message_queue_button"), "Delete Message successfully!")
				# Set the boolean to false
				webcontrol.Parameter_List_PLMN(config_element.get(
					"PLMN", "enable_checkbox"), config_element.get("PLMN", "enable_value"), status)
				webcontrol.ACS_Initiate_Connection()
				webcontrol.HeNS_Request_Message_PLMN(
					status, heMS_SetParameterValues)
				webcontrol.HeNB_Response_Message(
					status, heNB_SetParameterValuesResponse)
				# Set the plmnid
				webcontrol.Parameter_List_PLMN(config_element.get(
					"PLMN", "plmnid_checkbox"), config_element.get("PLMN", "plmnid_value"), merge_plmn)
				webcontrol.ACS_Initiate_Connection()
				webcontrol.HeNS_Request_Message_PLMN(
					merge_plmn, heMS_SetParameterValues)
				webcontrol.HeNB_Response_Message(
					status, heNB_SetParameterValuesResponse)
				# Set the boolean to true
				webcontrol.Parameter_List_PLMN(config_element.get(
					"PLMN", "enable_checkbox"), config_element.get("PLMN", "enable_value"), str(int(status)+1))
				webcontrol.ACS_Initiate_Connection()
				webcontrol.HeNS_Request_Message_PLMN(
					str(int(status)+1), heMS_SetParameterValues)
				webcontrol.HeNB_Response_Message(
					status, heNB_SetParameterValuesResponse)
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
				tc.ServiceMode_Verify_PLMN(cellmapper_plmn)
				merge_plmn = "12301"
				cellmapper_plmn = "123-01"
		print '\nThe Cycle time is : ' + config_setting.get("cycle_times", "times") + ' times.\nFinished.'

if __name__ == "__main__":
	unittest.main()
	# testcase = PLMN()
	# testcase.test_PLMN()
