import re

str1=open('ps.txt').read()
str2=str1.split('\n')
#print str1
for i in str2:
#	print i
	m = re.search(r'rmi.port=(\d+)',i)
	if m != None:
		print m.group(1)
	
