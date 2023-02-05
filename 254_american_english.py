'''254. АМЕРИКАНСКИЙ АНГЛИЙСКИЙ
В американском английском дату часто записывают в следующем формате «January 1, 2020». Напишите программу, которая преобразовывает дату из американского формата в украинский — «1 января 2020».

Пример использования:
> python program.py "January 1, 2020"
> 1 января 2020'''

import sys
from datetime import datetime
american_date = sys.argv[1]

ukrainian_months = [None, 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

date = datetime.strptime(american_date, "%B %d, %Y")
print(date)

date = f"{date.day} {ukrainian_months[date.month]} {date.year}"
print(date)
