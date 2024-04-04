'''
closure
scope에 제약을 받지 않는 변수들을 포함하고 있는 코드블럭
'''

def Times(a,b):
    c = a * b
    return c

print(Times(2, 3))
kbs = Times
print(kbs(2, 3))

del Times # func address delete
print(kbs)

def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())

out()

print('\nouter~~~~~~~~~~~')
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner  # this is closure

obj1 = outer()
print(obj1())
print(obj1())

print('\nouter2~~~~~~~~~~~')
def outer2(tax):
    def inner2(su,dan):
        amount = su* dan * tax
        return amount
    return inner2

r = outer2(0.2)
res1 = r(10,5000)
print(res1)

res2 = r(2,2000)
print(res2)


r2 = outer2(0.05)
res3 = r2(2,2000)
print(res3)
