class StepperIndex:

	def __getitem__(self,i):
		return self.data[i]

x = StepperIndex()
x.data = 'spam'

# item in x call __getitem__
# for loops call __getitem__
for item in x:
	print item,


class Squares:
	def __init__(self, start, stop):
		self.value = start -1 
		self.stop = stop

	def __iter__(self):
		return self

	def next(self):
		if self.value == self.stop:
			raise StopIteration
		self.value += 1
		return self.value ** 2

# for calls iter, __iter__
for i in Squares(1, 5):
# each iteration class next()
	print i,
