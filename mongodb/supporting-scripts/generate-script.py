import sys

def main():
	throughputList = []
	threadList = []
	tempThroughput = 500
	tempThread = 2

	args = sys.argv
	logPath = args[1]
	mongosPort = args[2]
	
	for i in range(10):
		throughputList.append(tempThroughput)
		tempThroughput += 500
	
	for i in range(16):
		threadList.append(tempThread)
		tempThread += 2

	scriptFile = open("generated-script-for-run-data.sh", "w")

	for thread in threadList:
		for throughput in throughputList:
			command = "./bin/ycsb run mongodb -P workloads/workloada -p "\
				"mongodb.url=compg4:" + mongosPort  + " -p mongodb.database=test -p "\
				"recordcount=25000 -p fieldcount=20 "\
				"-threads " + str(thread) + " -p target=" + str(throughput) + \
				" -p mongodb.writeConcern=normal -p operationcount=1000 -s > " + \
				logPath + "/run-thread-" + str(thread) + "-throughput-" + str(throughput) + ".log"
			scriptFile.write("%s \n" % command)
	
	scriptFile.close()

if __name__ == '__main__':
	main()
