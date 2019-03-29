'''
Created on 13 Mar. 2018

@author: Amit.Kumar1
'''
import sqlite3

conn = sqlite3.connect('C:/Users/Amit.Kumar1/dbfiles/myTestdb.db')
cur = conn.cursor()

cur.execute("select * from stocks where symbol = 'RHAT'")
for row in cur:
    print(row)
