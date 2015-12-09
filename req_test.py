import requests

if __name__ == "__main__" :
	url1 = 'http://baidu.com'
	r = requests.get(url1)
	print r.headers
	print r.headers['content-type']
