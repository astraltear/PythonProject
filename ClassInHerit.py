# -*- coding: utf-8 -*-

class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age = age
        print 'Initialized SchoolMember:{} !!'.format(self.name)
        
    def tell(self):
        print "SchoolMember tell >>> Name:{} Age:{}".format(self.name, self.age)
        
class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print "Initialzed Teacher:{}".format(self.name)
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)
        
class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print "Initialzed Student:{}".format(self.name)
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks :"{:d}"'.format(self.marks)
        

t = Teacher("Jane",40,30000)
s = Student("rookie",20,100)

members=[t,s]
for member in members:
    member.tell()