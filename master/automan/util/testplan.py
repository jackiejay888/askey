'''
Created on 2017/02/08
@author: wayne_teng
'''
#-*- coding: utf-8 -*-

from client import client
from client_module import client_module
from android import AdbClient
from android import Android

# from mail import mail
import unittest
import subprocess,ConfigParser
import os,datetime,time
import HTMLTestRunner
import parameter

config = ConfigParser.ConfigParser()
config.read("..\\..\\ini\\Path.conf") #C:\automation\ini\Path.conf
config.read("..\\..\\ini\\Android_Path.conf") #C:\automation\ini\Android_Path.conf


# iperf_folder = config.get("setting", "iperf_folder")
# iperf_SIP = config.get("setting", "iperf_SIP")
# iperf_AIP = config.get("setting", "iperf_AIP")
# iperf_time = config.get("setting", "iperf_time")
# monitor_time = config.get("setting", "monitor_time")
# output_file = config.get("setting", "output_file")
# local_file = config.get("setting", "local_file")
# Server_host = config.get("setting", "Server_host")
# Server_user = config.get("setting", "Server_user")
# Server_passwd = config.get("setting", "Server_passwd")
# ftpremote_file = config.get("setting", "ftpremote_file")

# host = config.get("Femtocell", "host")
# user = config.get("Femtocell", "user")
# passwd = config.get("Femtocell", "passwd")

class Test_plan(unittest.TestCase,client_module,AdbClient,Android):
	global repeat_Times,ipsec_type_set
# ============== IPsec iperf ================
	def __init__(self, testname, ipsec_type_set=None, bandwidth=None):
		super(Test_plan, self).__init__(testname)
		self.ipsec_type_set = ipsec_type_set
		self.bandwidth = bandwidth

	def setUp(self):
		print "Start by Automated execution"

	def tearDown(self):
		print "Stop by Automated execution"

	def ipsec_128_128(self):
		repeat_Times="1"
		ipsec_type_set = "128_128"		
		self.clean_log()
		self.iperf_server_set(repeat_Times,ipsec_type_set)
		self.iperf_server_result(repeat_Times,ipsec_type_set)

	def ipsec_256_256(self):
		repeat_Times="1"
		ipsec_type_set = "256_256"		
		self.clean_log()
		self.iperf_server_set(repeat_Times,ipsec_type_set)
		self.iperf_server_result(repeat_Times,ipsec_type_set)

	def test_packet(self):	
		self.wireshark()

