#!/bin/bash

if ! grep -q danqoo /etc/passwd
then
	useradd -m -s /bin/bash danqoo
fi
usermod -G sshers danqoo
PASS=`cat /dev/urandom |tr -cd '0-9a-z'|head -c 10`
hostname
echo "danqoo:$PASS"| chpasswd 
echo "$PASS"
