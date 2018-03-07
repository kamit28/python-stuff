'''
Created on 28 Feb. 2018

@author: Amit.Kumar1

example for SQL Server DB access using pymssql module
'''
import pymssql

conn = pymssql.connect("host:port", "user-name", "password", "db-name")

cursor = conn.cursor()

## Table create example 
''' create table emp_007  '''
sql = """CREATE TABLE dbo.emp_007 (
   FIRST_NAME  VARCHAR(20) NOT NULL,
   LAST_NAME  VARCHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""
cursor.execute(sql)
conn.commit()

count_sql = "SELECT count(1) FROM dbo.emp_007"

cursor.execute(count_sql)
for row in cursor:
    print('row= %r' % (row,))

# Insert row example
insert_sql = "INSERT INTO dbo.emp_007 VALUES (%s, %s, %d, %s, %d)"
args = ('Amit', 'Kumar', 38, 'M', 7700.50)
try:
    cursor.execute(insert_sql, args)
    conn.commit()
except Exception as ex:
    print("Exception Occured" + str(ex))
    conn.rollback()

cursor.execute(count_sql)
for row in cursor:
    print('row= %r' % (row,))

# Select row example
select_sql = "SELECT * FROM dbo.emp_007 where AGE=%d"
cursor.execute(select_sql, 38)

for row in cursor:
    print('row= %r' % (row,))

## Update example
update_sql = "UPDATE emp_007 SET INCOME = %d WHERE FIRST_NAME = %s"
try:
    cursor.execute(update_sql, (7900.00, "Amit"))
    conn.commit()
except pymssql.DatabaseError as dbe:
    print(str(dbe))
    conn.rollback()

# select then insert
count_sql = "SELECT count(1) FROM dbo.emp_007 where FIRST_NAME=%s"
cursor.execute(count_sql, "Anshu")
count = cursor.fetchone()[0]
if count == 0:
    insert_sql = "INSERT INTO dbo.emp_007 VALUES (%s, %s, %d, %s, %d)"
    args = ('Anshu', 'Kumari', 35, 'F', 5600.80)
    try:
        cursor.execute(insert_sql, args)
        conn.commit()
    except Exception as ex:
        print("Exception Occured" + str(ex))
        conn.rollback()

count_sql = "SELECT count(1) FROM dbo.emp_007"

cursor.execute(count_sql)
for row in cursor:
    print('row= %r' % (row,))
    
#Drop table
drop_sql = "DROP TABLE emp_007"
cursor.execute(drop_sql)
conn.commit()

# Close the cursor
cursor.close()

#close the connection
conn.close()
