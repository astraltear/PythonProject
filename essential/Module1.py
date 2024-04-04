# -*- coding: utf-8 -*-

def getName() :
    return __name__

print ("Module1  print!!")
'''
이 파일을 단독실행 할때에만 아래의 코드가 작동한다.
'''
if __name__ == '__main__':
    print ("Module1 Main execute!")