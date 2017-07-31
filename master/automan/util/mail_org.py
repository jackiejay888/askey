'''
Created on 2017/02/08
@author: wayne_teng
'''
#-*- coding: utf-8 -*-

import os
import sys
import smtplib
import mimetypes
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart

SMTP_SERVER=smtplib.SMTP('smtp.gmail.com', 587)
EMAIL_SUBJECT='Report of AutoTesting'
FROM_USER='QA'
fp = open("..\..\ini\Mailing_List.txt", "r")
# fileName = r'.\output.xml'
fileName = r'..\\..\\temp\\result.zip'
User = 'femtocell.qa@gmail.com'
Password = 'Bsdusw188888888'

fileString = fp.read()
fp.close()
TO_USERS=fileString.split()

class Mail(object):
	def __init__(self):
		'''
		Constructor
		'''
		pass

	def Mysendmail(self,fromaddr,toaddrs,subject):
			COMMASPACE=','
			msg = MIMEMultipart()
 			msg['From'] = fromaddr
			msg['To'] = COMMASPACE.join(toaddrs)
			msg['Subject'] = subject      
			txt = MIMEText("The latest report of AutoTesting is attached, plz check for further details")
			msg.attach(txt)
			ctype, encoding = mimetypes.guess_type(fileName)
			if ctype is None or encoding is not None:
				ctype = 'application/octet-stream'
			maintype, subtype = ctype.split('/', 1)
			att = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype = subtype)

			File = fileName.split("\\")       
			att.add_header('Content-Disposition', 'attachment', filename = File[-1])   
			msg.attach(att)   
			server=smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.ehlo()
			server.login(User,Password)
			server.sendmail(fromaddr,toaddrs,msg.as_string())
			server.quit()

if __name__=='__main__':
		# ron_pass
		TC = Mail()
		TC.Mysendmail(FROM_USER, TO_USERS, EMAIL_SUBJECT)
		print 'Send Test result to everyone Successful'
