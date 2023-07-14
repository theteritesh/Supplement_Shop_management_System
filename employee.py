from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
 
class employeeClass:
    
    def Add(self):
        if self.var_emp_id.get()=='':
            messagebox.showerror('Error','Emp_Id Field Are Required',parent=self.window)
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
                query='create table userinfo(emp_id int primary key not null,contact varchar(55),name varchar(55),email varchar(55),user_type varchar(55),password varchar(55),salary varchar(55))'
                mycursor.execute(query)
            except:
                mycursor.execute('use sup_shop')
                

            query='select * from userinfo where emp_id=%s'
            mycursor.execute(query,(self.var_emp_id.get()))

            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','Emp_ID Already Exists',parent=self.window)

            else:
                query='insert into userinfo(emp_id,contact  ,name  ,email  ,user_type  ,password  ,salary  ) values(%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(self.var_emp_id.get(),self.var_contact.get(),self.var_name.get(),self.var_email.get(),self.var_user_type.get(),self.var_password.get(),self.var_salary.get()))
                con.commit()
                messagebox.showinfo("Success","Data Added Succesfully")
                self.show()
    def show(self):
        
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()

        try:
                query='create database sup_shop'
                mycursor.execute(query)
                query='use sup_shop'
                mycursor.execute(query)
                query='create table userinfo(emp_id int primary key not null,contact varchar(55),name varchar(55),email varchar(55),user_type varchar(55),password varchar(55),salary varchar(55))'
                mycursor.execute(query)
        except:
                mycursor.execute('use sup_shop')

        
        try:
            query='select * from userinfo'
            mycursor.execute(query)
            rows=mycursor.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)



        except:
            messagebox.showerror('Error','Problem to show info',parent=self.window)
            return

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']

        self.var_emp_id.set(row[0])
        self.var_contact.set(row[1])
        self.var_name.set(row[2])
        self.var_email.set(row[3])
        self.var_user_type.set(row[4])
        self.var_password.set(row[5])
        self.var_salary.set(row[6])

    def Update(self):
        if self.var_emp_id.get()=='':
            messagebox.showerror('Error','Emp_Id Field Are Required',parent=self.window)
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
                query='create table userinfo(emp_id int primary key not null,contact varchar(55),name varchar(55),email varchar(55),user_type varchar(55),password varchar(55),salary varchar(55))'
                mycursor.execute(query)
            except:
                mycursor.execute('use sup_shop')

            query='select * from userinfo where emp_id=%s'
            mycursor.execute(query,(self.var_emp_id.get()))

            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Emp_ID',parent=self.window)

            else:
                query='Update userinfo set contact=%s  ,name=%s  ,email=%s  ,user_type=%s  ,password=%s  ,salary=%s where emp_id=%s'
                mycursor.execute(query,(self.var_contact.get(),self.var_name.get(),self.var_email.get(),self.var_user_type.get(),self.var_password.get(),self.var_salary.get(),self.var_emp_id.get()))
                con.commit()
                messagebox.showinfo("Success","Data Updated Succesfully")
                self.show()
        
    def delete(self):
         con=pymysql.connect(host='localhost',user='root',password='')
         mycursor=con.cursor()
         mycursor.execute('use sup_shop')
         try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error','Emp_Id Field Are Required',parent=self.window)
            else:
                query='select * from userinfo where emp_id=%s'
                mycursor.execute(query,(self.var_emp_id.get()))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Emp_ID',parent=self.window)
                else:
                    op=messagebox.askyesno("Conform","Do You really Want To Delete")
                    if op==True:
                        query='delete from userinfo where emp_id=%s'
                        mycursor.execute(query,(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Data Deleted Succesfully")
                        self.clear()
         except:
            messagebox.showerror('Error','Problem to delete info',parent=self.window)
            return
         

    def clear(self):

        self.var_emp_id.set("")
        self.var_contact.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_user_type.set("Admin")
        self.var_password.set("")
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchBy.set("Select")
        self.show()

    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        try:
            if self.var_searchBy.get()=="select":
                messagebox.showerror("Error","Select search by option",parent=self.window)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.window)
            else:               
                query='select * from userinfo  where '+self.var_searchBy.get()+" Like '%"+self.var_searchtxt.get()+"%'"
                mycursor.execute(query)
                rows=mycursor.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.window)

        except:
            messagebox.showerror("Error","Problem to Search Info",parent=self.window)

