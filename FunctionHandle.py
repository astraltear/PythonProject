# -*- coding: utf-8 -*-


def divide(a,b):
    q = a// b  # 몫
    r = a - q*b # 나머지
    return (q,r)

quota , remain =  divide(10,3)

print quota, remain

# -*- coding: utf-8 -*-


def greeting(hour,morning_msg="hello"):
    if hour <9:
        print morning_msg
    elif hour < 12:
        pass
    
    else:
        print morning_msg
    


greeting(7)
retVal = greeting(14, "test")
print "return value:"+str(retVal)



def Times(a,b):
    return a*b

print Times(10,10)

print Times

myTimes = Times

print myTimes(2, 4)

def setValue(newValue):
    x = newValue # return None


retVal = setValue(10)
print retVal


x =10

def sum2(x,y):
    x=1
    return x+y

print sum2(4,2)
print x     # 함수 내부에서 변경한 사항이 외부에 영향을 미치지 않는다. 


def change1(x):
    x[0]='H'
    
wordlist=['J','a','m']

change1(wordlist)

print wordlist


