from tkinter import Tk

from mysql.connector.connection import MySQLConnection


def database(roll,name,class1,contact,f_name,address,gender):
    import mysql.connector as msql
    roll=roll
    name=name
    class1=class1
    contact=contact
    f_name=f_name
    address=address
    gender=gender
    
    obj=msql.connect(
        host='localhost',
        user='root',
        password='Rishu@123',
        database='gaurav'
    )
    print("table created")
    cursor_obj=obj.cursor()
    cursor_obj.execute("create table if not exists managem(rollno integer(20),name varchar(20),class varchar(20),contact integer(20),f_name varchar(20),address varchar(30),gender varchar(30))")
    print("table created")
    cursor_obj.execute("insert into managem values(%s,%s,%s,%s,%s,%s,%s)",(roll,name,class1,contact,f_name,address,gender))
    obj.commit()
    print("n\n\n\n\\connection succesful\\n\n\n\n")
   # fr=cursor_obj.execute("select * from manage")
#def a():

 #   c1=obj.cursor()
  #  a1=cursor_obj.execute("truncate table manage")
#