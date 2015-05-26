'''
Created on 2014. 2. 26.

@author: Choi
'''
a ="RequestHandle World"
for c in a:
    print c

# list
b =["Dave","Mark","Ann","Phil"]
for name in b:
    print name

# dictionary
c={"gogo":490.10, "IBM":10.20,"AAPL":30.12}
for key in c:
    print c[key]
    
    
score=80
if 90 <= score <=100:
    print("grade A")
elif 80 <= score <90:
    print("grade B")
elif 70 <= score <80:
    print("grade C")
elif 60 <= score <70:
    print("grade D")
else:
  print("grade F")  
    
    
    
for n in [2,3]:
    for i in range(1,10):
        print str(n)+"*"+str(i)+"="+str(n*i)