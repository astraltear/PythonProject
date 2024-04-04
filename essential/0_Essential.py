# -*- coding: utf-8 -*-
principal = 1000
rate = 0.5
numyears = 5
year = 1

while year <=numyears:
    principal = principal * (1 + rate)
    print ( year, principal)
    print ( "%3d %0.2f" % (year,principal))
    year +=1

person_tuple="tupleA",

print("person_tuple", person_tuple)


for n in range(10):
    print ( "2 to the %d power is %d" % (n, 2**n) )

c={"GOOG":490.10 , "IBM":91.50, "AAPL":123.15 }
for key in c:
    print ("key::", key)

for item in c.items():
    print ("item:",item)
    print (item[0], "==>",item[1] )


print(47//4)

def remainder(a,b):
    q = a//b # // 끝수를 버리고 나누기
    r = a- q*b
    return r


count = 0
def foo():
    count=1
    print ("foo inner:",count)

foo()
print("foo outer:",count)

def bar():
    global count
    count=5
    print ("bar inner:",count)

bar()
print("bar outer:",count)

class Stack(object):
    def __init__(self):
        self.stack=[]

    def push(self,object):
        self.stack.append(object)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)

    def __repr__(self):
        return str(self.stack)


s = Stack()
s.push("Dave")
s.push(34)
s.push([7,8,9,])

print (s)
print(s.pop())
del s
#print (s)

import sys
val_a=36
# 참조 횟수 값은 예상보다 휠씬 큰 경우가 많다.
# 인터프리터는 숫자나 문자열 같은 변경 불가능한 객체에 의해서 사용되는
# 메모리를 절약하기 위해서 이들을 프로그램의 여러 곳에서 최대한 공유한다.
print( "ref count:", sys.getrefcount(val_a))


list_a = [1,2,3,4]
list_b = list_a
print ( list_a is list_b )
list_b[2]=100
print ( list_a )

# 얕은 복사
list_c=[1,2,[3,4]]
list_d = list(list_c)
print ( list_c is list_d )

list_d.append(100)
print("list_c:", list_c)
print("list_d:", list_d)

list_d[2][0]= -100

print("after list_c:", list_c)
print("after list_d:", list_d)


# 깊은 복사
import copy
list_e = [1,2,[3,4]]
list_f = copy.deepcopy(list_e)
list_f[2][0]=-100
print("list_e:", list_e)
print("list_f:", list_f)

# 1급 객체 

items ={"number":42, "text":"Hello World"}

items["func"]= abs
print(items["func"](-34))

import math
items["mod"]=math
items["error"]=ValueError
nums=[1,2,3,4]
items["append"] = nums.append
print( items["mod"].sqrt(4) )

items["append"]("ddd")
print( nums )

line="GOOD,100,490.10"
field_type=[str,int,float]
raw_fields = line.split(",")
fields = [ ty(val) for ty,val in zip(field_type, raw_fields) ]
print(fields)

aformat="Your name is {0} and your age is {age}"
print( aformat.format("Mike",age=40) )

a_list=[2,3,4,5]
print ( repr(a_list) )

def countdown(n):
    while n > 0:
        yield "T-minus %d\n" % n
        n-= 1
    yield "Kaboom!\n"

count = countdown(5)
print( dir(count)  )
print ( count.__next__() )
print ( count.__next__() )
print ( count.__next__() )
print ( count.__next__() )
print ( count.__next__() )
print ( count.__next__() )

import pickle
obj = Stack()
f= open('objtoFile','wb')
pickle.dump(obj,f)
f.close()

f2 = open('objtoFile','rb')
obj2 = pickle.load(f2)
print( obj2 )
f2.close()

# shelve모듈은 pickle 모듈과 유사하지만 객체들을 사전 같은 데이터 베이스에 저장한다.
import shelve

db = shelve.open("obj.db")
db['key'] = Stack()
obj4 = db['key']
print("---->",obj4)
db.close()


