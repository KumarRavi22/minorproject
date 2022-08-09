
from os import name
import tkinter as tk
from tkinter import Image, Label, Listbox, Message, StringVar, Tk, ttk,messagebox
from tkinter import font
from tkinter.constants import COMMAND, HORIZONTAL, TRUE
import st_msql as mng
from PIL import ImageTk,Image




window = tk.Tk()
def add():
    if var1.get()=="" and var2.get()=="" and var3.get()=="" and var4.get()=="" and var5.get()=="" and var6.get()=="" and var7.get()=="":
        messagebox.showerror("insert status","All fields are compulsor")
    else:
        rll=int(var1.get())
        nm=var2.get()
        cl=var3.get()
        con=int(var4.get())
        fn=var5.get()
        addr=var6.get()
        gen=var7.get()
        show()
        mng.database(rll,nm,cl,con,fn,addr,gen)
        messagebox.showinfo("inserted status","data is inserted succesfully")
    




window.geometry("1350x700+60+80")
#img= ImageTk.PhotoImage(Image.open("C:/Users/Dell/Desktop/BCA/minor.png"))
#image1 = Label(image=img)
#image1.pack()


var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()




window.resizable(width=True,height=True)
window.configure(bg="#856ff8")
window.title('Student Management System')

l1 = tk.Label(window,text="Student Management System",font=("Arial", 30,"bold","underline"),fg="black",bg="yellow")
l1.pack(side=tk.TOP)

#pic = tk.PhotoImage(file="C:/Users/Dell/Desktop/BCA/minor.png",width="1500",height="800")
#gLabel = tk.Label(image=pic).pack(side="top")


f=tk.LabelFrame(window,text="Detail",font=("Arial",25),bg="#C9BE92",relief=tk.GROOVE)
f.place(x=20,y=100,width=420,height=560)

roll_no=tk.Label(f,text="Rollno",font=("Arial",17))
roll_no.grid(row=0,column=0,padx=2,pady=2)
roll_ent=tk.Entry(f,bd=7,textvariable=var1)
roll_ent.grid(row=0,column=1,padx=2,pady=2)

name1=tk.Label(f,text="Name",font=("Arial",17))
name1.grid(row=1,column=0,padx=2,pady=2)
name1=tk.Entry(f,bd=7,textvariable=var2)
name1.grid(row=1,column=1,padx=2,pady=2)

class1=tk.Label(f,text="Class",font=("Arial",17))
class1.grid(row=2,column=0,padx=2,pady=2)
class1=tk.Entry(f,bd=7,textvariable=var3)
class1.grid(row=2,column=1,padx=2,pady=2)

contact1=tk.Label(f,text="Contact",font=("Arial",17))
contact1.grid(row=3,column=0,padx=2,pady=2)
contact1=tk.Entry(f,bd=7,textvariable=var4)
contact1.grid(row=3,column=1,padx=2,pady=2)
fname=tk.Label(f,text="F_Name",font=("Arial",17))
fname.grid(row=4,column=0,padx=2,pady=2)
fname=tk.Entry(f,bd=7,textvariable=var5)
fname.grid(row=4,column=1,padx=2,pady=2)


ad=tk.Label(f,text="Address",font=("Arial",17))
ad.grid(row=5,column=0,padx=2,pady=2)
ad=tk.Entry(f,bd=7,textvariable=var6)
ad.grid(row=5,column=1,padx=2,pady=2)

ge=tk.Label(f,text="Gender",font=("Arial",17))
ge.grid(row=6,column=0,padx=2,pady=2)
ge=ttk.Combobox(f,font=("Arial",15),textvariable=var7)
ge['values']=("Male","Female","Others")
ge.grid(row=6,column=1,padx=2,pady=2)


#######Buttons of frame details########################################
def clear():
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    var6.set("")
    var7.set("")
####################################################################

def delete():
    import mysql.connector as mysl
    if var1.get()=="":
        messagebox.showinfo("Deleted status","ROLLNO is compulsory for delete")
    else:
        con=mysl.connect(
            host='localhost',
            user='root',
            password='Rishu@123',
            database='gaurav'
        )
        cursor=con.cursor()
        cursor.execute("delete from managem where rollno='"+var1.get()+"'")
        cursor.execute("commit")
        var1.set("")
        show()
        messagebox.showinfo("Deleted status","Deleted succesfully")
        con.close()


