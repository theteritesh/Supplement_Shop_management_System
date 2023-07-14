from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
import time
import os 
from tkinter import messagebox
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import Billing
from report import reportClass

class dash:
    def __init__(self,window):
        self.window=window
        self.window.title("Dashboard")
        self.window.geometry("1300x670+20+20")
        self.window.config(bg='white')

        #title
        logo=Image.open("image/logo.jpg").resize((80,70))
        self.photo=ImageTk.PhotoImage(logo)

        title=Label(self.window,text='Supplement Shop Management System',image=self.photo,compound=LEFT
                    ,font=('Georgia',30,'bold'),bg='DarkGoldenrod1',fg='black',anchor="w",padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #log out Button

        btn_logout=Button(self.window,text='Logout',font=('times new roman',15,'bold'),fg='White',bg='black',
                        activebackground='black',activeforeground='White',cursor='hand2',command=self.log_out)
        btn_logout.place(x=1200,y=10,height=50,width=150)

        #clock

        self.lbl_clock=Label(self.window,text='Welcome To Supplement Shop Management System \t\t Date:dd-mm-yyyy\t\t Time:hh:mm:ss',
                    font=('Georgia',15),bg='Gray14',fg='White')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #menu

        LeftMenu=Frame(self.window,bd=2,relief=RIDGE,bg='White')
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menu=Label(LeftMenu,text='Menu',font=('Georgia',20),bg='Gray14',fg='White')
        lbl_menu.pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text='Employee',font=('Georgia',20),bg='White',fg='black',
                            cursor='hand2',command=self.employee)
        btn_employee.pack(side=TOP,fill=X)

        btn_supplier=Button(LeftMenu,text='Supplier',font=('Georgia',20),bg='White',fg='black',
                            cursor='hand2', command=self.supplier)
        btn_supplier.pack(side=TOP,fill=X)

        btn_category=Button(LeftMenu,text='Category',font=('Georgia',20),bg='White',fg='black',
                            cursor='hand2',command=self.category)
        btn_category.pack(side=TOP,fill=X)

        btn_product=Button(LeftMenu,text='Products',font=('Georgia',20),bg='White',fg='black',
                            cursor='hand2',command=self.product)
        btn_product.pack(side=TOP,fill=X)

        btn_seles=Button(LeftMenu,text='Seles',font=('Georgia',20),bg='White',fg='black',
                            cursor='hand2',command=self.sales)
        btn_seles.pack(side=TOP,fill=X)

        btn_billing=Button(LeftMenu,text='Billing',font=('Georgia',20),bg='White',fg='black',
                            cursor='hand2',command=self.billing)
        btn_billing.pack(side=TOP,fill=X)

        btn_report=Button(LeftMenu,text='Report',font=('Georgia',20),bg='White',fg='black',
                            cursor='hand2',command=self.report)
        btn_report.pack(side=TOP,fill=X)

        btn_exit=Button(LeftMenu,text='Exit',font=('Georgia',20),bg='White',fg='black',
                            cursor='hand2')
        btn_exit.pack(side=TOP,fill=X)

        #content
        self.lbl_employee=Label(self.window,text="Total Employee\n [n]",font=('Georgia',20)
                           , bg="deep sky blue",fg="Black",bd=5,relief=RIDGE)
        self.lbl_employee.place(x=300,y=120,height=130,width=250)

        self.lbl_supplier=Label(self.window,text="Total Supplier\n [n]",font=('Georgia',20)
                           , bg="orange red",fg="Black",bd=5,relief=RIDGE)
        self.lbl_supplier.place(x=650,y=120,height=130,width=250)

        self.lbl_category=Label(self.window,text="Total Category\n [n]",font=('Georgia',20)
                           , bg="green yellow",fg="Black",bd=5,relief=RIDGE)
        self.lbl_category.place(x=1000,y=120,height=130,width=250)

        self.lbl_product=Label(self.window,text="Total Product\n [n]",font=('Georgia',20)
                           , bg="maroon1",fg="Black",bd=5,relief=RIDGE)
        self.lbl_product.place(x=500,y=300,height=130,width=250)

        self.lbl_sales=Label(self.window,text="Total Sales\n [n]",font=('Georgia',20)
                           , bg="cyan2",fg="Black",bd=5,relief=RIDGE)
        self.lbl_sales.place(x=850,y=300,height=130,width=250)
        

        #footer
        footer=Label(self.window,text='Any Technical Issue Contact us \n Contact:Ritesh(9067467472),Omkar(8788077104)',
                    font=('Times New Roman',15),bg='Gray14',fg='White')
        footer.pack(side=BOTTOM,fill=X)

        self.update_content()

    #---------------------------------------------------------------------------

    def employee(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=salesClass(self.new_win)

    def billing(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=Billing(self.new_win)

    def report(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=reportClass(self.new_win)

    def update_content(self):
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        try:
            query="select * from product"
            mycursor.execute(query)
            product=mycursor.fetchall()
            self.lbl_product.config(text=f"Total Products\n {str(len(product))}")

            query="select * from supplier"
            mycursor.execute(query)
            supplier=mycursor.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n {str(len(supplier))}")

            query="select * from category"
            mycursor.execute(query)
            category=mycursor.fetchall()
            self.lbl_category.config(text=f"Total Category\n {str(len(category))}")

            query="select * from userinfo"
            mycursor.execute(query)
            employee=mycursor.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n {str(len(employee))}")
            bill=len(os.listdir("bills"))
            self.lbl_sales.config(text=f"Total Sales \n {str(bill)}")
        
            time1=time.strftime('%I:%M:%S')
            date1=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f'Welcome To Supplement Shop Management System \t\t Date:{str(date1)}\t\t Time:{str(time1)}')
            self.lbl_clock.after(200,self.update_content)


        except Exception as ex:
            messagebox.showerror("Error",f"Problem to Search Info:{str(ex)}",parent=self.window)

    def log_out(self):
        window.destroy()
        os.system("python signin.py")





if __name__=="__main__":
    window=Tk()
    obj=dash(window)
    window.state('zoomed')
    window.mainloop()
