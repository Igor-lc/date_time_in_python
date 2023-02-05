from calendar import Calendar

c = Calendar()
for year in c.yeardatescalendar(2016):
    for month in year:
        for week in month:
            for day in week:
                print(day)
            print('_' * 20, "End of the week", '_' * 20)
        print('_' * 20, "End of the month", '_' * 20)
