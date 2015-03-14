import Module1
from datepac import today as td

def getName() :
    return __name__

if __name__ == '__main__':
    print "Call Module1 Main:", getName()
    print "module_test:", Module1.getName()
    
    print td.fullDate()
    print "%s-%s-%s" % (td.getDate(), td. getMonth(), td.getYear())