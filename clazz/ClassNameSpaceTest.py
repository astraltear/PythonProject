def foo(*args):
    for i in args:
        print(i, end=' ')

foo(1,2,3,4,5,'one','two')

print()


def foo(**args):
    for k,v in args.items():
        print(k,':', v)


foo(a='one',b='1',c=2)


class Student:
    old = -1
    name = 'N/A'

    def __init__(self,name,old=17):
        self.name=name
        self.old = old

    def print_name(self):
        print(self.name)

    def print_old(self):
        print(self.old)


s = Student('Chul Soo', 16)

Student.print_name(s)
s.print_name()

print('Chul Soo age', s.old)
del(s.old)
print('Chul Soo age', s.old)

print('Chul Soo name', s.name)
del(s.name)
print('Chul Soo name', s.name)

print()

class Test:
    i = 3

t= Test()
print(Test)
print( t.__class__)


class Person:
    name='Default Name'

p1 = Person()
p2 = Person()
p1.name='p1 name'

Person.title = 'New Title'

print( p1.title )
print( p2.title )
print( p1.name )
print( Person.name )

p1.age=30
print(p1.age)
#print( p2.age )   # Person.age 가 없어서 에러가 난다  age는 p1에만 있음


str="Not Class Member"
class GString:
    str=""

    def Set(self,msg):
        self.str=msg

    def print(self):
        print(str)  # self를 이용하여 클래스 멤버변수를 접근하지 않은 경우
                    # 글로벌 멤버변수에 접근


g = GString()
g.Set('First Message')
g.print()
print(g.str)


class Test2:
    data = 'Default'

i2 = Test2()
i3 = Test2()
i2.__class__.data = 'class data change'

print( 'i2.data:', i2.data)
print( 'i3.data:', i3.data)

i2.data = 'i2 only data change'

print( 'after i2.data:',i2.data)
print( 'after i2.__class__.data:',i2.__class__.data)
print( 'after i3.data:', i3.data)


name_1 = 'g_name'
class Person_1:
    name_1 = 'Person_1 default name'

    def print_person(self):
        print('My name is ' + name_1)


p_1 = Person_1()
p_2 = Person_1()
print('p_1.name_1: '+p_1.name_1)
print('p_2.name_1: '+p_2.name_1)

p_1.name_1 = 'appllo'
print('p_1.name_1: '+p_1.name_1)
print('p_2.name_1: '+p_2.name_1)

Person_1.title1 = 'default title'
print('p_1.title1: '+p_1.title1)
print('p_2.title1: '+p_2.title1)

p_1.print_person()


p_3 = Person_1()
p_2.__class__.name_1 = 'class name'
print('p_2.name_1: '+p_2.name_1)
print('p_3.name_1: '+p_3.name_1)
