from dateutil.parser import parse

dates = [
    "2023/07/11 13:35",
    "07/11/2023 13:35",
    "2023-07-11 13:35:00",
    "11 jul 2023, 13:35",
    "11.07.2023 00:00"   # !!!!
]

for date in dates:
    print(parse(date))
