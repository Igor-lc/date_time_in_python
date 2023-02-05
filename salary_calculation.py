'''251. МАКСИМАЛЬНОЕ ОПОЗДАНИЕ
В прошлом задании вы находили список опоздавших сотрудников, теперь нужно найти сотрудника с максимальным опозданием.
Напишите программу, которая анализирует файл из прошлого задания и выводит идентификатор, а также время прихода сотрудника, который опоздал больше всего'''

from datetime import time
with open('visits.txt', encoding='utf-8') as visits:
    t = time(9, 0, 0)
    id_ = ''
    for i in visits.readlines():
        u_id, v_t = i.split(',')
        h, m, s = v_t.split(':')
        late_t = time(int(h), int(m), int(s))

        if t < late_t:
            t = late_t
            id_ = f'{u_id},{t}'

print(id_)
