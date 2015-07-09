prices={"banana":4, "apple":2,"orange":1.5,"pear":3}
stock={"banana":6, "apple":0,"orange":32,"pear":15}

'''
for item in prices.items():
    print item
'''

sum =0
for key in prices:
    sum= sum+prices[key]*stock[key]
    print key
    print "price: "+str(prices[key])
    print "stock: "+str(stock[key])
    print

print "sum: "+str(sum)



groceries=["banana","orange","apple"]

def compute_bill(goodsList):
    total=0
    for goods in goodsList:
        if stock[goods] != 0:
            total+= prices[goods]
            stock[goods]-=1
    return total


print compute_bill(groceries)
print stock
