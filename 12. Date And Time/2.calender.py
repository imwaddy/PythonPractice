#!/usr/bin/python3

import calendar
print()


cal = calendar.month(2022, 6)
print("Here is the calendar:")
print(cal)

print()


# Check first day of week
d = calendar.firstweekday()
print("First Week Day: ", d)

dict = {0: "Monday", 1: "Tuesday", 2:"Wendsday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
print("cal", dict[d])


# Python Date and Calendar: https://www.tutorialspoint.com/python3/python_date_time.htm

# Python datetime package: learn from here https://www.programiz.com/python-programming/datetime
