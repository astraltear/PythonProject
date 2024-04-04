'''
use sqlite
'''

import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version_info)

# conn = sqlite3.connect(':memory')
conn = sqlite3.connect('nice.db')
cursor = conn.cursor()

query = 'create table IF NOT EXISTS fri(name text(10), phone text(15), address text ) '

cursor.execute(query)

#query2 = ["insert into fri values('abc','010-222-3333','seoul 122')","insert into fri values('def','010-222-3333','seoul 122')"]
query2 = "insert into fri values('abc','010-222-3333','seoul 122')"
cursor.execute(query2)

query2 = "insert into fri values('def','010-5555-6666','seoul 9999')"
cursor.execute(query2)

query3 = "select * from fri"
cursor.execute(query3)
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchall())
print(cursor.fetchall())

query3 = "select * from fri"
cursor.execute(query3)
for r in cursor:
    print(r[0], r[1],r[2])