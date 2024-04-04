class Stock:
    market="kospi"


print "dir():", dir()
print "Stock.market:", Stock.market
print "Stock.__dict__:",Stock.__dict__

s1 = Stock()
s2 = Stock()
print dir()

# empty dict
print s1.__dict__ , s2.__dict__

s1.market="kosdak"
print s1.__dict__ , s2.__dict__
print s1.market, s2.market

