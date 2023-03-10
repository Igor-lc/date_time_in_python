'''255. НОМЕР ДНЯ И НЕДЕЛИ
Напишите программу, которая первым аргументом командной строки получает дату и время в формате "ГГГГ-ММ-ДД", а затем выводит номер дня и номер недели в году для этой даты. Учитывайте
украинский вариант, когда неделя начинается с понедельника. Данные нужно выводить в формате: «День: D, неделя: M» (смотрите ниже в примере использования).

Пример использования:
> python program.py "2020-01-01"
> День: 1, неделя: 0'''


import sys
from datetime import datetime as dt

date = dt.strptime(sys.argv[1], "%Y-%m-%d")

day = int(date.strftime("%j"))
week = int(date.strftime("%W"))

day_week_of_the_year = f"День: {day}, неделя: {week}"

print(day_week_of_the_year)
