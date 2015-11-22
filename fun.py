#! /usr/bin/env python
"""
function test
"""


def intersect(seq1, seq2):
	res = []
	for x in seq1:
		if x in seq2:
			res.append(x)
	return res

s1 = 'spam'
s2 = 'scam'
print intersect(s1, s2)


class Third():
	def __init__(self, value):
		self.data = value
	

	def __add__(self, other):
		return self.data + other

t1 = Third(11)
print (t1 + 9)


class Inder():
	def __getitem__(self, index):
		return index*2

x = Inder()
print x[2], x[3]
