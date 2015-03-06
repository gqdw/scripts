#!/usr/bin/python
#coding:utf-8
import smtplib
from email.mime.text import MIMEText
def sendmail(to,subject,message):
	user='35992656@qq.com' 
	passwd='xxx'
	#to='332305654@qq.com'
	
	msg=MIMEText(message)
	
	msg["Subject"] = 	subject	
	msg['From']	=	user
	msg['to']	=	to
	print msg.as_string()
	s=smtplib.SMTP('smtp.qq.com')
	s.login(user,passwd)
	s.sendmail(user,to,msg.as_string())
	s.close()


sendmail('332305654@qq.com',"标题","信息")

