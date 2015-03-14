import Module1

def getName() :
    return __name__

if __name__ == '__main__':
    print "Call Module1 Main:", getName()
    print "module_test:", Module1.getName()