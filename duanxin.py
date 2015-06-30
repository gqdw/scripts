#! /usr/bin/python
#coding:utf-8
import urllib2
import urllib
import sys
import xml.etree.ElementTree as etree
import logging
import datetime
import sqlite3
import redis

#reload(sys)
#sys.setdefaultencoding('utf8')

def sendm(mobile,content):
	url = 'http://.136.70:8888/sms.aspx'
	data = urllib.urlencode({
		"userid":'',
		"account":'',
		"password":'',
		"mobile":mobile,
		"content":content,
		"sendTime":"",
		"action":"send",
		"extno":""})
	req = urllib2.Request(url,data)
	res = urllib2.urlopen(req)
	return res.read()

#msg=u'你好上海驻云信息科技有限公司'
number=sys.argv[1]
msg=sys.argv[2]

tmsg = msg
#tmsg = msg.encode("UTF-8")
#sendm('18221278606',tmsg)
xm = sendm(number,tmsg)
#print xm
#print type(xm)
root = etree.fromstring(xm)
#root = tree.getroot()
for child in root:
        if child.tag == 'returnstatus':
                print (child.text)

#for arg in sys.argv:
#print sys.argv[1]



#
#<?xml version="1.0" encoding="utf-8" ?><returnsms>
# <returnstatus>Success</returnstatus>
# <message>ok</message>
# <remainpoint>9858</remainpoint>
# <taskID>7620631</taskID>
# <successCounts>1</successCounts></returnsms>

#add for log
dt = datetime.datetime.now()
str_t = dt.strftime('%Y-%m-%d %H:%M:%S %f')
logging.basicConfig(filename='/tmp/sms.log',level=logging.DEBUG)
logging.debug('date: %s',str_t)
logging.debug('number: %s',number)
logging.debug('msg: %s',msg)
# add for log total sms number in redis
# 2015-06-23
try:
	r = redis.Redis(host='localhost',port=6379,db=0)
	r.incr('totals')
	logging.debug('totals +1')
except:
	pass

#add for log into sqlite
#CREATE TABLE sms(id integer primary key autoincrement,
#time text,
#number text,
#msg text);
#conn = sqlite3.connect("/usr/local/zabbix-2.2.9/sms.db")
#cursor = conn.cursor()
#params = ( str_t,number,unicode(msg))
#cursor.execute("insert into sms('time','number','msg') values(? , ? ,? )",params)
#cursor.close()
#conn.commit()
#conn.close()
