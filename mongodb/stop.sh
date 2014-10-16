#Killing mongo processes from comp nodes

echo "Stoping mongo in compg4"
ssh compg4 "bash -s" < ./supporting-scripts/stop-mongo-processes.sh

echo "Stoping mongo in compg6"
ssh compg6 "bash -s" < ./supporting-scripts/stop-mongo-processes.sh

echo "Stoping mongo in compg7"
ssh compg7 "bash -s" < ./supporting-scripts/stop-mongo-processes.sh

echo "Stoping ycsb in compg5"
ssh compg5 "bash -s" < ./supporting-scripts/stop-ycsb.sh
