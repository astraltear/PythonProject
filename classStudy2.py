'''
Class fundamental
'''

class Car:
    handle = 0
    speed = 0

    def __init__(self,name,speed):
        print("constructor")
        self.name = name
        self.speed = speed

    def showData(self):
        km = '킬로미터'
        msg = '속도' +str(self.speed)+km
        return msg

print(Car.handle, Car.speed)
# name 변수는 Car에 존재하지 않는다 인스턴스 생성시 존재하게 된다
# print(Car.name)

print('\n car1----------------------')
car1 = Car('bus',10) #생성자 호출
print(car1.name,car1.handle,car1.speed)

car1.color='blue'
print('car1.color:',car1.color)

car99 = Car # 생성자 호출하지  않음

print('\n car2----------------------')
car2 = Car('taxi',50)
print(car2.name,car2.handle,car2.speed)
# print('car2.color:',car2.color) error

print(id(Car), id(car1), id(car2))

print('car1 :',car1.showData())
print('car2 :',car2.showData())

car1.speed = 88
print('car1 :',car1.showData())




