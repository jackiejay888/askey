'''
Created on 2017/03/02
@author: ron_chen
Upload from ftp.speed.hinet.net 
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


class Ftp_Upload_Hinet(unittest.TestCase, Android, AdbClient, RS232_Putty):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution"

	def tearDown(self):
		print "Stop by Automated execution"

	def test_Ftp_Upload_Hinet(self):
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
			self.ADB_Event("123")
			self.ADB_Event("123")
			self.Folder_Select("uploads")
			self.Ftp_Localfolder()
			self.ADB_Event("123")
			self.ADB_Event("123")
			self.Folder_Select("Upload")

			for j in range(1, int(config.get("ftp_setting", "times"))+1):
				print 'Upload Times: ' + str(j)
				time.sleep(10)
				self.Ftp_Upload(config.get("ftp_setting", "filename_upload"))
				self.Transfer_Speed_Ststus()
				self.Screen_Shot_Save("FTP_Upload")
				self.ADB_Event("66")
				self.ADB_Event("66")

				if j % 10 == 0:
					os.system(
						"copy ..\\..\\Result\\log\\speed_result.txt ..\\..\\Result\\report\\upload_" + str(j)+" /Y")
					print(
						"copy ..\\..\\Result\\log\\speed_result.txt ..\\..\\Result\\report\\upload_" + str(j)+" /Y")
					self.Count_Transfer_Speed()
					self.Del_File("..\\..\\Result\\log\\speed_result.txt")

			time.sleep(5)
			self.Count_Transfer_Speed()
			self.Del_File("..\\..\\Result\\log\\speed_result.txt")
			self.Mobile_Device_Disconnect()
			os.system(
				"copy ..\\..\\Result\\report\\speed.txt ..\\..\\Result\\report\\upload_speed.txt /Y")

if __name__ == "__main__":
	unittest.main()
	# TC = Ftp_Upload_Hinet()
	# TC.test_Ftp_Upload_Hinet()
