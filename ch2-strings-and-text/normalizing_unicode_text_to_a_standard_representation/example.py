# You’re working with Unicode strings, but need to make sure that all of the strings have
#the same underlying representation.

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s2 == s1)
print(len(s1))
print(len(s2))

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t2 == t1)

print(ascii(t1))