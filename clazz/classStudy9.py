'''
inherit
'''

class Person:
    say ='I am man'
    age = '20'

    def __init__(self,age):
        print('Person Constructor')
        self.age = age

    def printInfo(self):
        print('age:{} , say:{}'.format(self.age,self.say))


    def Hello(self):
        print('Hello!!!!!', self.subject)





class Employee(Person):
    say = 'working animal'
    subject = 'worker'

    def __init__(self):
        print('Employee Constructor')
        super().__init__(self.age)

    def ePrintInfo(self):
        self.printInfo()
        super().printInfo()
        print(self.say, super().say)

e = Employee()
print(e.say, e.age,e.subject)

e.printInfo()
e.Hello()

e.ePrintInfo()


class Worker(Person):
    def __init__(self,age):
        print('Worker Constructor')
        super().__init__(age)



w = Worker(30)

class Programmer(Worker):
    def __init__(self,age):
        print('Programmer Constructor')
        super().__init__(age)  #Bound Call
        Worker.__init__(self, age) # UnBound Call

p = Programmer(33)

print(type(p))
print(Person.__bases__)
print(Programmer.__bases__)
