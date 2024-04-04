'''
self
'''

kor = 100

def abc():
    print('function!')

class My:
    kor = 90

    def abc(self):
        print('method')

    def show(self):
        kor = 77
        print(self.kor)  # 90
        print(kor)       # 77
        self.abc()      # method
        abc()           # function!


m = My()
m.show()
