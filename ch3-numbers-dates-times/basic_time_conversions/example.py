# arithmetic involving different units of time, use the date
# time module.
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds()/3600)

# to represent specific dates and times, create datetime instances and use the
# standard mathematical operations
from datetime import datetime

a = datetime(2025, 9, 23)
print(a + timedelta(days=10))

b = datetime(2025, 12, 21)
d = b - a
print(d.days)

now = datetime.today()
print(now)
print(now - timedelta(minutes=10))