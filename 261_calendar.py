'''261. ПЕРВЫЙ ПОНЕДЕЛЬНИК МЕСЯЦА. Каждый день в 9 часов утра на сервере запускается скрипт, задача которого сформировать и отправить отчет за прошлый месяц.
Отчет за прошлый месяц необходимо отправлять в первый понедельник текущего месяца. Напишите программу, которая принимает дату, а затем выводит True если это первый понедельник.'''

import sys, calendar
from datetime import datetime as dt, timedelta
date = dt.strptime(sys.argv[1], "%Y-%m-%d")

# version 1
for week in calendar.monthcalendar(date.year, date.month):
    if week[0] != 0:
        break
print(dt(date.year, date.month, week[0]) == dt(date.year, date.month, date.day))


# version 2
def is_first_monday_2(date):
    first_monday_day = [week[0] for week in calendar.monthcalendar(date.year, date.month) if week[0] != 0][0]
    return dt(date.year, date.month, first_monday_day) == dt(date.year, date.month, date.day)
print(is_first_monday_2(date))


# version 3
def find_first_monday(date):
    d = dt(date.year, date.month, 7)  # С 1 до 7 числа есть один понедельник. Получаем 7 число переданного месяца.
    offset = -d.weekday()  # Смотрим какой это день недели (0 - пн, 6 - вс).
    # Пример: в январе 2022 года первый понедельник был 3 января.
    #           Сперва мы получили 7 января и вычислили, что это пятница (4 день недели если считать с нуля).
    #           Далее мы из 7 вычитаем 4 и получаем 3. 3 - это дата первого понедельника.
    first_monday = d + timedelta(offset)
    return dt(date.year, date.month, date.day) == first_monday
print(find_first_monday(date))
