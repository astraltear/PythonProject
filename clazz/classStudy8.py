'''
parent class
'''

class Animal():
    age = 0

    def move(self):
        print('move animal')

class Dog(Animal):
    def my(self):
        print('I\'m dog')


dog1 = Dog()
dog1.my()
dog1.move()

dog1.age=30
print(dog1.age)

class Horse(Animal):
    pass

horse1 = Horse()
horse1.move()
