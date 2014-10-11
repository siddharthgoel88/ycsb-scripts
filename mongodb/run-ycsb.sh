#!/bin/bash

DIR=$HOME/mongodb-logs

mkdir -p $DIR

$1/ycsb load mongodb -P mongodb.url=access0:$2 -p mongodb.database=test -p recordcount=100000 -p fieldcount=20 -p fieldlength=200 -p mongodb.writeConcern=normal -s > $DIR/load-mongodb.log 

$1/ycsb run mongodb -P mongodb.url=access0:$2 -p mongodb.database=test -p recordcount=100000 -p fieldcount=20 -p fieldlength=200 -p mongodb.writeConcern=normal -s > $DIR/run-mongodb.log 
