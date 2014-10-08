USER=`id --u -n`
HOST=`hostname`
DIR="/temp/mongodb-$USER-$HOST"

#Kill if process is already running
ps axf | grep mongo | grep -v grep | awk '{print "kill -9 " $1}' | bash
rm -rf $DIR/*
