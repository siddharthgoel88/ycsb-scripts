ps axf | grep ycsb | grep -v grep | awk '{print "kill -9 " $1}' | bash
