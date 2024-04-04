'''
variable global local scope
variable reference sequence
local > enclosing func > global

'''

player = 'world player'

def FuncSoccer():
    name="Hone"
    player = 'local player'
    print(name,player)

FuncSoccer()
print(player)

a=10
b=20
c=30
def Foo():
    a=40
    b= 35
    c=7

    def Bar():
        global  c
        print("a:{}, b:{}, c:{}".format(a,b,c))

    Bar()


Foo()

v1 = 1
def Vartest(v1):
    v1 = v1+1
    print('local v1', v1)

    v2 = v1
    v2 = v2+v1
    print('local v2', v2)

Vartest(v1)
print('global v1', v1)

g1 = 1
def gFunc():
    global  g1
    a = g1
    g1 = 2
    print(a, g1)
    print(id(a), id(g1))
    return a

print(gFunc())
