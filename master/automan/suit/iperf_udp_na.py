'''
Created on 2017/03/02
@author: ron_chen
NB Server & android Client (iperf)
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


class Iperf_UDP_Na(unittest.TestCase, Android, AdbClient, RS232_Putty):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution."

	def tearDown(self):
		print "Stop by Automated execution."

	def test_Iperf_UDP_Na(self):
		self.RS232_Connect_Putty()
		os.system("adb shell am force-stop com.magicandroidapps.iperf")

		for i in range(1, int(config.get("setting", "run_times"))+1):

			for j in range(1, int(config.get("iperf_setting", "times"))+1):
				self.Del_File("result.txt")
				iperf_command = "-s -i 5 -u"
				self.Swiandroidh_Iperf()
				self.Mobile_Device_Connect()
				self.Killall_Iperf()
				self.Service_Iperf_Start_N('iperf '+iperf_command)
				self.Iperf_Log_Clean()
				self.Iperf_Client_U("12m")
				os.system("adb shell input keyevent 26")
				os.system("adb shell input keyevent 4")
				time.sleep(15)
				self.Getfile_Command_Iperf()
				self.Screen_Shot_Save("iperf_udp_na")
				self.Mobile_Device_Disconnect()
				self.Strip_Split_Iperf_UDP("na")
				self.Move_File("Down_")
				self.Split_Move_File("Down_split_")

if __name__ == "__main__":
	unittest.main()
	# TC = Iperf_UDP_Na()
	# TC.test_Iperf_UDP_Na()
