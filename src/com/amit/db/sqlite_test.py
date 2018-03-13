'''
Created on 13 Mar. 2018

@author: Amit.Kumar1
'''
import sqlite3

conn = sqlite3.connect('<path/to/db/file/dbfile.db>')
cur = conn.cursor()

cur.execute('''create table stocks(
date text,
trans text,
symbol text,
qty real,
price real
)''')

cur.execute('''insert into stocks
values('2018-03-13', 'BUY', 'RHAT', 100, 135.11)
''')

conn.commit()
conn.close()
