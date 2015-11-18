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
