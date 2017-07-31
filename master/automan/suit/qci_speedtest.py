'''
@author: wayne_teng
'''

import unittest, os
import sys, ConfigParser, time
sys.path.insert(0, '..\\util')
from uiautomator import device as d
from uiautomator import Device
from uiautomator_control import Uiautomator_Control

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Android_Path.conf")

d = Device(config.get("uiautomator_control_setting", "device_id"))	

class Qci_Speedtest(unittest.TestCase,uiautomator_control):

	def setUp(self):
		print "Start by Automated execution"

	def tearDown(self):
		print "Stop by Automated execution"

	def test_Qci_Speedtest(self):

		for i in range(1,int(config.get("setting","run_times"))+1):
			os.system("adb shell am force-stop org.zwanoo.android.speedtest")
			print "execute run_times is ", i

			for j in range(1,int(config.get("Speedtest_setting","times"))+1):
				print "execute times is ", j
				
				for k in range(1,int(config.get("uiautomator_control_setting","apn"))+1):
					print "execute QCI Type is", k
					self.Restart_ADB()
					self.Switch_Home()
					self.Switch_Setting()
					self.Switch_More()
					self.Switch_APN()			
					self.Add_APN('QCI'+str(k))
					self.Restart_ADB()
					time.sleep(5)
					self.Speed_Test()

if __name__ == '__main__':
	unittest.main()
	# TC = Qci_Speedtest()
	# TC.test_Qci_Speedtest()