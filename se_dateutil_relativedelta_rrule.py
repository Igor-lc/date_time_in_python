from datetime import datetime as dt
from datetime import timedelta
from dateutil import relativedelta
from dateutil import rrule

star_day = dt(2016, 1, 31)  # 2016 - высокосный, подставляем разные даты
print(star_day + timedelta(days=31))
print(star_day + relativedelta.relativedelta(months=1))
print(star_day + relativedelta.relativedelta(years=1))
print()

for date in rrule.rrule(freq=rrule.HOURLY, dtstart=star_day, count=3):
    print(date)
print()

end_date = dt(2017, 1, 1)
for date in rrule.rrule(freq=rrule.MONTHLY, dtstart=star_day, until=end_date):
    print(date)
