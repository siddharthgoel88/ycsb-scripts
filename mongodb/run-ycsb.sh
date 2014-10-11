#!/bin/bash

DIR=$HOME/mongodb-logs

mkdir -p $DIR

$1/ycsb load mongodb -P mongodb.url=compg4:$2 -p mongodb.database=test -p recordcount=25000000 -p mongodb.writeConcern=normal -s > $DIR/load-mongodb.log 

$1/ycsb run mongodb -P mongodb.url=compg4:$2 -p mongodb.database=test -p recordcount=25000000 -p mongodb.writeConcern=normal -s > $DIR/run-mongodb.log 
