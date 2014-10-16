#!/bin/bash

MONGOS_PORT=2014
RECORDCOUNT=25000000
YCSB="/home/s/sgoel/code/distributed-databases/YCSB/"

echo "Starting YCSB on compg5"
ssh compg5 "bash -s" < ./supporting-scripts/load-script.sh $YCSB $MONGOS_PORT $RECORDCOUNT
