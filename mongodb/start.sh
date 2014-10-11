#!/bin/bash

MONGOBIN="/home/s/sgoel/code/distributed-databases/mongodb/bin/"
YCSBBIN="/home/s/sgoel/code/distributed-databases/YCSB/bin/"
MONGOD_PORT=2010
MONGOS_PORT=2014

echo "Starting mongod on access0 on port $MONGOD_PORT !!"
ssh access0 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT

echo "Starting mongod on access1 on port $MONGOD_PORT !!"
ssh access1 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT

echo "Starting mongod on access2 on port $MONGOD_PORT !!"
ssh access2 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT

echo "Starting mongos on access0 on port $MONGOS_PORT !!"
ssh access0 "bash -s" < ./run-mongos.sh $MONGOBIN $MONGOD_PORT $MONGOS_PORT

echo "Starting YCSB on access3"
ssh access3 "bash -s" < ./run-ycsb.sh $YCSBBIN $MONGOS_PORT
