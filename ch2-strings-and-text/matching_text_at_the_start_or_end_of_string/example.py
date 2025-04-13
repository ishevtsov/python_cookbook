# You need to check the start or end of a string for specific text patterns, such as filename
# extensions, URL schemes, and so on.

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

import os

filenames = os.listdir('.')
print(filenames)

files = [name for name in filenames if name.endswith(('.c', '.h'))]
print(files)

from urllib.request import urlopen

def read_data(name):
	if name.startswith(('http:', 'hhtps:', 'ftp:')):
		return urlopen(name).read()
	else:
		with open(name) as f:
			return f.read()

choices = ['http:', 'ftp:']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))
