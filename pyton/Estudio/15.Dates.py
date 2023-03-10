### Dates ###

from datetime import datetime

now = datetime.now()

timestamp = now.timestamp()

year_2023 = datetime(2023,1,1)

def print_date(date):
    print(now.day)
    print(now.year)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(date.timestamp())


#print_date(now)

from datetime import time

curren_time = time(21,6,30)

print(curren_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

#current_date.year = current_date.year + 1

print(current_date.year)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)

end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)