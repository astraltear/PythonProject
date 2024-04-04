'''
    class
        접근지정자, method overloading 없음
'''

class TestClass:
    var1  = 1

    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')

    def printMessage(self):
        name="korean"
        print(name,self.var1)



if __name__ =='__main__':

    test = TestClass()
    print(test.var1)

    test2 = TestClass
    test2().printMessage() #Bound method call

    TestClass.printMessage(test) #UnBound method call

    TestClass.printMessage() # Error
