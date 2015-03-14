def getDate():
    return "12"

def getMonth():
    return "03"

def getYear():
    return "2015"

def fullDate():
    return "%s-%s-%s" % (getDate(), getMonth(), getYear())

print "today module has called!!"

if __name__ == '__main__':
    print "%s-%s-%s" % (getDate(), getMonth(), getYear())
    pass