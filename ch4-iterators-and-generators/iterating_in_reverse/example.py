# You want to iterate in reverse over a sequence.

a = [1, 2, 3, 4]
for x in reversed(a):
	print(x)

class Countdown:
	def __init__(self, start):
		self.start = start

	# Forward iterator
	def __iter__(self):
		n = self.start
		while n > 0:
			yield n
			n -= 1

	# Reverse iterator
	def __reversed__(self):
		n = 1
		while n <= self.start:
			yield n
			n += 1

fc = Countdown(5)
for c in fc:
	print(c, end=' ')
print()

rc = Countdown(5)
for c in reversed(rc):
	print(c, end=' ')
print()