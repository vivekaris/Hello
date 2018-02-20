import sqlite3

conn = sqlite3.connect('iot.db')
#print "Opened database successfully";



cursor = conn.execute("SELECT * from student")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("Contact = ", row[3])
   print("\n")


print ("Operation done successfully");
conn.close()

conn.close()