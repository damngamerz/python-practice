#Current System Time
import time;

ticks =time.time()

print("Number of ticks since epoch",ticks)

print(time.localtime())

#Getting local Time 

localtime =time.localtime(time.time())

print("Local current time:",localtime)

#Getting formatted time 
localtime = time.asctime(time.localtime(time.time()))

print("Formatted Time:",localtime)

#Getting calendar for a month

import calendar

cal=calendar.month(2017,1)
print ("Here is the calendar:")
print(cal)
