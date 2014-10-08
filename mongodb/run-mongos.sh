#!/bin/bash

HOST=`hostname`
LOGDIR="$HOME/mongodb-logs"

#Kill process if it is already running
ps axf | grep mongos | grep -v grep | awk '{print "kill -9 " $1}'

#Delete the directory if it is existing
rm -rf $DIR

#Creates directory for logging if it does not exists
mkdir -p $LOGDIR

export PATH=$PATH:$1:

#$2 is the port on which we want to run mongod are running while on
#$3 mongos will run nohup will run the mongod in background and 
#store logs in $LOGDIR
nohup mongos --configdb compg4:$2,compg6:$2,compg7:$2 --port $3 > "$LOGDIR/mongos-$HOST.log"

