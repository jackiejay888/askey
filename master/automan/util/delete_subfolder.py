'''
Created on 2017/03/07
@author: ron_chen
@title: Clear all folder data.(femtolog,log,pic,report,temp)

Add function on 2017/05/11
@author: Ron Chen
@title: New function(Delete_location_Subfolder)
'''


#-*- coding: utf-8 -*-

import os
import unittest
import shutil

class Delete_Subfolder(object):

	def Delete_Result_Subfolder(self):
		femtolog_foldername = "..\\..\\Result\\femtolog"
		log_foldername = "..\\..\\Result\\log"
		pic_foldername = "..\\..\\Result\\pic"
		report_foldername = "..\\..\\Result\\report"
		temp_foldername = "..\\..\\temp\\"
		xml_foldername = "..\\..\\Result\\xml"
		suit_xml_foldername = "..\\suit\\*.xml"

		command = "rmdir /s /q \"%s\""
		command = command % femtolog_foldername
		os.system(command)
		os.system("mkdir" + femtolog_foldername)
		print "The femtolog data was cancel."

		command = "rmdir /s /q \"%s\""
		command = command % log_foldername
		os.system(command)
		os.system("mkdir" + log_foldername)
		print "The log data was cancel."		

		command = "rmdir /s /q \"%s\""
		command = command % pic_foldername
		os.system(command)
		os.system("mkdir" + pic_foldername)
		print "The pic data was cancel."

		command = "rmdir /s /q \"%s\""
		command = command % report_foldername
		os.system(command)
		os.system("mkdir" + report_foldername)
		print "The report data was cancel."	

		command = "rmdir /s /q \"%s\""
		command = command % temp_foldername
		os.system(command)
		os.system("mkdir" + temp_foldername)
		print "The temp data was cancel."	
 
 		command = "rmdir /s /q \"%s\""
		command = command % xml_foldername
		os.system(command)
		os.system("mkdir" + xml_foldername)
		print "The xml data was cancel."	

		os.system("del " + suit_xml_foldername)
		print "The suit xml data was cancel."

	def Delete_Path_Subfolder(self,path):
 		command = "rmdir /s /q \"%s\""
		command = command % path
		os.system(command)
		os.system("mkdir" + path)
		print "The folder data was cancel."	

if __name__ == "__main__": 
	print 'The delete_subfolder.py code.'
	testcase = Delete_Subfolder()
	testcase.Delete_Result_Subfolder()
	# testcase.Delete_Path_Subfolder("..\\..\\Result\\femtolog")