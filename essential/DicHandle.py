'''
Created on 2014. 2. 26.

@author: Choi
'''
stock={
       "name":"GPGP",
       "shares":100,
       "price":490.10
       }

print stock["name"]

stock["name"]="AAAA"

print stock["name"]

prices ={
         "GOOG" : 490.10,
         "AAPL" : 123.50,
         "IBM"  : 91.50,
         "MSFT" :  52.13,
         "SCOX" : 34.30
}

if "SCOX" in prices:
    p = prices["SCOX"]
else: 
    p = 0.0
    
print p

p = prices.get("SCOXE",0.0)
print p

del prices["MSFT"]

print list(prices)