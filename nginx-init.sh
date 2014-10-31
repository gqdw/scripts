#/bin/bash
#2014-10-31 11:12:54
. /etc/init.d/functions
prog=/usr/local/nginx/sbin/nginx
progname=`basename $prog`
start(){
	[ $EUID -ne 0 ] && exit 4
	echo -n $"Starting $prog: "
	daemon $prog $OPTIONS
	RETVAL=$?
#	[ $RETVAL -eq 0 ] && echo "start success"
	echo 
	return $RETVAL
}
stop(){
	[ "$EUID" != "0" ] && exit 4
	echo -n $"Shutting down $prog: "
	killproc $prog
	RETVAL=$?
	echo 
#	[ "$?" -eq 0 ] && echo "stop success"
	return $RETVAL
}




case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  status)
        status $prog
        ;;
  restart|force-reload)
        stop
        start
        ;;
  reload)
        exit 3
        ;;
  *)
	echo "usage: $0 start/stop/restart"
esac
