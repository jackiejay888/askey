'''
Created on 2017/03/02
@author: ron_chen
Handy with Volte
'''
import sys
sys.path.insert(0, '..\\util')
import os
import string
import subprocess
import unittest
import time
import ConfigParser
from android import Android
from android import AdbClient
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from network import RS232_Putty
from uiautomator_control import Uiautomator_Control

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")


class Handy_Volte(unittest.TestCase, Android, AdbClient, RS232_Putty):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution"
		global plmn
		plmn = "123-45"

	def tearDown(self):
		print "Stop by Automated execution"

	def test_Handy_Volte(self):
		self.RS232_Connect_Putty()
		ui = Uiautomator_Control()
		ui.Switch_Home()
		ui.Switch_Setting_Note4()
		ui.Switch_More_networks()
		ui.Switch_Mobile_networks()
		ui.Access_Point_Names()
		ui.Remove_APN_Note4()
		ui.Add_APN('ims')
		ui.Click_Radio_Button()
		ui.Add_APN('internet')
		self.Start_Airplane()
		self.Stop_Airplane()
		self.ADB_Event("4")
		ui.Switch_Mobile_networks()
		ui.Access_Point_Names()
		self.ADB_Event("61")
		self.ADB_Event("61")
		self.ADB_Event("61")
		self.ADB_Event("61")
		self.ADB_Event("66")
		# Waiting for the devices sync to cell
		time.sleep(10)
		ui.Switch_Home()
		ui.CellMapper()
		ui.ServiceMode_Verify_PLMN(plmn)
		ui.Switch_Home()
		ui.Restart_ADB()
		os.system("adb shell am force-stop com.anite.handy")

		for i in range(1, int(config.get("setting", "run_times"))+1):

			for j in range(1, int(config.get("handy_setting", "times"))+1):
				print "The " + str(j) + " times"
				self.Swiandroidh_Handy()
				self.Mobile_Device_Connect()
				time.sleep(28)
				print "mobile_device_connect is success."
				time.sleep(1)
				# By the second test run on handy application.
				j = j + 1
				self.Switch_Voice_Quality(j)
				self.Handy_Start_Script()
				time.sleep(1)
				self.Handy_Run_Script()
				print "Run script."
				time.sleep(293)
				self.Screen_Shot_Save("Volte")
				time.sleep(25)
				self.Handy_Keep_Log()
				time.sleep(5)
				self.Get_Handy_Folder()
				self.Mobile_Device_Disconnect()

if __name__ == "__main__":
	unittest.main()
	# TC = Handy_Volte()
	# TC.test_Handy_Volte()
