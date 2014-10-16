#!/bin/bash

MONGOBIN="/home/s/sgoel/code/distributed-databases/mongodb/bin/"
MONGOD_PORT=2010
MONGOS_PORT=2014

echo "Starting mongod on compg4 on port $MONGOD_PORT !!"
ssh compg4 "bash -s" < ./supporting-scripts/run-mongod.sh $MONGOBIN $MONGOD_PORT

echo "Starting mongod on compg6 on port $MONGOD_PORT !!"
ssh compg6 "bash -s" < ./supporting-scripts/run-mongod.sh $MONGOBIN $MONGOD_PORT

echo "Starting mongod on compg7 on port $MONGOD_PORT !!"
ssh compg7 "bash -s" < ./supporting-scripts/run-mongod.sh $MONGOBIN $MONGOD_PORT

sleep 5

echo "Starting mongos on compg4 on port $MONGOS_PORT !!"
ssh compg4 "bash -s" < ./supporting-scripts/run-mongos.sh $MONGOBIN $MONGOD_PORT $MONGOS_PORT

