# -*- coding: utf-8 -*-

a ="RequestHandle World"
for c in a:
    print( c )

# list
b =["Dave","Mark","Ann","Phil"]
for name in b:
    print( name)

# dictionary
c={"gogo":490.10, "IBM":10.20,"AAPL":30.12}
for key in c:
    print( c[key])
    
    
score=80
if 90 <= score <=100:
    print(("grade A") )
elif 80 <= score <90:
    print(("grade B") )
elif 70 <= score <80:
    print(("grade C") )
elif 60 <= score <70:
    print(("grade D") )
else:
  print(("grade F")  )
    
    
    
for n in [2,3]:
    for i in range(1,10):
        print( str(n)+"*"+str(i)+"="+str(n*i) )
        
        
def GetBiggerThan20(i):
    return i > 20

L=[10,20,30,40]

filterdList = filter(GetBiggerThan20,L)  # iterator를 반환
print( filterdList )

mapList =map(GetBiggerThan20,L)  # function 연산을 수행한다. 
print( mapList )

def add10(i):
    return  i+10

addList = map(add10,L)
print( addList )


import time
b =["Dave","Mark","Ann","Phil"]

if b.__len__() == 0 :
    print( "111" )

for name in b:
    time.sleep(5)
    print( name )
    

number=23
running=True

while running:
    guess = int(raw_input("Enter an integer:"))
    
    if guess==number:
        print( "OK" )
        running=False
    elif guess < number:
        print( "No higher than" )
    else :
        print( "No lower than" )

else:
    print( "the while loop is over." )

       