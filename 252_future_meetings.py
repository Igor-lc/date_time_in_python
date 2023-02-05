'''252. БУДУЩИЕ ВСТРЕЧИ
В файле calendar.txt, который лежит рядом с программой, содержится информация о встречах. Каждая встреча записывается с новой строки и хранится
в формате ID,ДД.ММ.ГГГГ ЧЧ:ММ, где ID — это идентификатор встречи в календаре, а ДД.ММ.ГГГГ ЧЧ:ММ — дата и время встречи.
Напишите программу, которая анализирует данный файл и выводит ID встреч, которые произойдут в будущем (относительно текущего времени). Выведите
идентификаторы встреч через запятую с пробелом в порядке их следования в файле.'''

from datetime import datetime as dt
future_meetings = []
with open('calendar.txt', encoding='utf-8') as c:
    for a in c.readlines():
        u_id, d = a.split(',')
        d, t = d.split(' ')
        day, month, year = d.split('.')
        h, m = t.split(':')

        dtime = dt(int(year), int(month), int(day), int(h), int(m))
        if dt.now() < dtime:
            future_meetings.append(u_id)

future_meetings = ', '.join(future_meetings)
print(future_meetings)
