'''
Created on 2017/02/08
@author: wayne_teng
'''

import os
import string
import subprocess
import unittest
import time
import ConfigParser
# import HTMLTestRunner
from time import sleep
from network import SCP
from subprocess import check_output
from delete_subfolder import Delete_Subfolder
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")


class Android(object):

	# def __init__(self):
	# 	'''
	# 	Constructor
	# 	'''
	# 	pass

	def Finddevices(self):
		global devices_id
		try:
			adb_ouput = check_output(["adb", "devices"])
			devices_id = adb_ouput.split()[-2]
			print "Find a new device - PASS"
		except CalledProcessError as e:
			raise e.returncode, ('not found mobile, please check - FAIL')

	def Mobile_Device_Connect(self):  # android Setting
		try:
			self.Finddevices()
			desired_caps = {}
			desired_caps['platformName'] = 'Android'
			desired_caps['platformVersion'] = '4.4.1'
			desired_caps['deviceName'] = devices_id
			# desired_caps['newCommandTimeout'] = 120
			desired_caps['newCommandTimeout'] = 700
			global driver
			driver = webdriver.Remote(
				'http://127.0.0.1:4723/wd/hub', desired_caps)
			print "Mobile connection successful - PASS"
		except:
			raise Exception("Not connection with Mobile - FAIL")

	def Mobile_Device_Disconnect(self):
		driver.quit()

	def Check_Mobile_Nexus(self):
		SN = check_output(["adb", "devices"]).split()[-2]
		list = ['2e85c29e', '6fecda25', '1916d86a', '7061ce07']
		if SN not in list:
			print "The Mobile is Nexus - PASS"
		else:
			raise Exception, "Please change other mobile (Nexus) - FAIL"

	def Check_Mobile_Note4(self):
		SN = check_output(["adb", "devices"]).split()[-2]
		list = ['2e85c29e', '6fecda25', '1916d86a', '7061ce07']
		if SN in list:
			print "The Mobile is Note4 - PASS"
		else:
			raise Exception, "Please change other mobile (Note4) - FAIL"

#========================== iperf ======================================
	def Service_Iperf_Start(self, command):
		try:
			el = driver.find_element_by_id(
				config.get("iperf", "iperf_server_start"))
			el.click()
			el.clear()
			el.send_keys(command)
			el = driver.find_element_by_id(
				config.get("iperf", "iperf_status_button"))
			el.click()
			print "Press start button - PASS"
		except:
			raise Exception("Not press iperf start button - FAIL")

	def Iperf_Log_Clean(self):
		el = driver.find_element_by_class_name(
			config.get("iperf", "iperf_menu"))
		el.click()
		el = driver.find_element_by_android_uiautomator(
			config.get("iperf", "iperf_menu_clear"))
		el.click()

