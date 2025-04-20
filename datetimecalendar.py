# Datetime and Calendar Modules in python:
# Today's date and time.
# Day,Month,Year, Hour, Minute,Second,Microsecond.
# Weekday,Day Name,Month Name,Year Name. 


import datetime as dt
import calendar as cal

print(dt.datetime.now())
print(dt.datetime.today())

print(dt.datetime.now().date())
print(dt.datetime.now().time())

print(dt.datetime.now().day)
print(dt.datetime.now().month)
print(dt.datetime.now().year)

print(dt.datetime.now().day)
print(dt.datetime.now().hour)

print(dt.datetime.now().minute)
print(dt.datetime.now().second)
print(dt.datetime.now().microsecond)

print(dt.datetime.now().strftime('%Y'))
print(dt.datetime.now().strftime('%m'))
print(dt.datetime.now().strftime('%d'))
print(dt.datetime.now().strftime('%Y-%m-%d--%H:%M:%S'))

print(dt.datetime.now().weekday())

day_no = dt.datetime.now().weekday()
print(cal.day_name[day_no])

m_no = dt.datetime.now().month
print(cal.month_name[m_no]) 