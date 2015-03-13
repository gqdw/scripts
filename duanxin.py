#coding:utf-8
import urllib2
import urllib

def sendm(mobile,content):
	url = 'http://218.244.136.70:8888/sms.aspx'
#	url = 'http://218.244.136.70:8888/smsGBK.aspx'
	data = urllib.urlencode({
		"userid":'1180',
		"account":'shzybj',
		"password":'jgy123456',
		"mobile":mobile,
		"content":content,
		"sendTime":"",
		"action":"send",
		"extno":""})
	req = urllib2.Request(url,data)
	res = urllib2.urlopen(req)
	print res.read()	

#msg=u'你好上海驻云信息科技有限公司'
msg=u'''Trigger: {TRIGGER.NAME}
Trigger status: {TRIGGER.STATUS}
Trigger severity: {TRIGGER.SEVERITY}
Trigger URL: {TRIGGER.URL}
Item values:
3. {ITEM.NAME3} ({HOST.NAME3}:{ITEM.KEY3}): {ITEM.VALUE3}
'''
tmsg = msg.encode("UTF-8")
sendm('18221278606',tmsg)
