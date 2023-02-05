'''ЕЖЕМЕСЯЧНЫЕ ПЛАТЕЖИ
Напишите программу, которая принимает из командной строки два параметра: дату первого платежа в формате «ГГГГ-ММ-ДД» и количество платежей, а затем выводит график ежемесячных платежей
начиная с переданной даты.  Каждую дату графика нужно выводить в формате «ДД.ММ.ГГ», а сами даты следует разделить запятой и пробелом.

Пример использования
> python program.py "2020-04-07" 3
> 07.04.20, 07.05.20, 07.06.20 '''


from sys import argv
from datetime import datetime as dt
from dateutil import relativedelta
date = dt.strptime(argv[1], "%Y-%m-%d")

payments = []
for m in range(int(argv[2])):
    nd = date + relativedelta.relativedelta(months=m)
    payments.append(dt.strftime(nd, '%d.%m.%y'))

print(', '.join(payments))
