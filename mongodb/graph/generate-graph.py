import os
import re
import time
import datetime
import linecache
from matplotlib import pyplot

logdir = '$HOME/mongodb-logs'

class Stats:
	def __init__(self):
		self.threads = 0
		self.expThr = 0.0	
		self.runtime = 0.0
		self.achThr = 0.0


def parseLastValue(string):
	return re.findall('\d+.\d+', string)[-1]


def display(statsList):
	for stats in statsList:
		print "Threads = " + str(stats.threads) + "\tExpThr = " + str(stats.expThr) +\
			"\tRuntime = " + str(stats.runtime) + "\tAchThr = " + str(stats.achThr)


def save(path, ext='png', close=True, verbose=True):
    
    # Extract the directory and filename from the given path
    directory = os.path.split(path)[0]
    filename = "%s.%s" % (os.path.split(path)[1], ext)
    if directory == '':
        directory = '.'
 
    # If the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
 
    # The final path to save to
    savepath = os.path.join(directory, filename)
 
    if verbose:
        print("Saving figure to '%s'..." % savepath)

    pyplot.gcf().set_size_inches(18.5,10.5)
   
   # Actually save the figure
    pyplot.savefig(savepath, figsize=(50, 40), dpi=80)
    
    # Close it
    if close:
        pyplot.close()

    if verbose:
        print("Done")


def achThrExpThrGraph(statsList):
	colors = ['bo-', 'go-', 'ro-', 'co-', 'mo-', 'yo-', 'ko-', 'bo--', 'go--', 'ro--', 'co--', 'mo--', 'yo--', 'ko--' ]
	threads = list(set([stats.threads for stats in statsList ]))
	threads.sort()
	numOfThreads = len(threads)
	expThr = list(set([stats.expThr for stats in statsList ]))
	expThr.sort()
	numOfThr = len(expThr)
	achThr = [stats.achThr for stats in statsList ]

	for i in range(numOfThreads):
		pyplot.plot(expThr,achThr[(i*numOfThr):((i+1)*numOfThr) ],colors[i],label='Total Threads='+str(threads[i]))

	pyplot.grid(axis='both')
	pyplot.xlabel('Expected Throughput (operations/second)')
	pyplot.ylabel('Achieves Throughput (opertions/second)')
	pyplot.axis([0, 1.1 * max(expThr) , 0, 50000.0 ])
	pyplot.title('Plot of throughput attained in mongodb with various threads running 500000 operation counts')
	pyplot.legend(loc=2)
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
	save("Mongodb-throughput-graph-"+str(st), ext="png", close=False, verbose=True)
	#pyplot.show()


def main():
	global logdir
	statsList = []
	#output = '# of Threads\tExpected Throughput\tRuntime\t\t\tAchieved Throughput\n'
	for subdir, dirs, files in os.walk(logdir):
		for file in files:
			filePath = os.path.join(subdir, file)
			matchObj = re.match( r'run-thread-(\d*)-throughput-(\d*)-timestamp-*',file, re.M|re.I)
			
			if not matchObj:
				continue
			
			threads = matchObj.group(1)
			expectedThroughput = matchObj.group(2)
			runtime = parseLastValue( linecache.getline(filePath, 5) )
			achievedThroughput = parseLastValue( linecache.getline(filePath, 6) )

			stats = Stats()
			stats.threads = int(threads)
			stats.expThr = int(expectedThroughput)
			stats.runtime = float(runtime)
			stats.achThr = float(achievedThroughput)
			statsList.append(stats)
			#output += threads + "\t\t" + expectedThroughput + "\t\t\t" + runtime + "\t\t\t" + achievedThroughput + "\n"

	statsList.sort( key=lambda stat : (stat.threads, stat.expThr) )
	display(statsList)
	print len(statsList)
	achThrExpThrGraph(statsList)
	#print output


if __name__ == '__main__':
	main()
