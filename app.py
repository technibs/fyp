from flask import Flask,render_template
import os
import json
import signal
app=Flask(__name__)
fh=open("processid.txt","w")
fh.write(str(os.getpid()))
fh.close()
fp=open("data.json","w")
recv=0
def handleUsr1(signum,frame):
    global recv
    recv=1
    data={"value":recv}
    with open("static/data.json","w") as outfile:
        json.dump(data,outfile)
    print("Received signal",recv)
def handleUsr2(signum,frame):
    global recv
    recv=2
    data={"value":recv}
    with open("static/data.json","w") as outfile:
        json.dump(data,outfile)
    print("Received signal",recv)
def handleWinch(signum,frame):
    global recv
    recv=3
    data={"value":recv}
    with open("static/data.json","w") as outfile:
        json.dump(data,outfile)
    print("Received signal",recv)
    
signal.signal(signal.SIGUSR1,handleUsr1)
signal.signal(signal.SIGUSR2,handleUsr2)
signal.signal(signal.SIGWINCH,handleWinch)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/bla")
def disp():
    global recv
    if (recv==1):
            return render_template("208.html")
    elif(recv==2):
            return render_template("eclab.html")
    elif(recv==3):
            return render_template("hod.html")
    elif recv==0:
            return render_template("error.html")

app.run(host='0.0.0.0',port=8001,debug=True)
