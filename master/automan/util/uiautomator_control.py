# -*- coding: utf-8 -*-
'''
Created on 2017/03/13
@author: wayne_teng

Add function on 2017/04/26
@author: Ron Chen
@title: Execute the device action by uiautomator control
'''
import os
import re
import sys
import time
import ConfigParser
from appium import webdriver
from android import Android
from android import AdbClient
from subprocess import check_output
from uiautomator import Device
from uiautomator import device as d
from uiautomator import AutomatorDeviceObject as auto

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")
config_setting = ConfigParser.ConfigParser()
config_setting.read(".\..\\..\\ini\\web_control_setting.conf")
d = Device(check_output(["adb", "devices"]).split()[-2])


class Uiautomator_Control(object):

	def Initial_Setup(self):
		if d(resourceId="com.android.settings:id/text_layout").exists:
			d(resourceId="com.android.settings:id/text_layout").click()
			time.sleep(1)
			os.system("adb shell input keyevent 82")
			os.system("adb shell input keyevent 19")
			os.system("adb shell input keyevent 66")
			print "Delete Access Point Names - PASS"

	def Switch_Home(self):
		time.sleep(1)
		d.press.home()
		print "Switch_Home - PASS"

	def Switch_Back(self):
		d.press.back()
		print "Switch_Back - PASS"

	def Switch_Setting(self):
		# while True:
		for search_times in range(int(config_setting.get("search_times", "times"))):
			time.sleep(3)
			print "Prepare to click the \"Settings\" button"
			if d(text="Settings").exists:
				print "Found the \"Settings\" button"
				d(text="Settings").click()
				print "Click the \"Settings\" button"
				print "Switch_Setting - PASS"
				break

	# Note4
	def Switch_Setting_Note4(self):
		time.sleep(3)
		for setting in range(int(config_setting.get("search_times", "times"))):
			print 'The Switch_setting times is : '+str(setting+1)
			if d(text="Settings").exists:
				d(text="Settings").click()
				print "Switch_Setting_Note4 - PASS"
				break
			else:
				print 'The Setting isn\'t found'
				continue

	def Switch_More(self):
		time.sleep(1)
		d(scrollable=True).scroll.to(text="More")
		if d(text="More").exists:
			d(text="More").click()
			print "Switch_More - PASS"
		else:
			raise Exception("Can not Switch_More - FAIL")

	# Note4
	def Switch_More_networks(self):
		time.sleep(1)
		d(scrollable=True).scroll.to(text="More networks")
		if d(text="More networks").exists:
			d(text="More networks").click()
			print "Switch_More_networks - PASS"
		else:
			raise Exception("Can not Switch_More_networks - FAIL")

	def Switch_Cellular_Networks(self):
		time.sleep(1)
		if d(text="Cellular networks").exists:
			d(text="Cellular networks").click()
			print "Switch_Cellular_Networks - PASS"
		else:
			raise Exception("Can not Switch_Cellular_Networks - FAIL")

	# Note4
	def Switch_Mobile_networks(self):
		time.sleep(1)
		if d(text="Mobile networks").exists:
			d(text="Mobile networks").click()
			print "Switch_Mobile_networks - PASS"
		else:
			raise Exception("Can not Switch_Cellular_Networks - FAIL")

	def Switch_Network_Operators(self):
		time.sleep(1)
		if d(text="Network operators").exists:
			d(text="Network operators").click()
			print "Switch_Network_Operators - PASS"
		else:
			raise Exception("Can not Switch_Network_Operators - FAIL")

	# Note4
	def Information_Alert(self):
		time.sleep(2)
		if d(text="OK").exists:
			d(text="OK").click()
			print "Click the \"OK\" button - PASS"
		else:
			print "The OK button is not displayed - FAIL"

	# Note4
	def Access_Point_Names(self):
		time.sleep(1)
		if d(text="Access Point Names").exists:
			d(text="Access Point Names").click()
			print "Click the \"APN\" button - PASS"
		else:
			print "The APN button is not displayed - FAIL"

	def Click_Device_Value0(self):
		time.sleep(80)
		if d(text=config_setting.get("setting", "PLMN")).exists:
			d(text=config_setting.get("setting", "PLMN")).click()
			android = Android()
			android.Copy_Trace_Folder()
			raise Exception("The device is clicked. - FAIL")
		else:
			print "The device is not clicked. - PASS"

	def Click_Device_Value1(self, device):
		for search_times in range(int(config_setting.get("search_times", "times"))):
			time.sleep(1)
			self.Switch_Back()
			time.sleep(1)
			print 'The Research times : ' + str(search_times + 1)
			self.Switch_Network_Operators()

			# Judgment the PLMN number by nexus or note4
			plmn = config_setting.get("setting", "PLMN")
			merge_plmn = plmn.split(" ")[0]+plmn.split(" ")[1]

			if device == 'nexus':
				print 'The device is nexus.'
				time.sleep(180)
				if d(text=plmn).exists:
					print 'nexus'
					d(text=plmn).click()
					break

			if device == 'note4':
				print 'The device is note4.'
				self.Information_Alert()
				# time.sleep(95)
				time.sleep(180)
				if d(text=merge_plmn).exists:
					print 'note4'
					d(text=merge_plmn).click()
					break

			if search_times+1 == int(config_setting.get("search_times", "times")):
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("The device is not clicked. - FAIL")
		print "The device is clicked. - PASS"

	def Switch_APN(self):
		time.sleep(2)
		if d(text="Cellular networks").exists:
			d(text="Cellular networks").click()
			print "Switch_Cellular networks - PASS"
			time.sleep(1)
			if d(text="Access Point Names").exists:
				d(text="Access Point Names").click()
				print "Switch_Access Point Names - PASS"
				self.Initial_Setup()
			else:
				raise "can not Switch Access Point Names - FAIL"
		else:
			raise "can not Switch Cellular networks - FAIL"

	def Add_APN(self, new_apn):
		time.sleep(2)
		# d.press.home()
		print "Add APN name and APN type."
		button = d(className='android.widget.TextView', description='New APN')
		button.click()
		time.sleep(3)

		print "Switch Edit access point - PASS"
		if d(text="Name").exists:
			d(text="Name").click()
			print "Select Name set - PASS"
			time.sleep(1)
			d(resourceId="android:id/edit").clear_text()
			# d(resourceId="android:id/edit").set_text(config.get("uiautomator_control_setting", "apn"))
			d(resourceId="android:id/edit").set_text(new_apn)
			d(text="OK").click()
			time.sleep(3)
		else:
			raise "Can not setting Access Point Names - FAIL"

		if d(text="APN").exists:
			d(text="APN").click()
			print "Select APN set - PASS"
			time.sleep(1)
			d(resourceId="android:id/edit").clear_text()
			# d(resourceId="android:id/edit").set_text(config.get("uiautomator_control_setting", "apn"))
			d(resourceId="android:id/edit").set_text(new_apn)
			d(text="OK").click()
		else:
			raise "Can not setting Access Point - FAIL"

		if new_apn == 'internet':
			time.sleep(1)
			d(scrollable=True).scroll.to(text="APN type")
			if d(text="APN type").exists:
				d(text="APN type").click()
				print "Select APN type - PASS"
				time.sleep(1)
				d(resourceId="android:id/edit").clear_text()
				d(resourceId="android:id/edit").set_text(new_apn+',supl')
				d(text="OK").click()
				time.sleep(3)
			else:
				raise Exception("Can not Select APN type - FAIL")

		os.system("adb shell input keyevent 82")
		os.system("adb shell input keyevent 19")
		os.system("adb shell input keyevent 66")
		time.sleep(1)
		self.Android_Screenshot("Finish_add_apn_")

	def Click_Radio_Button(self):
		time.sleep(3)
		if d(resourceId="android:attr/label").exists:
			d(resourceId="android:attr/label").click()
			
	def Remove_APN(self):
		print "Remove APN"
		if d(resourceId="com.android.settings:id/text_layout").exists:
			d(resourceId="com.android.settings:id/text_layout").click()
			time.sleep(1)
			os.system("adb shell input keyevent 82")
			os.system("adb shell input keyevent 19")
			os.system("adb shell input keyevent 66")
			self.Android_Screenshot("remove_apn_")
			print "Remove APN - PASS"

	# Note4
	def Remove_APN_Note4(self):
		time.sleep(2)
		if d(className="android.widget.ImageButton", description="More options").exists:
			d(className="android.widget.ImageButton",
			  description="More options").click()
		time.sleep(1)
		if d(text="Reset to default").exists:
			d(text="Reset to default").click()
			time.sleep(1)
			d(text="OK").click()
			time.sleep(2)

	def Android_Screenshot(self, error):
		Path = ("../../Result/pic/")
		now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
		d.screenshot(Path+error+'_'+now+".jpg")
		print "Save "+Path+error+'_'+now+".jpg"

	def Speed_Test(self, filename):
		android = Android()
		adbClient = AdbClient()
		print "Speed_Test"
		# adbClient.Swiandroidh_Speedtest()
		android.Mobile_Device_Connect()
		time.sleep(2)
		android.Verify_Speed()
		time.sleep(40)
		android.Speed_Download()
		android.Speed_Upload()
		android.Screen_Shot_Save(filename)
		android.Mobile_Device_Disconnect()

	def SpeedTest_True(self, filename):
		android = Android()
		adbClient = AdbClient()
		print "Speed_Test_True"
		# adbClient.Swiandroidh_Speedtest()
		time.sleep(6)
		android.Mobile_Device_Connect()
		time.sleep(2)
		android.Verify_SpeedTest_Value1()
		time.sleep(40)
		android.Speed_Download()
		android.Speed_Upload()
		android.Screen_Shot_Save(filename)
		android.Mobile_Device_Disconnect()

	def Restart_ADB(self):
		os.system("taskkill /F /IM adb.exe")
		os.system("adb kill-server")
		os.system("adb devices")
		print "Restart_ADB - PASS"

	def Reconnect_ADB(self):
		os.system("adb reconnect")
		print "Reconnect_ADB - PASS"

	def CellMapper(self):
		if d(text="Phone").exists:
			d(text="Phone").click()
			if d(resourceId="com.android.contacts:id/tab_custom_view_text").exists:
				d(resourceId="com.android.contacts:id/tab_custom_view_text").click()
			if d(resourceId="com.android.contacts:id/dialButton").exists:
				d(resourceId="com.android.contacts:id/digits").clear_text()
				d(resourceId="com.android.contacts:id/digits").set_text(
					config.get("cellmapper_setting", "dial_number"))
				time.sleep(3)
			else:
				raise 'Cannot found the dial button'
			print "CellMapper - PASS"
		else:
			raise 'Cannot found the Phone element'

	def ServiceMode(self, frequency):
		if d(text="ServiceMode").exists:
			print 'The ServiceMode was found'

			if d(text=" LTE RRC:IDLE BAND:" + config.get("cellmapper_setting", "band") + " BW: " + config.get("cellmapper_setting", "Bandwidth") + "MHz").exists:
				print 'The RRC and BAND and BW was found IDLE'
			elif d(text=" LTE RRC:CONN BAND:" + config.get("cellmapper_setting", "band") + " BW: " + config.get("cellmapper_setting", "Bandwidth") + "MHz").exists:
				print 'The RRC and BAND and BW was found CONN'

				if d(text=" MCC-MNC:" + config.get("cellmapper_setting", "PLMN") + ",TAC:" + config.get("cellmapper_setting", "TAC")).exists:
					print 'The PLMN and TAC was found'

					if d(text=" Earfcn: " + frequency + ", PCI: " + config.get("cellmapper_setting", "cellID")).exists:
						print 'The Earfun and CellID was found'
					else:
						raise 'Cannot found the Earfun and CellID text'
				else:
					raise 'Cannot found the PLMN and TAC text'
			else:
				raise 'Cannot found the RRC and BAND and BW text'
			print 'ServiceMode - PASS'
		else:
			raise 'Cannot found the ServiceMode text'

	def ServiceMode_Verify_PLMN(self, plmm):
		try:

			if d(text="ServiceMode").exists:
				print 'The ServiceMode was found'
					
				if d(text=" MCC-MNC:" + plmm + ",TAC:" + "69").exists:
					print 'The PLMN and TAC was found'
					return True
				else:
					print 'The PLMN and TAS was not found'
					return False
			else:
				raise 'Cannot found the ServiceMode text'
		except Exception as e:
			raise e

