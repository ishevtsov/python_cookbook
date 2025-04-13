# You’re trying to match a block of text using a regular expression, but you need the match
# to span multiple lines.

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''

result = comment.findall(text1)
print(result)
result = comment.findall(text2)
print(result)

# add support for newlines.
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
result = comment.findall(text1)
print(result)
result = comment.findall(text2)
print(result)
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
result = comment.findall(text2)