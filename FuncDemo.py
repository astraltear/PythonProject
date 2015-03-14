def foo(a, b=3):
    print('a:', a,'b:', b )

foo(1,2)
foo(7)
foo(b=90, a=20)

def foo2(*args):
    for i in args:
        print i
    print("\n")

foo2(1,2,3,4)