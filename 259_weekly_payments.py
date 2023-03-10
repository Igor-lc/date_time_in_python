'''ЕЖЕНЕДЕЛЬНЫЕ ПЛАТЕЖИ
Напишите программу, которая принимает из командной строки два параметра: дату первого платежа в формате «ГГГГ-ММ-ДД» и количество платежей, а затем выводит график еженедельных платежей начиная с переданной даты.

Каждую дату графика нужно выводить в формате «ДД.ММ.ГГ», а сами даты следует разделить запятой и пробелом.

Пример использования
> python program.py "2020-04-07" 5
> 07.04.20, 14.04.20, 21.04.20, 28.04.20, 05.05.20'''


from datetime import datetime as dt, timedelta
import sys

date = dt.strptime(sys.argv[1], "%Y-%m-%d")
count_w = int(sys.argv[2])

pd = []
for i in range(count_w):
    n_date = date + timedelta(days=i*7)
    pd.append(dt.strftime(n_date, '%d.%m.%y'))

print(', '.join(pd))
