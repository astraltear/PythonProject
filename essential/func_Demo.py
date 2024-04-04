# -*- coding: utf-8 -*-
from __builtin__ import str

def foo(a, b=3):
    print(('a:', a,'b:', b ) )

foo(1,2)
foo(7)
foo(b=90, a=20)

def foo2(*args):
    for i in args:
        print( i)
    print(("\n"))

foo2(1,2,3,4)

def foo3(**dic): 
    for (k,v) in dic.items():
        print((k, ":", v) )
    print(())

foo3(a=1,b=2,c=3)


# 인수의 갯수가 정해지지 않은 가변 인수 전달 *를 사용 튜플형식으로 전달
def union2(*ar):
    res = []
    for item in ar:
        for x in item:
            if not x in res:
                res.append(x)
    return res

alist = union2("HAN","EGG","SPAM")
print( alist )

# **를 사용하면 정의되지 않은 인수를 사전형식으로 전달
def userURIBuilder(server, port, **user):
    str="http://"+server+":"+port+"/?"
    for key in user.keys():
        str+= key+"="+user[key]+"&"
    return str

print( userURIBuilder("test.com", "8088",id='user',passwd="1234",name='mike',age='20') )


