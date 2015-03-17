# -*- coding: utf-8 -*-
'''
    oracle과 연결하기 위해서는 python이 구동하는 OS에서 oracle client oci.dll 파일이 필요하며
    cx_Oracle 이라는  python library가 필요하다. 
'''
import cx_Oracle

IP = "111.222.333.90"
PORT = 1521
SID = "ora9"
UID = "user"
UPW = "pwd"

def getLiveVolume():
    rows = ()
    try :
        dsn = cx_Oracle.makedsn(IP, PORT, SID)
        connection = cx_Oracle.connect(UID, UPW, dsn)
        cur = connection.cursor()
        
        queryStr = ''' select distinct(a.involumeid) void, a.inmp3file, a.inwmafile
                    from installment a, livevolume b
                    where  b.lvvolumeid = a.involumeid
                    and lvregdate = to_char(sysdate -1, 'YYYYMMDD')
                    order by void asc '''
        
        cur.execute(queryStr)
        rows = cur.fetchall()

    except Exception, e :
        print e
    
    finally :
        cur.close()
        connection.close()
    
    return rows