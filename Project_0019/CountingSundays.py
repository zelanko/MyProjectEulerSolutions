from datetime import datetime
from itertools import product

sundays = 0

# First day of month 1 Jan 1901 to 1 Dec 2000
for year, month in product(range(1901, 2001), range(1, 13)):
    dt = datetime(year, month, 1)
    if dt.weekday() == 6:
        sundays += 1

print(sundays)
    
