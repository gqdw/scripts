# logstash-2016.05.01
import datetime
import requests
n = datetime.datetime.now()
print n.strftime('%Y.%m.%d')

delta = datetime.timedelta(days=-20)

str_d = (n+delta).strftime('%Y.%m.%d')
print str_d
# curl -XDELETE '10.24.154.234:9200/logstash-2016.04.10?pretty'
# 05.04
# 04.12
print('http://10.24.xx.xx:9200/logstash-%s?pretty' % str_d )
r = requests.delete('http://10.24.154.234:9200/logstash-%s?pretty' % str_d )
print r.text
# f = urllib2.urlopen('http://10.24.154.234:9200/logstash-%s?pretty' % str_d )

