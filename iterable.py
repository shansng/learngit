# -*- ecoding:utf-8 -*-

<<<<<<< HEAD
#2016-2-22
print "hello world!"
=======
#2016-2-22
print "hello world!"
>>>>>>> feature1

import random

class RandomIterable:
	def __iter__(self):
		return self
	def next(self):
		if random.choice(["go", "go", "stop"]) == "stop"
			raise StopIteration # signals "the end"
		return 1
		