########################################################
def update():
        rll1=var1.get()
        nm2=var2.get()
        cl3=var3.get()
        con4=var4.get()
        fn5=var5.get()
        addr6=var6.get()
        gen7=var7.get()
        import mysql.connector as mysl
        if(rll1=="" or nm2=="" or cl3=="" or con4=="" or fn5=="" or addr6=="" or gen7==""):
            messagebox.showinfo("update status","ROLLNO and contact is compulsory for for update")
        else:
            con=mysl.connect(
                host='localhost',
                user='root',
                password='Rishu@123',
                database='gaurav'
            )
            cursor=con.cursor()
            cursor.execute("update managem set name='"+nm2+"',class='"+cl3+"',contact='"+con4+"',f_name='"+fn5+"',address='"+addr6+"',gender='"+gen7+"' where rollno='"+rll1+"'")
            cursor.execute("commit")
            show()
            messagebox.showinfo("update status","update succesfully")
            con.close()

########################################################################################

def show():
    import mysql.connector as mysl
    con=mysl.connect(
        host='localhost',
        user='root',
        password='Rishu@123',
        database='gaurav'
    )
    cur=con.cursor()
    cur.execute("select * from managem")
    rows=cur.fetchall()
    mf.delete(0,mf.size())
    for row in rows:
        insertedData=str(row[0])+'     '+ row[1]+'  '+row[2]+'  '+str(row[3])+'  '+row[4]+'   '+row[5]+'   '+row[6]
        mf.insert(mf.size()+1,insertedData)
    con.commit()    
    con.close()





















#################################################################################################
b1=tk.Button(f,text="ADD",font=("Arial",13,"bold"),width=15,command=add)
b1.grid(row=8,column=0,padx=2,pady=2)

up=tk.Button(f,text="UPDATE",font=("Arial",13,"bold"),width=15,command=update)
up.grid(row=8,column=1,padx=5,pady=5)

del1=tk.Button(f,text="DELETE",font=("Arial",13,"bold"),width=15,command=delete)
del1.grid(row=9,column=0,padx=2,pady=2)


cl=tk.Button(f,text="CLEAR",font=("Arial",13,"bold"),width=15,command=clear)
cl.grid(row=9,column=1,padx=2,pady=2)



f2=tk.Frame(window,bg="yellow",relief=tk.GROOVE)
f2.place(x=460,y=100,width=850,height=560)

 
sf=tk.Frame(f2,bg="red",border=10,relief=tk.GROOVE)
sf.pack(side=tk.TOP,fill=tk.X)


sr=tk.Label(sf,text="DISPLAY",font=("Arial",14,"bold"),bg="red")
sr.grid(row=0,column=0,padx=12,pady=2)

#sin=ttk.Combobox(sf,font=("Arial",14))
#sin['value']=("Name","Rollno","Class","F_Name")
#sin.grid(row=0,column=1,padx=12,pady=2)


#######Buttons of frame2##########

#sb=tk.Button(sf,text="SEARCH",font=("Arial",13,"bold"),width=15,bd=9)
#sb.grid(row=0,column=2,padx=12,pady=2)

#sa=tk.Button(sf,text="SHOW ALL",font=("Arial",13,"bold"),width=15,bd=9)
#sa.grid(row=0,column=3,padx=12,pady=2)

mf=Listbox(f2,bg="#F3E5AB",bd=11,relief=tk.GROOVE)
mf.pack(fill=tk.BOTH,expand=True)
show()

#list=Listbox(mf)
#list.grid(row=0,column=8)
#st=ttk.Treeview(mf,columns=("Rollno","Name","Class","Contact","F_Name"))
#st.pack(fill=tk.BOTH,expand=True) 
#st.heading("Rollno",text="Rollno")
#st.heading("Name",text="Name")
#st.heading("Class",text="Class")
#st.heading("Contact",text="Contact")
#st.heading("F_Name",text="F_Name")

window.mainloop()


