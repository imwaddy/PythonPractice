#!/usr/bin/python3

print()

import time
from datetime import datetime

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
print()

# Convert ticks into date
your_date = datetime.fromtimestamp(ticks)
print("RECONVERTED DATE FROM TICKS : ", your_date)
print()

# Time Tuple / Time Struct
t = time.localtime()
print("Time Struct: ", t)
print()

# passing seconds localtime function
t = time.localtime(237)
print("Time Struct: ", t)
print()

# passing ticks localtime function
localtime = time.localtime(time.time())
print("Local current time :", localtime)
print()

# formatted time
localtime = time.asctime(time.localtime(time.time()))
print("Local current time (Formatted) :", localtime)
print()

# timezone attribute - Attribute time.timezone is the offset in seconds of the local time zone (without DST) 
# from UTC (>0 in the Americas; <=0 in most of Europe, Asia, Africa).
tz = time.timezone
print ("Time Zone :", tz)
print()

# tzname attribute - Attribute time.tzname is a pair of locale-dependent strings, which are the names
#  of the local time zone without and with DST, respectively.
tzName = time.tzname
print ("Time Zone Name :", tzName)
print()