print( bin(9) )
print(int(8.3), float(5), str(5)+'oh' )

a = 10
b = eval('a+10')
print(b)

print(round(1.2))

import math
print(math.ceil(1.2), math.ceil(1.6))
print(math.floor(1.2), math.floor(1.6))

b_list = [True,1,False,'abc']
print(all(b_list))
print(any(b_list))

b_list2 = [2,4,5,6]
result = all( a < 10 for a in b_list2 )
print(result)

result = any( b< 3 for b in b_list2  )
print(result)

import sys
print(sys.path)

import math
print(math.pi)

import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2015,11)

import os
print(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.listdir('/'))

import random
print(random.random())
print(random.randint(1,2000))

from random import randint
print(randint(1,10))

from random import *
print(random())


'''
user define func
'''
def DoFunc0():
    print('DoFunc0 run')

def DoFunc1():
    print('DoFunc1 run')
    return 'A'

def DoFunc2(name):
    print('hello '+name)

print(DoFunc1()) # return A
print(DoFunc0()) # return None

OtherFuc = DoFunc0
OtherFuc()
print(globals())

DoFunc2('Hong')

def Dofunc3(arg1,arg2):
    r=arg1+arg2
    return r

returnfunc3 = Dofunc3('10', '20')
print(returnfunc3) # result : 1020

print(Dofunc3(arg2="Hello", arg1="John")) # result : JohnHello

def swap(a,b):
    return b, a

print(swap(3,100))

def Area_tri(a,b):
    c = a * b/2
    Area_print(c)

def Area_print(c):
    print('triangle ', c)


Area_tri(3, 5)