'''
Created on 2014. 2. 20.

@author: Choi
'''
filename="E:\projects\IntegrateWorkSpace\PythonTest\primitive\inputdata.txt"
portfolio=[]

for line in open(filename):
    fields = line.split(",")
    name = fields[0]
    shares= int(fields[1])
    price = int(fields[2])
    stock = (name,shares,price)
    portfolio.append(stock)

for man in portfolio:
    print( man)
    print( man[0], man[1], man[2])

for name, shares, price in portfolio:
    print( "===>", name, shares,price)