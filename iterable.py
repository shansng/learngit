# -*- ecoding:utf-8 -*-

#2016-2-22
print "hello world!"

import random

class RandomIterable:
	def __iter__(self):
		return self
	def next(self):
		if random.choice(["go", "go", "stop"]) == "stop"
			raise StopIteration # signals "the end"
		return 1
		