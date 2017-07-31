'''
Created on 2017/03/02
@author: ron_chen
Upload from 10.1.107.213
'''
import sys
sys.path.insert(0, '..\\util')
import os, string, subprocess
import unittest, time, ConfigParser
from android import Android
from android import AdbClient
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")

class Ftp_Upload_Server(unittest.TestCase, Android, AdbClient):

	# def __init__(self):
	# 	'''
	# 	Constructorq
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution"

	def tearDown(self):
		print "Stop by Automated execution"

	def test_Ftp_Upload_Server(self):
		os.system("adb shell am force-stop com.ftpcafe")
		android = Android()
		adbClient = AdbClient()
		run_times = config.get("setting","run_times")
		times = config.get("ftp_setting","times")
		filename = config.get("ftp_setting", "filename_upload")
		filestart = config.get("ftp_setting", "filename_upload")
		fileend = config.get("ftp_setting", "filename_upload_size")
		print "NB Server & android Client (ftp loop upload)"
		adbClient.Swiandroidh_FtpClient()

		for i in range(1,int(run_times)+1):
			self.Mobile_Device_Connect()
			# adbClient.Download_Over()
			# android.Ftp_Creat_Account()

			for j in range(1,int(times)+1):	
				print 'Upload Times: ' + str(i)
				self.Ftplog_Renew()
				self.Ftp_Autoselect_Server('server')
				self.Ftp_Connect()
				self.Verify_Ftp_Connect()
				self.Folder_Select("Uploads")
				self.Ftp_Localfolder()
				self.ADB_Event("123")
				self.ADB_Event("123")
				self.Folder_Select("Uploads")
				self.Ftp_Upload(filename)
				self.Transfer_Status(filestart,fileend)
				self.Getfile_Command()
				self.Check_File_Status()
				self.ADB_Event("4")
				self.Screen_Shot_Save("FTP_Upload")
				self.FTP_Urate()
				self.ADB_Event("66")
				self.ADB_Event("66")
				self.ADB_Event("111")
				self.ADB_Event("111")
				self.ADB_Event("111")
				
		self.mobile_device_disconnect()
		print "mobile_device_disconnect"

if __name__ == "__main__":
	unittest.main()
	# TC = Ftp_Upload_Server()
	# TC.test_Ftp_Upload_Server()