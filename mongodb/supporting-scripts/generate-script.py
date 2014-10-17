import sys
import time
import datetime

def main():
	throughputList = []
	threadList = []
	tempThroughput = 500
	tempThread = 1

	args = sys.argv
	logPath = args[1]
	mongosPort = args[2]
	
	for i in range(9):
		throughputList.append(tempThroughput)
		tempThroughput *= 2
	
	for i in range(10):
		threadList.append(tempThread)
		tempThread *= 2

	scriptFile = open("generated-script-for-run-data.sh", "w")
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

	for thread in threadList:
		for throughput in throughputList:
			command = "./bin/ycsb run mongodb -P workloads/workloada -P large.dat -p " +\
				"mongodb.url=compg4:" + mongosPort  + " -p mongodb.database=test " +\
				"-threads " + str(thread) + " -p target=" + str(throughput) + \
				" -p mongodb.maxconnections=120 -p mongodb.writeConcern=normal -p operationcount=500000 -s > " + \
				logPath + "/run-thread-" + str(thread) + "-throughput-" + str(throughput) +\
				"-timestamp-" + str(st) + ".log"
			scriptFile.write("%s \n" % command)
	
	scriptFile.close()

if __name__ == '__main__':
	main()
