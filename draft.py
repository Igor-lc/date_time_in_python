import sys, calendar
from datetime import datetime as dt
date = dt.strptime(sys.argv[1], "%Y-%m-%d")


for week in calendar.monthcalendar(date.year, date.month):
    if week[0] != 0:
        break
print(dt(date.year, date.month, week[0]) == dt(date.year, date.month, date.day))
