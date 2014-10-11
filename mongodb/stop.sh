#Killing mongo processes from comp nodes

echo "Stoping mongo in access0"
ssh access0 "bash -s" < ./stop-mongo-processes.sh

echo "Stoping mongo in access1"
ssh access1 "bash -s" < ./stop-mongo-processes.sh

echo "Stoping mongo in access2"
ssh access2 "bash -s" < ./stop-mongo-processes.sh

echo "Stoping mongo in access3"
ssh access3 "bash -s" < ./stop-mongo-processes.sh
