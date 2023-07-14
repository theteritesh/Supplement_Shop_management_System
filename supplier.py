from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql

class supplierClass:
    
    def Add(self):
        if self.var_sup_invoice.get()=='':
            messagebox.showerror('Error','Invoice Field Are Required',parent=self.window)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Problem to Connect Database',parent=self.window)
                return

            try:
                query='create database sup_shop'
                mycursor.execute(query)
                query='use sup_shop'
                mycursor.execute(query)
                query='create table supplier(invoice int primary key not null,name varchar(55),contact varchar(55))'
                mycursor.execute(query)
            except:
                mycursor.execute('use sup_shop')

            query='select * from supplier where invoice=%s'
            mycursor.execute(query,(self.var_sup_invoice.get()))

            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','Invoice Already Exists',parent=self.window)

            else:
                query='insert into supplier(invoice,name,contact ) values(%s,%s,%s)'
                mycursor.execute(query,(self.var_sup_invoice.get(),self.var_name.get(),self.var_contact.get()))
                con.commit()
                messagebox.showinfo("Success","Data Added Succesfully")
                self.show()
    def show(self):
        
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        

        try:
            query='select * from supplier'
            mycursor.execute(query)
            rows=mycursor.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)



        except:
            messagebox.showerror('Error','Problem to show info',parent=self.window)
            return

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']

        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        

    def Update(self):
        if self.var_sup_invoice.get()=='':
            messagebox.showerror('Error','Invoice Field Are Required',parent=self.window)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Problem to Connect Database',parent=self.window)
                return

            try:
                query='create database sup_shop'
                mycursor.execute(query)
                query='use sup_shop'
                mycursor.execute(query)
                query='create table supplier(invoice int primary key not null,contact varchar(55),name varchar(55),email varchar(55),user_type varchar(55),password varchar(55),salary varchar(55))'
                mycursor.execute(query)
            except:
                mycursor.execute('use sup_shop')

            query='select * from supplier where invoice=%s'
            mycursor.execute(query,(self.var_sup_invoice.get()))

            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Invoice',parent=self.window)

            else:
                query='Update supplier set name=%s ,contact=%s where invoice=%s'
                mycursor.execute(query,(self.var_name.get(),self.var_contact.get(),self.var_sup_invoice.get()))
                con.commit()
                messagebox.showinfo("Success","Data Updated Succesfully")
                self.show()
        
    def delete(self):
         con=pymysql.connect(host='localhost',user='root',password='')
         mycursor=con.cursor()
         mycursor.execute('use sup_shop')
         try:
            if self.var_sup_invoice.get()=='':
                messagebox.showerror('Error','Invoice Field Are Required',parent=self.window)
            else:
                query='select * from supplier where invoice=%s'
                mycursor.execute(query,(self.var_sup_invoice.get()))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Invoice',parent=self.window)
                else:
                    op=messagebox.askyesno("Conform","Do You really Want To Delete")
                    if op==True:
                        query='delete from supplier where invoice=%s'
                        mycursor.execute(query,(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Data Deleted Succesfully")
                        self.clear()
         except:
            messagebox.showerror('Error','Problem to delete info',parent=self.window)
            return
         

    def clear(self):

        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        try:
            
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice no. should be required",parent=self.window)
            else:               
                query='select * from supplier  where invoice=%s'
                mycursor.execute(query,(self.var_searchtxt.get()))
                row=mycursor.fetchone()
                if row !=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.window)

        except:
            messagebox.showerror("Error","Problem to Search Info",parent=self.window)

#------------------------------------------------------------------------------
    def __init__(self,window):

        self.window=window
        self.window.title("SUPPLIER")
        self.window.geometry("1100x500+220+130")
        self.window.config(bg='white')
        self.window.focus_force()

        #All variable
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()


        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()

        #search bar

        searchframe=LabelFrame(self.window,text="Search Supplier",font=("goudy old style",12,"bold"),bg='white')
        searchframe.place(x=250,y=20,width=600,height=70)

        #option

        search_lbl=Label(searchframe,text="Search By Invoice No.",font=('goudy old style',14),bg="white")
        search_lbl.place(x=10,y=10)

        text_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",13),bg="lightyellow")
        text_search.place(x=200,y=10)

        btn_search=Button(searchframe,text="Search",font=("goudy old style",12),bg="green",fg="white",command=self.search)
        btn_search.place(x=400,y=8,width=150,height=25)

        #title

        title=Label(self.window,text='Supplier Details',font=('Georgia',15),bg='Gray14',fg='White')
        title.place(x=50,y=100,width=1000)

        #content
        #row1

        emp_spplier_invoice=Label(self.window,text='Invoice No. :-',font=('Georgia',15),bg='White')
        emp_spplier_invoice.place(x=50,y=150)

        emp_spplier_invoice_entry=Entry(self.window,textvariable=self.var_sup_invoice,font=('Georgia',15),bg='lightyellow')
        emp_spplier_invoice_entry.place(x=150,y=150,width=180)

        #row2

        name_lbl=Label(self.window,text='Name :-',font=('Georgia',15),bg='White')
        name_lbl.place(x=50,y=190)    

        name_Entry=Entry(self.window,textvariable=self.var_name,font=('Georgia',15),bg='lightyellow')
        name_Entry.place(x=150,y=190,width=180)    

        #row3
        contact_lbl=Label(self.window,text='Contact :-',font=('Georgia',15),bg='White')
        contact_lbl.place(x=350,y=150) 

        contact_Entry=Entry(self.window,textvariable=self.var_contact,font=('Georgia',15),bg='lightyellow')
        contact_Entry.place(x=500,y=150,width=180)

        #Button

        btn_Add=Button(self.window,text="Save",font=("goudy old style",12),bg="deep sky blue",fg="white",command=self.Add)
        btn_Add.place(x=800,y=150,width=150,height=25)

        btn_Update=Button(self.window,text="Update",font=("goudy old style",12),bg="green",fg="white",command=self.Update)
        btn_Update.place(x=800,y=190,width=150,height=25)

        btn_Delete=Button(self.window,text="Delete",font=("goudy old style",12),bg="red",fg="white",command=self.delete)
        btn_Delete.place(x=800,y=230,width=150,height=25)

        btn_Clear=Button(self.window,text="Clear",font=("goudy old style",12),bg="gray",fg="white",command=self.clear)
        btn_Clear.place(x=800,y=270,width=150,height=25)

        #Supplier details

        emp_frame=Frame(self.window,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=330,relwidth=1,height=170)

        scroll_y=Scrollbar(emp_frame,orient=VERTICAL)
        scroll_x=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.supplierTable.xview)
        scroll_y.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice",text="Invoice")
        self.supplierTable.heading("name",text="NAME")
        self.supplierTable.heading("contact",text="CONTACT")

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        
        self.supplierTable["show"]="headings"
        self.supplierTable.pack(fill=BOTH,expand=1)

        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()




if __name__=="__main__":
    window=Tk()
    obj=supplierClass(window)
    window.mainloop()