'''
sqlite2
'''

import sqlite3
import random
def func(dbName):
    try:
        conn = sqlite3.connect(dbName)
        cur = conn.cursor()
        
#         cur.execute('create table IF NOT EXISTS emp (id integer primary key, name text ) ')
        cur.execute('create table IF NOT EXISTS emp (id integer , name text ) ')
        
        for i in range(10):
            query = "insert into emp values(?,?)"
            cur.execute(query,( random.randint(0,20),'KIM'))
        
        query = "insert into emp values(?,?)"
        tdata = (4,'LEE')
        cur.execute(query,tdata)
        
        query = "insert into emp values(?,?)"
        tdatas = ((4,'LEE'),(9,'LEE'))
        cur.executemany(query,tdatas)
        
        query = "insert into emp values(?,?)"
        ldata = [(59,'LEE')]
        cur.executemany(query,ldata)
        
        query = "insert into emp values(?,?)"
        ldatas = [(4,'LEE'),(9,'LEE')]
        cur.executemany(query,ldatas)
        
        # not allow set
#         query = "insert into emp values(?,?)"
#         sdata = {4,'LEE'}
#         cur.executemany(query,sdata)
        
        query = "insert into emp values(:sabun,:irum)"
        ddata = {'sabun':99,'irum':'HAN'}
        cur.execute(query,ddata)
        
        query = "select * from emp where id=99"
        cur.execute(query)
        
        
        datas = cur.fetchall()
        print(datas)
        print(datas[0][1])
        
    except sqlite3.Error as err:
        print(err)
    
    finally:
        conn.commit()
        cur.close()
        conn.close()
    
if __name__ =='__main__':
    func('goods.db')    
    