#!/usr/bin/python
#coding:utf-8
import smtplib
from email.mime.text import MIMEText
class SendMail(object):
	def __init__(self,user,passwd):
		self.user = user
		self.passwd = passwd

	def sendmail(self,to,subject,message):
#		user='35992656@qq.com' 
#		passwd='xxx'
		#to='332305654@qq.com'
		
		msg=MIMEText(message.encode('utf-8'),'plain','utf-8')
		msg["Subject"] = 	subject	
		msg['From']	=	self.user
		msg['to']	=	to
		print msg.as_string()
		s=smtplib.SMTP('smtp.qq.com')
		s.login(self.user,self.passwd)
		s.sendmail(self.user,to,msg.as_string())
		s.close()
	

#sendmail('332305654@qq.com',"标题",u"信息")
if __name__ == '__main__':
	s = SendMail('332305654@qq.com' ,'jingru18')
	s.sendmail('332305654@qq.com',"标题",u"信息")
