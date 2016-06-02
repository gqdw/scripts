import os
import subprocess
import datetime
import logging
import MySQLdb
class dbdump(object):
	def __init__(self):
		self.dbhost = 'rds.aliyuncs.com'
		self.dbpass = 'xx'
		self.dbuser = 'back'
		self.dblist = []
		self.today = datetime.datetime.today().strftime('%Y-%m-%d-%p')
		self.workdir = '/data/mysql_backup/'

	def get_dbs(self):
		db = MySQLdb.connect(self.dbhost, self.dbuser, self.dbpass, 'information_schema')
		cursor = db.cursor()
		sql = 'select schema_name from schemata'
		cursor.execute(sql)
		results = cursor.fetchall()
		for record in results:
			self.dblist.append(record[0])
		db.close()
		for i in ['mysql', 'performance_schema', 'information_schema']:
			self.dblist.remove(i)

	def backup(self):
		if not os.path.exists(self.workdir + self.today):
			os.mkdir(self.workdir + self.today)
		for db in self.dblist:
			self.dumpdb(db)


	def dumpdb(self, db):
		cmd = 'mysqldump -h %s -u %s -p%s %s' % (self.dbhost, self.dbuser, self.dbpass, db)
		logging.warning('dumpdb: %s' % cmd)
		filename = self.workdir + self.today + '/' + db + '.sql'
		with open(filename, 'w') as f:
			subprocess.check_call(cmd.split(), stdout=f)	
		cmd2 = 'pigz %s' % filename
		subprocess.check_call(cmd2.split())

if __name__ == '__main__':
        # pdb.set_trace()
	# logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
	# logging.warning('start main')
	# print get_dbs()
	# db_list = get_dbs()
	# db_list.reverse()
	# backup(db_list)
	db1 = dbdump()
	db1.get_dbs()
	db1.backup()

