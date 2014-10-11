#!/bin/bash

DIR=$HOME/mongodb-logs

mkdir -p $DIR
echo $1

export PATH=$HOME/python/bin/:$PATH
#source $HOME/.bashrc

echo $PATH
python -V
cd $1

python ./bin/ycsb load mongodb -P workloads/workloada -p mongodb.url=access0:$2 -p mongodb.database=test -p recordcount=100000 -p fieldcount=20 -p fieldlength=200 -p mongodb.writeConcern=normal -s > $DIR/load-mongodb.log 

python ./bin/ycsb run mongodb -P workloads/workloada -p mongodb.url=access0:$2 -p mongodb.database=test -p recordcount=100000 -p fieldcount=20 -p fieldlength=200 -p mongodb.writeConcern=normal -s > $DIR/run-mongodb.log 
