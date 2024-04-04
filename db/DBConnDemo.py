#-*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect('kospi.db')
cursor = con.cursor()

cursor.execute("drop table kospi")
cursor.execute("create table kospi(Name text, ClosingPrice int)")
cursor.execute("insert into kospi values('LG����', 74500)")
cursor.execute("insert into kospi values('���̹�', 774000)")
cursor.execute("INSERT INTO kospi VALUES('����', 169100)")

con.commit()
con.close()

con = sqlite3.connect('kospi.db')
cursor = con.cursor()

cursor.execute("select * from kospi")
for row in cursor:
    print row

cursor.execute("select * from kospi")
print "fetchone:", cursor.fetchone()

cursor.execute("select * from kospi")
listarr = cursor.fetchall()
print "fetchall:", listarr

for obj in listarr:
    print obj[0], obj[1]
