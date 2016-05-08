
# 10.168.105.153:9200
from datetime import datetime
from elasticsearch import Elasticsearch

# 10.168.105.153:9200
es = Elasticsearch(['http://10.168.105.153'])
# print es.info()
# print es.indices
# create index test-0508
es.indices.create(index='test-0508')
# es.indices.delete('test-0508')
ids = es.indices.get('*')
for i in ids:
	print i