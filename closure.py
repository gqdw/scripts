#!/usr/bin/env python
"""
closure function test
"""


def maker(N):
	def action(X):
		return X ** N
	return action

f = maker(3)
print f(3), f(4)
g = maker(2)
print g(3), g(4)



def func():
	x = 4
	action = (lambda n: x ** n)
	return action

x = func()
print x(2)

