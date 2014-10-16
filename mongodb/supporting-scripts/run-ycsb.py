#!/usr/bin/python

import os
import sys
import subprocess as sp
import shlex

ycsbPath = ""
mongosPort = ""
throughputList = [500, 1000, 2000, 3000, 4000]
threadList = [2, 4, 8, 16, 32]
recordCount = "25000000"
operationCount = "25000000"

def loadData():
        global ycsbPath, mongosPort, recordCount
        cmd = ycsbPath + "bin/ycsb load mongodb -P " + ycsbPath  + "workloads/workloada -p mongodb.url=compg4:" +mongosPort  +  " -p mongodb.database=test" +\
                        " -p recordcount=" + recordCount + " -p fieldcount=20 -p fieldlength=200 -p mongodb.writeConcern=normal" + \
                        " -threads 24 -s"

        log_dir = os.environ['HOME'] + "/mongodb-logs/"
        load_log_file = "ycsb-load-data.log"
        load_err_file = "ycsb-load-error.log"
	cmd = cmd + " > " + log_dir + load_log_file
        #logF = open(os.path.join(log_dir, load_log_file), "w")
        #logErr = open(os.path.join(log_dir, load_err_file), "w")
	print cmd
        #p = sp.Popen([ycsbPath + 'bin/ycsb','load', arg], stderr=logErr, stdout=logF)
        #p = sp.Popen(shlex.split(cmd), stderr=logErr, stdout=logF)


def runWithData():
        global ycsbPath, mongosPort, recordCount, operationCount, throughputList, threadList

        for throughput in throughputList:
                for thread in threadList:
			throughput = str(throughput)
			thread = str(thread)
                        cmd = ycsbPath + "bin/ycsb run mongodb -P " + ycsbPath  + "workloads/workloada -p mongodb.url=compg4:" + mongosPort  +  " -p mongodb.database=test" +\
                                        " -p recordcount=" + recordCount + " -p operationcount=" + operationCount  + " -p fieldcount=20" +\
                                        " -p fieldlength=200 -p mongodb.writeConcern=normal" + " -threads " + thread + " -target " + throughput  + " -s"

                        log_dir = os.environ['HOME'] + "/mongodb-logs/"
                        load_log_file = "ycsb-run-thread-" +  thread + "-target-" + throughput + ".log"
                        load_err_file = "ycsb-run-error-thread-" +  thread + "-target-" + throughput + ".log"
			cmd = cmd + " > " + log_dir + load_log_file
			print cmd
                        #logF = open(os.path.join(log_dir, load_log_file), "w")
                        #logErr = open(os.path.join(log_dir, load_err_file), "w")
                        #p = sp.Popen([ycsbPath + 'bin/ycsb','run', arg], stderr=logErr, stdout=logF)
                        #p = sp.Popen(shlex.split(cmd), stderr=logErr, stdout=logF)


'''
def runWithData():
        global ycsbPath, mongosPort, recordCount, operationCount, throughputList, threadList

	fullcmd = ""
        for throughput in throughputList:
                for thread in threadList:
			throughput = str(throughput)
			thread = str(thread)
                        cmd = ycsbPath + "bin/ycsb run mongodb -P " + ycsbPath  + "workloads/workloada -p mongodb.url=compg4:" + mongosPort  +  " -p mongodb.database=test" +\
                                        " -p recordcount=" + recordCount + " -p operationcount=" + operationCount  + " -p fieldcount=20" +\
                                        " -p fieldlength=200 -p mongodb.writeConcern=normal" + " -threads " + thread + " -target " + throughput  + " -s"

			print "Run command:\n" ,cmd
                        log_dir = os.environ['HOME'] + "/mongodb-logs/"
                        log_file = "ycsb-run-thread-" +  thread + "-target-" + throughput + ".log"
			cmd = cmd + " > " + log_dir + log_file
			fullcmd = fullcmd + cmd + "; " 
	
	p = sp.Popen(shlex.split(fullcmd))
'''

def main():
        global ycsbPath, mongosPort
        #print 'Number of arguments:', len(sys.argv), 'arguments.'
        #print 'Argument List:', str(sys.argv)
        args = sys.argv
        ycsbPath = args[1]
        mongosPort = args[2]
        loadData()
        runWithData()

if __name__ == "__main__":
	main()
