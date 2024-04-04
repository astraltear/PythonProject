

logFile = open("filecheck.log",'w')


try:
    1/0
except Exception as e:      
        logFile.write(e.message)

else:
    print( "else" )
    
finally:
    print( "finally")

logFile.close()

try:
    2/1
except TypeError:
    print( "TypeError")

else:
    print( "else" )

finally:
    print( "finally" )


def RaiseException():
    raise NameError

try:
    RaiseException()
except:
    print( "raise Error" )