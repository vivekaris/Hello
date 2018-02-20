import sqlite3

conn = sqlite3.connect('iot.db')
#print "Opened database successfully";


rn=input("ID: ")
name=input("Enter Name : ")
contact=input("Contact Num : ")
age=input("Enter Age : ")


conn.execute("insert into student (ID,NAME,AGE,contact) VALUES (?,?,?,?)",(rn,name,age,contact));
print("successfully");
conn.commit()

conn.close()