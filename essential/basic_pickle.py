# -*- coding: utf-8 -*-

colors = ['red','green','black','blue','yellow']

import pickle
f = open('colors','wb')  # write binary
pickle.dump(colors, f)
f.close()

f2 = open('colors','rb')
colors2 = pickle.load(f2)   # read binary
f2.close()
print( colors2)