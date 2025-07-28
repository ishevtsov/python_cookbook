# You want to implement a custom iteration pattern that’s different than the usual built-
# in functions (e.g., range(), reversed(), etc.).

def frange(start, stop, increment):
	x = start
	while x < stop:
		yield x
		x += increment

for n in frange(0, 4, 0.5):
	print(n)