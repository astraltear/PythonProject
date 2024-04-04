# -*- coding: UTF-8 -*-

class Animal(object):
    is_alive = True
    health="good"
    def __init__(self,name,age,is_hungry):
        self.name=name
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
        print "name: "+self.name
        print "age: "+str(self.age)

zebra=Animal('Jeffrey',2,True)
giraffe = Animal("Bruce",1,False)
panda = Animal("Chad",7,True)
hippo = Animal("Hippo",3,False)
sloth = Animal("sloth",2,True)
ocelot = Animal("ocelot",10,True) 

print zebra.name, zebra.age, zebra.is_hungry, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_hungry, giraffe.is_alive
print panda.name, panda.age, panda.is_hungry, panda.is_alive

hippo.description()

print sloth.health
print ocelot.health


class ShoppingCart(object):
    items_in_cart={}

    def __init__(self,customer_name):
        self.customer_name = customer_name

    def add_item(self,product,price):
        if not product in self.items_in_cart:
            self.items_in_cart[product]=price
            print product +" added."
        else:
            print product+" is already in the cart."

    def remove_item(self,product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product +" removed."
        else:
            print product+" is not in the cart."


my_cart= ShoppingCart("Choi")
my_cart.add_item("lemon",4000)

print my_cart.items_in_cart


#상속
class Customer(object):
    def __init__(self,customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "your shopping cart!"


class ReturningCustomer(Customer):
    def display_order_history(self):
        print "your order history!"


monty_python=ReturningCustomer("ID:12345")
monty_python.display_cart()
monty_python.display_order_history()


class Shape(object):
    def __init__(self,number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3

# method override
class Employee(object):
    def __init__(self):
        pass
        #self.employee_name=employee_name

    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):

    def __init__(self):
        pass

    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 12.00

    # call super method
    def full_time_wage(self,hours):
        return super(PartTimeEmployee,self).calculate_wage(hours)


agent = Employee()
print "agent salary: "+str(agent.calculate_wage(4))

partTime = PartTimeEmployee()
print "part time salary:"+str( partTime.calculate_wage(4) )
print "part tiem full salary: "+str( partTime.full_time_wage(4) )

milton = PartTimeEmployee()
print "part tiem full salary: "+str( milton.full_time_wage(10) )


class Car(object):
    def __init__(self,model,color,mpg):
        print "Car INIT ",model, color,mpg

class ElectricCar (Car):
    def __init__(self,model,color,mpg,battery_type):
        super(ElectricCar,self).__init__(model,color,mpg)
    
car =Car("A","red",100)
eCar = ElectricCar("B","blue",200,"battery")

class Point3D(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __repr__(self):
        return str(self.x)+str(self.y)+str(self.z)

my_point=Point3D(1,2,3)
print my_point









