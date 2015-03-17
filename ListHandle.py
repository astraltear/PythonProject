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

'''
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print "nested:"+str(nested_item)
    else:
        print "outer:"+str(each_item)
'''