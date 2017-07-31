'''
Created on 2017/03/02
@author: ron_chen
NB Client & android Server (iperf)
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


class Iperf_UDP_An(unittest.TestCase, Android, AdbClient, RS232_Putty):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution."

	def tearDown(self):
		print "Stop by Automated execution."

	def test_Iperf_UDP_An(self):
		self.RS232_Connect_Putty()
		os.system("adb shell am force-stop com.magicandroidapps.iperf")

		for i in range(1, int(config.get("setting", "run_times"))+1):

			for j in range(1, int(config.get("iperf_setting", "times"))+1):
				self.Del_File("result.txt")
				iperf_command = "-s -i 5 -u"
				self.Swiandroidh_Iperf()
				self.Mobile_Device_Connect()
				self.Service_Iperf_Start(iperf_command)
				self.Iperf_Log_Clean()
				self.Get_Android_IP()
				self.Client_IperfU_Start("120m")
				os.system("adb shell input keyevent 26")
				os.system("adb shell input keyevent 4")
				time.sleep(15)
				self.Screen_Shot_Save("iperf_udp_an")
				self.Mobile_Device_Disconnect()
				self.Strip_Split_Iperf_UDP("an")
				self.Move_File("Up_")
				self.Split_Move_File("Up_split_")

if __name__ == "__main__":
	unittest.main()
	# TC = Iperf_UDP_An()
	# TC.test_Iperf_UDP_An()
