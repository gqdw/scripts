num=10
if [ $# -eq 1 ];then
	num=$1
fi
cat /dev/urandom | tr -cd '0-9a-zA-Z' |head -c $num
echo
