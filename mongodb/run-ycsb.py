#!/home/s/sgoel/python/bin/python

import sys
import subprocess as sp

ycsbPath = ""
mongosPort = 0
throughputList = [500, 1000, 2000, 3000, 4000]
threadList = [2, 4, 8, 16, 32]
recordCount = 2500
operationCount = 2500

def loadData():
        global ycsbPath, mongosPort, recordCount
        arg = "mongodb -P " + ycsbPath  + "/workloads/workloada -p mongodb.url=compg4:" + mongosPort  +  " -p mongodb.database=test" +\
                        "-p recordcount=" + recordCount + " -p fieldcount=20 -p fieldlength=200 -p mongodb.writeConcern=normal" + \
                        " -threads 24 -s"

        log_dir = os.environ['HOME'] + "/mongodb-logs/"
        load_log_file = "ycsb-load-data.log"
        load_err_file = "ycsb-load-error.log"
        logF = open(os.path.join(log_dir, load_log_file), "w")
        logErr = open(os.path.join(log_dir, load_err_file), "w")
        p = sp.Popen([ycsbPath + '/bin/ycsb.sh','load', arg], stderr=logErr, stdout=logF)

def runWithData():
        global ycsbPath, mongosPort, recordCount, operationCount, throughputList, threadList

        for throughput in throughputList:
                for thread in threadList:
                        arg = "mongodb -P " + ycsbPath  + "/workloads/workloada -p mongodb.url=compg4:" + mongosPort  +  " -p mongodb.database=test" +\
                                        "-p recordcount=" + recordCount + " -p operationcount=" + operationCount  + " -p fieldcount=20" +\
                                        " -p fieldlength=200 -p mongodb.writeConcern=normal" + " -threads " + thread + " -target " + throughput  + " -s"

                        log_dir = os.environ['HOME'] + "/mongodb-logs/"
                        load_log_file = "ycsb-run-thread-" +  thread + "-target-" + throughput + ".log"
                        load_err_file = "ycsb-run-error-thread-" +  thread + "-target-" + throughput + ".log"
                        logF = open(os.path.join(log_dir, load_log_file), "w")
                        logErr = open(os.path.join(log_dir, load_err_file), "w")
                        p = sp.Popen([ycsbPath + '/bin/ycsb.sh','run', arg], stderr=logErr, stdout=logF)

def main():
        global ycsbPath, mongosPort
        print 'Number of arguments:', len(sys.argv), 'arguments.'
        print 'Argument List:', str(sys.argv)
        args = sys.argv
        ycsbPath = args[1]
        mongosPort = int(args[2])
        loadData()
        runWithData()

if __name__ == "__main__":
        main()
