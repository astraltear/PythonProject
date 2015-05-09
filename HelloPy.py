'''
Created on 2015. 5. 8.

@author: choiyj
'''


def greeting(hour,morning_msg="hello"):
    if hour <9:
        print morning_msg
    elif hour < 12:
        pass
    
    else:
        print morning_msg
    


greeting(7)
greeting(14, "test")

