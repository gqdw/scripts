# coding: utf-8


# python 迭代器版本
for line in open('duanxin.py'):
	print line

for line in open('duanxin.py').readlines():
	print line

L = [1, 2, 3]
i = iter(L)
print i.next(), i.next(), next(i)