#=============================== ftp ========================================
	def Ftp_Autoselect_Server(self, element):
		profile_session = driver.find_element_by_id(
			config.get("ftp", "profile_session"))
		profile_session.click()
		time.sleep(1)
		if element == 'hinet':
			try:
				element_profile_hinet = driver.find_element_by_xpath(
					"//android.widget.CheckedTextView[contains(@text,'hinet')]")
				element_profile_hinet.click()
				print 'The hinet button is displayed'
			except:
				raise Exception("The hinet button is not displayed")
		if element == 'server':
			try:
				element_profile_server = driver.find_element_by_xpath(
					"//android.widget.CheckedTextView[contains(@text,'server')]")
				element_profile_server.click()
				print 'The server button is displayed'
			except:
				raise Exception("The server button is not displayed")

	def Ftp_Creat_Account(self):
		try:
			el = driver.find_element_by_id(config.get("ftp", "new_session"))
			el.click()
			el = driver.find_element_by_id(config.get("ftp", "session_name"))
			el.click()
			el.send_keys(config.get("ftp_setting", "session_name"))
			el = driver.find_element_by_id(config.get("ftp", "host"))
			el.click()
			el.send_keys(config.get("ftp_setting", "host"))
			el = driver.find_element_by_id(config.get("ftp", "user"))
			el.click()
			el.send_keys(config.get("ftp_setting", "user"))
			os.system("adb shell input keyevent 20")
			el = driver.find_element_by_id(config.get("ftp", "password"))
			el.click()
			el.send_keys(config.get("ftp_setting", "password"))
			el = driver.find_element_by_id(config.get("ftp", "save"))
			el.click()
			print "FTP account create successful - Pass"
		except:
			raise Exception("Not create a new account- FAIL")

	def Ftp_Connect(self):
		for i in range(0, 3):
			try:
				el = driver.find_element_by_id(config.get("ftp", "connect"))
				el.click()
				break
			except:
				time.sleep(3)
				if i == 2:
					raise Exception("Cannot connect ftp server")

	def Verify_Ftp_Connect(self):
		for i in range(0, 4):
			try:
				el = driver.find_element_by_xpath(
					"//android.widget.TextView[contains(@text,'Remote')]")
				print "Connect FTP Server Successful - PASS"
				break
			except:
				time.sleep(5)
				if i == 3:
					raise Exception("Not Connect FTP Server - FAIL")

	def Ftp_Download(self, filename):
		time.sleep(2)
		action1 = TouchAction(driver)
		el = driver.find_element_by_xpath(
			"//android.widget.TextView[contains(@text,'"+filename+"')]")
		action1.long_press(el).wait(10000).perform()
		for i in range(0, 3):
			try:
				el = driver.find_element_by_android_uiautomator(
					'new UiSelector().text("Download")')
				el.click()
				print "Start ftp download Successful - PASS"
				break
			except:
				time.sleep(3)
				if i == 2:
					raise Exception("Not Start ftp download - FAIL")

	def Ftp_Upload(self, filename):
		time.sleep(2)
		action1 = TouchAction(driver)
		el = driver.find_element_by_xpath(
			"//android.widget.TextView[contains(@text,'"+filename+"')]")
		action1.long_press(el).wait(10000).perform()
		for i in range(0, 3):
			try:
				el = driver.find_element_by_android_uiautomator(
					'new UiSelector().text("Upload")')
				el.click()
				print "Start ftp Upload Successful - PASS"
				break
			except:
				time.sleep(3)
				if i == 2:
					raise Exception("Not Start ftp Upload - FAIL")

	def Ftp_Localfolder(self):
		for i in range(0, 3):
			try:
				el = driver.find_element_by_xpath(
					"//android.widget.TextView[contains(@text,'Local')]")
				el.click()
				print "Switch to Local folder - PASS"
				break
			except:
				time.sleep(2)
				if i == 2:
					raise Exception("Not switch to Local folder - FAIL")

	def Ftp_Remotefolder(self):
		for i in range(0, 3):
			try:
				el = driver.find_element_by_xpath(
					"//android.widget.TextView[contains(@text,'Remote')]")
				el.click()
				print "Switch to Remote folder - PASS"
				break
			except:
				time.sleep(2)
				if i == 2:
					raise Exception("Cannot find the Remote folder - FAIL")

	def Folder_Select(self, filename):
		for i in range(0, 3):
			try:
				el = driver.find_element_by_xpath(
					"//android.widget.TextView[contains(@text,'"+filename+"')]")
				time.sleep(2)
				el.click()
				print "Swiandroidh localfolder Successful - PASS"
				break
			except:
				print "Not Swiandroidh localfolder"
				time.sleep(2)
				if i == 2:
					raise Exception("Cannot find the filename folder - FAIL")

	def Verify_Speed(self):
		for i in range(0, 10):
			try:
				time.sleep(2)
				el = driver.find_element_by_xpath(
					"//android.widget.TextView[contains(@text,'Begin Test')]")
				el.click()
				print "Start Internet Speedtest - PASS"
				break
			except:
				print "Not found start button"
				time.sleep(5)
				if i == 9:
					raise Exception("Cannot find the Begin Test button - FAIL")

	def Verify_SpeedTest_Value1(self):
		for i in range(0, 10):
			try:
				time.sleep(10)
				el = driver.find_element_by_xpath(
					"//android.widget.TextView[contains(@text,'Begin Test')]")
				el.click()
				print "The Cell was launshed. - PASS"
				break
			except:
				print "Not found start button"
				adbCliend = AdbClient()
				adbCliend.Start_Airplane()
				adbCliend.Stop_Airplane()
				driver.find_element_by_xpath(
					"//android.widget.TextView[contains(@text,'RESULTS')]").click()
				time.sleep(5)
				driver.find_element_by_xpath(
					"//android.widget.TextView[contains(@text,'SPEEDTEST')]").click()
				time.sleep(10)
				if i == 9:
					self.Copy_Trace_Folder()
					raise Exception("The Cell was not launched. - FAIL")

	def Copy_Trace_Folder(self):
		delete_subfolder = Delete_Subfolder()
		delete_subfolder.Delete_Path_Subfolder("..\\..\\Result\\femtolog")
		time.sleep(5)
		scp = SCP()
		scp.SCP_Download_Folder('150', '/tmp/trace/', 'femtolog')
		scp.SCP_Download_Folder('150', '/var/log/', 'femtolog')
		scp.SCP_Download_Folder('150', '/mnt/flash/coredumps/', 'femtolog')
		print 'The trace folder was copied.'

	def Speed_Download(self):
		try:
			el = driver.find_element_by_id(
				'org.zwanoo.android.speedtest:id/downloadSpeed')
			Speed_download = el.text
			print Speed_download, "Speed_download"
			# print type(Speed_download)
			os.system("echo Speed_download Transfer speed is : " +
					  str(Speed_download)+" Mbps/sec >> ..\\..\\Result\\log\\speed_result.txt")
			print "Catch the downloadspeed content - PASS"
		except:
			raise Exception("No found downloadspeed content - FAIL")

	def Speed_Upload(self):
		try:
			el = driver.find_element_by_id(
				'org.zwanoo.android.speedtest:id/uploadSpeed')
			Speed_upload = el.text
			print Speed_upload, "Speed_upload"
			# print type(Speed_upload)
			os.system("echo Speed_upload Transfer speed is : "+str(Speed_upload) +
					  " Mbps/sec >> ..\\..\\Result\\log\\speed_result.txt")
			print "Catch the uploadspeed - PASS"
		except:
			raise Exception("No found uploadspeed content - FAIL")

	def Transfer_Percentage(self):
		try:
			global percentage
			el = driver.find_element_by_id('com.ftpcafe:id/percentage')
			percentage = el.text
			print percentage, "percentage"
			# os.system("echo Speed_uplad Transfer speed is : "+str(Speed_upload)+" Mbps/sec >> speed_result.txt")
			print "Catch the percentage - PASS"
		except:
			raise Exception("No found percentage - FAIL")

	def Transfer_Speed(self):
		try:
			el = driver.find_element_by_id('com.ftpcafe:id/speed')
			Speed_download = el.text
			a = Speed_download.split(' ')[0]
			print float(a)/128, "Speed_Transfer"
			# print float(Speed_download)*8,"Speed_download"
			# os.system("echo Speed_download Transfer speed is : "+str(Speed_download)+" Mbps/sec >> speed_result.txt")
			os.system(
				"echo "+str(float(a)/128)+">> ..\\..\\Result\\log\\speed_result.txt")
			print "Catch the speed content - PASS"
		except:
			raise Exception("No found speed content - FAIL")

	def Transfer_Speed_Ststus(self):
		try:
			global percentage
			while True:
				self.Transfer_Percentage()
				if percentage == '100%':
					self.Transfer_Speed()
					print "String found - PASS"
					break
				else:
					time.sleep(5)
					self.Transfer_Percentage()
					print "String not found"
		except:
			raise Exception("String not found - FAIL")

	def Count_Transfer_Speed(self):
		try:
			with open('..\\..\\Result\\log\\speed_result.txt') as f:
				lines = f.read().splitlines()
				sumall = sum(float(item) for item in lines)
				average = sumall/int(config.get("ftp_setting", "times"))
				print "FTP Transfer Average/time is : "+str(average)
				os.system("echo FTP Speed Transfer speed is : " +
						  str(average)+" Mbps/sec >> ..\\..\\Result\\report\\speed.txt")
			print "FTP Transfer Average/time - PASS"
		except:
			raise Exception("FTP Transfer Average/time - FAIL")

#=============================== Conttol =================================
	def Screen_Shot_Save(self, error):
		Path = ("../../Result/pic/")
		now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
		driver.save_screenshot(Path+error+'_'+now+".jpg")
		print "save "+Path+error+'_'+now+".jpg"
#===============================Handy Conttol ============================

	def Handy_Switch_Volte(self):
		try:
			el = driver.find_element_by_id(
				'com.anite.handy:id/home_screen_script')
			el.click()
			print "Catch the home screen script - PASS"
		except:
			raise Exception("No found the home screen script - FAIL")

	def Handy_Start_Script(self):
		try:
			el = driver.find_element_by_id(
				'com.anite.handy:id/home_screen_script')
			time.sleep(3)
			el.click()
			print "Catch the home screen script - PASS"
		except:
			raise Exception("No found the home screen script - FAIL")

	def Handy_Run_Script(self):
		try:
			el = driver.find_element_by_xpath(
				"//android.widget.TextView[contains(@text,'Volte.hsfx')]")
			time.sleep(3)
			el.click()
			el = driver.find_element_by_xpath(
				"//android.widget.TextView[contains(@text,'Load & Run')]")
			time.sleep(3)
			el.click()
			print "Catch the volte.hsfx and Load & Run button - PASS"
		except:
			raise Exception(
				"No found the volte.hsfx and Load & Run button - FAIL")

	def Iperf_Client(self):
		print "su -c "+config.get("setting", "iperf_folder")+" -c "+config.get("setting", "iperf_SIP")+" -t "+config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " > " + config.get("setting", "output_file")


