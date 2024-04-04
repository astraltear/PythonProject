
'''
param name match
'''

def showGugu(start, end=5):
    for dan in range(start,end+1):
        print(dan)


showGugu(2, 3)
showGugu(2)
showGugu(end=4, start=2)
showGugu(7, end=8)
# showGugu(start=7, 8)  SyntaxError: non-keyword arg after keyword arg

def Func1(*args):
    #print(args)
    for x in args:
        print(x)

Func1('one','two','three')

def Func2(a, *args):
    print(a)
    print(args)


Func2('one','two','three')

'''
TypeError: Func3() missing 1 required keyword-only argument: 'a'
def Func3( *args, a):
    print(a)
    print(args)

Func3('one','two','three')
'''

# dict param
def Func3(w,h, **others):
    print('weight {} height {}'.format(w, h))
    print(others)

Func3(60, 170, iname='hong',iage=24)
Func3(60, 170, iname='hong')


print('\nFunc4~~~~~~~~~~~')
def Func4(a,b,*c, **d): #def Func4(a,b,*c, **d,e):  SyntaxError: invalid syntax  - 딕 자료형 뒤에 다른 것이 올 수 없다??
    print(a)
    print(b)
    print(c)
    print(d)

print('\n4-1~~~~~~~~~~~')
Func4(1, 2)
print('\n4-2~~~~~~~~~~~')
Func4(1, 2,'one','two','three')
print('\n4-3~~~~~~~~~~~')
Func4(1, 2,'one','two','three',iname='Kim',iage=34,iman=True)



print('\nFunc5~~~~~~~~~~~')
def Func5(a,b,c):
    print(a)
    print(b)
    print(c)

print('\n5-1~~~~~~~~~~~')
Func5(1, 2, 3)

print('\n5-2~~~~~~~~~~~')
tup=(10,20)  # tup=(10,20,30) error 갯수 안 맞음
dic = {'c':30} # dic = {'k':30} error 이름 안 맞음
Func5(*tup, **dic)

print('\n5-3~~~~~~~~~~~')
tup=(10,)
dic = {'b':50,'c':30}
Func5(*tup, **dic)

print('\n5-4~~~~~~~~~~~')
tup=(10,)
dic = {'c':50}

Func5(1,*tup, **dic)

''' syntax error ??? SyntaxError: invalid syntax  - 딕 자료형 뒤에 다른 것이 올 수 없다??
print('\n5-5~~~~~~~~~~~')
tup=(10,)
dic = {'b':50}

Func5(*tup, **dic,c=3)
'''