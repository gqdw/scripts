# coding: utf-8
import redis


# redis 的pipeline效率还是超高的，比普通的12s左右。pipeline的只要2.5s左右。10w的set对比。
r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    db=0)
for i in range(100000):
	r.set(i,i)

pipe = r.pipeline(transaction=False)
for i in range(100000):
	pipe.set(i,i)

pipe.execute()
