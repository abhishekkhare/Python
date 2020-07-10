import datetime as dt
import time as tm

print(tm.time())

dtNow = dt.datetime.fromtimestamp(tm.time())
print(dtNow)
dtCurrent = dt.datetime(2020,07,9,16,55,05,500572)
print(dtCurrent)
print(dtNow.year, dtNow.month, dtNow.day, dtNow.hour, dtNow.minute, dtNow.second)

delta = dt.timedelta(days = 100)
print(delta)

today = dt.date.today()
print(today)

print(today-delta)