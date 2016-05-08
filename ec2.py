
# 10.168.105.153:9200
from datetime import datetime
from elasticsearch import Elasticsearch

# 10.168.105.153:9200
# print es.info()
# print es.indices
# create index test-0508
# es.indices.create(index='test-0508', ignore=400)
# es.indices.delete('test-0508')

def main():
	es = Elasticsearch(['http://10.168.105.153'])
	ids = es.indices.get('*')
	for k in ids:
		# print k, ids[k]
		print es.count(index=k)

if __name__ == '__main__':
	main()