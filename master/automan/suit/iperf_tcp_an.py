'''
Created on 2017/03/02
@author: ron_chen
NB Client & android Server (iperf)
'''
import sys
sys.path.insert(0, '..\\util')
import os, string, subprocess
import unittest, ConfigParser, time
from time import sleep
from android import Android
from android import AdbClient
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from network import RS232_Putty

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")

class Iperf_TCP_An(unittest.TestCase, Android, AdbClient):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution."

	def tearDown(self):
		print "Stop by Automated execution."

	def test_Iperf_TCP_An(self):
		rs232_putty = RS232_Putty()
		rs232_putty.RS232_Connect_Putty()
		os.system("adb shell am force-stop com.magicandroidapps.iperf")
		android = Android()
		adbClient = AdbClient()

		for i in range(1,int(config.get("setting","run_times"))+1):
			
			for j in range(1,int(config.get("iperf_setting", "times"))+1):		
				adbClient.Del_File("result.txt")
				iperf_command = "-s -i 5"
				time.sleep(2)
				# adbClient.Swiandroidh_Iperf()
				android.Mobile_Device_Connect()	
				android.Service_Iperf_Start(iperf_command)
				android.Iperf_Log_Clean()
				adbClient.Get_Android_IP()
				adbClient.Client_Iperf_Start()
				android.Screen_Shot_Save("iperf_tcp_an")
				android.Mobile_Device_Disconnect()
				adbClient.Strip_Split_Iperf()
				adbClient.Move_File("Up_")
				adbClient.Split_Move_File("Up_split_")

if __name__ == "__main__":
	unittest.main()
	# TC = Iperf_TCP_An()
	# TC.test_Iperf_TCP_An()