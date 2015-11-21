#!/usr/bin/env python
"""
for test class
"""


class Person:

	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay


if __name__ == '__main__':
	bob = Person('bob smith')
	sue = Person('sue jones', job='dev', pay=100000)
	print bob.name, bob.pay
	print sue.name, sue.pay
