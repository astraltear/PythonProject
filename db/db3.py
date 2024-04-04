'''
remote db connection by maria db
'''

import mysql.connector
from mysql.connector import errorcode

config ={
         'user':'root',
         'password':'root',
         'host':'localhost',
         'database': 'test',
         'port':'3306'
}

try:
    conn = mysql.connector.connect(**config)
    print(conn)
    cur = conn.cursor();
    
    sql = 'select * from sangdata'
    
    cur.execute(sql)
    
    for item in cur:
        print(item[0], item[1],item[2])
    #print(cur.fetchall())
    
    sql_insert = "insert into sangdata values(%s,%s,%s,%s)"
    
    tdata =(4,'커피',5,300)
    cur.execute(sql_insert,tdata)
    
    conn.commit()

except mysql.connector.Error as mysqlError:
    if mysqlError.errorno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('접근 오류') 
        
    elif mysqlError.errorno == errorcode.ER_BAD_DB_ERROR:
        print('DB ERROR!~!!!') 
    
    else:
        print('other error',mysqlError)    
    
finally:
    cur.close()
    conn.close()
        






