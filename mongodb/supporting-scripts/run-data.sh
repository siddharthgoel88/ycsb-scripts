#!/bin/bash

echo "YCSB Path is $2"
echo "Mongodb log directory is $3"
echo "Mongos Port = $4"

echo "Changing path to $1"
cd $1
cd supporting-scripts

echo "Generating script"
python generate-script.py $3 $4
chmod a+x ./generated-script-for-run-data.sh

echo "Moving script to $2"
mv ./generated-script-for-run-data.sh $2

echo "Changing to $2"
cd $2

echo "Running workload"
nohup bash ./generated-script-for-run-data.sh &

echo "End"
exit
