'''
Created on 2014. 2. 20.

@author: Choi
'''
s = set([3,5,90,23])
t = set("RequestHandle")

print t

a = s & t
print a

b = s | t
print b

c = s - t
print c

d = s ^ t
print d

t.add('X')
s.update([12,34,54])

print t
print s

t.remove('H')

print t