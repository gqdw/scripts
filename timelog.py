#import datetime
from datetime import datetime, timedelta
import time

class timelog:
#	start_time = datetime.now()

	def __init__(self):
		self.start_time = datetime.now()
		print "Timer plugin is active."
#print "will sleep 4"
#time.sleep(4)
	def end(self):
		self.end_time = datetime.now()
	def p(self):
		print "past %d seconds\n" % ((self.end_time - self.start_time).seconds)

tl = timelog()
time.sleep(3)
tl.end()
tl.p()
#delta = end_time - start_time
#print "past %d seconds\n" % delta.seconds

#def days_hours_minutes_seconds(timedelta):
#	minutes = (timedelta.seconds//60)%60
#	r_seconds = timedelta.seconds - (minutes * 60)
#	return timedelta.days, timedelta.seconds//3600, minutes, r_seconds
#
#def playbook_on_stats():
#	
#	end_time = datetime.now()
#	timedelta = end_time - start_time
#	print "Playbook run took %s days, %s hours, %s minutes, %s seconds" % (days_hours_minutes_seconds(timedelta))
#playbook_on_stats()


