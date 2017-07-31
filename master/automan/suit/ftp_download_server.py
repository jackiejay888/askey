'''
Created on 2017/03/02
@author: ron_chen
Download from QA-Server
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

class ftp_Download_Server(unittest.TestCase, Android, AdbClient):

	# def __init__(self):
	# 	'''
	# 	Constructorq
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution"

	def tearDown(self):
		print "Stop by Automated execution"

	def test_Ftp_Download_Server(self):
		os.system("adb shell am force-stop com.ftpcafe")
		android = Android()
		adbClient = AdbClient()
		run_times = config.get("setting","run_times")
		times = config.get("ftp_setting","times")
		filename = config.get("ftp_setting","filename_download")
		filestart = config.get("ftp_setting", "filename_download")
		fileend = config.get("ftp_setting", "filename_download_size")
		print "NB Server & android Client (ftp loop download)"			
		self.Swiandroidh_FtpClient()

		for i in range(1,int(run_times)+1):
			android.Mobile_Device_Connect()
			# self.Download_Over()
			# self.Ftp_Creat_Account()

			for j in range(1,int(times)+1):
				print 'Donwload Times: ' + str(j)
				self.Ftplog_Renew()
				self.Ftp_Autoselect_Server('server')
				self.Ftp_Connect()
				self.Verify_Ftp_Connect()
				self.Folder_Select("Downloads")
				self.Ftp_Download(filename)
				print "The filename is " + filename
				self.Del_File("..\..\\Result\\log\\vsftpd.log")
				self.Transfer_Status(filestart,fileend)
				self.Getfile_Command()
				self.Check_File_Status()
				self.ADB_Event("4")
				self.Screen_Shot_Save("FTP_Download")
				self.FTP_Drate()
				self.ADB_Event("66")
				self.ADB_Event("66")
				self.ADB_Event("111")
				self.ADB_Event("111")
				self.ADB_Event("111")
				
		self.Mobile_Device_Disconnect()
		print "mobile_device_disconnect"

if __name__ == "__main__":
	unittest.main()
	# TC = ftp_Download_Server()
	# TC.test_Ftp_Download_Server()