#------------------------------------------------------------------------------
    def __init__(self,window):

        self.window=window
        self.window.title("Employee")
        self.window.geometry("1100x500+220+130")
        self.window.config(bg='white')
        self.window.focus_force()

        #All variable
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()


        self.var_emp_id=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_user_type=StringVar()
        self.var_salary=StringVar()

        #search bar

        searchframe=LabelFrame(self.window,text="Search Employee",font=("goudy old style",12,"bold"),bg='white')
        searchframe.place(x=250,y=20,width=600,height=70)

        #option

        combo_search=ttk.Combobox(searchframe,textvariable=self.var_searchBy,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=('goudy old style',10))
        combo_search.place(x=10,y=10,width=180)
        combo_search.current(0)

        text_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",13),bg="lightyellow")
        text_search.place(x=200,y=10)

        btn_search=Button(searchframe,text="Search",font=("goudy old style",12),bg="green",fg="white",command=self.search)
        btn_search.place(x=400,y=8,width=150,height=25)

        #title

        title=Label(self.window,text='Emplyee Details',font=('Georgia',15),bg='Gray14',fg='White')
        title.place(x=50,y=100,width=1000)

        #content
        #row1

        emp_id_lbl=Label(self.window,text='Emp Id :-',font=('Georgia',15),bg='White')
        emp_id_lbl.place(x=50,y=150)

        contact_lbl=Label(self.window,text='Contact :-',font=('Georgia',15),bg='White')
        contact_lbl.place(x=350,y=150) 

        emp_id_Entry=Entry(self.window,textvariable=self.var_emp_id,font=('Georgia',15),bg='lightyellow')
        emp_id_Entry.place(x=150,y=150,width=180)

        contact_Entry=Entry(self.window,textvariable=self.var_contact,font=('Georgia',15),bg='lightyellow')
        contact_Entry.place(x=500,y=150,width=180)

        #row2

        name_lbl=Label(self.window,text='Name :-',font=('Georgia',15),bg='White')
        name_lbl.place(x=50,y=190)  

        Email_lbl=Label(self.window,text='Email :-',font=('Georgia',15),bg='White')
        Email_lbl.place(x=350,y=190)   

        name_Entry=Entry(self.window,textvariable=self.var_name,font=('Georgia',15),bg='lightyellow')
        name_Entry.place(x=150,y=190,width=180)  

        Email_Entry=Entry(self.window,textvariable=self.var_email,font=('Georgia',15),bg='lightyellow')
        Email_Entry.place(x=500,y=190,width=180)   

        #row3

        password_lbl=Label(self.window,text='Password:-',font=('Georgia',15),bg='White')
        password_lbl.place(x=48,y=230)

        user_type_lbl=Label(self.window,text='User Type :-',font=('Georgia',15),bg='White')
        user_type_lbl.place(x=350,y=230)

        password_Entry=Entry(self.window,textvariable=self.var_password,font=('Georgia',15),bg='lightyellow')
        password_Entry.place(x=152,y=230,width=180) 

        combo_user_type=ttk.Combobox(self.window,textvariable=self.var_user_type,values=("Admin","Emplyee"),state='readonly',justify=CENTER,font=('goudy old style',10))
        combo_user_type.place(x=500,y=230,width=180)
        combo_user_type.current(0)

        #row4

        salary_lbl=Label(self.window,text='Salary :-',font=('Georgia',15),bg='White')
        salary_lbl.place(x=250,y=280)

        salary_Entry=Entry(self.window,textvariable=self.var_salary,font=('Georgia',15),bg='lightyellow')
        salary_Entry.place(x=350,y=280,width=180)

        #Button

        btn_Add=Button(self.window,text="Save",font=("goudy old style",12),bg="deep sky blue",fg="white",command=self.Add)
        btn_Add.place(x=800,y=150,width=150,height=25)

        btn_Update=Button(self.window,text="Update",font=("goudy old style",12),bg="green",fg="white",command=self.Update)
        btn_Update.place(x=800,y=190,width=150,height=25)

        btn_Delete=Button(self.window,text="Delete",font=("goudy old style",12),bg="red",fg="white",command=self.delete)
        btn_Delete.place(x=800,y=230,width=150,height=25)

        btn_Clear=Button(self.window,text="Clear",font=("goudy old style",12),bg="gray",fg="white",command=self.clear)
        btn_Clear.place(x=800,y=270,width=150,height=25)

        #Employee details

        emp_frame=Frame(self.window,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=330,relwidth=1,height=170)

        scroll_y=Scrollbar(emp_frame,orient=VERTICAL)
        scroll_x=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("emp_id","contact","name","email","user_type","password","salary"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.EmployeeTable.xview)
        scroll_y.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("emp_id",text="EMP ID")
        self.EmployeeTable.heading("contact",text="CONTACT")
        self.EmployeeTable.heading("name",text="NAME")
        self.EmployeeTable.heading("email",text="EMAIL")
        self.EmployeeTable.heading("user_type",text="USER TYPE")
        self.EmployeeTable.heading("password",text="PASSWORD")
        self.EmployeeTable.heading("salary",text="SALARY")

        self.EmployeeTable.column("emp_id",width=90)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("user_type",width=100)
        self.EmployeeTable.column("password",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable["show"]="headings"
        self.EmployeeTable.pack(fill=BOTH,expand=1)

        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()




if __name__=="__main__":
    window=Tk()
    obj=employeeClass(window)
    window.mainloop()