'''
Created on 2017/02/08
@author: wayne_teng
'''
#-*- coding: utf-8 -*-

import time,os,unittest
from selenium import webdriver
# import HTMLTestRunners


class speedtest(unittest.TestCase):

	def setUp(self):
		print "Start Unittest..."


	def tearDown(self):
		print "Stop Unitetest..."

	def test(self):

		for i in range(1,2):
			print i

			driver = webdriver.Chrome('..\\..\\tools\\chromedriver')  # Optional argument, if not specified will search path.
			driver.set_window_size(1024, 600)
			driver.maximize_window()

			driver.get('http://www.speedtest.net/');
			time.sleep(5) 
			os.system("cmd.exe /c C:\Sikuli-IDE\Sikuli-IDE.bat -r  ..\..\sikuli\speedtest.skl") 
			# C:\automation\sikuli\speedtest.skl
			os.system("taskkill /f /im cmd.exe")
			time.sleep(60) 
			driver.save_screenshot("..\\..\\Result\\pic\\"+str(i)+".png")  # C:\automation\Result\pic
			time.sleep(5) 
			driver.close()


if __name__ == "__main__":
	# ron_pass
	unittest.main()
