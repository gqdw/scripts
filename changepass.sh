#!/bin/bash

#if ! grep -q danqoo /etc/passwd
#then
#	useradd -m -s /bin/bash danqoo
#fi
#usermod -G sshers danqoo
if [ $# -ne 1 ];then
	len=10
else
	len=$1
fi
PASS=`cat /dev/urandom |tr -cd '0-9a-zA-Z'|head -c $len`
#hostname
#echo "danqoo:$PASS"| chpasswd 
echo "$PASS"
