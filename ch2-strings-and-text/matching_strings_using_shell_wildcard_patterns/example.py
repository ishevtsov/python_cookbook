# You want to match text using the same wildcard patterns as are commonly used when
# working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
result = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(result)

addresses = [
	'5412 N CLARK ST',
	'1060 W ADDISON ST',
	'1039 W GRANVILLE AVE',
	'2122 N CLARK ST',
	'4802 N BROADWAY',
]

from fnmatch import fnmatchcase
result = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(result)