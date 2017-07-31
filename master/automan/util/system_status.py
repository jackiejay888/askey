'''
Created on 2017/05/27
@author: ron_chen
@title: The memory status report by machine.
'''

#-*- coding: utf-8 -*-

import os
cpu = os.popen("wmic cpu get loadpercentage").read()
memory = os.popen(
	"WMIc OS Get FreePhysicalMemory^,TotalVisibleMemorySize").read()
path = ".\\..\\..\\Result\\log\\System_Status.txt"


class System_Status(object):

	def cpu_percentage(self):
		print 'The cpu_percentage function.'
		str_cpu = "echo CPU Percentage = "+cpu.split()[1]+"% >> "+path+"\""
		os.system(str_cpu)
		print "CPU Percentage = "+cpu.split()[1]+"%"

	def free_memory(self):
		print 'The free_memory function.'
		free_memory = str(
			int(round(float(memory.split()[2])/float(memory.split()[3])*100)))
		str_free_memory = "echo Free Memory = "+free_memory+"% >> "+path+"\""
		print "Free Memory Percentage = "+free_memory+"%"
		os.system(str_free_memory)

	def used_memory(self):
		print 'The used_memory function.'
		used_memory = str(
			int(round((1-float(memory.split()[2])/float(memory.split()[3]))*100)))
		str_used_memory = "echo Used Memory = "+used_memory+"% >> "+path+"\""
		print "Used Memory Percentage = "+used_memory+"%"
		os.system(str_used_memory)

if __name__ == "__main__":
	print 'The Stauts function.'
	# ms = System_Status()
	# ms.cpu_percentage()
	# ms.free_memory()
	# ms.used_memory()
