'''
function decorator
'''
def Deco1(f):
    return lambda: f() + 5

def Deco2(f):
    def print_f():
        print(f())
    return print_f

def Func():
    return 3

f = Deco2(Deco1(Func))
f()

# use decorator

@Deco2
@Deco1
def Func2():
    return 3

Func2()

#recursive call
def CountDown(n):
    if n== 1:
        print('END')
        return True
    return n * CountDown(n-1)

print(CountDown(10))