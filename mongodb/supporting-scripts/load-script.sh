#!/bin/bash

LOGDIR="$HOME/mongodb-logs"
echo "YCSB Path = $1"
echo "mongos is running on port = $2"
echo "Total records to be loaded = $3"
cd $1
mkdir -p $LOGDIR

echo "*************************************DATA LOADING STARTING********************************"

nohup python ./bin/ycsb load mongodb -P workloads/workloada -p mongodb.url=compg4:$2 -p mongodb.database=test -p recordcount=$3 -p fieldcount=20 -p fieldlength=200 -p threadcount=10 -p mongodb.writeConcern=normal -s  > "$LOGDIR/load-$3-records.log" &

