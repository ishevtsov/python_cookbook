# You want to search for and replace a text pattern in a string.

text = 'yeah, but no, but yeah, but no, but yeah'
result = text.replace('yeah', 'yep')
print(text)
print(result)


# For more complicated patterns, use the sub() functions/methods in the re module.

# rewrite dates of the form “11/27/2012” as “2012-11-27.”
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

result = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)
print(result)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
result = datepat.sub(r'\3-\1-\2', text)
print(result)

from calendar import month_abbr

def change_date(m):
	mon_name = month_abbr[int(m.group(1))]
	return f'{m.group(2)} {mon_name} {m.group(3)}'

result = datepat.sub(change_date, text)
print(result)