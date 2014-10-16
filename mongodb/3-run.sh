#!/bin/bash

LOGDIR="$HOME/mongodb-logs"
YCSB="/home/s/sgoel/code/distributed-databases/YCSB"
MONGOS_PORT=2014

mkdir -p $LOGDIR

ssh compg5 "bash -s" < ./supporting-scripts/run-data.sh $PWD $YCSB $LOGDIR $MONGOS_PORT
