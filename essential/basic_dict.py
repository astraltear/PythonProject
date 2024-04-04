# -*- coding: utf-8 -*-

'''
Created on 2014. 2. 26.

@author: Choi
'''
stock={
       "name":"GPGP",
       "shares":100,
       "price":490.10
       }

print(stock["name"] )

stock["name"]="AAAA"

print(stock["name"])

prices ={
         "GOOG" : 490.10,
         "AAPL" : 123.50,
         "IBM"  : 91.50,
         "MSFT" :  52.13,
         "SCOX" : 34.30
}

if "SCOX" in prices:
    p = prices["SCOX"]
else: 
    p = 0.0
    
print(p)

p = prices.get("SCOXE",0.0)
print(p)

del prices["MSFT"]

print(list(prices))


dic_obj={'jan':1,'feb':2,'mar':3,'apr':4,'aug':8,'dec':12}

print( dic_obj['jan'], dic_obj['feb'], dic_obj['mar'] )

d2 = dict(jan=1,feb=2,mar=3,apr=4,may=5,jun=6,jul=7,aug=8,sep=9,oct=10,nov=11,dec=12)

print("=================>",d2)

month_names=[('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)]
print(dict(month_names))
print(month_names)


print( {name: num for name, num in month_names} )
print( {name: num for name, num in month_names if num %2==0} )

months = dict(month_names)
print( {v: k for k,v in months.items()} )

print(months.get('Jan'))    # None
print(months.get('Jan',1))  # 1
print(months.get('Jan'))    #None

print(months.setdefault('Jan',1))   # 1
print(months.get('Jan'))            # 1

print(months.keys())
print(months.values())
print(months.items())

print(hash('jan')%8)
print(hash('apr')%8)

a={'jan':1,'apr':4}
b={'apr':4,'jan':1}
print (a==b)
print ( a.items() == b.items() )


# 삽입한 순서대로 순회가 이루어진다 
from collections import OrderedDict
d = OrderedDict()
d['girls']=1
d['generation'] = 2
d['ggg'] = 3
d['babybaby']=4
print( d.items() )

from collections import defaultdict
words = open('./words.txt').read().splitlines()
by_len2 = defaultdict(lambda: [])
for w in words:
    by_len2[len(w)].append(w)
# print (by_len2)


from shelve import open
shelf = open('test')
shelf['hello'] = 1
shelf['world'] = 2
shelf.close()

shelf2 = open('test')
print(shelf2.items())