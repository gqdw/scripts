
# 获取当前系统日期，格式为： 2009-2-21
DATE=`date "+%F"`

# 定义mysql 服务的主目录
DB_DIR=/alidata/mysql

# 定义备份后的路径
BAK_DIR=/alidata/backup
BAK_PATH=$BAK_DIR/$DATE

#  判断备份文件存放的路径是否存在
if [ ! -d $BAK_PATH ];then
    mkdir -p $BAK_PATH
fi

# 进入/usr/local/mysql/data  目录查看都有哪些数据库
#cd $DB_DIR/data DB_NAME=`ls -dF -1 * | grep "/$" | cut -d/ -f1`

# 利用mysqldump 对所有数据库进行SQL语句备份
#for db_name in $DB_NAME
#do
db_name=shengchan
SENDER=/usr/local/zabbix-agentd/bin/zabbix_sender
$DB_DIR/bin/mysqldump -u root -S /tmp/mysql.sock $db_name > $BAK_PATH/$db_name-$DATE.sql
if [ 0 -eq "$?" ];then
	$SENDER -z zabbix.jiagouyun.com -s "yz_web4" -k mysql.backup -o 1
else
	$SENDER -z zabbix.jiagouyun.com -s "yz_web4" -k mysql.backup -o 0
fi
#ddone

# 删除15天以前备份的文件
#find $BAK_DIR -name "*" -mtime +15 |xargs rm -rf
#exit 0
