'''
Method Override
'''
class Parent:
    def printData(self):
        print('parent method')


class Child1(Parent):
    def printData(self):
        print('child method override')

c1 = Child1()
c1.printData()


c2 = c1

print(id(c2), id(c1))

par = Parent()
par = c1
par.printData()


for i in [c1, c2]:
    i.printData()