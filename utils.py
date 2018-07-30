
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY, MONTHLY
import numpy as np

start_date = date(2017,1,1);
final_date = date.today() + relativedelta(months=2);


class PayDay(object):

    def __init__(self, start_date, final_date): 
        self.start_date = start_date
        self.final_date = final_date
        self.payDay_Table = {day:np.zeros(7) for day in rrule(DAILY, dtstart=start_date, until=final_date)}

    def __str__(self):
        string = ''
        for payDay in self.payDay_Table.items():
            string += ('Day: {}, \
                        Q1: {}, \
                        Q2: {}, \
                        Q3: {}, \
                        Q4: {}, \
                        Q5: {}, \
                        Gain: {}\n'.format(payDay[0], 
                                         payDay[1][0], 
                                         payDay[1][1], 
                                         payDay[1][2], 
                                         payDay[1][3], 
                                         payDay[1][4], 
                                         payDay[1][5]))
        return string

    def get(self):
        value = []
        for payDay in self.payDay_Table.items():
            value.append([payDay[0], 
                           payDay[1][0],  
                           payDay[1][1],  
                           payDay[1][2],  
                           payDay[1][3], 
                           payDay[1][4], 
                           payDay[1][5]])
        return value

    def update(self, reservation):
        duration = (reservation.checkout - reservation.checkin).days
        payDay =  reservation.value/duration
        for day in rrule(DAILY, dtstart=reservation.checkin, until=reservation.checkout - relativedelta(days=1)):
            self.payDay_Table[day][int(reservation.room)-1] += payDay
            self.payDay_Table[day][5] += payDay

class PayMonth(object):

    def __init__(self,payDay):
        self.payMonth_Table = {month:np.zeros(7) for month in rrule(MONTHLY, dtstart=payDay.start_date, until=payDay.final_date)}
        for item in payDay.payDay_Table.items():
            auxDate = datetime(item[0].year, item[0].month, 1)
            self.payMonth_Table[auxDate] += payDay.payDay_Table[item[0]]

    def __str__(self):
        string = ''
        for payMonth in self.payMonth_Table.items():
            string += ('Month: {}, \
                        Q1: {}, \
                        Q2: {}, \
                        Q3: {}, \
                        Q4: {}, \
                        Q5: {}, \
                        Gain: {}, \
                        Spend: {}\n'.format(payMonth[0], 
                                         payMonth[1][0], 
                                         payMonth[1][1], 
                                         payMonth[1][2], 
                                         payMonth[1][3], 
                                         payMonth[1][4], 
                                         payMonth[1][5], 
                                         payMonth[1][6]))
        return string

    def get(self):
        value = []
        for payMonth in self.payMonth_Table.items():
            value.append([payMonth[0], 
                           payMonth[1][0],  
                           payMonth[1][1],  
                           payMonth[1][2],  
                           payMonth[1][3], 
                           payMonth[1][4], 
                           payMonth[1][5], 
                           payMonth[1][6]])
        return value

    def update(self, spend):
        auxDate = datetime(spend.date.year, spend.date.month, 1)
        self.payMonth_Table[auxDate][6] +=  spend.value