if __name__ == '__main__':
	print 'The uiautomator_control.py code.'
	# #################### Ron's code ####################
	# uiautomator_control = Uiautomator_Control()
	# uiautomator_control.CellMapper()
	# uiautomator_control.ServiceMode_Verify_PLMN("123-45")
	# uiautomator_control.Switch_Home()
	# uiautomator_control.Switch_Setting_Note4()
	# uiautomator_control.Switch_More_networks()
	# uiautomator_control.Switch_Mobile_networks()
	# uiautomator_control.Access_Point_Names()
	# uiautomator_control.Remove_APN_Note4()
	# uiautomator_control.Add_APN('QCI9')

	# uiautomator_control.Switch_Home()
	# uiautomator_control.Switch_Setting_Note4()
	# uiautomator_control.Switch_More_networks()
	# uiautomator_control.Switch_Mobile_networks()
	# uiautomator_control.Access_Point_Names()
	# uiautomator_control.Remove_APN_Note4()
	# uiautomator_control.Add_APN('ims')
	# uiautomator_control.Add_APN('internet')
	# time.sleep(1)
	# os.system("adb shell input keyevent 4")
	# time.sleep(1)
	# os.system("adb shell input keyevent 66")
	# for i in range(0,3):
	# 	time.sleep(1)
	# 	os.system("adb shell input keyevent 61")
	# time.sleep(1)
	# os.system("adb shell input keyevent 66")
	# uiautomator_control.Switch_Home()

	# uiautomator_control.Add_APN('QCI9')
	# uiautomator_control.Switch_Home()

	# # tc = Uiautomator_Control()
	# # tc.Switch_Home()
	# # tc.Switch_Setting_Note4()
	# # tc.Switch_More_networks()
	# # tc.Switch_Mobile_networks()
	# # tc.Switch_Network_Operators()
	# # tc.Information_Alert()
	# # tc.Click_Device_Value1_Note4()
	# # tc.Switch_Home()
	# # tc.CellMapper()
	# # tc.ServiceMode()
	# #################### Wayne's code ####################
	# tc = Uiautomator_Control()
	# for i in range(0,5):
	# 	os.system("adb shell am force-stop org.zwanoo.android.speedtest")
	# 	print "Execute times is ", i+1
	# 	tc.Restart_ADB()
	# 	tc.Switch_Home()
	# 	tc.Switch_Setting()
	# 	tc.Switch_More()
	# 	tc.Switch_APN()
	# 	tc.Add_APN('QCI9')
	# 	tc.Restart_ADB()
	# 	time.sleep(5)
	# 	tc.Speed_Test("QCI_Speed")
	# 	tc.Remove_APN()
	# ################################################################################
	# ################### Ron's code ####################
	# for i in range(50):
	#   print 'The ' + str(i+1) + ' times'
	#   os.system("adb shell am force-stop org.zwanoo.android.speedtest")
	#   print 'Speedtest app was killed'
	#   adbClient = AdbClient()
	#   adbClient.Start_Airplane()
	#   adbClient.Stop_Airplane()
	#   uiautomator_control = Uiautomator_Control()
	#   uiautomator_control.Restart_ADB()
	#   uiautomator_control.Switch_Home()
	#   uiautomator_control.Switch_Setting()
	#   uiautomator_control.Switch_More()
	#   uiautomator_control.Switch_Cellular_Networks()
	#   uiautomator_control.Switch_Network_Operators()
	#   time.sleep(160)
	#   uiautomator_control.Click_Device()
	#   uiautomator_control.Switch_Home()
	#   uiautomator_control.Restart_ADB()
	#   print 'The setting was finished'
	#   uiautomator_control.Speed_Test("Nexus5x_Speed")
	# ##########################################################################