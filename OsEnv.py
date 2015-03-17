'''
Created on 2014. 3. 10.

@author: Choi
'''
import os
s = os.environ['PATH']

print s

print os.name, "\n"

import time

print time.clock(), time.gmtime(time.time()) 
