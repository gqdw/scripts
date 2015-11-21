#!/usr/bin/env python
"""
for test class
"""


class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))

	def __str__(self):
		return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
	def giveRaise(self, percent, bonus=.10):
		Person.giveRaise(self, percent + bonus)
	
	def __init__(self, name, pay):
		Person.__init__(self, name, 'mgr', pay)

if __name__ == '__main__':
	bob = Person('bob smith')
	sue = Person('sue jones', job='dev', pay=100000)
#	print bob.name, bob.pay
#	print sue.name, sue.pay
#	print bob.lastName(), sue.lastName()
	tom = Manager('tom jones', 50000)
	tom.giveRaise(.10)
	print bob
	print sue
	sue.giveRaise(.10)
	print sue
#	print sue.pay
	print tom.lastName()
	print tom
