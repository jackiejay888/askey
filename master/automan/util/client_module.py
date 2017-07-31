'''
Created on 2017/02/08
@author: wayne_teng
'''
#-*- coding: utf-8 -*-

from client import client
import unittest
import os,datetime,time
import HTMLTestRunner

class client_module(client):
# 	def __init__(self):
# 		'''
# 		Constructor
# 		'''
# 		pass

	def iperf_server_set(self,repeat_Times,ipsec_type_set):
		# repeat_Times=1
		# ipsec_type_set="256_256
		self.clean_log()
		self.run_server_ipsec(ipsec_type_set)
		self.run_ipsec_times(int(repeat_Times),ipsec_type_set)
		self.CheckStatus(ipsec_type_set)

	def iperf_server_result(self,repeat_Times,ipsec_type_set):
		print ipsec_type_set
		if ipsec_type_set == "128_0":
			self.count_result(int(repeat_Times),"count_"+ipsec_type_set,"IKE proposal: AES_CBC_128, ESP: NULL/HMAC_SHA1_96") 
		elif ipsec_type_set == "128_128":
			self.count_result(int(repeat_Times),"count_"+ipsec_type_set,"IKE proposal: AES_CBC_128, ESP: AES_CBC_128/HMAC_SHA1_96") 
		elif ipsec_type_set == "128_256":
			self.count_result(int(repeat_Times),"count_"+ipsec_type_set,"IKE proposal: AES_CBC_128, ESP: AES_CBC_256/HMAC_SHA1_96") 			
		elif ipsec_type_set == "256_0":
			self.count_result(int(repeat_Times),"count_"+ipsec_type_set,"IKE proposal: AES_CBC_256, ESP: NULL/HMAC_SHA1_96") 				
		elif ipsec_type_set == "256_256":
			self.count_result(int(repeat_Times),"count_"+ipsec_type_set,"IKE proposal: AES_CBC_256, ESP: AES_CBC_256/HMAC_SHA1_96") 			
		elif ipsec_type_set == "256_128":
			self.count_result(int(repeat_Times),"count_"+ipsec_type_set,"IKE proposal: AES_CBC_256, ESP: AES_CBC_128/HMAC_SHA1_96") 		
		else:
			raise Exception,"Can not caeate a ipesc tunnel"

	def change_bandwidth(self,bandwidth):
		# os.system("copy c:\\remote\\ini\\configFile c:\\remote\\configFile /Y")
		os.system("copy ..\\..\\automation\\ini\\configFile ..\\..\\automation\\configFile /Y")
		
		self.replace_change("configFile","LTE_DL_BANDWIDTH 100","LTE_DL_BANDWIDTH "+bandwidth)
		self.replace_change("configFile","LTE_UL_BANDWIDTH 100","LTE_UL_BANDWIDTH "+bandwidth)
		self.replace_change("configFile","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n100","LTE_OAM_NEIGHBOUR_DL_BANDWIDTH_SIB3 n"+bandwidth)

	def change_ciphering(self):
		self.replace_change("configFile",'LTE_CIPHERING_ALGO_LIST "128-EEA1"','LTE_CIPHERING_ALGO_LIST "128-EEA2"')
		self.replace_change("configFile",'LTE_INTEGRITY_ALGO_LIST "128-EIA1"','LTE_INTEGRITY_ALGO_LIST "128-EIA2"')

	def restart_TeNB(self): # put file to Ubuntu
		self.exec_command("/sbin/reboot")
		time.sleep(25)
		self.exec_command("-m ipsec.txt")	
		self.exec_command("-m start.txt")
		# time.sleep(200)	




if __name__ == "__main__": 
	# unittest.main()  
	# HTMLTestRunner.main()

	# testunit=unittest.TestSuite()
	# repeat_Times=1
	# ipsec_type_set="256_256"
	# testunit.addTest(client_module("iperf_server_set"))
	# # testunit.addTest(client_module("test_ipsec_128_128"))

	# now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
	# fp=open("result"+now+".html",'wb')
	# #runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'result:')
	# runner=HTMLTestRunner.HTMLTestRunner(verbosity = 2,stream=fp,title='test result',description=u'result:')

	# runner.run(testunit) 
	# fp.close()
	TC = client_module()
	# TC.restart_TeNB()
	TC.iperf_server_set('1',"256_256")
	TC.iperf_server_result('1',"256_256")
	# TC.change_bandwidth("22")
	# TC.change_bandwidth("120")
	# TC.change_bandwidth("75")	
