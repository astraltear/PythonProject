import time

logFile = open("filecheck.log",'w')


try:
    1/0
except Exception as e:      
        logFile.write(e.message)

logFile.close()

b =["Dave","Mark","Ann","Phil"]

if b.__len__() == 0 :
    print "111"

for name in b:
    time.sleep(5)
    print name
    
