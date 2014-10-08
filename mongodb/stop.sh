#Killing mongo processes from comp nodes

echo "Stoping mongo in compg4"
ssh compg4 "bash -s" < ./stop-mongo-processes.sh

echo "Stoping mongo in compg6"
ssh compg6 "bash -s" < ./stop-mongo-processes.sh

echo "Stoping mongo in compg7"
ssh compg7 "bash -s" < ./stop-mongo-processes.sh
