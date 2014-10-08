#Kill if process is already running
ps axf | grep mongo | grep -v grep | awk '{print "kill -9 " $1}' | bash
