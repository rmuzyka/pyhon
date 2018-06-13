import datetime
import time
import calendar
import timeit

start = time.time()
# localtime 
print time.localtime(time.time())
print time.localtime()
print time.time()
print time.asctime()
print time.clock()

print '\n\n'
print calendar.month(2018,6)
print
print [x for x in calendar.Calendar(firstweekday=3).iterweekdays()]

print
print 'Current date: ', datetime.date.today()
print 'Current year: ', datetime.date.today().strftime('%Y')
print 'Current day: ', datetime.date.today().strftime('%d')
print 'week number of the year: ', datetime.date.today().strftime('%W')
print 'weekday of the week: ', datetime.date.today().strftime('%w')
print 'day of the year: ', datetime.date.today().strftime('%j')
print 'Current month: ', datetime.date.today().strftime('%B')
print 'Current hour: ', datetime.date.today().strftime('%I')
print 'Current minute?: ', datetime.date.today().strftime('%M')
print 'Current : ', datetime.date.today().strftime('%p')
print 'Current day of week: ', datetime.date.today().strftime('%A')
print datetime.date.today().strftime("%A, %d. %B %Y %I:%M%p")



print 
print "Time in seconds since the epoch: %s" %time.time()
print "Current date and time: " , datetime.datetime.now()
# print "current time ", datetime.time.now()
print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

print time.timezone

time.sleep(0)
end = time.time()
print end-start
from timeit import default_timer as timer
print 'timer ', timeit.default_timer()

print '\n\n'
print datetime.MAXYEAR
print datetime.date
print datetime.datetime
print
d = datetime.timedelta(days=1, minutes=12, hours=-5, seconds=3, microseconds=2)
print d
print (d.days, d.seconds, d.microseconds)

print
print datetime.date(1919,3,1)
print datetime.date.today()
print datetime.date.fromtimestamp(time.time())
print datetime.date.year
# print datetime.date.strftime()

print
d = datetime.date.fromordinal(730920)
print d
t = d.timetuple()
for i in t:
    print i
print d.isoformat()
d = datetime.date.today()
print d.strftime("%d//%m//%y")
print d.strftime('%A %d. %B %Y')
print 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d,'day','month')

print '\n'
d = time.localtime()
print time.localtime()
print d[0]
print d[1]


