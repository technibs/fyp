import os
import signal
import time
import random
val=2
test=0
fh=open("processid.txt","r")
processId=int(fh.read())
fh.close()

while True:
	if val==test:
		print("Same",val)
	elif val == 1:
		test=val
		os.kill(processId,signal.SIGUSR1)
		print("In site 1")
	elif val == 2:
		test=val
		os.kill(processId,signal.SIGUSR2)
		print("In site 2")
	elif val ==3:
		test=val
		os.kill(processId,signal.SIGWINCH)
		print("In site 3")
	else:
		print("In site none")
	time.sleep(30)
	val=random.randint(1,3)
		
		


