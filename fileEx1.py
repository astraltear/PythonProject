'''
C:\Users\choiyj\projects\PycharmProj\Python3\read.txt
'''

import os

try:
    #f = open('C:\Users\choiyj\projects\PycharmProj\Python3\read.txt','r')
    f = open(os.getcwd()+'/read.txt',mode='r')
    #f.read()
    #f.readline()

    for i in f:
        print(i)

    f.close()

    fw = open(os.getcwd()+'/read.txt',mode='a')
    fw.write('test write\n')
    fw.close()

    import glob
    files  = glob.glob('*.txt')
    #files  = glob.glob('*')
    #files  = glob.glob('?????.txt')
    for file in files:
        print(file)



except Exception as e:
    print(e)
finally:
    pass