# ============== IPsec iperf ================
	def iperf_NA(self):
		adbClient = AdbClient()
		adbClient.service_iperf_start()
		adbClient.iperf_client()
		adbClient.get_file()
		adbClient.Check_iStatus(local_file)
		adbClient.move_file("UP_TCP_")

	def iperf_AN(self):
		android = Android()
		adbClient = AdbClient()
		adbClient.swiandroidh_iperf()
		iperf_command = "-s -i -5"
		android.mobile_device_connect()	
		android.service_iperf_start(iperf_command)
		android.iperf_log_clean()	
		adbClient.client_iperf_start()
		adbClient.adb_event("4")
		android.screen_shot_save(iperf_command)
		android.mobile_device_disconnect()
		adbClient.move_file("Down_androidP_")

	def iperf_NA_U52(self):
		adbClient = AdbClient()
		UP_UDP = "52m"
		adbClient.swiandroidh_iperf()
		adbClient.service_iperfU_start()
		adbClient.iperf_client_U(UP_UDP)
		adbClient.get_file()
		adbClient.Check_iStatus(local_file)
		adbClient.move_file("UP_UDP_")

	def iperf_NA_U39(self):
		adbClient = AdbClient()
		UP_UDP = "39m"
		adbClient.swiandroidh_iperf()
		adbClient.service_iperfU_start()
		adbClient.iperf_client_U(UP_UDP)
		adbClient.get_file()
		adbClient.Check_iStatus(local_file)
		adbClient.move_file("UP_UDP_")

	def iperf_NA_U26(self):
		adbClient = AdbClient()
		UP_UDP = "26m"
		adbClient.swiandroidh_iperf()
		adbClient.service_iperfU_start()
		adbClient.iperf_client_U(UP_UDP)
		adbClient.get_file()
		adbClient.Check_iStatus(local_file)
		adbClient.move_file("UP_UDP_")

	def iperf_NA_U13(self):
		adbClient = AdbClient()
		UP_UDP = "13m"
		adbClient.swiandroidh_iperf()
		adbClient.service_iperfU_start()
		adbClient.iperf_client_U(UP_UDP)
		adbClient.get_file()
		adbClient.Check_iStatus(local_file)
		adbClient.move_file("UP_UDP_")

	def iperf_AN_U160(self):
		android = Android()
		adbClient = AdbClient()
		DL_UDP = "160m"
		adbClient.swiandroidh_iperf()
		iperf_command = "-s -i -5 -u"
		android.mobile_device_connect()	
		android.service_iperf_start(iperf_command)
		android.iperf_log_clean()	
		adbClient.client_iperfU_start(DL_UDP)
		adbClient.adb_event("4")
		android.screen_shot_save(iperf_command)
		android.mobile_device_disconnect()
		adbClient.move_file("Down_UDP_")

	def iperf_AN_U120(self):
		android = Android()
		adbClient = AdbClient()
		DL_UDP = "120m"
		adbClient.swiandroidh_iperf()
		iperf_command = "-s -i -5 -u"
		android.mobile_device_connect()	
		android.service_iperf_start(iperf_command)
		android.iperf_log_clean()	
		adbClient.client_iperfU_start(DL_UDP)
		adbClient.adb_event("4")
		android.screen_shot_save(iperf_command)
		android.mobile_device_disconnect()
		adbClient.move_file("Down_UDP_")

	def iperf_AN_U80(self):
		android = Android()
		adbClient = AdbClient()
		DL_UDP = "80m"
		adbClient.swiandroidh_iperf()
		iperf_command = "-s -i -5 -u"
		android.mobile_device_connect()	
		android.service_iperf_start(iperf_command)
		android.iperf_log_clean()	
		adbClient.client_iperfU_start(DL_UDP)
		adbClient.adb_event("4")
		android.screen_shot_save(iperf_command)
		android.mobile_device_disconnect()
		adbClient.move_file("Down_UDP_")

	def iperf_AN_U40(self):
		android = Android()
		adbClient = AdbClient()
		DL_UDP = "40m"
		adbClient.swiandroidh_iperf()
		iperf_command = "-s -i -5 -u"
		android.mobile_device_connect()	
		android.service_iperf_start(iperf_command)
		android.iperf_log_clean()	
		adbClient.client_iperfU_start(DL_UDP)
		adbClient.adb_event("4")
		android.screen_shot_save(iperf_command)
		android.mobile_device_disconnect()
		adbClient.move_file("Down_UDP_")

	def FTP_NA_Download(self):
		android = Android()
		adbClient = AdbClient()
		filename = "1.pdf"
		filestart = "/1.pdf"
		fileend = "104857600 bytes"
		print "NB Server & android Client (ftp download)"		
		adbClient.swiandroidh_FtpClient()	
		adbClient.ftplog_renew()
		android.mobile_device_connect()
		adbClient.download_over()
		android.ftp_creataccount()
		android.ftp_connect()
		android.Verify_ftp_connect()
		android.folder_select("Download")
		android.ftp_download(filename)
		adbClient.Transfer_Status(filestart,fileend)		
		adbClient.getfile_command()
		adbClient.Check_FileStatus()
		adbClient.adb_event("4")
		android.screen_shot_save("FTP_Download")
		adbClient.FTP_Drate()
		android.mobile_device_disconnect()

	def FTP_NA_Upload(self):
		android = Android()
		adbClient = AdbClient()
		times = "1"
		filename = "2.pdf"
		filestart = "/2.pdf"
		fileend = "62914560 bytes"
		print "NB Server & android Client (ftp upload)"
		adbClient.swiandroidh_FtpClient()		
		adbClient.ftplog_renew()
		android.mobile_device_connect()
		adbClient.download_over()
		android.ftp_creataccount()
		android.ftp_connect()
		android.Verify_ftp_connect()
		android.folder_select("Upload")
		android.ftp_localfolder()
		adbClient.adb_event("123")
		adbClient.adb_event("123")	
		android.folder_select("Upload")
		android.ftp_upload(filename)	
		adbClient.Transfer_Status(filestart,fileend)
		adbClient.getfile_command()
		adbClient.Check_FileStatus()
		adbClient.adb_event("4")
		android.screen_shot_save("FTP_Upload")
		adbClient.FTP_Urate()
		android.mobile_device_disconnect()

	def FTP_NA_Download_S(self):
		android = Android()
		adbClient = AdbClient()
		print "NB Server & android Client (ftp download)"		
		adbClient.swiandroidh_FtpClient()	
		android.mobile_device_connect()
		adbClient.download_over()
		android.ftp_creataccount()
		for i in range(0,int(times)):
			adbClient.ftplog_renew()
			android.ftp_connect()
			android.Verify_ftp_connect()
			android.folder_select("Download")			
			android.ftp_download(filename)
			adbClient.del_file("vsftpd.log")			
			adbClient.Transfer_Status(filestart,fileend)
			adbClient.getfile_command()
			adbClient.Check_FileStatus()
			adbClient.adb_event("4")
			android.screen_shot_save("FTP_Download")
			adbClient.FTP_Drate()
			adbClient.adb_event("66")
			adbClient.adb_event("66")
			adbClient.adb_event("111")
			adbClient.adb_event("111")
			adbClient.adb_event("111")				
		android.mobile_device_disconnect()
		print "mobile_device_disconnect"

	def FTP_NA_Upload_S(self):
		android = Android()
		adbClient = AdbClient()
		print "NB Server & android Client (ftp upload)"
		adbClient.swiandroidh_FtpClient()
		android.mobile_device_connect()
		adbClient.download_over()
		android.ftp_creataccount()
		for i in range(0,int(times)):							
			adbClient.ftplog_renew()
			android.ftp_connect()
			android.Verify_ftp_connect()
			android.folder_select("Upload")
			android.ftp_localfolder()
			adbClient.adb_event("123")
			adbClient.adb_event("123")	
			android.folder_select("Upload")
			android.ftp_upload(filename)	
			adbClient.Transfer_Status(filestart,fileend)
			adbClient.getfile_command()
			adbClient.Check_FileStatus()
			adbClient.adb_event("4")
			android.screen_shot_save("FTP_Upload")
			adbClient.FTP_Urate()
			adbClient.adb_event("66")
			adbClient.adb_event("66")
			adbClient.adb_event("111")
			adbClient.adb_event("111")
			adbClient.adb_event("111")	
		android.mobile_device_disconnect()
	
	def bandwidth_type100(self):
		bandwidth = "100"		
 		TC.change_bandwidth(bandwidth)
		client.putconfigFile_femto()
		adbClient.Start_airplane()
		TC.restart_TeNB()
		time.sleep(50)
		adbClient.Stop_airplane()

	def bandwidth_type75(self):
		bandwidth = "75"		
 		TC.change_bandwidth(bandwidth)
		client.putconfigFile_femto()
		adbClient.Start_airplane()
		TC.restart_TeNB()
		time.sleep(50)
		adbClient.Stop_airplane()

	def bandwidth_type50(self):
		bandwidth = "50"		
 		TC.change_bandwidth(bandwidth)
		client.putconfigFile_femto()
		adbClient.Start_airplane()
		TC.restart_TeNB()
		time.sleep(50)
		adbClient.Stop_airplane()

	def bandwidth_type25(self):
		bandwidth = "25"	
 		TC.change_bandwidth(bandwidth)
		client.putconfigFile_femto()
		adbClient.Start_airplane()
		TC.restart_TeNB()
		time.sleep(50)
		adbClient.Stop_airplane()

	def ciphering_type100(self):
		bandwidth = "100"
		TC.change_bandwidth(bandwidth)
		TC.change_ciphering()		
		client.putconfigFile_femto()
		adbClient.Start_airplane()
		TC.restart_TeNB()
		time.sleep(50)
		adbClient.Stop_airplane()

	def ciphering_type75(self):
		bandwidth = "75"
		TC.change_bandwidth(bandwidth)
		TC.change_ciphering()		
		client.putconfigFile_femto()
		adbClient.Start_airplane()
		TC.restart_TeNB()
		time.sleep(50)
		adbClient.Stop_airplane()

	def ciphering_type50(self):
		bandwidth = "50"
		TC.change_bandwidth(bandwidth)
		TC.change_ciphering()		
		client.putconfigFile_femto()
		adbClient.Start_airplane()
		TC.restart_TeNB()
		time.sleep(50)
		adbClient.Stop_airplane()

	def ciphering_type25(self):
		bandwidth = "25"
		TC.change_bandwidth(bandwidth)
		TC.change_ciphering()		
		client.putconfigFile_femto()
		adbClient.Start_airplane()
		TC.restart_TeNB()
		time.sleep(50)
		adbClient.Stop_airplane()

