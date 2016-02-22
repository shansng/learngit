# -*- ecoding:utf-8 -*-

#2016-2-20
print "hello China!"

import random

class RandomIterable:
	def __iter__(self):
		return self
	def next(self):
		if random.choice(["go", "go", "stop"]) == "stop"
			raise StopIteration # signals "the end"
		return 1
		