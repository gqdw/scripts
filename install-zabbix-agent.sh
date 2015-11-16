#!/bin/bash

prefix="/usr/local/zabbix-agentd"
name=`hostname`
if  grep -i centos /etc/issue  >> /dev/null
then
	iscentos=1
else
	iscentos=0
fi
function initgcc {
	if [ "$iscentos" -eq "1" ]
	then
		yum install -y gcc
	else 
		apt-get install -y build-essential
	fi
}
function install {
	cd /opt
	if [ ! -f "zabbix-2.2.3.tar.gz" ]
	then
		wget http://zy-res.oss-cn-hangzhou.aliyuncs.com/server/zabbix-2.2.3.tar.gz -O zabbix-2.2.3.tar.gz
		tar xzf zabbix-2.2.3.tar.gz
	fi
	cd zabbix-2.2.3
	if [ -d "$prefix" ]
	then
		echo "/usr/local/zabbix-agentd existed"
		exit 
	fi
	./configure --enable-agent  --prefix=${prefix}
	make -j 2
	make install
	groupadd zabbix
	useradd -g zabbix zabbix
	if [ "$iscentos" -eq "1" ] 
	then
		cp misc/init.d/fedora/core/zabbix_agentd /etc/init.d/
		chmod +x /etc/init.d/zabbix_agentd
		sed -i "s#BASEDIR=/usr/local#BASEDIR=${prefix}#" /etc/init.d/zabbix_agentd
		chkconfig zabbix_agentd --add
		chkconfig zabbix_agentd on
	else
		cp misc/init.d/debian/zabbix-agent /etc/init.d/
		chmod +x /etc/init.d/zabbix-agent
	#	sed -i "s#BASEDIR=/usr/local#BASEDIR=${prefix}#" /etc/init.d/zabbix-agent
		sed -i "s#DAEMON=/usr/local/sbin#DAEMON=${prefix}/sbin#" /etc/init.d/zabbix-agent
		update-rc.d zabbix-agent defaults
	fi
	
}

function config {
#	echo "ListenPort=30005" >> ${prefix}/etc/zabbix_agentd.conf
	cp ${prefix}/etc/zabbix_agentd.conf ${prefix}/etc/zabbix_agentd.conf-old

	sed -i "s/Server=127.0.0.1/Server=zabbix.jiagouyun.com/" ${prefix}/etc/zabbix_agentd.conf
	sed -i "s/Hostname=Zabbix server/Hostname=${name}/" ${prefix}/etc/zabbix_agentd.conf
	sed -i "s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/" ${prefix}/etc/zabbix_agentd.conf
	sed -i "s?# Include=/usr/local/etc/zabbix_agentd.conf.d/? Include=${prefix}/etc/zabbix_agentd.conf.d/?"  ${prefix}/etc/zabbix_agentd.conf
#	echo "LogFile=/tmp/zabbix_agentd.log
#	#DebugLevel=3
#	Server=zabbix.jiagouyun.com
#	#ServerActive=zabbix.jiagouyun.com
#	Hostname= 
#	Include=${prefix}/etc/zabbix_agentd.conf.d/">${prefix}/etc/zabbix_agentd.conf
#	${prefix}/sbin/zabbix_agentd
	echo "please check the hostname in the zabbix_agentd.conf"
}
initgcc
install
config
