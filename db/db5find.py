'''
search
'''

import mysql.connector


config ={
         'user':'root',
         'password':'root',
         'host':'localhost',
         'database': 'test',
         'port':'3306'
}



try:
    
    search_txt="ew"
    
    conn = mysql.connector.connect(**config)

    cur = conn.cursor();
    sql_select ="select * from pymem where name like '%{0}%' ".format(search_txt)
    cur.execute(sql_select)
    
    print(cur.fetchall())
    
except Exception as err:
    print('reading err!!',err)

finally:
    cur.close()
    conn.close()