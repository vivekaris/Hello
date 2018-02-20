import sqlite3

conn = sqlite3.connect('iot.db')
#print ("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS astudent
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         contact        CHAR(50));''')
print ("Table created successfully")




conn.close()