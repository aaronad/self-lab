#!/usr/bin/python
from time import strftime
import datetime,time

now = strftime('%Y-%m-%d %H:%M:%S')
hour = strftime('%H')
min = strftime('%M')
sec = strftime('%S')
#print now
print hour, min
i = 0
new_min = int(min) + 60
new_sec = int(sec)
time.sleep(1)
while new_sec != int(strftime('%S')) :
      print "new_sec = ",new_sec
      print "current time is ", strftime('%S')
      time.sleep(1)
      i += 1
      print "i = ", i

if new_sec == int(strftime('%S')) :
   print "the second Match"
else :
   print "the second Not Match"

if new_min > 60 :
   new_min = new_min - 60
   hour = int(hour) + 1
   print hour, min
else :
   print hour, min

