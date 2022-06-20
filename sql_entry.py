import mysql.connector as msql
def sql_entry(fname,mname,lname):
    from tkinter import StringVar

    ob = msql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Alpha@980',
    database ='raw'
    )     
    print("\nconnect success")
    ob1=ob.cursor()
    
    print("\nEnter in DataBase Success\n")
    ob1.execute("create table if not exists raw1( name varchar(20),name1 varchar(20),name2 varchar(20))")
    print("TABLE DETAILS\n")    
    ob1.execute("insert into raw1 values (%s,%s,%s)",(fname,mname,lname)) 
    ob.commit()
    ob.close()
    print("TABLE DETAILSsssssss")