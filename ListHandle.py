'''
Created on 2014. 2. 20.

@author: Choi
'''
names=['Dave','Mark','Ann','Phil']
names[0:2] = ['1','2','3']

print names
print names[0:2]

numberlist =[1,2,3]+[4,5]
print numberlist

cast =["Cleese","Palin","Jones","Idle"]
print cast, len(cast), cast[1]

cast.append("Gilliam")
print cast

print cast.pop()
print cast

cast.extend(["Champan","Anna"])
print cast

cast.remove("Champan")
print cast

cast.insert(0, "Bee")
print cast

movies =["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
            ["Graham Champan",
                ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]
            ]
         ]

print movies[4][1][2]


cats=["Michael","Terry"]
print isinstance(cats,list)

cats = len(cats)
print isinstance(cats,list)

def printLol(theList):
    for each_item in theList:
        if isinstance(each_item, list):
            printLol(each_item)
        else:
            print ">>>"+str(each_item)

print printLol(movies)

msgList=["orange","banana","kiwi","tomato"]

msgList.insert(3, "grape")

print msgList.count("orange")
print msgList.index("orange")
print msgList.pop(2)
print msgList

for msg in msgList:
    print "in for:"+msg

'''
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print "nested:"+str(nested_item)
    else:
        print "outer:"+str(each_item)
'''
    
    
v = ['w','x','y','z']
[a,b,c,d]=v

print a,b,c,d

[MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY] = range(7)

print MONDAY,TUESDAY

li_99 = [2,8,16,5]
li_98=[elem*2 for elem in li_99]
print(li_98)

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print params.items()

paramsKeys = [k for k,v in params.items()]
print paramsKeys

paramsVal = [v for k,v in params.items()]
print paramsVal

li_97=["a","mpilgrimm","foo","b","c","b","d","d"]
print [elem for elem in li_97 if len(elem) >1]
print [elem for elem in li_97 if li_97.count(elem)== 1]
