# At what local time did your friend in Bangalore, India, have to show up to attend?
from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)