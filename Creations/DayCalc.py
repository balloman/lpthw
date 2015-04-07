import math
#Month Value Table
jan = 0
feb = 3
mar = 3
apr = 6
may = 1
jun = 4
jul = 6
aug = 2
sep = 5
oc = 0
nov = 3
dec = 5
#Century Value Table
six = 0
seven = 5
eight = 3
nine = 1
now = 0
#Day Table
Sunday = 1
Monday = 2
Tuesday = 3
Wednesday = 4
Thursday = 5
Friday = 6
Saturday = 7
Saturday2 = 0
#Actual Program
print "I have found a way to calculate the day that you were born!"
print "I just need you birthday."
print "What month were you born in. Please input it in number form from 1-12"
month = int(raw_input())
if month == 1:
    nmonth = jan
elif month == 2:
    nmonth = feb
elif month == 3:
    nmonth = mar
elif month == 4:
    nmonth = apr
elif month == 5:
    nmonth = may
elif month == 6:
    nmonth = jun
elif month == 7:
    nmonth = jul
elif month == 8:
    nmonth = aug
elif month == 9:
    nmonth = sep
elif month == 10:
    nmonth = oc
elif month == 11:
    nmonth = nov
elif month == 12:
    nmonth = dec
print "What day(date) were you born on?"
day = int(raw_input())
equation = day + nmonth
if equation > 6:
    divisor = equation / 7
    math.trunc(divisor)
    divisor = divisor * 7
    svalue = equation - divisor
elif equation <= 6:
    svalue = equation
print "What is the last 2 digits of the year were you born in?"
year = int(raw_input())
decider = year
divisor2 = year / 28
math.trunc(divisor2)
divisor2 = divisor2 * 28
year = year - divisor2
#Other Variable
oyear = year / 4
math.trunc(oyear)
nvalue = year + oyear
print "What century were you born in? 21,20,19,18, or 17"
century = int(raw_input())
if century == 21:
    century = now
    nvalue + century
elif century == 20:
    century = nine
    nvalue + century
elif century == 19:
    century = eight
    nvalue + century
elif century == 18:
    century = seven
    nvalue + century
elif century == 17:
    century = six
    nvalue + century
if month < 3:
    nvalue - 2

print "Loading"
if nvalue > 6:
    equation2 = nvalue + svalue
    divisor3 = equation2 / 7
    math.trunc(divisor3)
    divisor3 = divisor3 * 7
    endvalue = equation2 - divisor3
elif nvalue <= 6:
    endvalue = nvalue + svalue
if endvalue == Sunday:
    bday = "Sunday"
elif endvalue == Monday:
    bday = "Monday"
elif endvalue == Tuesday:
    bday = "Tuesday"
elif endvalue == Wednesday:
    bday = "Wednesday"
elif endvalue == Thursday:
    bday = "Thursday"
elif endvalue == Friday:
    bday = "Friday"
elif endvalue == Saturday:
    bday = "Saturday"
elif endvalue == Saturday2:
    bday = "Saturday"

print "You were born on a %s" % bday