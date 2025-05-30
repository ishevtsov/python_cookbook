mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# all positive numbers
plist = [n for n in mylist if n > 0]
print(plist)

# all negative numbers
plist = [n for n in mylist if n < 0]
print(plist)

# use generator expression
plist = (n for n in mylist if n > 0)
print(list(plist))


values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

ivals = list(filter(is_int, values))
print(ivals)

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

# Compressing example
from itertools import compress

addresses = [
	'5412 N CLARK',
	'5148 N CLARK',
	'5800 E 58TH',
	'2122 N CLARK'
	'5645 N RAVENSWOOD',
	'1060 W ADDISON',
	'4801 N BROADWAY',
	'1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print(more5)

result = list(compress(addresses, more5))
print(result)