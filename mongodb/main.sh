#!/bin/bash

MONGOBIN="/home/s/sgoel/code/distributed-databases/mongodb/bin/mongod"
MONGOD_PORT=2010
MONGOS_PORT=2014

ssh compg4 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT
ssh compg6 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT
ssh compg7 "bash -s" < ./run-mongod.sh $MONGOBIN $MONGOD_PORT

ssh compg4 "bash -s" < ./run-mongos.sh $MONGOBIN $MONGOS_PORT $MONGOD_PORT
