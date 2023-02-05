from datetime import datetime as dt
from pytils import dt as ru_dt


date = dt(2016, 1, 1)
print(ru_dt.ru_strftime("%d %B %Y (%A)", date, inflected=True, inflected_day=True, preposition=True))


end_date = dt(2016, 2, 14)
print(ru_dt.distance_of_time_in_words(date, to_time=end_date))
print(ru_dt.distance_of_time_in_words(end_date, to_time=date))
