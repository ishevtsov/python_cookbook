# You need to split a string into fields, but the delimiters (and spacing around them) aren’t
# consistent throughout the string.

import re

line = 'asdf fjdk; afed, fjek,asdf,    foo'

result = re.split(r'[;,\s]\s*', line)
print(result)