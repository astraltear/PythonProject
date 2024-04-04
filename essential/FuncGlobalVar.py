# -*- coding: utf-8 -*-
ga = 1

def edit_a(i):
    #ga = i  # ga는 로컬 변수로 인식한다. 
    #print "innner function: ",ga
    
     # global 을 선언해야 한다 
    global ga 
    ga = i
   
    
edit_a(4)
print ga
    