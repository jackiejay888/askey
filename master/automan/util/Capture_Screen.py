import pyscreenshot as ImageGrab
import os
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Capture_Screen(object):

	def Desktop_Capture(self):
		now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
		im = ImageGrab.grab()
		# im.show()
		ImageGrab.grab_to_file('..\\..\\Result\\pic\\'+'Desktop_'+now+'.png')
		print "save screen to file", now+'.png'

	# def Chrome_Capture(self, save_fn="chrome.png"):
	# 	# options = webdriver.ChromeOptions()
	# 	# options.add_argument("--start-maximized")   #chrom browser maximization
	# 	# options.add_argument("-incognito")  #open in incognito mode
	# 	browser = webdriver.Chrome()
	# 	# browser = webdriver.Chrome(chrome_options=options)
	# 	browser.get("http://www.google.com/")
	# 	time.sleep(2)
	# 	browser.get_screenshot_as_file(save_fn)
	# 	browser.close()

	# def Chrome_Capture(self):
	# 	# path = 'chromedriver.exe'
	# 	browser = webdriver.Chrome('chromedriver.exe')
	# 	# browser = webdriver.Chrome(executable_path = path)
	# 	browser.get("http://www.google.com/")
	# 	time.sleep(2)
	# 	browser.save_screenshot("123.png")
	# 	browser.close()

	def Firefox_Capture(self):
		now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
		profile = webdriver.FirefoxProfile()
		profile.set_preference("browser.privatebrowsing.autostart", True)
		browser = webdriver.Firefox(firefox_profile=profile)
		browser.maximize_window()
		browser.get("http://www.google.com/")  # Load page
		time.sleep(2)

		browser.save_screenshot(now+'.png')
		print "save screen to file", now+'.png'
		time.sleep(2)
		browser.close()

	def IE_Capture(self):
		now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
		browser = webdriver.Ie("IEDriverServer.exe")  # Get local session of IE
		browser.maximize_window()
		browser.get("http://www.google.com/")  # Load page
		time.sleep(2)
		browser.save_screenshot(now+'.png')
		print "save screen to file", now+'.png'
		time.sleep(2)
		browser.close()

if __name__ == "__main__":
	TC = Capture_Screen()
	TC.Desktop_Capture()
	# TC.Chrome_Capture()
	# TC.Firefox_Capture()
	# TC.IE_Capture()
