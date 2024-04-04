from socket import *

rhost = raw_input("DEST:")

fromport = 30
toport = 40

for i in range(fromport, toport):
    s = socket(AF_INET,SOCK_STREAM)
    if s.connect_ex((rhost,i)) == 0:
        print( i , "is open")
    else:
        print( i, "is not open")
    s.close()
    
print( "finish")