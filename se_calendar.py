from calendar import Calendar, TextCalendar, HTMLCalendar, LocaleTextCalendar

c = Calendar()
print(list(c.monthdatescalendar(2023, 1)))
print(list(c.monthdayscalendar(2023, 1)))
print()

t = TextCalendar()
print(t.formatmonth(2023, 1))
t.prmonth(2023, 1)
t.pryear(2023)

t2 = LocaleTextCalendar(locale="ukr_ukr")
t2.pryear(2023)

h = HTMLCalendar()
# print(h.formatyearpage(2016, 2))
f = open("calendar.html", "w")
f.write(h.formatyearpage(2016).decode("utf8"))
f.close()
