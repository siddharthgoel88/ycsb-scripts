#!bin/bash

HOST=`hostname`
LOGDIR="$HOME/mongodb-logs/access-logs"

#Delete the directory if it is existing
rm -rf $DIR

#Creates directory for logging if it does not exists
mkdir -p $LOGDIR

export PATH=$PATH:$1:

#$2 is the port on which we want to run mongod are running while on
#$3 mongos will run nohup will run the mongod in background and 
#store logs in $LOGDIR
nohup mongos --configdb access0:$2,access1:$2,access2:$2 --port $3 > "$LOGDIR/mongos-$HOST.log" &

sleep 5

echo "Adding access0 to shards"
mongo --port $3 --eval "sh.addShard('access0:$2')"

echo "Adding access1 to shards"
mongo --port $3 --eval "sh.addShard('access1:$2')"

echo "Adding access2 to shards"
mongo --port $3 --eval "sh.addShard('access2:$2')"

echo "Creating database: test"
mongo --port $3 --eval "use test"

echo "Creating collection: usertable"
mongo --port $3 --eval "db.createCollection('usertable')"

echo "Enabling Sharding"
mongo --port $3 --eval "sh.enableSharding('test')"

echo "Add index over which sharding has to happen"
mongo --port $3 --eval "db.usertable.ensureIndex({ id: 'hashed'})"

echo "Sharding collection"
mongo --port $3 --eval "sh.shardCollection('test.usertable', {'_id':'hashed'})"

