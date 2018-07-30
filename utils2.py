from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
import numpy as np

# import pandas as pd

# def addDay(date,number_of_days):
#     return date + timedelta(days=number_of_days)

# def diff_month(d1, d2):
#     return (d1.year - d2.year) * 12 + d1.month - d2.month

# calendar_size = 1460;
# calendar_size = (final_date - start_date).days

# daterange = pd.date_range(start_date, final_date)

start_date = date(2017,1,1);
final_date = date.today() + relativedelta(months=2);

# def datarange(start_date, final_date):
# 	for n in range((final_date-start_date).days+1):
# 		yield start_date + timedelta(n)

# PayDayTable = {date:np.zeros(5) for date in datarange(start_date, final_date)}


# print(PayDayTable)
# print(PayDayTable[date.today()])
# print(PayDayTable[date.today()][0])
# print(PayDayTable[date.today()][1:3])

# for item in PayDayTable.items():
# 	print(item[0])
# 	print(item[1])

# print(PayDayTable[date.today()])


# def datarange_months(start_date, final_date):
# 	for n in range((final_date-start_date).months+1):
# 		yield start_date + timedelta(n)

# PayDayTable = {date:np.zeros(5) for date in datarange_months(start_date, final_date)}

from datetime import datetime
from dateutil.rrule import rrule, DAILY, MONTHLY

dates = [dt for dt in rrule(DAILY, dtstart=start_date, until=final_date)]

# print(dates)

PayDayTable = {dt:np.zeros(5) for dt in rrule(MONTHLY, dtstart=start_date, until=final_date)}
PayDayTable 
# print(PayDayTable)

# print(date.today())

# today = date.today()
# # print(today)

# x = datetime(today.year, today.month, 1)
# print(x)

print(PayDayTable[])

# for item in PayDayTable.items():
# 	# print(item[0])
# 	if x == item[0]:
# 		print(item[0])

	# today.month == item[0].month 
	# print(PayDayTable[item[0]])


# a = np.zeros(5)
# b = np.zeros(5)

# a[2] = 1
# b[2] = 2
# b[3] = 3

# print(a)
# print(b)

# c = a+b
# print(c)