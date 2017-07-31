import os
import sys

class Replace(object):

	def __init__(self):
		'''
		Constructor
		'''
		pass
	def Set_Parameter(self):#, old_word, new_word
		infile = "..\util\mail.py"
		f1 = open(infile, 'r').read()
		old_word = "The latest report of AutoTesting is attached, plz check for further details"
		new_word = old_word +"Download link "+sys.argv[1]
		f2 = open(infile, 'w')
		m = f1.replace(old_word, new_word)
		f2.write(m)

if __name__ == "__main__":
	TC = Replace()  # Run_Test  = class name
	TC.Set_Parameter()