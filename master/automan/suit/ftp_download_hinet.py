'''
Created on 2017/03/02
@author: ron_chen
Download from ftp.speed.hinet.net 
'''
import sys
sys.path.insert(0, '..\\util')
import os
import string
import subprocess
import unittest
import time
import ConfigParser
from network import RS232_Putty
from android import Android
from android import AdbClient
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")


class Ftp_Download_Hinet(unittest.TestCase, Android, AdbClient, RS232_Putty):

	# def __init__(self):
	# 	'''
	# 	Constructorq
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution"

	def tearDown(self):
		print "Stop by Automated execution"

	def test_Ftp_Download_Hinet(self):
		self.RS232_Connect_Putty()
		os.system("adb shell am force-stop com.ftpcafe")
		self.Del_File("..\\..\\Result\\log\\speed_result.txt")
		self.Swiandroidh_FtpClient()

		for i in range(1, int(config.get("setting", "run_times"))+1):
			self.Mobile_Device_Connect()
			# self.Download_Over()
			# self.Ftp_Creat_Account()
			self.Ftp_Autoselect_Server('hinet')
			self.Ftp_Connect()
			self.Verify_Ftp_Connect()

			for j in range(1, int(config.get("ftp_setting", "times"))+1):
				print 'Donwload Times: ' + str(j)
				time.sleep(10)
				os.system("adb shell input keyevent 123")
				time.sleep(1)
				os.system("adb shell input keyevent 123")
				self.Ftp_Download(config.get(
					"ftp_setting", "filename_download"))
				self.Transfer_Speed_Ststus()
				self.Screen_Shot_Save("FTP_Download")
				self.ADB_Event("66")
				self.ADB_Event("66")

				if j % 10 == 0:
					os.system(
						"copy ..\\..\\Result\\log\\speed_result.txt ..\\..\\Result\\report\\Download_" + str(j)+" /Y")
					print(
						"copy ..\\..\\Result\\log\\speed_result.txt ..\\..\\Result\\report\\Download_" + str(j)+" /Y")
					self.Count_Transfer_Speed()
					self.Del_File("..\\..\\Result\\log\\speed_result.txt")

			time.sleep(5)
			self.Count_Transfer_Speed()
			self.Del_File("..\\..\\Result\\log\\speed_result.txt")
			self.Mobile_Device_Disconnect()
			os.system(
				"copy ..\\..\\Result\\report\\speed.txt ..\\..\\Result\\report\\download_speed.txt /Y")

if __name__ == "__main__":
	unittest.main()
	# TC = Ftp_Download_Hinet()
	# TC.test_Ftp_Download_Hinet()
