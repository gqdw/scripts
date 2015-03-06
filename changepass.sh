#!/bin/bash

#if ! grep -q danqoo /etc/passwd
#then
#	useradd -m -s /bin/bash danqoo
#fi
#usermod -G sshers danqoo
get_pass()
{
	if [ $# -ne 1 ];then
		len=10
	else
		len=$1
	fi
	PASS=`cat /dev/urandom |tr -cd '0-9a-zA-Z'|head -c $len`
	#hostname
	#echo "danqoo:$PASS"| chpasswd 
	echo "$PASS"
}
#p=$(get_pass)
p=`get_pass`
echo "$p"
#echo "$p"
