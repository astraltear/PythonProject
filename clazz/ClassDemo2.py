# -*- coding: utf-8 -*-
class Test:
    # 생성자 역할
    def __init__(self,name):
        self.name=name
                
    def info(self):
        return self.name
    
    # 소멸자
    def __del__(self):
        print("%s 인스턴스 소멸" % self.name)
        
    def __add__(self,other):
        print(self.name+" and "+other.name+" together")
    
s = Test("한양대학교")
print s.info()

s1 = Test("건국대학교")
s+s1