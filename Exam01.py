# -*- coding: utf-8 -*-
import sys

print "RequestHandle World",  25+35/6, 3+5, 2432423423-23423463646345353, 452432*2323, "가나다"+"라마바"
print "Save World", 100-24 % 3
print "한글"
print 3+2 < 5-7

cars =100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car

print cars_not_driven, cars_driven, carpool_capacity, passangers

my_name = 'CHoi'
my_age = 10
my_height = 40
my_weight = 50
my_foot = 20

print "%s에 대해 말해봐요" % my_name
print "%d 살 이네요" % my_age
print  "%d %d " %(my_height, my_weight  )

t = "This is Python Class, And 1st day"
print t[3], t[-1], t[1:3]

t = "2015-03-10 14:21:35"
date = t[:10]
time = t[11:]

print "date:", date
print "time:", time

myList = ['a','b','c','d','e','f']
print myList[0], myList [-2], myList[:]

myList2 = myList # shllow copy
myList3  = myList[:] # deep copy

myList.append('g')

print myList2
print myList3

print 'd' in myList2   


text = "abcabcde"
myList = list(text)
print myList

myTuple = tuple(text)
print myTuple

mySet = set(text)
print mySet

myDic = {'1class':98, '2class':85, '3class':95}
for k,v in myDic.items():
    print(k,v)
    
print sys.getdefaultencoding()

tinydict = {'name':'john',"code":6705,"dept":"dev"}
print tinydict['name']
print tinydict, tinydict.keys(), tinydict.values()

fruits = ['kiwi','banana','orange','grape']
for index in range(len(fruits)):
    print fruits[index]
    
    
    
print range(0,10,2)


