#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
Created on 2017/03/29
@author: Ron Chen
@title: The ACS server connection by selenium RC with IE 9
'''
import os
import time
import math
import pyautogui
import ConfigParser
import win32clipboard
import win32com.client
import pyscreenshot as ImageGrab
from network import SCP
from selenium import selenium
from android import Android
from android import AdbClient
from delete_subfolder import Delete_Subfolder

config_element = ConfigParser.ConfigParser()
config_element.read(".\..\\..\\ini\\web_control_element.conf")
config_setting = ConfigParser.ConfigParser()
config_setting.read(".\..\\..\\ini\\web_control_setting.conf")
selenium = selenium("localhost", config_setting.get("setting", "port"), "*iexplore",
					"http://" + config_setting.get("setting", "ip_address") + ":8082/CWMServer/")
autoit = win32com.client.Dispatch("AutoItX3.Control")


class Webcontrol(object):

	###################  main menu  ####################
	def Initial(self):
		try:
			os.system(config_element.get("setting", "cancel_msta"))
			selenium.start()
			selenium.open("/CWMServer/index.jsp")
			selenium.window_maximize()
			print "The screen was open - PASS"
		except:
			raise Exception("The screen was not open - FAIL")

	def Login(self):
		try:
			selenium.open(config_element.get("setting", "acs_address_sub"))
			selenium.type("id="+config_element.get("login", "username_id"),
						  config_setting.get("setting", "username"))
			selenium.type("id="+config_element.get("login", "password_id"),
						  config_setting.get("setting", "password"))
			selenium.click("id="+config_element.get("login", "login_Id"))
			selenium.wait_for_page_to_load(
				config_element.get("setting", "wait_time"))
			print "Login to the web - PASS"
			pyautogui.click(1000, 30)
			selenium.click(
				"xpath="+config_element.get("setting", "askey_logo"))
			print "Get the ASKEY image - PASS"
		except:
			raise Exception("No login to the web - FAIL")

	def Exit(self):
		try:
			selenium.close()
			os.system(config_element.get("setting", "cancel_msta"))
			print 'The page was closed'
		except:
			raise Exception("The page was not closed")

	###################  system menu  ####################
	def System_Operation_Data(self):
		try:
			selenium.click("id="+config_element.get("system", "system_id"))
			selenium.click(
				"link="+config_element.get("system", "system_operation_data"))
			print "Open the System_Operation_Data screen - PASS"
		except:
			raise Exception("The System_Operation_Data function - FAIL")

	def System_Unknown_Cpe(self):
		try:
			selenium.click("id="+config_element.get("system", "system_id"))
			selenium.click(
				"link="+config_element.get("system", "system_unknown_cpe"))
			print "Open the System_Unknown_Cpe screen - PASS"
		except:
			raise Exception("The System_Unknown_Cpe function - FAIL")

	def System_Cpe_Assignment(self):
		try:
			selenium.click("id="+config_element.get("system", "system_id"))
			selenium.click(
				"link="+config_element.get("system", "system_cpe_assignment"))
			print "Open the System_Cpe_Assignment screen - PASS"
		except:
			raise Exception("The System_Cpe_Assignment function - FAIL")

	def System_Cpe_Upgrade(self):
		try:
			selenium.click("id="+config_element.get("system", "system_id"))
			selenium.click(
				"link="+config_element.get("system", "system_cpe_upgrade"))
			print "Open the System_Cpe_Upgrade screen - PASS"
		except:
			raise Exception("The System_Cpe_Upgrade function - FAIL")

	###################  security menu  ###################
	def Security_User(self):
		try:
			selenium.click("id="+config_element.get("security", "security_id"))
			selenium.click(
				"link="+config_element.get("security", "security_user"))
			print "Open the Security_User screen - PASS"
		except:
			raise Exception("The Security_User function - FAIL")

	def Security_Change_Password(self):
		try:
			selenium.click("id="+config_element.get("security", "security_id"))
			selenium.click("link="+config_element.get("security",
													  "security_change_password"))
			print "Open the Security_Change_Password screen - PASS"
		except:
			raise Exception("The Security_Change_Password function - FAIL")

	def Security_Logout(self):
		try:
			selenium.click("id="+config_element.get("security", "security_id"))
			selenium.click(
				"link="+config_element.get("security", "security_logout"))
			selenium.get_confirmation()
			selenium.choose_ok_on_next_confirmation()
			print "Open the Security_Logout screen - PASS"
		except:
			raise Exception("The Security_Logout function - FAIL")

	def Security_License(self):
		try:
			selenium.click("id="+config_element.get("security", "security_id"))
			selenium.click(
				"link="+config_element.get("security", "security_license"))
			print "Open the Security_License screen - PASS"
		except:
			raise Exception("The Security_License function - FAIL")

	###################  event menu  ###################
	def Event_Message_Log(self):
		try:
			selenium.click("id="+config_element.get("event", "event_id"))
			selenium.click(
				"link="+config_element.get("event", "event_message_log"))
			print "Open the Event_Message_Log screen - PASS"
		except:
			raise Exception("The Event_Message_Log function - FAIL")

	def Event_Inform_Log(self):
		try:
			selenium.click("id="+config_element.get("event", "event_id"))
			selenium.click(
				"link="+config_element.get("event", "event_inform_log"))
			print "Open the Event_Inform_Log screen - PASS"
		except:
			raise Exception("The Event_Inform_Log function - FAIL")

	def Event_Upgrade_Log(self):
		try:
			selenium.click("id="+config_element.get("event", "event_id"))
			selenium.click(
				"link="+config_element.get("event", "event_upgrade_log"))
			print "Open the Event_Upgrade_Log screen - PASS"
		except:
			raise Exception("The Event_Upgrade_Log function - FAIL")

	def Event_System_Log(self):
		try:
			selenium.click("id="+config_element.get("event", "event_id"))
			selenium.click(
				"link="+config_element.get("event", "event_system_log"))
			print "Open the Event_System_Log screen - PASS"
		except:
			raise Exception("The Event_System_Log function - FAIL")

	def Event_Active_Alarm(self):
		try:
			selenium.click("id="+config_element.get("event", "event_id"))
			selenium.click(
				"link="+config_element.get("event", "event_active_alarm"))
			print "Open the Event_Active_Alarm screen - PASS"
		except:
			raise Exception("The Event_Active_Alarm function - FAIL")

	def Event_History_Alarm(self):
		try:
			selenium.click("id="+config_element.get("event", "event_id"))
			selenium.click(
				"link="+config_element.get("event", "event_history_alarm"))
			print "Open the Event_History_Alarm screen - PASS"
		except:
			raise Exception("The Event_History_Alarm function - FAIL")

	def Event_Alarm_Definition(self):
		try:
			selenium.click("id="+config_element.get("event", "event_id"))
			selenium.click("link="+config_element.get("event",
													  "event_alarm_definition"))
			print "Open the Event_Alarm_Definition screen - PASS"
		except:
			raise Exception("The Event_Alarm_Definition function - FAIL")

	def Event_Log_Auto_Backup(self):
		try:
			selenium.click("id="+config_element.get("event", "event_id"))
			selenium.click(
				"link="+config_element.get("event", "event_log_auto_backup"))
			print "Open the Event_Log_Auto_Backup screen - PASS"
		except:
			raise Exception("The Event_Log_Auto_Backup function - FAIL")

	###################  file_db menu  ###################
	def File_DB_Configuration_File(self):
		try:
			selenium.click("id="+config_element.get("file_db", "file_db_id"))
			selenium.click("link="+config_element.get("file_db",
													  "file_db_configuration_file"))
			print "Open the File_DB_Configuration_File screen - PASS"
		except:
			raise Exception("The File_DB_Configuration_File function - FAIL")

	def File_DB_Log_File(self):
		try:
			selenium.click("id="+config_element.get("file_db", "file_db_id"))
			selenium.click(
				"link="+config_element.get("file_db", "file_db_log_file"))
			print "Open the File_DB_Log_File screen - PASS"
		except:
			raise Exception("The File_DB_Log_File function - FAIL")

	def File_DB_Image_File(self):
		try:
			selenium.click("id="+config_element.get("file_db", "file_db_id"))
			selenium.click(
				"link="+config_element.get("file_db", "file_db_image_file"))
			print "Open the File_DB_Image_File screen - PASS"
		except:
			raise Exception("The File_DB_Image_File function - FAIL")

	def File_DB_Certificate(self):
		try:
			selenium.click("id="+config_element.get("file_db", "file_db_id"))
			selenium.click(
				"link="+config_element.get("file_db", "file_db_certificate"))
			print "Open the File_DB_Certificate screen - PASS"
		except:
			raise Exception("The File_DB_Certificate function - FAIL")

	def File_DB_DB_Auto_Backup(self):
		try:
			selenium.click("id="+config_element.get("file_db", "file_db_id"))
			selenium.click("link="+config_element.get("file_db",
													  "file_db_db_auto_backup"))
			print "Open the File_DB_DB_Auto_Backup screen - PASS"
		except:
			raise Exception("The File_DB_DB_Auto_Backup function - FAIL")

	def File_DB_DB_Utility(self):
		try:
			selenium.click("id="+config_element.get("file_db", "file_db_id"))
			selenium.click(
				"link="+config_element.get("file_db", "file_db_db_utility"))
			print "Open the File_DB_DB_Utility screen - PASS"
		except:
			raise Exception("The File_DB_DB_Utility function - FAIL")

	def File_DB_History_Log_File(self):
		try:
			selenium.click("id="+config_element.get("file_db", "file_db_id"))
			selenium.click("link="+config_element.get("file_db",
													  "file_db_history_log_file"))
			print "Open the File_DB_History_Log_File screen - PASS"
		except:
			raise Exception("The File_DB_History_Log_File function - FAIL")

	def File_DB_File_Server_Config(self):
		try:
			selenium.click("id="+config_element.get("file_db", "file_db_id"))
			selenium.click("link="+config_element.get("file_db",
													  "file_db_file_server_config"))
			print "Open the File_DB_File_Server_Config screen - PASS"
		except:
			raise Exception("The File_DB_File_Server_Config function - FAIL")

	###################  testing menu  ###################
	def Testing_Pd128_Test(self):
		try:
			selenium.click("id="+config_element.get("testing", "testing_id"))
			selenium.click(
				"link="+config_element.get("testing", "testing_pd128_test"))
			print "Open the Testing_Pd128_Test screen - PASS"
		except:
			raise Exception("The Testing_Pd128_Test function - FAIL")

	def Testing_Cpe_Parameter_Test(self):
		try:
			selenium.click("id="+config_element.get("testing", "testing_id"))
			selenium.click("link="+config_element.get("testing",
													  "testing_cpe_parameter_test"))
			selenium.close()
			print "Open the Testing_Cpe_Parameter_Test screen - PASS"
		except:
			raise Exception("The Testing_Cpe_Parameter_Test function - FAIL")

	###################  help menu  ###################
	def Help_Contact_Information(self):
		try:
			selenium.click("id="+config_element.get("help", "help_id"))
			selenium.click("link="+config_element.get("help",
													  "help_contact_information"))
			selenium.close()
			print "Open the Help_Contact_Information screen - PASS"
		except:
			raise Exception("The Help_Contact_Information function - FAIL")

	def Help_Release_Information(self):
		try:
			selenium.click("id="+config_element.get("help", "help_id"))
			selenium.click("link="+config_element.get("help",
													  "help_Release_information"))
			selenium.close()
			print "Open the Help_Release_Information screen - PASS"
		except:
			raise Exception("The Help_Release_Information function - FAIL")

	def Help_Acs_Help(self):
		try:
			selenium.click("id="+config_element.get("help", "help_id"))
			selenium.click("link="+config_element.get("help", "help_acs_help"))
			print "Open the Help_Acs_Help screen - PASS"
		except:
			raise Exception("The Help_Acs_Help function - FAIL")

	def Help_Acs_Url(self):
		try:
			selenium.click("id="+config_element.get("help", "help_id"))
			selenium.click("link="+config_element.get("help", "help_acs_url"))
			print "Open the Help_Acs_Url screen - PASS"
		except:
			raise Exception("The Help_Acs_Url function - FAIL")

	def Help_Dashboard(self):
		try:
			selenium.click("id="+config_element.get("help", "help_id"))
			selenium.click(
				"link="+config_element.get("help", "help_dashboard"))
			print "Open the Help_Dashboard screen - PASS"
		except:
			raise Exception("The Help_Dashboard function - FAIL")

	###################  other menu  ###################
	def Add_All_Devices(self):
		try:
			self.System_Operation_Data()
			selenium.click(
				"xpath="+config_element.get("add_file", "click_add_button"))
			for add_file_times in range(0, 1):
				print "The " + str(add_file_times+1) + " add the file"
				time.sleep(1)
				selenium.click(
					"name="+config_element.get("add_file", "downframe"))
				selenium.type("xpath="+config_element.get("add_file",
														  "oui_text"), config_setting.get("add_file", "oui_value"))
				selenium.type("xpath="+config_element.get("add_file", "product_class"),
							  config_setting.get("add_file", "product_value"))
				selenium.type("xpath="+config_element.get("add_file", "serial_number"),
							  config_setting.get("add_file", "serial_number") + " - " + str(add_file_times+1))
				selenium.click(
					"css="+config_element.get("add_file", "submit_button"))
				################### Verify the success message ################
				selenium.click(
					"name="+config_element.get("add_file", "downframe"))
				add_cpe_successfully = selenium.get_text(
					"xpath="+config_element.get("add_file", "add_cpe_successfully"))
				if add_cpe_successfully == "The CPE has exsited.":
					print add_cpe_successfully
				elif add_cpe_successfully == "Add successfully.":
					print add_cpe_successfully
				else:
					raise Exception("Add file was not success")
			print "Add the file - PASS"
		except:
			raise Exception("Add the file was not success")

	def Delete_All_Devices(self):
		try:
			self.System_Operation_Data()
			total_file = selenium.get_text(
				"xpath="+config_element.get("delete_file", "get_allfile_number"))
			total_file_number = total_file.split()[1]
			print "The total number is " + total_file_number  # catch the total number
			for delete_times in range(0, int(math.ceil(float(total_file_number)/25))):
				time.sleep(5)  # wait the previous delete file
				print "Delete " + str(delete_times+1) + " times"
				selenium.click(
					"css="+config_element.get("delete_file", "select_allfile_checkbox"))
				selenium.click(
					"xpath="+config_element.get("delete_file", "delete_all_device_button"))
				selenium.get_confirmation()
				################### Verify the success message ################
				selenium.click(
					"name="+config_element.get("delete_file", "downframe"))
				delete_cpe_successfully = selenium.get_text(
					"xpath="+config_element.get("delete_file", "delete_successfully"))
				time.sleep(5)
				if delete_cpe_successfully == "Delete cpe successfully!":
					print delete_cpe_successfully
				else:
					raise Exception("Delete file was not success")
				print "Delete allfile - PASS"
		except:
			raise Exception("Delete file was not success")

	def Dashboard_Refresh(self):
		try:
			for i in range(0, 1):
				selenium.click(
					"xpath="+config_element.get("setting", "refresh_button"))
				print "click refresh button - " + str(i+1) + " PASS"
		except:
			raise Exception("The fresh button was not click - FAIL")

	def Click_Serial_Number(self):
		try:
			selenium.click(
				"link="+config_setting.get("setting", "serial_number"))
			print "Click the serial number you want"
		except:
			raise Exception("The serial number cannot click - FAIL")

	def Clear_All_Data(self, location, button, message):
		try:
			self.System_Operation_Data()
			self.Click_Serial_Number()
			# Clear the Message Log data #
			selenium.click(
				"link="+location)
			total_file = selenium.get_text(
				"xpath="+config_element.get("delete_file", "get_allfile_number"))
			total_file_number = total_file.split()[1]
			# catch the total number
			print "The total number is " + total_file_number
			total_delete_times = str(
				int(math.ceil(float(total_file_number)/25)))
			print "The total delete times is " + total_delete_times
			for delete_times in range(0, int(math.ceil(float(total_file_number)/25))):
				# wait the previous delete file
				time.sleep(4)
				print "Delete " + str(delete_times+1) + " times"
				selenium.click(
					"css="+config_element.get("delete_file", "select_allfile_checkbox"))
				selenium.click(
					"xpath="+button)
				selenium.get_confirmation()
				successfully_request_to_message_log = selenium.get_text(
					"xpath="+config_element.get("system", "parameter_value_successfully"))
				if successfully_request_to_message_log == message:
					print successfully_request_to_message_log
				else:
					raise Exception("Get value was not success")
		except:
			raise Exception("The all message log was not clear - FAIL")

	def Set_Value(self, boolean):

		if boolean == '0':
			# change the parameter value boolean to 0 #
			time.sleep(1)
			selenium.type("css="+config_element.get("adminstate", "adminstate_value"),
						  config_element.get("adminstate", "boolean_false"))
			time.sleep(1)
			print 'The value was change to ' + boolean
			selenium.click("xpath="+config_element.get("adminstate",
													   "adminstate_set_value_button"))
		if boolean == '1':
			# change the parameter value boolean to 1 #
			time.sleep(1)
			selenium.type("css="+config_element.get("adminstate", "adminstate_value"),
						  config_element.get("adminstate", "boolean_true"))
			time.sleep(1)
			print 'The value was change to ' + boolean
			selenium.click("xpath="+config_element.get("adminstate",
													   "adminstate_set_value_button"))

	def Parameter_List_Adminstate(self, boolean):
		try:
			self.System_Operation_Data()
			self.Click_Serial_Number()
			selenium.click(
				"link="+config_element.get("system", "system_parameter_list"))
			time.sleep(2)
			print "Click the Parameter List"
			selenium.click("link="+config_element.get("adminstate",
													  "adminstate_location"))
			self.Set_Value(boolean)
			successfully_request_to_message_queue = selenium.get_text(
				"xpath="+config_element.get("adminstate", "parameter_value_successfully"))
			if successfully_request_to_message_queue == "Successfully add SetParameterValues request to the Message Queue!":
				print successfully_request_to_message_queue
			else:
				raise Exception("Get value was not success")
		except:
			raise Exception("The parameter location was not found - FAIL")

	def Set_Value_By_Earfcn(self, earfcn):
		selenium.click("xpath="+config_element.get("Earfcn","earfcnDL_checkbox"))
		selenium.type("xpath="+config_element.get("Earfcn","earfcnDL_value"),earfcn)
		selenium.click("xpath="+config_element.get("Earfcn","earfcnUL_checkbox"))
		selenium.type("xpath="+config_element.get("Earfcn","earfcnUL_value"),earfcn)
		selenium.click("xpath="+config_element.get("Earfcn","earfcn_set_value_button"))

	def Parameter_List_Earfcn(self, earfcn):
		try:
			self.System_Operation_Data()
			self.Click_Serial_Number()
			selenium.click(
				"link="+config_element.get("system", "system_parameter_list"))
			time.sleep(2)
			print "Click the Parameter List"
			selenium.click("link="+config_element.get("Earfcn",
													  "rf_location"))
			self.Set_Value_By_Earfcn(earfcn)
			time.sleep(2)
			successfully_request_to_message_queue = selenium.get_text(
				"xpath="+config_element.get("Earfcn", "parameter_value_successfully_folder"))
			if successfully_request_to_message_queue == "Successfully add SetParameterValues request to the Message Queue":
				print successfully_request_to_message_queue
			else:
				raise Exception("Get value was not success")
		except:
			raise Exception("The parameter location was not found - FAIL")

	def Parameter_List_PLMN(self, checkbox, location, value):
		try:
			self.System_Operation_Data()
			self.Click_Serial_Number()
			selenium.click(
				"link="+config_element.get("system", "system_parameter_list"))
			time.sleep(2)
			print "Click the Parameter List"
			selenium.click("link="+config_element.get("PLMN","plmnlist_location"))
			selenium.click("xpath="+config_element.get("PLMN","plmnid_location"))
			selenium.click("xpath="+checkbox)
			selenium.click("xpath="+location)
			selenium.type("xpath="+location,value)
			selenium.click("xpath="+config_element.get("PLMN","plmnid_set_value_button"))
			time.sleep(2)
			# successfully_request_to_message_queue = selenium.get_text(
			# 	"xpath="+config_element.get("PLMN", "parameter_value_successfully_folder"))
			# if successfully_request_to_message_queue == "Successfully add SetParameterValues request to the Message Queue":
			# 	print successfully_request_to_message_queue
			# else:
			# 	raise Exception("Get value was not success")
		except Exception as e:
			raise e

	def ACS_Initiate_Connection(self):
		try:
			self.System_Operation_Data()
			self.Click_Serial_Number()
			time.sleep(2)
			selenium.click(
				"link="+config_element.get("system", "system_message_queue"))
			print "Click the message queue"
			for i in range(2):
				selenium.click(
					"xpath="+config_element.get("system", "system_refresh_button"))
				print "Click the refresh " + str(i+1) + " times"
			# Verify the SetParameterValues text can be get
			# time.sleep(1)  # Wait the 1 sec for get the acs parametervalues text on 106/06/11
			setParameterValues = selenium.get_text(
				"xpath="+config_element.get("detail_message", "acs_parametervalues_text"))
			if setParameterValues == 'SetParameterValues':
				print 'Get the SetParameterValues text!!'
			else:
				print "Do not Get the SetParameterValues text!!"
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("Do not Get the SetParameterValues text!!")
			self.Autoit_Tab_button(38, 200)
			autoit.Sleep(2000)
			autoit.Send("{ENTER}")
			print 'Click the ACS TCP Initiate Connection was finished'
			autoit.Sleep(2000)
			# IE 9
			autoit.WinWaitActive(
				"[title:ACS Notify Page - Windows Internet Explorer]", "")
			autoit.ControlClick(
				"ACS Notify Page - Windows Internet Explorer", "", "ToolbarWindow321")
			self.Autoit_Tab_button(4, 100)
			autoit.Sleep(2000)
			autoit.Send("{ENTER}")
			autoit.Sleep(2000)
			delete_subfolder = Delete_Subfolder()
			delete_subfolder.Delete_Path_Subfolder("..\\..\\Result\\femtolog")
			adbClient = AdbClient()
			time.sleep(2)
			adbClient.Swiandroidh_ACS()
			autoit.WinClose("[class:IEFrame]")
			# Click the refresh button
			for i in range(1):
				selenium.click(
					"xpath="+config_element.get("system", "system_refresh_button"))
				print "Click the refresh " + str(i+1) + " times"
			autoit.Sleep(2000)
			print "Click the acs initiate connectin button"
		except:
			raise Exception("The ace initiate button was not click - FAIL")

	def Get_Clipboard(self):
		try:
			# get clipboard data
			time.sleep(3)
			win32clipboard.OpenClipboard()
			get_data = win32clipboard.GetClipboardData()
			win32clipboard.CloseClipboard()
			print "Get Clipboard is - " + '"' + get_data + '"'
			return get_data
		except:
			raise Exception("The clipboard cannot get - FAIL")

	def Set_Clipboard(self):
		try:
			# set clipboard data
			time.sleep(3)
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			win32clipboard.SetClipboardText()
			win32clipboard.CloseClipboard()
		except:
			raise Exception("The clipboard cannot set - FAIL")

	def HeNS_Request_Message(self, boolean, heMS_SetParameterValues):
		# try:
			pyautogui.click(1000, 30)
			self.System_Operation_Data()
			self.Click_Serial_Number()
			# Click the Message Log #
			selenium.click(
				"link="+config_element.get("system", "system_message_log"))
			# Refresh the list content
			for refresh in range(2):
				selenium.click(
					"xpath="+config_element.get("system", "system_refresh_button"))
			# Select the HeMS detail message
			print 'Type the serial number.'
			self.Click_CheckBox()
			selenium.type("id="+config_element.get("detail_message",
												   "search_askey_root"), config_element.get("detail_message", "input_askey_root"))
			time.sleep(3)
			selenium.click(
				"xpath="+config_element.get("detail_message", "search_button"))
			print "Select the key code"
			# Verify the SetParameterValues text can be get
			setParameterValues = selenium.get_text(
				"xpath="+config_element.get("detail_message", "parametervalues_text"))
			if setParameterValues == 'SetParameterValues':
				print 'Get the SetParameterValues text!!'
			else:
				print "Do not Get the SetParameterValues text!!"
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("Do not Get the SetParameterValues text!!")
			self.Autoit_Detail_Message(40)
			# Get the message from Get_clipboard
			message_log_detail_dialog = self.Get_Clipboard()
			# Verify the boolean value
			if '<Value xsi:type="boolean">' + boolean + '</Value>' in message_log_detail_dialog:
				print 'The boolean was matched - SUCCESS'
			elif '<Value xsi:type="boolean">' + 'true' + '</Value>' in message_log_detail_dialog:
				print 'The boolean was matched - SUCCESS'
			elif '<Value xsi:type="boolean">' + 'false' + '</Value>' in message_log_detail_dialog:
				print 'The boolean was matched - SUCCESS'
			else:
				print "The boolean was not matched - FAIL"
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("The boolean was not matched - FAIL")
			time.sleep(1)
			now = time.strftime("%Y-%m-%d-%H_%M_%S",
								time.localtime(time.time()))
			heMS_SetParameterValues = heMS_SetParameterValues + '_' + now + '.txt'
			fp = open(heMS_SetParameterValues, "w")
			fp.write(message_log_detail_dialog)
			autoit.Sleep(1000)
			autoit.Send("!{F4}")
			print "Close the Detail page"
		# except:
		# 	raise Exception("The HeNS_Request_Message was not success - FAIL")

	def HeNS_Request_Message_Earfcn(self, earfcn, heMS_SetParameterValues):
		# try:
			pyautogui.click(1000, 30)
			self.System_Operation_Data()
			self.Click_Serial_Number()
			# Click the Message Log #
			selenium.click(
				"link="+config_element.get("system", "system_message_log"))
			# Refresh the list content
			for refresh in range(2):
				selenium.click(
					"xpath="+config_element.get("system", "system_refresh_button"))
			# Select the HeMS detail message
			print 'Type the serial number.'
			self.Click_CheckBox()
			selenium.type("id="+config_element.get("detail_message",
												   "search_askey_root"), config_element.get("detail_message", "input_askey_root"))
			time.sleep(3)
			selenium.click(
				"xpath="+config_element.get("detail_message", "search_button"))
			print "Select the key code"
			# Verify the SetParameterValues text can be get
			setParameterValues = selenium.get_text(
				"xpath="+config_element.get("detail_message", "parametervalues_text"))
			if setParameterValues == 'SetParameterValues':
				print 'Get the SetParameterValues text!!'
			else:
				print "Do not Get the SetParameterValues text!!"
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("Do not Get the SetParameterValues text!!")
			self.Autoit_Detail_Message(40)
			# Get the message from Get_clipboard
			message_log_detail_dialog = self.Get_Clipboard()
			print '<Value xsi:type="unsignedInt">'+earfcn+'</Value>'
			# Verify the earfcn value
			if '<Value xsi:type="unsignedInt">'+earfcn+'</Value>' in message_log_detail_dialog:
				print 'The earfcn was matched - SUCCESS'
			else:
				print "The earfcn was not matched - FAIL"
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("The earfcn was not matched - FAIL")

			time.sleep(1)
			now = time.strftime("%Y-%m-%d-%H_%M_%S",
								time.localtime(time.time()))
			heMS_SetParameterValues = heMS_SetParameterValues + '_' + now + '.txt'
			fp = open(heMS_SetParameterValues, "w")
			fp.write(message_log_detail_dialog)
			autoit.Sleep(1000)
			autoit.Send("!{F4}")
			print "Close the Detail page"
		# except:
		# 	raise Exception("The HeNS_Request_Message was not success - FAIL")

	def HeNS_Request_Message_PLMN(self, value, heMS_SetParameterValues):
		# try:
			pyautogui.click(1000, 30)
			self.System_Operation_Data()
			self.Click_Serial_Number()
			# Click the Message Log #
			selenium.click(
				"link="+config_element.get("system", "system_message_log"))
			# Refresh the list content
			for refresh in range(2):
				selenium.click(
					"xpath="+config_element.get("system", "system_refresh_button"))
			# Select the HeMS detail message
			print 'Type the serial number.'
			self.Click_CheckBox()
			selenium.type("id="+config_element.get("detail_message",
												   "search_askey_root"), config_element.get("detail_message", "input_askey_root"))
			time.sleep(3)
			selenium.click(
				"xpath="+config_element.get("detail_message", "search_button"))
			print "Select the key code"
			# Verify the SetParameterValues text can be get
			setParameterValues = selenium.get_text(
				"xpath="+config_element.get("detail_message", "parametervalues_text"))
			if setParameterValues == 'SetParameterValues':
				print 'Get the SetParameterValues text!!'
			else:
				print "Do not Get the SetParameterValues text!!"
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("Do not Get the SetParameterValues text!!")
			self.Autoit_Detail_Message(39)
			# Get the message from Get_clipboard
			message_log_detail_dialog = self.Get_Clipboard()

			if value == '0' or value == '1':
				print '<Value xsi:type="boolean">'+value+'</Value>'
				# Verify the value
				if '<Value xsi:type="boolean">'+value+'</Value>' in message_log_detail_dialog:
					print 'The boolean was matched - SUCCESS'
				else:
					print "The boolean was not matched - FAIL"
					android = Android()
					android.Copy_Trace_Folder()
					raise Exception("The boolean was not matched - FAIL")

			if value == config_setting.get("setting", "PLMN").split(" ")[0]+config_setting.get("setting", "PLMN").split(" ")[1]:
				print '<Value xsi:type="string">'+value+'</Value>'
				# Verify the value
				if '<Value xsi:type="string">'+value+'</Value>' in message_log_detail_dialog:
					print 'The string was matched - SUCCESS'
				else:
					print "The string was not matched - FAIL"
					android = Android()
					android.Copy_Trace_Folder()
					raise Exception("The string was not matched - FAIL")

			time.sleep(1)
			now = time.strftime("%Y-%m-%d-%H_%M_%S",
								time.localtime(time.time()))
			heMS_SetParameterValues = heMS_SetParameterValues + '_' + now + '.txt'
			fp = open(heMS_SetParameterValues, "w")
			fp.write(message_log_detail_dialog)
			autoit.Sleep(1000)
			autoit.Send("!{F4}")
			print "Close the Detail page"
		# except:
		# 	raise Exception("The HeNS_Request_Message was not success - FAIL")

	def HeNB_Response_Message(self, status, heNB_SetParameterValuesResponse):
		try:
			pyautogui.click(1000, 30)
			self.System_Operation_Data()
			self.Click_Serial_Number()
			# Click the Message Log #
			selenium.click(
				"link="+config_element.get("system", "system_message_log"))
			# Select the HeNB detail message
			print 'Type the serial number.'
			self.Click_CheckBox()
			time.sleep(3)
			selenium.click(
				"xpath="+config_element.get("detail_message", "search_button"))
			print "Select the key code"
			# Verify the SetParameterValuesResponse text can be get
			setParameterValuesResponse = selenium.get_text(
				"xpath="+config_element.get("detail_message", "parametervalues_text"))
			if setParameterValuesResponse == 'SetParameterValuesResponse':
				print 'Get the SetParameterValuesResponse text!!'
			else:
				print "Do not Get the SetParameterValues text!!"
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("Do not Get the SetParameterValues text!!")
			self.Autoit_Detail_Message(40)
			# Get the message from Get_clipboard
			message_log_detail_dialog = self.Get_Clipboard()
			# Verify the status value
			if '<Status>' + status + '</Status>' in message_log_detail_dialog:
				print 'The status was matched - SUCCESS'
			else:
				print "The status was not matched - FAIL"
				android = Android()
				android.Copy_Trace_Folder()
				raise Exception("The status was not matched - FAIL")
			time.sleep(1)
			now = time.strftime("%Y-%m-%d-%H_%M_%S",
								time.localtime(time.time()))
			heNB_SetParameterValuesResponse = heNB_SetParameterValuesResponse + '_' + now + '.txt'
			fp = open(heNB_SetParameterValuesResponse, "w")
			fp.write(message_log_detail_dialog)
			autoit.Sleep(1000)
			autoit.Send("!{F4}")
			print "Close the Detail page"
		except:
			raise Exception("The HeNB_Response_Message was not success - FAIL")

	def Click_CheckBox(self):
		selenium.type("id=" + config_element.get("detail_message", "serial_number_name"),
					  config_setting.get("setting", "serial_number"))
		for keyDown in range(18):
			pyautogui.keyDown('tab')
		for key_down in range(19):
			pyautogui.keyDown('down')

	def Autoit_Detail_Message(self, number):
		selenium.click(
			"xpath="+config_element.get("detail_message", "search_button"))
		pyautogui.click(1000, 30)
		self.Autoit_Tab_button(number, 100)
		autoit.Sleep(5000)
		autoit.Send("{ENTER}")
		print "Click the Detail page was finished"
		autoit.Sleep(2000)
		autoit.ControlClick(config_element.get("detail_message", "controlclick_title"),
							"", config_element.get("detail_message", "controlclick_nn"))
		pyautogui.click(600, 100)  # click the pop up windows by pyautogui
		print 'click the pop up windows'
		autoit.Sleep(2000)  # wait the controlclick the pop up window
		self.Autoit_Tab_button(8, 500)
		autoit.Sleep(2000)
		autoit.Send("^a")
		autoit.Sleep(2000)
		autoit.Send("^c")

	def Autoit_Tab_button(self, number, times):
		for tab in range(0, number):
			autoit.Send("{TAB}")
			autoit.Sleep(times)

if __name__ == "__main__":
	# ##################  test  ###################
	print 'Selenium Remote Control'
	# os.system("taskkill /F /IM iexplore.exe")
	# webcontrol = Webcontrol()
	# webcontrol.Initial()
	# webcontrol.Login()
	# webcontrol.Clear_All_Data(config_element.get("system", "system_message_queue"), config_element.get(
	# 	"delete_file", "delete_all_message_queue_button"), "Delete Message successfully!")
	# webcontrol.HeNS_Request_Message_Earfcn()
	# ##################  main menu  ###################
	# webcontrol = Webcontrol()
	# webcontrol.Initial()
	# webcontrol.Login()
	# ################  testcase: adminstate   ###################
	# boolean = config_setting.get("setting", "boolean")
	# status = config_setting.get("setting", "status")
	# heMS_SetParameterValues = config_element.get(
	# 	"location", "heMS_SetParameterValues")
	# heNB_SetParameterValuesResponse = config_element.get(
	# 	"location", "heNB_SetParameterValuesResponse")
	# webcontrol.Clear_All_Data(config_element.get("system", "system_message_queue"), config_element.get(
	# 	"delete_file", "delete_all_message_queue_button"), "Delete Message successfully!")
	# webcontrol.Clear_All_Data(config_element.get("system", "system_message_log"), config_element.get(
	# 	"delete_file", "delete_all_message_button"), "Delete Message Log Successfully!")
	# webcontrol.Parameter_List_Adminstate(boolean)
	# webcontrol.ACS_Initiate_Connection()
	# webcontrol.HeNS_Request_Message(boolean, heMS_SetParameterValues)
	# webcontrol.HeNB_Response_Message(status, heNB_SetParameterValuesResponse)
	# webcontrol.Security_Logout()
	# webcontrol.Exit()
	# ##################  system menu  ###################
	# webcontrol.System_Operation_Data()
	# webcontrol.System_Unknown_Cpe()
	# webcontrol.System_Cpe_Assignment()
	# webcontrol.System_Cpe_Upgrade()
	# ##################  security menu  ###################
	# webcontrol.Security_User()
	# webcontrol.Security_Change_Password()
	# webcontrol.Security_License()
	# ##################  event menu  ###################
	# webcontrol.Event_Message_Log()
	# webcontrol.Event_Inform_Log()
	# webcontrol.Event_Upgrade_Log()
	# webcontrol.Event_System_Log()
	# webcontrol.Event_Active_Alarm()
	# webcontrol.Event_History_Alarm()
	# webcontrol.Event_Alarm_Definition()
	# webcontrol.Event_Log_Auto_Backup()
	# ##################  file_db menu  ###################
	# webcontrol.File_DB_Configuration_File()
	# webcontrol.File_DB_Log_File()
	# webcontrol.File_DB_Image_File()
	# webcontrol.File_DB_Certificate()
	# webcontrol.File_DB_DB_Auto_Backup()
	# webcontrol.File_DB_DB_Utility()
	# webcontrol.File_DB_History_Log_File()
	# webcontrol.File_DB_File_Server_Config()
	# ##################  testing menu  ###################
	# webcontrol.Testing_Pd128_Test()
	# # webcontrol.Testing_Cpe_Parameter_Test()
	# ##################  help menu  ###################
	# # webcontrol.Help_Contact_Information()
	# # webcontrol.Help_Release_Information()
	# webcontrol.Help_Acs_Help()
	# webcontrol.Help_Acs_Url()
	# webcontrol.Help_Dashboard()
	# ##################  other menu  ###################
	# webcontrol.Dashboard_Refresh()
	# webcontrol.Security_Logout()
	# webcontrol.Exit()
