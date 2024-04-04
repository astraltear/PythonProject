# -*- coding: utf-8 -*-

import time
print (time.time())     # 1970년 1월 1일 기준 누적된 초를 float로 반환
print (time.gmtime())   # utc 기준시간
print ( time.localtime()  ) # 시스템 기준 현재시간 
t = time.gmtime(1234567890)
print ( t )

curTime = time.localtime()
print ( curTime.tm_mon )
print ( curTime.tm_hour )
print ( time.asctime(curTime) )

t2 = time.time()
time.sleep(4)
t3 = time.time()
spendtime = t3-t2
print( "wait {0} seconds".format(spendtime) )

import datetime
print( datetime.date(2015,6,7) )
print( datetime.date.fromtimestamp(time.time()) )
print( datetime.date.today() )
print( datetime.timedelta(days=-3) )