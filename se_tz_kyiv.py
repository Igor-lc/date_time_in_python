from datetime import datetime as dt
from pytz import timezone

nsk_tz = timezone("Europe/Kyiv")

doc = open("post.txt", encoding='utf8')

date, content = doc.readlines()
date = dt.strptime(date.strip(), '%Y-%m-%d %H:%M:%S %Z%z')
print(date)

date = date.astimezone(nsk_tz)
print(date)

doc.close()
