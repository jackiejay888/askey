import sys

class filesearch(object):

	def deleteLine(self):
		fn = 'TM500_command.txt'
		f = open(fn)
		output = []
		for line in f:
			if not "#" in line:
				output.append(line)
		f.close()
		f = open(fn, 'w')
		f.writelines(output)
		f.close()

if __name__ == "__main__":
	TC = filesearch()  # Run_Test  = class name
	TC.deleteLine()