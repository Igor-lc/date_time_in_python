'''ПАРСИМ ДАТУ
Напишите программу, которая из первого аргумента командной строки принимает дату и время в формате "ГГГГММДДЧЧММСС", а затем выводит эту же дату в формате "ДД.ММ.ГГ ЧЧ:ММ".

Пример использования:
> python program.py 20190418133454
> 18.04.19 13:34'''

from datetime import datetime
import sys
date_ = sys.argv[1]

strp = datetime.strptime(date_, "%Y%m%d%H%M%S")
strf = datetime.strftime(strp, "%d.%m.%y %H:%M")

print(strp)
print()
print(strf)
