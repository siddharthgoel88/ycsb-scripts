#!/bin/bash

MONGOBIN="/home/s/sgoel/code/distributed-databases/mongodb/bin/"
YCSBBIN="/home/s/sgoel/code/distributed-databases/YCSB/bin/"
MONGOD_PORT=2010
MONGOS_PORT=2014

echo "Starting mongod on compg4 on port $MONGOD_PORT !!"
ssh compg4 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT

echo "Starting mongod on compg6 on port $MONGOD_PORT !!"
ssh compg6 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT

echo "Starting mongod on compg7 on port $MONGOD_PORT !!"
ssh compg7 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT

echo "Starting mongos on compg4 on port $MONGOS_PORT !!"
ssh compg4 "bash -s" < ./run-mongos.sh $MONGOBIN $MONGOD_PORT $MONGOS_PORT

echo "Starting YCSB on compg5"
ssh compg5 "bash -s" < ./run-ycsb.sh $YCSBBIN $MONGOS_PORT
