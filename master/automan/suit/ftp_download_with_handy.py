'''
Created on 2017/03/14
@author: ron_chen
Download from QA-Server with handy
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

class Ftp_Download_With_Handy(unittest.TestCase, Android, AdbClient):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def setUp(self):
		print "Start by Automated execution"

	def tearDown(self):
		print "Stop by Automated execution"

	def test_Ftp_Download_With_Handy(self):
		os.system("adb shell am force-stop com.ftpcafe")
		os.system("adb shell am force-stop com.anite.handy")
		android = Android()
		adbClient = AdbClient()
		run_times = config.get("setting","run_times")
		times = config.get("ftp_setting","times")
		filename = config.get("ftp_setting","filename_handy")
		filestart = config.get("ftp_setting", "filename_handy")
		fileend = config.get("ftp_setting", "filename_handy_size")
		print "NB Server & android Client (ftp loop download)"	

		for i in range(1,int(run_times)+1):

			for j in range(1,int(times)+1):
				self.Swiandroidh_FtpClient()
				self.Mobile_Device_Connect()
				# adbClient.Download_Over()
				# android.Ftp_Creat_Account()				
				#*******************Download from 10.1.107.213*****************
				# print 'Donwload Times: ' + str(j)
				# self.Ftplog_Renew()
				# self.Ftp_Autoselect_Server('server')
				# self.Ftp_Connect()
				# self.Verify_Ftp_Connect()
				# self.Folder_Select("Downloads")
				# self.Ftp_Download(filename)

				#****************** Download from speed.hine.net***************
				self.Ftp_Autoselect_Server('hinet')
				self.Ftp_Connect()
				self.Verify_Ftp_Connect()
				print 'Donwload Times: ' + str(j)
				time.sleep(10)
				self.Ftp_Download(filename)
				
				#*******************Handy function ****************************
				self.Swiandroidh_Handy()
				self.Mobile_Device_Connect()
				time.sleep(28)
				print "mobile_device_connect is success."
				time.sleep(1)
				self.Switch_Voice_Quality(j)
				self.Handy_Start_Script()
				time.sleep(1)	
				self.Handy_Run_Script()
				print "Run script."
				time.sleep(112)
				self.Screen_Shot_Save("Volte")
				time.sleep(25)
				self.Handy_Keep_Log()
				time.sleep(5)
				self.Get_Handy_Folder()

		android.Mobile_Device_Disconnect()
		print "mobile_device_disconnect"

if __name__ == "__main__":
	unittest.main()
	# TC = Ftp_Download_With_Handy()
	# TC.test_Ftp_Download_With_Handy()