
# 10.168.105.153:9200
from datetime import datetime
from elasticsearch import Elasticsearch

# 10.168.105.153:9200
es = Elasticsearch(['http://10.168.105.153'])
print es.info()