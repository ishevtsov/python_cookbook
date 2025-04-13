# You want to match or search text for a specific pattern.

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match(r'\d+/\d+/\d+', text1):
	print('yes')
else:
	print('no')

if re.match(r'\d+/\d+/\d+', text2):
	print('yes')
else:
	print('no')

# If you’re going to perform a lot of matches, precompile
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text2):
	print('yes')
else:
	print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
result = datepat.findall(text)
print(result)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2015')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())