'''
Created on 2017/03/02
@author: ron_chen
Speed test
'''
import sys
sys.path.insert(0, '..\\util')
import os
import string
import subprocess
import unittest
import ConfigParser
import time
from time import sleep
from android import Android
from android import AdbClient
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from network import RS232_Putty

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")


class Speedtest(unittest.TestCase, Android, AdbClient, RS232_Putty):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution."

	def tearDown(self):
		print "Stop by Automated execution."

	def test_Speedtest(self):
		self.RS232_Connect_Putty()
		os.system("adb shell am force-stop org.zwanoo.android.speedtest")

		for i in range(1, int(config.get("setting", "run_times"))+1):

			for j in range(1, int(config.get("Speedtest_setting", "times"))+1):
				self.Swiandroidh_Speedtest()
				self.Mobile_Device_Connect()
				self.Verify_Speed()
				time.sleep(40)
				self.Speed_Download()
				self.Speed_Upload()
				self.Screen_Shot_Save("Speed")
				self.Mobile_Device_Disconnect()

if __name__ == "__main__":
	unittest.main()
	# TC = Speedtest()
	# TC.test_Speedtest()
