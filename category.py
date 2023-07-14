from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql

class categoryClass:

    def Add(self):
        if self.var_name.get()=='':
            messagebox.showerror('Error','Category Name Field Are Required',parent=self.window)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Problem to Connect Database',parent=self.window)
                return

            try:
                query='use sup_shop'
                mycursor.execute(query)
                query='create table category(cid int primary key auto_increment not null,name varchar(55))'
                mycursor.execute(query)
            except:
                mycursor.execute('use sup_shop')

            query='select * from category where name=%s'
            mycursor.execute(query,(self.var_name.get()))

            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','Category Already Exists',parent=self.window)

            else:
                query='insert into category(name) values(%s)'
                mycursor.execute(query,(self.var_name.get()))
                con.commit()
                messagebox.showinfo("Success","Data Added Succesfully")
                self.show()

    def show(self):
        
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        
        try:
            query='select * from category'
            mycursor.execute(query)
            rows=mycursor.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)

        except:
            messagebox.showerror('Error','Problem to show info',parent=self.window)
            return

    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']

        self.var_category_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
         con=pymysql.connect(host='localhost',user='root',password='')
         mycursor=con.cursor()
         mycursor.execute('use sup_shop')
         try:
            if self.var_name.get()=='':
                messagebox.showerror('Error','Please Select Category First',parent=self.window)
            else:
                query='select * from category where name=%s'
                mycursor.execute(query,(self.var_name.get()))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Name',parent=self.window)
                else:
                    op=messagebox.askyesno("Conform","Do You really Want To Delete")
                    if op==True:
                        query='delete from category where name=%s'
                        mycursor.execute(query,(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Data Deleted Succesfully")
                        self.show()
                        self.var_name.set("")
                        
         except:
            messagebox.showerror('Error','Problem to delete info',parent=self.window)
            return

    #---------------------------------------------------------------------------------
    def __init__(self,window):

        self.window=window
        self.window.title("CATEGORY")
        self.window.geometry("1100x500+220+130")
        self.window.config(bg='white')
        self.window.focus_force()

        #variable

        self.var_category_id=StringVar()
        self.var_name=StringVar()

        #title

        title_lbl=Label(self.window,text="Manage Product Category",font=('Georgia',30),bg='Gray14',fg='White',bd=3,relief=RIDGE)
        title_lbl.pack(side=TOP,fill=X,padx=10,pady=20)
    
        name_lbl=Label(self.window,text="Enter Category Name",font=('Georgia',20),bg='white')
        name_lbl.place(x=50,y=100)

        name_entry=Entry(self.window,textvariable=self.var_name,font=('Georgia',20),bg='lightyellow')
        name_entry.place(x=50,y=170,width=300)

        add_btn=Button(self.window,text="ADD",font=('Georgia',12),bg='green',fg="white",cursor="hand2",command=self.Add)
        add_btn.place(x=360,y=170,width=150,height=30)

        delete_btn=Button(self.window,text="DELETE",font=('Georgia',12),bg='red',fg="white",cursor="hand2",command=self.delete)
        delete_btn.place(x=520,y=170,width=150,height=30)

        #category details

        category_frame=Frame(self.window,bd=3,relief=RIDGE)
        category_frame.place(x=700,y=100,width=380,height=120)

        scroll_y=Scrollbar(category_frame,orient=VERTICAL)
        scroll_x=Scrollbar(category_frame,orient=HORIZONTAL)

        self.categoryTable=ttk.Treeview(category_frame,columns=("cid","name",),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.categoryTable.xview)
        scroll_y.config(command=self.categoryTable.yview)

        self.categoryTable.heading("cid",text="Category ID")
        self.categoryTable.heading("name",text="NAME")

        self.categoryTable.column("cid",width=90)
        self.categoryTable.column("name",width=100)
        
        self.categoryTable["show"]="headings"
        self.categoryTable.pack(fill=BOTH,expand=1)

        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)

       #image

        self.img1=Image.open("image/category.jpg").resize((500,240))
        self.photo1=ImageTk.PhotoImage(self.img1)

        self.img_lbl1=Label(self.window,image=self.photo1,bd=2,relief=RAISED)
        self.img_lbl1.place(x=50,y=250)

        self.img2=Image.open("image/category1.jpg").resize((500,240))
        self.photo2=ImageTk.PhotoImage(self.img2)

        self.img_lbl2=Label(self.window,image=self.photo2,bd=2,relief=RAISED)
        self.img_lbl2.place(x=570,y=250)

        self.show()



if __name__=="__main__":
    window=Tk()
    obj=categoryClass(window)
    window.mainloop()