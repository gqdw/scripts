#import time
#from datetime import timedelta ,datetime,date
#
#today = date.today()
#ld = today - timedelta(h=1)
#print ld

import datetime
import time
#t = datetime.datetime(2014,12, 6, 12, 10, 10)
#计算今天00:00的timestamp
t = datetime.date.today()
t2 = t - 24*3600*7
print t
timestamp = time.mktime(t.timetuple())
print timestamp
print time.mktime(t2.timetuple())


