import MySQLdb
import pdb
import subprocess
import datetime 
import os

def get_dbs():
	"""get db list"""
	host = '.mysql.rds.aliyuncs.com'
	user = 'back'
	password = ''
	db = MySQLdb.connect(host, user, password, 'information_schema')
	cursor = db.cursor()
	dblist = []
	sql = 'select schema_name from schemata'
	cursor.execute(sql)
	results = cursor.fetchall()
	for record in results:
		dblist.append(record[0])

	db.close()
	for i in ['mysql', 'performance_schema', 'information_schema']:
		dblist.remove(i)
	return dblist


def backup(dblist):
	today = datetime.datetime.today().strftime('%d-%m-%y')
	workdir = '/data/mysql_backup/'
	if not os.path.exists(workdir + today):
		os.mkdir(workdir + today)
	for db in dblist:
		filename = workdir + today + '/' + db + '.sql'
		print filename
		f = open(filename, 'w')
		cmd = 'mysqldump -h mysql.rds.aliyuncs.com -u back -p %s' % db
		print cmd	
		child =subprocess.Popen(cmd.split(), stdout=f)
	#	child =subprocess.Popen(cmd.split(), stdout=subprocess.STDOUT)
		child.communicate()
		# print res
		f.close()


def main():
        # pdb.set_trace()
	print get_dbs()
	db_list = get_dbs()
	backup(db_list)
#       db_list = get_dbs()
#       for db in db_list

if __name__ == '__main__':
	main()
