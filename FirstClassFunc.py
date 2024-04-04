'''
일급 함수
    함수 안에 함수가 존재할 경우, 인자로 함수를 전달, 반환값이 함수
'''

def Func1(a,b):
    return a+b

Func2 = Func1
print(Func2(3,4))

def Func3(f,a,b):
    return f(a,b)

mbc =Func3(Func2,3,4)
print(mbc)

# lambda anonymous function
# 람다 식 lambda param: statement

def Hap(x,y):
    return x + y

print(Hap(1,2))
result = (lambda x,y: x+y )(10,2)
print( result)

g = lambda x, y : x * y
print(g(4,5))

kbs = lambda a,su=10: a+su
print(kbs(20))
print(kbs(20,100))

sbs = lambda c,*tu, **dic : print(c,tu,dic)
sbs(7,2,3,m=5,n=6)
sbs = lambda c,*tu, **dic : print('result:',[c*x for x in dic.values()])
sbs(7,2,3,m=5,n=6)


print(  list( filter( lambda a:a< 5,range(10) )  ) )
print(  list( filter( lambda a:a%2==1,range(10) )  ) )