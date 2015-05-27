
txt = open("./FuncDemo.py")
for line in txt:
    print line
    
    
principal=1000
rate=0.05
year=1
numyears=5
f = open("./writefile","w")
while year <= numyears:
    principal = principal * (1 + rate)
    f.write(str(principal))
    print >> f, year,principal
    year +=1
f.close()

with open('./FuncDemo.py') as f:
    print f.readlines()
    print f.closed
    
print f.closed