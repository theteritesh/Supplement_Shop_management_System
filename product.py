from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
 
class productClass:
    #function
    def Add(self):
        if self.var_category.get()=='Select'or self.var_category.get()=='Empty' or self.var_supplier.get()=="Select" or self.var_supplier.get()=="Empty"  or self.var_name.get()=="":
            messagebox.showerror('Error','ALl Field Are Required',parent=self.window)
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
                query='create table product(pro_id int auto_increment primary key not null,supplier varchar(55),category varchar(55),name varchar(55),price varchar(55),qty varchar(55),status varchar(55))'
                mycursor.execute(query)
            except:
                mycursor.execute('use sup_shop')

            query='select * from product where name=%s'
            mycursor.execute(query,(self.var_name.get()))

            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','Product Already Exists',parent=self.window)

            else:
                query='insert into product( category , supplier , name , price , qty , status) values(%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(self.var_category.get(),self.var_supplier.get(),self.var_name.get(),self.var_price.get(),self.var_quantity.get(),self.var_status.get()))
                con.commit()
                messagebox.showinfo("Success","Data Added Succesfully",parent=self.window)
                self.show()
    def show(self):
        
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()

        try:
                query='use sup_shop'
                mycursor.execute(query)
                query='create table product(pro_id int auto_increment primary key not null ,supplier varchar(55),category varchar(55),name varchar(55),price varchar(55),qty varchar(55),status varchar(55))'
                mycursor.execute(query)
        except:
                mycursor.execute('use sup_shop')

        
        try:
            query='select * from product'
            mycursor.execute(query)
            rows=mycursor.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)



        except:
            messagebox.showerror('Error','Problem to show info',parent=self.window)
            return

    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pro_id.set(row[0])
        self.var_supplier.set(row[1])
        self.var_category.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6])

    def Update(self):
        if self.var_pro_id.get()==" ":
            messagebox.showerror('Error','Must Select The Product',parent=self.window)

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
                query='create table product(pro_id int auto_increment primary key not null ,supplier varchar(55),category varchar(55),name varchar(55),price varchar(55),qty varchar(55),status varchar(55))'
                mycursor.execute(query)
            except:
                mycursor.execute('use sup_shop')

            query='select * from product where pro_id=%s'
            mycursor.execute(query,(self.var_pro_id.get(),))

            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Product',parent=self.window)
            else:
                query='Update product set category=%s  ,supplier=%s  ,name=%s  ,price=%s  ,qty=%s  ,status=%s where pro_id=%s'
                mycursor.execute(query,(self.var_category.get(),self.var_supplier.get(),self.var_name.get(),self.var_price.get(),self.var_quantity.get(),self.var_status.get(),self.var_pro_id.get(),))
                con.commit()
                messagebox.showinfo("Success","Data Updated Succesfully",parent=self.window)
                self.show()
        
    def delete(self):
         con=pymysql.connect(host='localhost',user='root',password='')
         mycursor=con.cursor()
         mycursor.execute('use sup_shop')
         try:
            if self.var_name.get()==""'':
                messagebox.showerror('Error','Name Field Are Required',parent=self.window)
            else:
                query='select * from product where name=%s'
                mycursor.execute(query,(self.var_name.get(),))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Product Name',parent=self.window)
                else:
                    op=messagebox.askyesno("Conform","Do You really Want To Delete")
                    if op==True:
                        query='delete from product where name=%s'
                        mycursor.execute(query,(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Data Deleted Succesfully",parent=self.window)
                        self.clear()
         except:
            messagebox.showerror('Error','Problem to delete info',parent=self.window)
            return
         

    def clear(self):
        self.var_category.set("Select")
        self.var_supplier.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_status.set("Select")
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
                query='select * from product  where '+self.var_searchBy.get()+" Like '%"+self.var_searchtxt.get()+"%'"
                mycursor.execute(query)
                rows=mycursor.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.window)

        except:
            messagebox.showerror("Error","Problem to Search Info",parent=self.window)

    def fetch_category_sup(self):

        try:
            con=pymysql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
            mycursor.execute('use sup_shop')
        except:
            messagebox.showerror('Error','Problem to Connect Database',parent=self.window)
            return
        try:
            query='select name from category'
            mycursor.execute(query)
            cat=mycursor.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            query='select name from supplier'
            mycursor.execute(query)
            sup=mycursor.fetchall()
            self.sup_list.append("Empty")
            
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            
        except:
            messagebox.showerror("Error","Problem to fetch Info",parent=self.window)

         
              

    
    #-------------------------------------------------------------------------------
    def __init__(self,window):

        self.window=window
        self.window.title("Product")
        self.window.geometry("1100x500+220+130")
        self.window.config(bg='white')
        self.window.focus_force()
        #variables
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pro_id=StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_category_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()

        #frame

        product_frame=Frame(self.window,bd=3,relief=RIDGE,bg='white')
        product_frame.place(x=10,y=10,width=450,height=480)

        #title

        title=Label(product_frame,text='Product Details',font=('Georgia',18),bg='Gray14',fg='White')
        title.pack(side=TOP,fill=X)

        #label
        category_lbl=Label(product_frame,text='Category',font=('Georgia',18),bg='white')
        category_lbl.place(x=30,y=60)
        supplier_lbl=Label(product_frame,text='Supplier',font=('Georgia',18),bg='white')
        supplier_lbl.place(x=30,y=110)
        product_lbl=Label(product_frame,text='Name',font=('Georgia',18),bg='white')
        product_lbl.place(x=30,y=160)
        price_lbl=Label(product_frame,text='Price',font=('Georgia',18),bg='white')
        price_lbl.place(x=30,y=210)
        quantity_lbl=Label(product_frame,text='Quantity',font=('Georgia',18),bg='white')
        quantity_lbl.place(x=30,y=260)
        status_lbl=Label(product_frame,text='Status',font=('Georgia',18),bg='white')
        status_lbl.place(x=30,y=310)

        #Entry/combobox
        combo_category=ttk.Combobox(product_frame,textvariable=self.var_category,values=self.cat_list,state='readonly',justify=CENTER,font=('goudy old style',14))
        combo_category.place(x=150,y=60,width=200)
        combo_category.current(0)

        combo_supplier=ttk.Combobox(product_frame,textvariable=self.var_supplier,values=self.sup_list,state='readonly',justify=CENTER,font=('goudy old style',14))
        combo_supplier.place(x=150,y=110,width=200)
        combo_supplier.current(0)

        entry_name=Entry(product_frame,textvariable=self.var_name,font=('goudy old style',14),bg="lightyellow")
        entry_name.place(x=150,y=160,width=200)

        entry_price=Entry(product_frame,textvariable=self.var_price,font=('goudy old style',14),bg="lightyellow")
        entry_price.place(x=150,y=210,width=200)

        entry_quantity=Entry(product_frame,textvariable=self.var_quantity,font=('goudy old style',14),bg="lightyellow")
        entry_quantity.place(x=150,y=260,width=200)

        combo_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Select","Active","Non Active"),state='readonly',justify=CENTER,font=('goudy old style',14))
        combo_status.place(x=150,y=310,width=200)
        combo_status.current(0)

        btn_Add=Button(product_frame,text="Save",font=("goudy old style",12),bg="deep sky blue",fg="white",command=self.Add)
        btn_Add.place(x=10,y=400,width=100,height=40)

        btn_Update=Button(product_frame,text="Update",font=("goudy old style",12),bg="green",fg="white",command=self.Update)
        btn_Update.place(x=120,y=400,width=100,height=40)

        btn_Delete=Button(product_frame,text="Delete",font=("goudy old style",12),bg="red",fg="white",command=self.delete)
        btn_Delete.place(x=230,y=400,width=100,height=40)

        btn_Clear=Button(product_frame,text="Clear",font=("goudy old style",12),bg="gray",fg="white",command=self.clear)
        btn_Clear.place(x=340,y=400,width=100,height=40)

        #search bar

        searchframe=LabelFrame(self.window,text="Search Product",font=("goudy old style",12,"bold"),bg='white')
        searchframe.place(x=480,y=10,width=600,height=80)

        #option

        combo_search=ttk.Combobox(searchframe,textvariable=self.var_searchBy,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=('goudy old style',10))
        combo_search.place(x=10,y=10,width=180)
        combo_search.current(0)

        text_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",13),bg="lightyellow")
        text_search.place(x=200,y=10)

        btn_search=Button(searchframe,text="Search",font=("goudy old style",12),bg="green",fg="white",command=self.search)
        btn_search.place(x=400,y=8,width=150,height=25)

        #product details

        pro_frame=Frame(self.window,bd=3,relief=RIDGE)
        pro_frame.place(x=480,y=100,width=600,height=390)

        scroll_y=Scrollbar(pro_frame,orient=VERTICAL)
        scroll_x=Scrollbar(pro_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(pro_frame,columns=("pro_id","supplier","category","name","price","qty","status"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.ProductTable.xview)
        scroll_y.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pro_id",text="PRODUCT ID")
        self.ProductTable.heading("category",text="CATEGORY")
        self.ProductTable.heading("supplier",text="SUPPLIER")
        self.ProductTable.heading("name",text="NAME")
        self.ProductTable.heading("price",text="PRICE")
        self.ProductTable.heading("qty",text="QTY")
        self.ProductTable.heading("status",text="STATUS")

        self.ProductTable.column("pro_id",width=90)
        self.ProductTable.column("category",width=100)
        self.ProductTable.column("supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable["show"]="headings"
        self.ProductTable.pack(fill=BOTH,expand=1)

        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        
        






if __name__=="__main__":
    window=Tk()
    obj=productClass(window)
    window.mainloop()