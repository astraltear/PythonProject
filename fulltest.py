for a in ['1','2','3','4']:
    print a

i = 0
while i < 5:
    i=i+1
    print i

number = -123
print number

number2 = 4.24E10
print number2

number3 = 5.65e-10
print number3


x= 3
y=4

print x/y   # python 2.7 is 0
print x/(y * 1.0)

str1 = "Life is too short, You need Python"
print str1[0:4]
print str1[:19]
print str1[19:]

str2="Pithon"
# str2[1]="y"  not assignment
str2 = str2[:1]+"y"+str2[2:]
print str2, str2.upper(), str2.lower(), str2.count('t'), str2.find('n'), str2.index('o')

print ",".join(str2), str2.lstrip(), str2.rstrip(), str2.strip()

print str2.replace("n","A"), str2.swapcase()

print str1.split(), "a:b:e:d:e:f:g:h:i:j".split(":")

list1 = [1,2,['a','b',['Life','is']]]
print list1[2][2][0]

list2 = [1,2,3]
list3 = [4,5,6]
print list2 + list3

print list2 * 3

list2[1:2] = ['z','x','c']
print list2

dic1 = {1:'a'}
dic1[2]='b'
dic1['name']='pey'
dic1[3]=[1,2,3]
print dic1

del dic1['name']
print dic1

list_left = [1,2,3]
list_right = list_left[:]
list_left[1]=4
print list_left, list_right
print list_left is list_right

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

print sum_many(1,2,3,4,5,6)

def sum_and_mul(a,b):
    return a+b , a*b

resultsum = sum_and_mul(5,6)
print resultsum[0], resultsum[1]

re_left , re_right = sum_and_mul(23,6)
print re_left , re_right


class HousePark:
    lastname="park"
    def __init__(self,name):
        self.fullname = self.lastname+name

    def __add__(self,other):
        print "%s, %s plus" %(self.fullname, other.fullname)

    def __sub__(self,other):
        print "%s, %s sub" %(self.fullname, other.fullname)

    def __del__(self):
        print "%s del" %self.fullname
        
    def travel(self,where):
        print "%s, %s go travel HousePark" %(self.fullname, where)

    def love(self,other):
        print "%s, %s fall in love" %(self.fullname , other.fullname)


class HouseKim(HousePark):
    lastname ="kim"
    def travel(self,where,day):
        print "%s, %s travel % days go HouseKim" %(self.fullname, where, day)

pey = HousePark("Smith")
juliet = HouseKim("Juliet")
pey.travel("Busan")
juliet.travel("Busan",3)
pey.love(juliet)
pey + juliet
pey - juliet


