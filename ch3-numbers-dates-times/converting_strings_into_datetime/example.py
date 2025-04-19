# data in string format, but you want to convert those
# strings into datetime objects
from datetime import datetime

text = '2024-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)