class AdbClient:

	def ADB_Shell(self, shell_cmds):
		try:
			# shell_cmds += '; echo $?'
			shell_cmds = shell_cmds+'; echo $?'
			cmds = ['adb', 'shell', shell_cmds]
			stdout = subprocess.Popen(
				cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()

			lines = stdout.splitlines()
			print lines
			# print repr(stdout), lines
			reandroidode = int(lines[-1])
			if reandroidode != 0:
				errmsg = 'FAILed to execute ADB shell commands (%i)' % reandroidode
				if len(lines) > 1:
					errmsg += '\n' + '\n'.join(lines[:-1])
				raise Exception(RuntimeError(errmsg))
			return stdout
			print "The adb shell was finished - PASS"
		except:
			raise Exception("The adb shell was not finished - FAIL")

		# change the config

	def Get_Android_IP(self):
		os.system("adb shell ifconfig rmnet_data0 > .\\..\\..\\temp\\android_ip.txt")
		fileString = open(".\\..\\..\\temp\\android_ip.txt", "r").read()
		str_start = fileString.find("rmnet_data0: ip ")
		str_end = fileString.find("mask")
		global android_ip
		android_ip = fileString[str_start + 16:str_end - 1]
		print "Android IP =", android_ip

	def Iperf_Client(self):
		# try:
		# 	# move to android appium
		# 	time.sleep(1)
		# 	print "su -c "+config.get("setting", "iperf_folder")+" -c "+config.get("setting", "iperf_SIP")+" -t "+config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " > " + config.get("setting", "output_file")
		# 	self.ADB_Shell("su -c "+config.get("setting", "iperf_folder")+" -c "+config.get("setting", "iperf_SIP")+" -t "+config.get(
		# 		"setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " > " + config.get("setting", "output_file"))
		# 	# self.ADB_Shell("su -c "+config.get("setting", "iperf_folder")+" -c "+config.get("setting", "iperf_SIP")+" -t "+config.get("setting", "iperf_time")+ " -i "+ monitor_time + " > " + output_file)
		# 	time.sleep(int(config.get("setting", "iperf_time"))+10)
		# 	os.system("taskkill /F /IM iperf.exe")
		# 	print "Teh iperf client was finished - PASS"
		# except:
		# 	raise Exception("The iperf client was not finished - FAIL")

		try:
			element_content = driver.find_element_by_id(
				"com.magicandroidapps.iperf:id/cmdlineargs")
			element_content.click()
			element_content.clear()
			time.sleep(1)
			element_content.send_keys("-c " + config.get("setting", "iperf_SIP") + " -t " + config.get(
				"setting", "iperf_time") + " -i " + config.get("setting", "monitor_time"))
			print "-c " + config.get("setting", "iperf_SIP") + " -t " + config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " - PASS"
			element_start_button = driver.find_element_by_id(
				"com.magicandroidapps.iperf:id/startstopButton")
			element_start_button.click()
			time.sleep(int(config.get("setting", "iperf_time"))+10)
			print "The start button will be press - PASS"
			print "Teh iperf client was finished - PASS"

		except:
			raise Exception("The iperf client was not finished - FAIL")

		# change the config

	def Iperf_Client_U(self, UP_UDP):
		# try:
		# 	time.sleep(1)
		# 	print "su -c "+config.get("setting", "iperf_folder")+" -c "+config.get("setting", "iperf_SIP")+" -t "+config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " -b " + UP_UDP + " -l 1350 " + " > " + config.get("setting", "output_file")
		# 	self.ADB_Shell("su -c "+config.get("setting", "iperf_folder")+" -c "+config.get("setting", "iperf_SIP")+" -t "+config.get("setting",
		# 																															  "iperf_time") + " -i " + config.get("setting", "monitor_time") + " -b " + UP_UDP + " -l 1350 " + " > " + config.get("setting", "output_file"))

		# 	# self.ADB_Shell("su -c "+config.get("setting", "iperf_folder")+" -c "+config.get("setting", "iperf_SIP")+" -t "+config.get("setting", "iperf_time")+ " -i "+ config.get("setting", "monitor_time") + " > " + config.get("setting", "output_file"))
		# 	time.sleep(int(config.get("setting", "iperf_time"))+10)
		# 	os.system("taskkill /F /IM iperf.exe")
		# 	print "The iperf client U was finished - PASS"
		# except:
		# 	raise Exception("The iperf client U was not finished - FAIL")

		try:
			element_content = driver.find_element_by_id(
				"com.magicandroidapps.iperf:id/cmdlineargs")
			element_content.click()
			element_content.clear()
			time.sleep(1)
			element_content.send_keys("-c " + config.get("setting", "iperf_SIP") + " -u -t " + config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " -b " + UP_UDP)
			print "-c " + config.get("setting", "iperf_SIP") + " -u -t " + config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " -b " + UP_UDP + " - PASS"
			element_start_button = driver.find_element_by_id(
				"com.magicandroidapps.iperf:id/startstopButton")
			element_start_button.click()
			time.sleep(int(config.get("setting", "iperf_time"))+10)
			print "The start button will be press - PASS"
			print "Teh iperf client was finished - PASS"

		except:
			raise Exception("The iperf client was not finished - FAIL")

	def ADB_Event(self, number):
		self.ADB_Shell("input keyevent " + number)

	def Download_Over(self):
		try:
			time.sleep(5)
			self.ADB_Event("82")
			self.ADB_Event("20")
			self.ADB_Event("20")
			el = driver.find_element_by_android_uiautomator(
				'new UiSelector().text("Preferences")')
			el.click()
			# self.ADB_Event("23")
			self.ADB_Event("66")
			self.ADB_Event("66")
			self.ADB_Event("92")
			self.ADB_Event("66")
			self.ADB_Event("20")
			self.ADB_Event("66")
			self.ADB_Event("92")
			self.ADB_Event("92")
			self.ADB_Event("66")
			self.ADB_Event("4")
			print "The download over was finished"
		except:
			raise Exception("The download over was not finished")

#=========================================================================
	# change local_file config

	def Del_File(self, local_file):
		os.system("del " + local_file)
		print "delelte " + local_file + " - PASS"

	def Move_File(self, direction):
		try:
			# Path = ("c:/remote/report/")
			Path = ("../../Result/report/")
			now = time.strftime(
				"%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
			print("move " + config.get("setting", "local_file") +
				  " " + Path + direction + now + ".txt")
			os.system("move " + config.get("setting", "local_file") +
					  " " + Path + direction + now + ".txt")
		except:
			raise Exception("No move the file - FAIL")

	def Split_Move_File(self, direction):
		try:
			# Path = ("c:/remote/report/")
			Path = ("../../Result/report/")
			now = time.strftime(
				"%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
			print("move " + config.get("setting", "split_local_file") +
				  " " + Path + direction + now + ".txt")
			os.system("move " + config.get("setting", "split_local_file") +
					  " " + Path + direction + now + ".txt")
		except:
			raise Exception("No move the file - FAIL")

	def Get_File(self):
		try:
			# change config output_file
			os.system("adb pull "+config.get("setting", "output_file")+" . ")
			print "adb pull "+config.get("setting", "output_file")+" . "+" - PASS"
		except:
			raise Exception("No adb pull the output file - FAIL")

	def Get_Handy_Folder(self):
		try:
			os.system(
				"adb pull /sdcard/Nemo/Handy/Results ..\\..\\Result\\log ")
			print "adb pull /sdcard/Nemo/Handy/Results ..\\..\\Result\\log "+" - PASS"
		except:
			raise Exception(
				"No adb pull /sdcard/Nemo/Handy/Results ..\\..\\Result\\log - FAIL")

	def Put_File(self):
		try:
			# change config output_file
			os.system("adb push "+config.get("setting", "local_file") +
					  " "+config.get("setting", "output_file"))
			print "adb push "+config.get("setting", "local_file") + " "+config.get("setting", "output_file") + " - PASS"
		except:
			raise Exception("No adb push the output file - FAIL")

	def Service_Iperf_Start_N(self, exec_com):
		# os.system("taskkill /F /IM iperf.exe")
		# subprocess.Popen('..\\..\\tools\\iperf2\iperf.exe -s -i 5')
		try:
			time.sleep(5)
			PlinkCommand = "..\\..\\tools\\plink.exe" + " -ssh " + config.get("setting", "server_host") + " -l " + config.get(
				"setting", "server_user") + " -pw " + config.get("setting", "server_password") + " " + exec_com + " > " + config.get("iperf_setting", "iperflocal_file")
			time.sleep(1)
			subprocess.Popen(PlinkCommand)
			print "Plink command is = " + PlinkCommand + " - PASS"
			time.sleep(1)
		except:
			raise Exception("The service was not start by iperf - FAIL")

	def Killall_Iperf(self):
		try:
			KillAll_iperf = "..\\..\\tools\\plink.exe" + " -ssh " + config.get("setting", "server_host") + " -l " + config.get(
				"setting", "server_user") + " -pw " + config.get("setting", "server_password") + " " + "killall -9 iperf"
			os.system(KillAll_iperf)
			print "The killall is = " + KillAll_iperf + " - PASS"
		except:
			raise Exception("The iperf was not killed - FAIL")
		# change the config

	def Client_Iperf_Start(self):
		# try:
		# 	os.system("taskkill /F /IM iperf.exe")
		# 	os.system("..\\..\\tools\\iperf2\iperf.exe -c "+config.get("setting", "iperf_AIP")+" -t "+config.get("setting",
		# 																										 "iperf_time") + " -i " + config.get("setting", "monitor_time") + " > " + config.get("setting", "local_file"))
		# 	print "..\\..\\tools\\iperf2\iperf.exe -c "+config.get("setting", "iperf_AIP")+" -t "+config.get("setting",
		# 																									 "iperf_time") + " -i " + config.get("setting", "monitor_time") + " > " + config.get("setting", "local_file") + " - PASS"
		# except:
		# 	raise Exception("No execute the iperf start - FAIL")

		try:
			os.system("taskkill /F /IM iperf.exe")
			os.system("..\\..\\tools\\iperf2\iperf.exe -c "+android_ip+" -t "+config.get("setting",
																						 "iperf_time") + " -i " + config.get("setting", "monitor_time") + " > " + config.get("setting", "local_file"))
			print "..\\..\\tools\\iperf2\iperf.exe -c "+android_ip+" -t "+config.get("setting",
																					 "iperf_time") + " -i " + config.get("setting", "monitor_time") + " > " + config.get("setting", "local_file") + " - PASS"
		except:
			raise Exception("No execute the iperf start - FAIL")

	def Service_IperfU_Start(self):
		try:
			os.system("taskkill /F /IM iperf.exe")
			subprocess.Popen('..\\..\\tools\\iperf2\iperf.exe -s -i 5 -u')
			print "..\\..\\tools\\iperf2\iperf.exe -s -i 5 -u" + " - PASS"
		except:
			raise Exception("No execute the service iperfU start - FAIL")

		# change the config

	def Client_IperfU_Start(self, DL_UDP):
		# try:
		# 	os.system("taskkill /F /IM iperf.exe")
		# 	os.system("..\\..\\tools\\iperf2\iperf.exe -c "+config.get("setting", "iperf_AIP")+" -u -t "+config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " -b " + DL_UDP + " -l 1350 " + " > " + config.get("setting", "local_file"))
		# 	print "..\\..\\tools\\iperf2\iperf.exe -c "+config.get("setting", "iperf_AIP")+" -u -t "+config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " -b " + DL_UDP + \
		# 		" -l 1350 " + " > " + \
		# 		config.get("setting", "local_file") + " - PASS"
		# except:
		# 	raise Exception("No execute the client iperfU start - FAIL")

		try:
			os.system("taskkill /F /IM iperf.exe")
			os.system("..\\..\\tools\\iperf2\iperf.exe -c "+android_ip+" -u -t "+config.get("setting", "iperf_time") + " -i " +
					  config.get("setting", "monitor_time") + " -b " + DL_UDP + " -l 1350 " + " > " + config.get("setting", "local_file"))
			print "..\\..\\tools\\iperf2\iperf.exe -c "+android_ip+" -u -t "+config.get("setting", "iperf_time") + " -i " + config.get("setting", "monitor_time") + " -b " + DL_UDP + \
				" -l 1350 " + " > " + \
				config.get("setting", "local_file") + " - PASS"
		except:
			raise Exception("No execute the client iperfU start - FAIL")

	def Check_iStatus(self, fileName):
		# if os.path.exists(fileName):
		# 	print fileName, "Exist iperf export file"
		# 	pass
		# else:
		# 	errmsg = 'not exist iperf export file'
		# 	time.sleep(5)
		# 	raise RuntimeError (errmsg)
		for i in range(0, 3):
			try:
				if os.path.exists(fileName):
					print fileName, "Exist iperf export file - PASS"
					break
			except:
				print "not exist iperf export file"
				time.sleep(2)
				if i == 3:
					raise Exception("Not exist iperf export file - FAIL")

	def Swiandroidh_ACS(self):
		try:
			time.sleep(2)
			os.system(
				"cmd.exe /c C:\Sikuli-IDE\Sikuli-IDE.bat -r ..\\..\\sikuli\\switch_ACS.skl")
			# os.system("taskkill /f /im cmd.exe")
			print "The switch_ACS.skl was done - PASS"
		except:
			raise Exception("No execute the action - FAIL")

	def Swiandroidh_Iperf(self):
		try:
			time.sleep(2)
			os.system(
				"cmd.exe /c C:\Sikuli-IDE\Sikuli-IDE.bat -r ..\\..\\sikuli\\switch_iperf.skl")
			# os.system("taskkill /f /im cmd.exe")
			print "The switch_iperf.skl was done - PASS"
		except:
			raise Exception("No execute the action - FAIL")

	def Swiandroidh_FtpClient(self):
		try:
			time.sleep(2)
			os.system(
				"cmd.exe /c C:\Sikuli-IDE\Sikuli-IDE.bat -r ..\\..\\sikuli\\switch_FtpClient.skl")
			# os.system("taskkill /f /im cmd.exe")
			print "The switch_FtpClient.skl was done - PASS"
		except:
			raise Exception("No execute the action - FAIL")

	def Swiandroidh_Speedtest(self):
		try:
			time.sleep(2)
			os.system(
				"cmd.exe /c C:\Sikuli-IDE\Sikuli-IDE.bat -r ..\\..\\sikuli\\switch_Speedtest.skl")
			# os.system("taskkill /f /im cmd.exe")
			print "The switch_Speedtest.skl was done - PASS"
		except:
			raise Exception("No execute the action - FAIL")

	def Swiandroidh_Handy(self):
		try:
			time.sleep(2)
			os.system(
				"cmd.exe /c C:\Sikuli-IDE\Sikuli-IDE.bat -r ..\\..\\sikuli\\switch_Handy.skl")
			# os.system("taskkill /f /im cmd.exe")
			print "The switch_Handy.skl was done - PASS"
		except:
			raise Exception("No execute the action - FAIL")

	def Exec_Command(self, exec_com):  # command to Ubuntu
		try:
			# change the config
			PlinkCommand = "..\\..\\tools\\plink.exe -ssh "+config.get("setting", "server_host")+" "+"-l "+config.get(
				"setting", "server_user")+" "+"-pw "+config.get("setting", "server_password")+" "+exec_com
			print "Plink command is = "+PlinkCommand
			# a = os.system(PlinkCommand);
			os.system(PlinkCommand)
			pipe = subprocess.Popen(
				PlinkCommand, shell=True, stdout=subprocess.PIPE).stdout
			out = pipe.read()
			f = open('..\\..\\temp\\log.txt', 'w')
			f.write(out)
			f.close
			print "The exec_command was finished - PASS"
		except:
			raise Exception("The exec_command was not finished - FAIL")

	def Getfile_Command(self):  # get file from Ubuntu
		try:
			# change the config
			ftplocal_file = config.get("ftp", "ftplocal_file")
			PscpCommand = "..\\..\\tools\\pscp.exe -pw "+config.get("ftp_setting", "server_password")+" "+config.get(
				"ftp_setting", "server_user")+"@"+config.get("ftp_setting", "server_host")+":"+config.get("ftp", "ftpremote_file")+" "+ftplocal_file
			print "Pscp command is = "+PscpCommand
			os.system(PscpCommand)
			print "Got the file - PASS"
		except:
			raise Exception("The file was not got - FAIL")

	def Getfile_Command_Iperf(self):  # get file from Ubuntu
		try:
			PscpCommand = "..\\..\\tools\\pscp.exe -pw "+config.get("setting", "server_password")+" "+config.get(
				"setting", "server_user")+"@"+config.get("setting", "server_host")+":"+config.get("iperf_setting", "iperflocal_file")+" "+config.get("iperf", "iperflocal_file")
			print "Pscp command is = "+PscpCommand
			os.system(PscpCommand)
			print "Got the file - PASS"
		except:
			raise Exception("The file was not got - FAIL")

	def Strip_Split_Iperf(self):
		try:
			openfile = file('..\\suit\\speed_result.txt', 'r')
			writefile = '..\\suit\\split_speed_result.txt'
			for line in openfile:
				items = line.strip().split(' ')
				print items
			print items[-2]
			os.system('echo '+items[-2]+' > '+writefile)
			print 'echo '+items[-2]+' > '+writefile
			openfile.close()
		except:
			raise Exception("The file was not finished. - FAIL")

	def Strip_Split_Iperf_UDP(self, naan):
		try:
			openfile = file('..\\suit\\speed_result.txt', 'r')
			writefile = '..\\suit\\split_speed_result.txt'
			for line in openfile:
				items = line.strip().split(' ')
				print items
				if items[0] in '[':
					# na
					for number in range(0,10):
						if items[4] == '0.0-'+config.get("setting","iperf_time")+'.'+str(number):
							if naan == 'na':
								print items[11]
								os.system('echo '+items[11]+' > '+writefile)
								print 'echo '+items[10]+' > '+writefile
								break
							if naan == 'an':
								print items[-2]
								os.system('echo '+items[-2]+' > '+writefile)
								print 'echo '+items[-2]+' > '+writefile		
								break						
						if items[4] == '0.0-'+str(int(config.get("setting","iperf_time"))-1)+'.'+str(number):
							if naan == 'na':
								print items[11]
								os.system('echo '+items[11]+' > '+writefile)
								print 'echo '+items[10]+' > '+writefile
								break
							if naan == 'an':
								print items[-2]
								os.system('echo '+items[-2]+' > '+writefile)
								print 'echo '+items[-2]+' > '+writefile
								break
					if items[4] == '0.0-'+config.get("setting","iperf_time")+'.'+str(number):
						break
					if items[4] == '0.0-'+str(int(config.get("setting","iperf_time"))-1)+'.'+str(number):
						break
		except:
			raise Exception("The file was not finished. - FAIL")

	def Ftplog_Renew(self):
		try:
			self.Exec_Command("rm "+config.get("ftp", "ftpremote_file"))
			time.sleep(2)
			print "The rm " + config.get("ftp", "ftpremote_file") + " was finished"
			self.Exec_Command("touch "+config.get("ftp", "ftpremote_file"))
			time.sleep(1)
			print "The touch " + config.get("ftp", "ftpremote_file") + " was finished"
			self.Exec_Command("chmod 777 "+config.get("ftp", "ftpremote_file"))
			time.sleep(2)
			print "The chmod 777 " + config.get("ftp", "ftpremote_file") + " was finished"
			time.sleep(1)
			print "The chmod will be change by exec_command(). - PASS"
		except:
			raise Exception(
				"The chmod will NOT be change by exec_command(). - FAIL")

	def Check_File_Status(self):
		try:
			fileName = "..\\..\\Result\\log\\vsftpd.log"
			if os.path.exists(fileName):
				print fileName, "fileName is exists - PASS"
				pass
			else:
				#			raise IOError
				while not os.path.exists(fileName):
					time.sleep(5)
					time.sleep(60)
		except:
			raise Exception("The "+fileName+"is not exist - FAIL")

	def Transfer_Status(self, filestart, fileend):
		while True:
			try:
				time.sleep(5)
				os.system("del ..\\..\\Result\\log\\vsftpd.log")
				self.Getfile_Command()
				f = open("..\\..\\Result\\log\\vsftpd.log", 'r')
				fileString = f.read()
				f.close()
				a = fileString.find(filestart)
				b = fileString.find(fileend)

				if a and b != -1:
					# Not reached.
					print "String found - PASS"
					break
				else:
					time.sleep(20)
					print "String not found"
			except:
				raise Exception("The sting not found - FAIL")

	def FTP_Urate(self):
		try:
			# while True:
			for i in range(0, 100):
				f = open("..\\..\\Result\\log\\vsftpd.log", 'r')
				fileString = f.read()
				break
				f.close()

			for item in fileString.split("\n"):
				if "OK UPLOAD: Client" in item:
					fileString = item.strip()
					a = fileString.split(' ')[-1].split('.')[0]
					filename = fileString.split(' ')[-4]
					Upload_SPEED = float(a)*8/1024

					if int(Upload_SPEED) >= 0:
						print filename+"Transfer speed is : "+str(Upload_SPEED), "Mbps/sec"
						print "Step : File Transfer Complete (Upload) - PASS"
						os.system("echo "+filename+"Transfer speed is : " +
								  str(Upload_SPEED)+" Mbps/sec >> ..\\..\\Result\\log\\result.txt")
					else:
						raise Exception(
							"Step : File Transfer Not Complete (Upload)")
		except:
			raise Exception(
				"Step : File Transfer Not Complete (Upload) - FAIL")

	def FTP_Drate(self):
		try:
			for i in range(0, 100):
				f = open("..\\..\\Result\\log\\vsftpd.log", 'r')
				fileString = f.read()
				break
				f.close()

			for item in fileString.split("\n"):
				if "OK DOWNLOAD: Client" in item:
					fileString = item.strip()
					a = fileString.split(' ')[-1].split('.')[0]
					filename = fileString.split(' ')[-4]
					Download_SPEED = float(a)*8/1024
					# print Download_SPEED, "MB"
					# print int(Download_SPEED)

					if int(Download_SPEED) >= 0:
						print filename+"Transfer speed is : "+str(Download_SPEED), "Mbps/sec"
						print "Step : File Transfer Complete (Download) - PASS"
						os.system("echo "+filename+"Transfer speed is : " +
								  str(Download_SPEED)+" Mbps/sec >> ..\\..\\Result\\log\\result.txt")

					else:
						raise Exception(
							"Step : File Transfer Not Complete (Download) - FAIL")
		except:
			raise Exception(
				"Step : File Transfer Not Complete (Download) - FAIL")

	def Iperf_NA(self):
		adbClient.Service_Iperf_Start()
		adbClient.Iperf_Client()
		adbClient.get_file()
		adbClient.Check_iStatus(config.get("setting", "local_file"))
		adbClient.Move_File("UP_androidP_")

	def Iperf_AN(self):
		# adbClient.Swiandroidh_Iperf()
		iperf_command = "-s -i -5"
		android.Mobile_Device_Connect()
		android.Service_Iperf_Start(iperf_command)
		android.Iperf_Log_Clean()
		adbClient.client_iperf_start()
		adbClient.ADB_Event("4")
		android.Screen_Shot_Save(iperf_command)
		android.Mobile_Device_Disconnect()
		adbClient.Move_File("Down_androidP_")

	def Iperf_NA_U(self, UP_UDP):
		# adbClient.Swiandroidh_Iperf()
		adbClient.service_iperfU_start()
		adbClient.Iperf_Client_U(UP_UDP)
		adbClient.get_file()
		adbClient.Check_iStatus(config.get("setting", "local_file"))
		adbClient.Move_File("UP_UDP_")

	def Iperf_AN_U(self, DL_UDP):
		# adbClient.Swiandroidh_Iperf()
		iperf_command = "-s -i -5 -u"
		android.Mobile_Device_Connect()
		android.Service_Iperf_Start(iperf_command)
		android.Iperf_Log_Clean()
		adbClient.client_iperfU_start(DL_UDP)
		adbClient.ADB_Event("4")
		android.Screen_Shot_Save(iperf_command)
		android.Mobile_Device_Disconnect()
		adbClient.Move_File("Down_UDP_")

	def FTP_NA_Download(self, filename, filestart, fileend):
		print "NB Server & android Client (ftp download)"
		# adbClient.Swiandroidh_FtpClient()
		adbClient.Ftplog_Renew()
		android.Mobile_Device_Connect()
		# adbClient.Download_Over()
		# android.Ftp_Creat_Account()
		android.Ftp_Connect()
		android.Verify_Ftp_Connect()
		android.Folder_Select("Download")
		android.Ftp_Download(filename)
		adbClient.Transfer_Status(filestart, fileend)
		adbClient.Getfile_Command()
		adbClient.Check_File_Status()
		adbClient.ADB_Event("4")
		android.Screen_Shot_Save("Ftp_Download")
		adbClient.FTP_Drate()
		android.Mobile_Device_Disconnect()

	def FTP_NA_Upload(self, filename, filestart, fileend):
		print "NB Server & android Client (ftp upload)"
		# adbClient.Swiandroidh_FtpClient()
		adbClient.Ftplog_Renew()
		android.Mobile_Device_Connect()
		# adbClient.Download_Over()
		# android.Ftp_Creat_Account()
		android.Ftp_Connect()
		android.Verify_Ftp_Connect()
		android.Folder_Select("Upload")
		android.Ftp_Localfolder()
		adbClient.ADB_Event("123")
		adbClient.ADB_Event("123")
		android.Folder_Select("Upload")
		android.Ftp_Upload(filename)
		adbClient.Transfer_Status(filestart, fileend)
		adbClient.Getfile_Command()
		adbClient.Check_File_Status()
		adbClient.ADB_Event("4")
		android.Screen_Shot_Save("Ftp_Upload")
		adbClient.FTP_Urate()
		android.Mobile_Device_Disconnect()

	def FTP_NA_Download_S(self, times, filename, filestart, fileend):
		print "NB Server & android Client (ftp loop download)"
		# adbClient.Swiandroidh_FtpClient()
		android.Mobile_Device_Connect()
		# adbClient.Download_Over()
		# android.Ftp_Creat_Account()
		for i in range(0, int(times)):
			adbClient.Ftplog_Renew()
			android.Ftp_Connect()
			android.Verify_Ftp_Connect()
			android.Folder_Select("Download")
			android.Ftp_Download(filename)
			adbClient.Del_File("vsftpd.log")
			adbClient.Transfer_Status(filestart, fileend)
			adbClient.Getfile_Command()
			adbClient.Check_File_Status()
			adbClient.ADB_Event("4")
			android.Screen_Shot_Save("Ftp_Download")
			adbClient.FTP_Drate()
			adbClient.ADB_Event("66")
			adbClient.ADB_Event("66")
			adbClient.ADB_Event("111")
			adbClient.ADB_Event("111")
			adbClient.ADB_Event("111")
		android.Mobile_Device_Disconnect()
		print "Mobile_Device_Disconnect"

	def FTP_NA_Upload_S(self, times, filename, filestart, fileend):
		print "NB Server & android Client (ftp loop upload)"
		# adbClient.Swiandroidh_FtpClient()
		android.Mobile_Device_Connect()
		# adbClient.Download_Over()
		# android.Ftp_Creat_Account()
		for i in range(0, int(times)):
			adbClient.Ftplog_Renew()
			android.Ftp_Connect()
			android.Verify_Ftp_Connect()
			android.Folder_Select("Upload")
			android.Ftp_Localfolder()
			adbClient.ADB_Event("123")
			adbClient.ADB_Event("123")
			android.Folder_Select("Upload")
			android.Ftp_Upload(filename)
			adbClient.Transfer_Status(filestart, fileend)
			adbClient.Getfile_Command()
			adbClient.Check_File_Status()
			adbClient.ADB_Event("4")
			android.Screen_Shot_Save("Ftp_Upload")
			adbClient.FTP_Urate()
			adbClient.ADB_Event("66")
			adbClient.ADB_Event("66")
			adbClient.ADB_Event("111")
			adbClient.ADB_Event("111")
			adbClient.ADB_Event("111")
		android.Mobile_Device_Disconnect()
		print "Mobile_Device_Disconnect"

	# def Speed_test(self):
	# 	print "Speed test"
	# 	# adbClient.Swiandroidh_Speedtest()
	# 	android.Mobile_Device_Connect()
	# 	android.Verify_Speed()
	# 	time.sleep(40)
	# 	android.Speed_Download()
	# 	android.Speed_Upload()
	# 	android.Screen_Shot_Save("Speed")
	# 	android.Mobile_Device_Disconnect()

	def Start_Airplane(self):
		try:
			self.ADB_Shell("settings put global airplane_mode_on 1")
			self.ADB_Shell(
				"am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")
			time.sleep(6)
			print "The Start airplane was finished - PASS"
		except:
			raise Exception("The Start airplane was not finished - FAIL")

	def Stop_Airplane(self):
		try:
			self.ADB_Shell("settings put global airplane_mode_on 0")
			self.ADB_Shell(
				"am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")
			time.sleep(15)
			print "The Stop airplane was finished - PASS"
		except:
			raise Exception("The Stop airplane was not finished - FAIL")

	def Switch_Voice_Quality(self, j):
		try:
			print "The times: " + str(j)
			if j == 1:
				self.ADB_Event("4")
				time.sleep(1)
				self.ADB_Event("19")
				time.sleep(1)
				self.ADB_Event("61")
				time.sleep(1)
				self.ADB_Event("66")
			else:
				time.sleep(5)
				# Handy error location
				##############################
				self.ADB_Event("4")
				##############################
				self.ADB_Event("61")
				self.ADB_Event("21")
				self.ADB_Event("19")
				self.ADB_Event("66")
			time.sleep(1)
			self.ADB_Event("123")
			self.ADB_Event("19")
			self.ADB_Event("19")
			self.ADB_Event("19")
			self.ADB_Event("19")
			self.ADB_Event("19")
			self.ADB_Event("19")
			self.ADB_Event("19")
			self.ADB_Event("19")
			self.ADB_Event("19")
			self.ADB_Event("66")
			time.sleep(2)
			self.ADB_Event("21")
			self.ADB_Event("66")
			print "Switch_Voice_Quality function already done. - PASS"
		except:
			raise Exception(
				"Switch_Voice_Quality function already done. - FAIL")

	def Handy_Keep_Log(self):
		try:
			time.sleep(5)
			self.ADB_Event("61")
			self.ADB_Event("61")
			self.ADB_Event("61")
			self.ADB_Event("61")
			self.ADB_Event("61")
			self.ADB_Event("66")
			print "The handy keep log was finished - PASS"
		except:
			raise Exception("The handy keep log was not finished - FAIL")

if __name__ == "__main__":

	# ron_pass
	android = Android()
	adbClient = AdbClient()
	print 'The Android() and AdbClient() are declare.'

	# adbClient.Client_IperfU_Start("120m")
	# adbClient.Move_File("Up_")
	# adbClient.Strip_Split_Iperf()
	# adbClient.Strip_Split_Iperf_UDP('na')
	# adbClient.Client_IperfU_Start("120m")

	# adbClient.Client_IperfU_Start("120m")
	# print 'iperf -c 172.29.1.15 -u -i 5 -t 600 -b 120m -l 1350'
	# adbClient.Iperf_Client_U("12m")
	# print '-c 172.29.1.15 -u -i 5 -t 600 -b 12m'
	# android.Check_Mobile_Nexus()
	# android.Check_Mobile_Note4()
	# adbClient.Start_Airplane()
	# adbClient.Stop_Airplane()

	# Test
	# android.Mobile_Device_Connect()
	# for loop in range(0,2):
	# 	android.Ftp_Judgemnet_Hinet_Or_Server('hinet')
	# 	android.Ftp_Judgemnet_Hinet_Or_Server('server')
	# 	pass
	# android.Mobile_Device_Disconnect()

	# iperf_command = 'iperf -s -i 1'
	# adbClient.Service_Iperf_Start(iperf_command)

	# # ron_pass
	# for i in range(0,1):
	# 	adbClient.Speed_test()

# ===================================================================================

	# Pending (host 10.1.106.242 cannot run)
	# host = "10.1.106.242"
	# user = "root"
	# passwd = "root"
	# os.system("rd ..\\..\\Result\\log\\ /s /q")
	# os.system("mkdir ..\\..\\Result\\log")
	# for i in range(0,101):
	# 	adbClient.Start_airplane()
	# 	adbClient.exec_command("cp /root/rsys/scripts/1.sh /root/rsys/scripts/bash_start_TeNB.sh")
	# 	adbClient.exec_command("/root/rsys/scripts/reboot-fap")
	# 	time.sleep(5)
	# 	adbClient.Stop_airplane()
	# 	time.sleep(5)
	# 	adbClient.Speed_test()

	# adbClient.getlog_femto()
	# os.system("mkdir ..\\..\\Result\\log\\"+str(i)+"-1")
	# print "move ..\\..\\Result\\femtolog\\*.* ..\\..\\Result\\log\\"+str(i)+"-1")
	# os.system("move ..\\..\\Result\\femtolog\\*.* ..\\..\\Result\\log\\"+str(i)+"-1")
	# print "move ..\\..\\Result`\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-1")
	# os.system("move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-1")
	# print "move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-1")
	# os.system("move ..\\..\\Result\\pic\\*.* ..\\..\\Result\\log\\"+str(i)+"-1")

	# adbClient.Start_airplane()
	# adbClient.exec_command("cp /root/rsys/scripts/1.sh /root/rsys/scripts/bash_start_TeNB.sh")
	# adbClient.exec_command("/root/rsys/scripts/reboot-fap")
	# time.sleep(210)
	# adbClient.Stop_airplane()
	# time.sleep(40)
	# adbClient.Speed_test()

	# adbClient.getlog_femto()
	# os.system("mkdir ..\\..\\Result\\log\\"+str(i)+"-2")
	# print "move ..\\..\\Result\\femtolog\\*.* ..\\..\\Result\\log\\"+str(i)+"-2")
	# os.system("move ..\\..\\Result\\femtolog\\*.* ..\\..\\Result\\log\\"+str(i)+"-2")
	# print "move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-2")
	# os.system("move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-2")
	# print "move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-2")
	# os.system("move ..\\..\\Result\\pic\\*.* ..\\..\\Result\\log\\"+str(i)+"-2")

	# adbClient.Start_airplane()
	# adbClient.exec_command("cp /root/rsys/scripts/2.sh /root/rsys/scripts/bash_start_TeNB.sh")
	# adbClient.exec_command("/root/rsys/scripts/reboot-fap")
	# time.sleep(210)
	# adbClient.Stop_airplane()
	# time.sleep(40)
	# adbClient.Speed_test()

	# adbClient.getlog_femto()
	# os.system("mkdir ..\\..\\Result\\log\\"+str(i)+"-3")
	# print "move ..\\..\\Result\\femtolog\\*.* ..\\..\\Result\\log\\"+str(i)+"-3")
	# os.system("move ..\\..\\Result\\femtolog\\*.* ..\\..\\Result\\log\\"+str(i)+"-3")
	# print "move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-3")
	# os.system("move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-3")
	# print "move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-3")
	# os.system("move ..\\..\\Result\\pic\\*.* ..\\..\\Result\\log\\"+str(i)+"-3")

	# adbClient.Start_airplane()
	# adbClient.exec_command("cp /root/rsys/scripts/2.sh /root/rsys/scripts/bash_start_TeNB.sh")
	# adbClient.exec_command("/root/rsys/scripts/reboot-fap")
	# time.sleep(210)
	# adbClient.Stop_airplane()
	# time.sleep(40)
	# adbClient.Speed_test()

	# adbClient.getlog_femto()
	# os.system("mkdir ..\\..\\Result\\log\\"+str(i)+"-4")
	# print "move ..\\..\\Result\\femtolog\\*.* ..\\..\\Result\\log\\"+str(i)+"-4")
	# os.system("move ..\\..\\Result\\femtolog\\*.* ..\\..\\Result\\log\\"+str(i)+"-4")
	# print "move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-4")
	# os.system("move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-4")
	# print "move ..\\..\\Result\\femtolog\\ENGINEERING\\*.* ..\\..\\Result\\log\\"+str(i)+"-4")
	# os.system("move ..\\..\\Result\\pic\\*.* ..\\..\\Result\\log\\"+str(i)+"-4")

##########################################

	# ron_pass
	# adbClient.Del_File("result.txt")
	# adbClient.iperf_NA()
	# adbClient.iperf_AN()
	# adbClient.iperf_NA_U('52m')
	# adbClient.iperf_AN_U('160m')
	# android.Mobile_Device_Connect()
	# android.Screen_Shot_Save("Ftp_Upload")

	# # Cannot find the ftpremote_file
	# adbClient.FTP_NA_Download("1.pdf","/1.pdf","3236 bytes")
	# adbClient.FTP_NA_Upload("2.pdf","/2.pdf","62914560 bytes")
	# adbClient.FTP_NA_Download_S("1","1.pdf","/1.pdf","3236 bytes")
	# adbClient.FTP_NA_Upload_S("1","2.pdf","/2.pdf","62914560 bytes")

#=================ADB control======================================
	# # ron_pass
	# adbClient = AdbClient()
	# adbClient.ADB_Shell("su -c "+config.get("setting", "iperf_folder")+" -c "+config.get("setting", "iperf_SIP")+" -t "+config.get("setting", "iperf_time")+ " -i "+ config.get("setting", "monitor_time") + " > " + config.get("setting", "output_file"))
	# adbClient.Iperf_Client()
	# adbClient.get_file()
	# adbClient.put_file()

 #====================================================
	# ron_pass
	# android = Android()
	# adbClient = AdbClient()
	# adbClient.Del_File("result.txt")
	# for i in range(0,2):
	# 	print "Speed test"
	# 	adbClient.Swiandroidh_Speedtest()
	# 	android.Mobile_Device_Connect()
	# 	android.Verify_Speed()
	# 	time.sleep(40)
	# 	android.Screen_Shot_Save("Speed")
	# 	android.Mobile_Device_Disconnect()

	# ron_pass
	# android = Android()
	# adbClient = AdbClient()
	# android.Mobile_Device_Connect()
	# android.Verify_Speed()
	# time.sleep(40)
	# android.Screen_Shot_Save("Speed")
	# android.Speed_Download()
	# android.Speed_Upload()
	# android.Mobile_Device_Disconnect()

	# android = Android()
	# adbClient = AdbClient()
	# adbClient.Del_File("result.txt")
	# for i in range(0,3):
	# 	print i,"=================================================="
	# 	# Ftplog_Renew() problem
	# 	adbClient.Ftplog_Renew()
	# 	android.Mobile_Device_Connect()
	# 	# adbClient.Download_Over()
	# 	# android.Ftp_Creat_Account()
	# 	android.Ftp_Connect()
	# 	# cannot find the Download folder
	# 	android.Folder_Select("Download")
	# 	android.Ftp_Download("1.pdf")
	# 	adbClient.Transfer_Status("/1.pdf","3236 bytes")
	# 	adbClient.Getfile_Command()
	# 	adbClient.Check_File_Status()
	# 	adbClient.FTP_Drate()
	# 	android.Mobile_Device_Disconnect()

	#  #=================NB Server & android Client (ftp upload)==============

	# android = Android()
	# adbClient = AdbClient()
	# adbClient.Ftplog_Renew()
	# android.Mobile_Device_Connect()
	# adbClient.Download_Over()
	# android.Ftp_Creat_Account()
	# android.Ftp_Connect()
	# # cannot find the Upload folder
	# android.Folder_Select("Upload")
	# android.Ftp_Localfolder()
	# adbClient.ADB_Event("123")
	# adbClient.ADB_Event("123")
	# android.Folder_Select("Upload")
	# android.Ftp_Upload("1.pdf")
	# adbClient.Transfer_Status("/1.pdf","3236 bytes")
	# adbClient.Getfile_Command()
	# adbClient.Check_File_Status()
	# adbClient.FTP_Urate()
	# android.Mobile_Device_Disconnect()

	# android = Android()
	# adbClient = AdbClient()
	# # Ftplog_Renew problem
	# adbClient.Ftplog_Renew()
	# android.Mobile_Device_Connect()
	# adbClient.Download_Over()
	# android.Ftp_Creat_Account()
	# android.Ftp_Connect()
	# # cannot find the Download folder
	# android.Folder_Select("Download")
	# android.Ftp_Download("1.pdf")
	# adbClient.Transfer_Status("/1.pdf","3236 bytes")
	# adbClient.Getfile_Command()
	# adbClient.FTP_Drate()

	# # ron_pass
	# for i in range(0,2):
	# 	fileName = 'speed_result.txt'
	# 	adbClient.Del_File(fileName)
	# 	adbClient.Service_Iperf_Start()
	# 	adbClient.Iperf_Client()
	# 	adbClient.get_file()
	# 	adbClient.Check_iStatus(config.get("setting", "local_file"))
	# 	adbClient.Move_File("Down_")
