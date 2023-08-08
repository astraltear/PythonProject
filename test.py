
# list append
suitcase = [] 
suitcase.append("sunglasses")

suitcase.append("shirts")
suitcase.append("shoes")
suitcase.append("pants")

list_length =len(suitcase)

print ("list length: %d" % (list_length))
print (suitcase)

# list string split
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[0:2]
middle = suitcase[2:4]
last = suitcase[4:]

print (first)
print (middle)
print (last)

animals = "catdogfrog"
cat = animals[:3]
print (cat)

dog = animals[3:6]
print (dog)

frog = animals[6:]
print (frog)

# list index insert
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

duck_index= animals.index("duck")
print (duck_index)

animals.insert(duck_index,"cobra")
print (animals)


# list for loop
start_list = [5, 3, 1, 2, 4]
square_list=[]

for number in start_list:
    square_list.append(number)
    

square_list.sort()
print (square_list)


# dic add get del change
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print (residents['Puffin'])
print (residents['Sloth'])
print (residents['Burmese Python'])


menu={}
menu['Chicken Alfredo'] = 14.50
print (menu['Chicken Alfredo'])

menu['a']=2
menu['b']=3
menu['c']=4

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin']='Test'

print (zoo_animals)
print (len(menu))

# dic list change sort add

inventory={'gold':500,
           'pouch':['flint','twine','gemstone'],
           'backpack':['xylophone','dagger','bedroll','bread loaf']}

inventory['burlap bag']=['apple','small ruby','three-toed sloth']

inventory['pouch'].sort()

inventory['pocket']=['seashell','strange berry','lint']
inventory['backpack'].sort()

inventory['backpack'].remove('dagger')
inventory['gold']=inventory['gold']+50

print (inventory)


dic={"foo":"bar"}

for key in dic:
    print (dic[key])

# dic get key items()
webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for web in webster:
    print (web)
    print (webster[web])

for item in webster.items() :
    print (item)

# control flow
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for index in a:
    if index %2 ==0:
        print (index)

#list & function
def fizz_count(x):
    cnt=0
    for i in x:
        if i =='fizz':
            cnt=cnt+1
    return cnt
    
print (fizz_count(['fizz','buzz','fizz']))

n=[1,3,5]
n[1]=n[1]*5
n.append(4)
print (n)


def my_function(x):
    return x+3

number=5
print (my_function(number))

def list_function(nmlist):
    return nmlist[1]

nm=[1,3,5]
print( list_function(nm) )

def list_extender(mylist):
    mylist[-1]=mylist[-1]+9
    return mylist
    
nn = [3, 5, 7]
print( list_extender(nn) )

def total(n):
    sum=0
    for i in range(0,len(n)):
        sum+= n[i]
    return sum

print( total(nn))


n = ["Michael", "Lieberman"]

def join_strings(n):
    str=''
    for i in range(0,len(n)):
        str+=n[i]
    return str

print( join_strings(n))

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(m,n):
    m.extend(n)
    return m

print( join_lists(m,n))

"""
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

import types
def flatten(n):
    sumlist=[]
    for i in range(0,len(n)):
        if type(n[i]) == types.ListType:
            print( ">>"+str(len(n[i])))
            for j in range(0,len(n[i])):
                sumlist.append(n[i][j])
    return sumlist   
print( flatten(n))
"""
#Loop

count =0

if count < 5 :
    print( "if commnder", count)

while count <= 9:
    print( "while commnder", count)
    count +=1

num =1
while num <=10:
    print( num**2)
    num+=1

# input �Է��� �־ shell �� ����� �׷��� �ϴ� �ּ�
'''
choice = raw_input("enjoying the course? (y/n)")
while choice != 'y' and choice != 'n':
    choice = raw_input("enjoying the course? (y/n)")


from random import randrange
random_number = randrange(1,10)

count = 0

while count < 3:
    guess = raw_input("Enter a guess")
    if(guess == random_number):
        print( "You Win")
        break
    else:
        count+=1
else:
    print( "You lose")
'''

s = "A bird in the hand..."

for c in s:
    if c=='A' or c=='a':
        print( 'X',)
    else:
        print( c,)
print()
        
d = {'x': 9, 'y': 10, 'z': 20}

for key in d:
    print( key, d[key])


choices = ['pizza', 'pasta', 'salad', 'nachos']
for index,item in enumerate(choices):
    print( index+1,item)

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

# �Լ� zip�� �� ���� ����Ʈ�� ���޹޾� ����� ���� �����ϰ�,
# �� ª�� ���� ����Ʈ�� ���κп��� ������ ����ϴ�.
for a,b in zip(list_a,list_b):
    if a > b:
        print( a)
    else:
        print( b)
    


# dict
d = {
    "Name": "Guido",
    "Age": 56,
    "BDFL": True
}

print( d.items())

# ����Ʈ ����(list comprehension)
evens_to_50 =[i for i in range(51) if i % 2 ==0]
print( evens_to_50)

# 1���� 5������ ������ ���ڷ� �̷���� ����Ʈ new_list�� ����
new_list=[ x for x in range(1,6)]
print( new_list)

# �� ���ڵ��� �� ��� ����� �ʹٸ�, ������ ���� �ۼ�
doubles = [x*2 for x in range(1,6) ]
print( doubles)

# ���� �̷��� �� ��� ���� ���� �߿��� 3���� ������ �������� ���ڸ��� ����� �ʹ�
doubles_by3 = [x*2 for x in range(1,6) if (x*2)%3==0 ]
print( doubles_by3)

even_squares =[x**2 for x in range(1,11) if x%2==0]
print( even_squares)

cubes_by_four=[ x for x in range(1,11) if (x**3)%4==0 ]
print( cubes_by_four)

my_list = range(1, 11)
backwards = my_list[::-1]
print( backwards)

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print( backwards_by_tens)

to_21=range(1,22)
odds=to_21[::2]
print( odds)

middle_third= to_21[7:14]
print( middle_third)

#lambda
my_list = range(16)
print( filter(lambda x: x%3==0,my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print( filter(lambda x:x=='Python', languages))

squares=[x**2 for x in range(1,11)]
print( squares)
print( filter(lambda x: x>=30 and x<70, squares))


movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

print( movies.items())
for movie in movies.items():
    print( movie[0] ,":", movie[1])


threes_and_fives=[x for x in range(1,16) if x%3==0 or x%5==0]
print( threes_and_fives)

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
reverse_str = garbled[::-2]
print( reverse_str)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message=filter(lambda x: x!='X' ,garbled)
print( message)


# 2����
print( bin(1))
print( bin(2))
print( bin(3))
print( bin(4))
print( bin(5))
print( int( bin(0b1110 | 0b101) ,2))