if __name__ == "__main__": 
	# unittest.main()  
	# HTMLTestRunner.main()
	TC = client_module()
	client = client()
	adbClient = AdbClient()
	android = Android ()
#===================unittest and HTMLTest =================
	testunit=unittest.TestSuite()

	testunit.addTest(Test_plan("ipsec_256_256"))
	testunit.addTest(Test_plan("bandwidth_type100"))
	testunit.addTest(Test_plan("iperf_NA"))
	testunit.addTest(Test_plan("iperf_AN"))	
	testunit.addTest(Test_plan("iperf_NA_U52"))
	testunit.addTest(Test_plan("iperf_AN_U160"))
	testunit.addTest(Test_plan("FTP_NA_Download"))
	testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("bandwidth_type75"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))
	# testunit.addTest(Test_plan("iperf_NA_U39"))
	# testunit.addTest(Test_plan("iperf_AN_U120"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("bandwidth_type50"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))
	# testunit.addTest(Test_plan("iperf_NA_U26"))
	# testunit.addTest(Test_plan("iperf_AN_U80"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("bandwidth_type25"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))	
	# testunit.addTest(Test_plan("iperf_NA_U13"))
	# testunit.addTest(Test_plan("iperf_AN_U40"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# # # #==================== EIA1 "256_256"	
	# testunit.addTest(Test_plan("ipsec_256_256"))

	# testunit.addTest(Test_plan("bandwidth_type100"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))	
	# testunit.addTest(Test_plan("iperf_NA_U52"))
	# testunit.addTest(Test_plan("iperf_AN_U160"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("bandwidth_type75"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))
	# testunit.addTest(Test_plan("iperf_NA_U39"))
	# testunit.addTest(Test_plan("iperf_AN_U120"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("bandwidth_type50"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))
	# testunit.addTest(Test_plan("iperf_NA_U26"))
	# testunit.addTest(Test_plan("iperf_AN_U80"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("bandwidth_type25"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))	
	# testunit.addTest(Test_plan("iperf_NA_U13"))
	# testunit.addTest(Test_plan("iperf_AN_U40"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# # # # #==================== EIA2 "128_128"
	# testunit.addTest(Test_plan("ipsec_128_128"))

	# testunit.addTest(Test_plan("ciphering_type100"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))	
	# testunit.addTest(Test_plan("iperf_NA_U52"))
	# testunit.addTest(Test_plan("iperf_AN_U160"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("ciphering_type75"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))
	# testunit.addTest(Test_plan("iperf_NA_U39"))
	# testunit.addTest(Test_plan("iperf_AN_U120"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("ciphering_type50"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))
	# testunit.addTest(Test_plan("iperf_NA_U26"))
	# testunit.addTest(Test_plan("iperf_AN_U80"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("ciphering_type25"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))	
	# testunit.addTest(Test_plan("iperf_NA_U13"))
	# testunit.addTest(Test_plan("iperf_AN_U40"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	
	# # # #==================== EIA2 "256_256"
	
	# testunit.addTest(Test_plan("ipsec_256_256"))

	# testunit.addTest(Test_plan("ciphering_type100"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))	
	# testunit.addTest(Test_plan("iperf_NA_U52"))
	# testunit.addTest(Test_plan("iperf_AN_U160"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("ciphering_type75"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))
	# testunit.addTest(Test_plan("iperf_NA_U39"))
	# testunit.addTest(Test_plan("iperf_AN_U120"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("ciphering_type50"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))
	# testunit.addTest(Test_plan("iperf_NA_U26"))
	# testunit.addTest(Test_plan("iperf_AN_U80"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	

	# testunit.addTest(Test_plan("ciphering_type25"))
	# testunit.addTest(Test_plan("iperf_NA"))
	# testunit.addTest(Test_plan("iperf_AN"))	
	# testunit.addTest(Test_plan("iperf_NA_U13"))
	# testunit.addTest(Test_plan("iperf_AN_U40"))
	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# testunit.addTest(Test_plan("FTP_NA_Upload"))	
# #----------------------------------------------------
	now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
	fp=open("result_"+now+".html",'wb')
	runner=HTMLTestRunner.HTMLTestRunner(verbosity = 2,stream=fp,title='test result',description=u'result:')
	runner.run(testunit) 
	fp.close()
#===========================================================

	# TC = Test_plan()
	# # TC.iperf_server_set('1',"256_256")
	# TC.test_ipsec('5',"256_256")
	# TC.test_ipsec('3',"128_256")

	# repeat_Times="1"
	# ipsec_type_set = "128_128"	
	# testunit.addTest(Test_plan("ipsec"))
	# filename = "1.pdf"
	# filestart = "/1.pdf"
	# fileend = "104857600 bytes"

	# testunit.addTest(Test_plan("FTP_NA_Download"))
	# filename = "2.pdf"
	# filestart = "/2.pdf"
	# fileend = "62914560 bytes"
	# testunit.addTest(Test_plan("FTP_NA_Upload"))

	# adbClient.FTP_NA_Download("1.pdf","/1.pdf","104857600 bytes")
	# adbClient.FTP_NA_Upload("2.pdf","/2.pdf","62914560 bytes")
