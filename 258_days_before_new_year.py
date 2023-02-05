'''258. ДНЕЙ ДО НОВОГО ГОДА
Напишите программу, которая принимает из аргументов командной строки три параметра: год, месяц и день, а затем вычисляет число полных дней до ближайшего к этой дате нового года.

Пример использования:
> python program.py 2020 4 14
> 261'''



from datetime import datetime as dt
import sys

y, m, d = sys.argv[1:]

new_year = dt(int(y) + 1, 1, 1)
date = dt(int(y), int(m), int(d))

print((new_year - date).days - 1)
