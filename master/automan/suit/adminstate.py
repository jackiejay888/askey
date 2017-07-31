'''
Created on 2017/04/21
@author: ron_chen
@title: Verify the adminstate status with parameter value check
'''
import sys
sys.path.insert(0, '..\\util')
import os
import string
import time
import unittest
import ConfigParser
from system_status import System_Status
from android import Android
from android import AdbClient
from network import RS232_Putty
from webcontrol import Webcontrol
from subprocess import check_output
from uiautomator_control import Uiautomator_Control

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")
config_element = ConfigParser.ConfigParser()
config_element.read(".\..\\..\\ini\\web_control_element.conf")
config_setting = ConfigParser.ConfigParser()
config_setting.read(".\..\\..\\ini\\web_control_setting.conf")


class Adminstate(unittest.TestCase):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution."

	def tearDown(self):
		print "Stop by Automated execution."

	def test_Adminstate(self):
		webcontrol = Webcontrol()
		android = Android()
		android.Check_Mobile_Nexus()
		adbClient = AdbClient()
		cpu = System_Status()
		uiautomator_control = Uiautomator_Control()
		rs232 = RS232_Putty()
		rs232.RS232_Connect_Putty()
		for cycle_times in range(int(config_setting.get("cycle_times", "times"))):
			os.system("taskkill /F /IM iexplore.exe")
			print 'The Cycle times : ' + str(cycle_times+1)
			cpu.cpu_percentage()
			cpu.used_memory()
			cpu.free_memory()
			boolean = config_setting.get("setting", "boolean")
			for runtime in range(int(config.get("adminstate_setting", "times"))):
				print 'The Run Times : ' + str(runtime+1) + ', Set value = ' + boolean
				print 'Adminstate\'s testcase...'
				status = config_setting.get("setting", "status")
				heMS_SetParameterValues = config_element.get(
					"location", "heMS_SetParameterValues")
				heNB_SetParameterValuesResponse = config_element.get(
					"location", "heNB_SetParameterValuesResponse")
				cpu.cpu_percentage()
				cpu.used_memory()
				cpu.free_memory()
				webcontrol.Initial()
				webcontrol.Login()
				webcontrol.Clear_All_Data(config_element.get("system", "system_message_queue"), config_element.get(
					"delete_file", "delete_all_message_queue_button"), "Delete Message successfully!")
				###### Cell wait time ######
				# wait 30s, until to cell was launched, the device auto connected total used 90s #
				# wait 15s, until to cell was not launched, the device auto disconnected total used 20s #
				adbClient.Start_Airplane()
				webcontrol.Parameter_List_Adminstate(boolean)
				webcontrol.ACS_Initiate_Connection()
				webcontrol.HeNS_Request_Message(
					boolean, heMS_SetParameterValues)
				webcontrol.HeNB_Response_Message(
					status, heNB_SetParameterValuesResponse)
				adbClient.Stop_Airplane()
				###############################################################
				webcontrol.Security_Logout()
				time.sleep(1)
				webcontrol.Exit()
				cpu.cpu_percentage()
				cpu.used_memory()
				cpu.free_memory()
				time.sleep(1)
				print 'SpeetTest\'s testcase...'
				os.system("adb shell am force-stop org.zwanoo.android.speedtest")
				uiautomator_control.Restart_ADB()
				android.Check_Mobile_Nexus()
				uiautomator_control.Switch_Home()
				uiautomator_control.Switch_Setting()
				uiautomator_control.Switch_More()
				uiautomator_control.Switch_Cellular_Networks()
				uiautomator_control.Switch_Network_Operators()
				if boolean == "0":
					uiautomator_control.Click_Device_Value0()
				if boolean == "1":
					uiautomator_control.Click_Device_Value1("nexus")
				uiautomator_control.Switch_Home()
				uiautomator_control.Restart_ADB()
				print 'The setting was finished'
				if boolean == "1":
					uiautomator_control.SpeedTest_True("Nexus5x_Speed")
				cpu.cpu_percentage()
				cpu.used_memory()
				cpu.free_memory()
				boolean = "1"
		rs232.RS232_Disconnect_Putty()
		print '\nThe Cycle time is : ' + config_setting.get("cycle_times", "times") + ' times.\nFinished.'

if __name__ == "__main__":
	unittest.main()
	# testcase = Adminstate()
	# testcase.test_Adminstate()
