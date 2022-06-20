#pip install mysql-connector
def database(name,date,month,year,age):
  name=name
  date=date
  month=month
  year=year
  age=age
 
  import mysql.connector as msql

  obj=msql.connect(
  host='localhost',
  user='root',
  password='Alpha@980',
  database='book'
  )
  print("table created")
  cursor_obj=obj.cursor()
  cursor_obj.execute("create table if not exists age (name varchar(20),date integer(20),month integer(20),year integer(20),calulatedage integer(20))")
  print("table created")
  cursor_obj.execute("insert into age values(%s,%s,%s,%s,%s)",(name,date,month,year,age))
  obj.commit()
  print("n\n\n\n\\connection succesful\\n\n\n\n")


  