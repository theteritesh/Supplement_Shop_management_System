from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import time
import pymysql
import os
import tempfile
class Billing:
#functions

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
            query="select pro_id,name,price,qty,status from product where status='Active'"
            mycursor.execute(query)
            rows=mycursor.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)



        except:
            messagebox.showerror('Error','Problem to show info',parent=self.window)
            return
        

    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.window)
            else:               
                query="select pro_id,name,price,qty,status from product where name Like '%"+self.var_search.get()+"%' and status='Active'"
                mycursor.execute(query)
                rows=mycursor.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.window)

        except Exception as ex:
            messagebox.showerror("Error",f"Problem to Search Info:{str(ex)}",parent=self.window)

    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pro_id.set(row[0])
        self.var_product_name.set(row[1])
        self.var_price.set(row[2])
        self.instock_label.config(text=f"In Stock[{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    def get_data_cart(self,ev):
        f=self.cartTable.focus()
        content=(self.cartTable.item(f))
        row=content['values']
        self.var_pro_id.set(row[0])
        self.var_product_name.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.instock_label.config(text=f"In Stock[{str(row[4])}]")
        self.var_stock.set(row[4])


    def add_update_cart(self):
        if self.var_pro_id.get()=='':
            messagebox.showerror("Error","Please select the product",parent=self.window)

        elif self.var_qty.get()=='':
            messagebox.showerror("Error","Quentity is Required",parent=self.window)

        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quentity",parent=self.window)
        
        else:
            # price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            price_cal=self.var_price.get()
            cart_data=[self.var_pro_id.get(),self.var_product_name.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            #update cart
            present="NO"
            index=0
            for row in self.cart_list:
                if self.var_pro_id.get()==row[0]:
                    present="yes"
                    break
                index+=1

            if present=="yes":
                op=messagebox.askyesno("Confirm","Product already Do you want to make some Changes",parent=self.window)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index)
                    else:
                        # self.cart_list[index][2]=price_cal
                        self.cart_list[index][3]=self.var_qty.get()

            else:
                self.cart_list.append(cart_data)
            
            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_ammount=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_ammount= self.bill_ammount+(float(row[2])*int(row[3]))

        self.discount=(self.bill_ammount*5)/100
        self.net_pay=self.bill_ammount-self.discount
        self.bill_amount_label.config(text=f"Bill Amnt\n{str(self.bill_ammount)}")
        self.bill_netPay_label.config(text=f"Net Pay\n{str(self.net_pay)}")

        self.cart_title.config(text=f"Cart \t \t \tTotal Product :{str(len(self.cart_list))}")


        
    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values=row)
        except:
            messagebox.showerror('Error','Problem to show info',parent=self.window)
            return
        
    def generate_bill(self):
        if self.var_customer_name.get()=="" or self.var_contact.get()=="":
             messagebox.showerror('Error','Customer Details Are Requered',parent=self.window)
        
        elif len(self.cart_list)==0:
            messagebox.showerror('Error','Please Add Product To The Cart',parent=self.window)
        else:
            #bill Top
            self.bill_top()
            # bill middle
            self.bill_middle()
            # bil bottom
            self.bill_bottom()
            
            fp=open(f"bills/{str(self.invoice)}.txt",'w')
            fp.write(self.txt_bill.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Bill has been generated",parent=self.window)
            self.report()
            self.print=1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
        self.billing_time=time.strftime("%d/%m/%Y")
        bill_top_temp=f'''
\t\tHealth Suppliment Store
\t Phone No. 9067467472 , nashik-422203
{str("="*47)}
Customer Name:{self.var_customer_name.get()}
Bill No. {str(self.invoice)}\t\t\tDate:{str(self.billing_time)}
{str("="*47)}
Product Name\t\t\tQTY\tPrice
{str("="*47)}        
        '''
        self.txt_bill.delete('1.0',END)
        self.txt_bill.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_ammount}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.txt_bill.insert(END,bill_bottom_temp)
        
    def bill_middle(self):
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        try:
            
            for row in self.cart_list:
            # pid,name,price,qty,stock
                pro_id=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Non Active'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)

                query="update product set qty=%s,status=%s where pro_id=%s"
                mycursor.execute(query,(qty,status,pro_id))
                con.commit()
            con.close()
            self.show()

        except Exception as ex:
            print(ex)
            messagebox.showerror("Error",f"Problem to Search Info:{str(ex)}",parent=self.window)
            


    def clear_cart(self):
        self.var_pro_id.set('')
        self.var_product_name.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.instock_label.config(text=f"In Stock")
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_customer_name.set('')
        self.var_contact.set('')
        self.txt_bill.delete('1.0',END)
        self.cart_title.config(text=f"Cart \t \t \tTotal Product :0")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        time1=time.strftime('%I:%M:%S')
        date1=time.strftime("%d-%m-%Y")
        self.clock_label.config(text=f'Welcome To Supplement Shop Management System \t\t Date:{str(date1)}\t\t Time:{str(time1)}')
        self.clock_label.after(200,self.update_date_time)

    def print_bill(self):
        if  self.print==1:
            messagebox.showinfo("Print","Please wait while printing",parent=self.window)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print","Please generate bill first",parent=self.window)
           

    def report(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Problem to Connect Database',parent=self.window)
            return

        try:
            mycursor.execute('use sup_shop')
            query='create table report(bill_no int primary key not null,date varchar(55),cname varchar(55),contact varchar(55),bill_amt varchar(55),bill_dics varchar(55),net_pay varchar(55))'
            mycursor.execute(query)
        except:
            mycursor.execute('use sup_shop')

        query='insert into report(bill_no,date,cname,contact,bill_amt,bill_dics,net_pay ) values(%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query,(self.invoice,self.billing_time,self.var_customer_name.get(),self.var_contact.get(),self.bill_ammount,self.discount,self.net_pay))
        con.commit()
        messagebox.showinfo("Success","Data Added Succesfully")

    def log_out(self):
        window.destroy()
        os.system("python signin.py")

#====================================================================================
    def __init__(self,window):
        self.window=window
        self.window.title("Billing")
        self.window.geometry("1300x670+20+20")
        self.window.config(bg='white')
        self.cart_list=[]
        self.print=0

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

        self.clock_label=Label(self.window,text='Welcome To Supplement Shop Management System \t\t Date:dd-mm-yyyy\t\t Time:hh:mm:ss',
                    font=('Georgia',15),bg='Gray14',fg='White')
        self.clock_label.place(x=0,y=70,relwidth=1,height=30)


        #product frame
        

        product_frame=Frame(self.window,bd=4,relief=RIDGE,bg="white")
        product_frame.place(x=6,y=110,width=410,height=550)

        product_title=Label(product_frame,text="All Product",font=('Georgia',20),bg='Gray14',fg='White')
        product_title.pack(side=TOP,fill=X)
        #product Search Frame
        self.var_search=StringVar()

        product_frame2=Frame(product_frame,bd=2,relief=RIDGE,bg="white")
        product_frame2.place(x=2,y=42,width=398,height=90)

        search_label=Label(product_frame2,text="Search Product(By Name)",font=("times newm roman",15,"bold"),bg="White",fg="green")
        search_label.place(x=2,y=5)

        name_label=Label(product_frame2,text="Product Name",font=("times newm roman",12,"bold"),bg="White")
        name_label.place(x=2,y=45)

        name_entry=Entry(product_frame2,textvariable=self.var_search,font=("times newm roman",15,"bold"),bg="lightyellow")
        name_entry.place(x=128,y=47,width=150,height=22)

        search_btn=Button(product_frame2,text="Search",font=('Georgia',15),bg="deep sky blue",cursor="hand2",command=self.search)
        search_btn.place(x=285,y=45,width=100,height=25)

        showall_btn=Button(product_frame2,text="Show All",font=('Georgia',15),bg="lightblue",cursor="hand2",command=self.show)
        showall_btn.place(x=285,y=10,width=100,height=25)

        #product detail frame
        product_frame3=Frame(product_frame,bd=3,relief=RIDGE)
        product_frame3.place(x=2,y=140,width=398,height=380)

        scroll_y=Scrollbar(product_frame3,orient=VERTICAL)
        scroll_x=Scrollbar(product_frame3,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(product_frame3,columns=("pro_id","name","price","qty","status"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.productTable.xview)
        scroll_y.config(command=self.productTable.yview)

        self.productTable.heading("pro_id",text="pro_id")
        self.productTable.heading("name",text="NAME")
        self.productTable.heading("price",text="PRICE")
        self.productTable.heading("qty",text="QTY")
        self.productTable.heading("status",text="STATUS")

        self.productTable.column("pro_id",width=40)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=40)
        self.productTable.column("status",width=90)
        
        self.productTable["show"]="headings"
        self.productTable.pack(fill=BOTH,expand=1)

        self.productTable.bind("<ButtonRelease-1>",self.get_data)

        note_lbl=Label(product_frame,text="Enter ZERO Qunatity to remove product from Cart",font=('Georgia',11,"bold"),bg="White",fg="red")
        note_lbl.pack(side=BOTTOM,fill=X)

        #Customer frame
        self.var_customer_name=StringVar()
        self.var_contact=StringVar()

        customer_frame=Frame(self.window,bd=4,relief=RIDGE,bg="white")
        customer_frame.place(x=420,y=110,width=530,height=70)

        product_title=Label(customer_frame,text="Customer Details",font=('Georgia',15),bg='Gray14',fg='White')
        product_title.pack(side=TOP,fill=X)

        name_label=Label(customer_frame,text="Name",font=("times newm roman",15),bg="White")
        name_label.place(x=5,y=35)

        name_entry=Entry(customer_frame,textvariable=self.var_customer_name,font=("times newm roman",13),bg="lightyellow")
        name_entry.place(x=80,y=35,width=160)

        contact_label=Label(customer_frame,text="Contact No.",font=("times newm roman",15),bg="White")
        contact_label.place(x=245,y=35)

        contact_entry=Entry(customer_frame,textvariable=self.var_contact,font=("times newm roman",13),bg="lightyellow")
        contact_entry.place(x=355,y=35,width=160)
        
        #cart frame
        cart_frame=Frame(self.window,bd=2,relief=RIDGE,bg="white")
        cart_frame.place(x=420,y=190,width=530,height=360)

        self.cart_title=Label(cart_frame,text="Cart \t \t \tTotal Product :0",font=('Georgia',15),bg='Gray14',fg='White')
        self.cart_title.pack(side=TOP,fill=X)

        scroll_y=Scrollbar(cart_frame,orient=VERTICAL)
        scroll_x=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cartTable=ttk.Treeview(cart_frame,columns=("pro_id","name","price","qty"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cartTable.xview)
        scroll_y.config(command=self.cartTable.yview)

        self.cartTable.heading("pro_id",text="pro_id")
        self.cartTable.heading("name",text="NAME")
        self.cartTable.heading("price",text="PRICE")
        self.cartTable.heading("qty",text="QTY")
        self.cartTable["show"]="headings"
        self.cartTable.column("pro_id",width=90)
        self.cartTable.column("name",width=100)
        self.cartTable.column("price",width=100)
        self.cartTable.column("qty",width=100)
        
        self.cartTable.pack(fill=BOTH,expand=1)

        self.cartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        #add cart button frame
        self.var_pro_id=StringVar()
        self.var_product_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        cart_button_frame=Frame(self.window,bd=2,relief=RIDGE,bg="white")
        cart_button_frame.place(x=420,y=550,width=530,height=110)

        product_name_label=Label(cart_button_frame,text="Product Name",font=("times newm roman",15),bg="White")
        product_name_label.place(x=5,y=5)

        product_name_entry=Entry(cart_button_frame,textvariable=self.var_product_name,font=("times newm roman",15),bg="lightyellow",state="readonly")
        product_name_entry.place(x=5,y=35,width=190,height=22)

        product_price_label=Label(cart_button_frame,text="Price Per Qty",font=("times newm roman",15),bg="White")
        product_price_label.place(x=230,y=5)

        product_price_entry=Entry(cart_button_frame,textvariable=self.var_price,font=("times newm roman",15),bg="lightyellow",state="readonly")
        product_price_entry.place(x=230,y=35,width=150,height=22)

        product_qty_label=Label(cart_button_frame,text="Quantity",font=("times newm roman",15),bg="White")
        product_qty_label.place(x=390,y=5)

        product_qty_entry=Entry(cart_button_frame,textvariable=self.var_qty,font=("times newm roman",15),bg="lightyellow")
        product_qty_entry.place(x=390,y=35,width=120,height=22)

        self.instock_label=Label(cart_button_frame,text="In Stock",font=("times newm roman",15),bg="White")
        self.instock_label.place(x=5,y=70)

        clear_btn=Button(cart_button_frame,text="Clear",font=('Georgia',15),bg="lightgray",cursor="hand2",command=self.clear_cart)
        clear_btn.place(x=180,y=70,width=150,height=30)

        add_cart_btn=Button(cart_button_frame,text="ADD/Update cart ",font=('Georgia',15),bg="orange",cursor="hand2",command=self.add_update_cart)
        add_cart_btn.place(x=340,y=70,width=180,height=30)

        #customer bill area

        bill_area_frame=Frame(self.window,bd=2,relief=RIDGE,bg="white")
        bill_area_frame.place(x=953,y=110,width=410,height=410)

        bill_area_title=Label(bill_area_frame,text="Customer Bills",font=('Georgia',20),bg='Gray14',fg='White')
        bill_area_title.pack(side=TOP,fill=X)

        scroll_y2=Scrollbar(bill_area_frame,orient=VERTICAL)
        scroll_y2.pack(side=RIGHT,fill=Y)

        self.txt_bill=Text(bill_area_frame,yscrollcommand=scroll_y2.set)
        self.txt_bill.pack(fill=BOTH,expand=1)
        scroll_y2.config(command=self.txt_bill.yview)

        #billing buttons
        bill_menu_frame=Frame(self.window,bd=2,relief=RIDGE,bg="white")
        bill_menu_frame.place(x=953,y=520,width=410,height=140)

        self.bill_amount_label=Label(bill_menu_frame,text="Bill Amount \n0",font=('Georgia',13,"bold"),bg='royalblue',fg='White')
        self.bill_amount_label.place(x=2,y=5,width=120,height=70)

        self.bill_discount_label=Label(bill_menu_frame,text="Discount \n5%",font=('Georgia',13,"bold"),bg='springgreen4',fg='White')
        self.bill_discount_label.place(x=124,y=5,width=120,height=70)

        self.bill_netPay_label=Label(bill_menu_frame,text="Net Pay \n0",font=('Georgia',13,"bold"),bg='Gray36',fg='White')
        self.bill_netPay_label.place(x=246,y=5,width=160,height=70)

        bill_print_btn=Button(bill_menu_frame,text="Print",cursor="hand2",font=('Georgia',13,"bold"),bg='magenta2',fg='White',command=self.print_bill)
        bill_print_btn.place(x=2,y=80,width=120,height=50)

        bill_clear_btn=Button(bill_menu_frame,text="Clear All",cursor="hand2",font=('Georgia',13,"bold"),bg='gray20',fg='White',command=self.clear_all)
        bill_clear_btn.place(x=124,y=80,width=120,height=50)

        bill_generete_btn=Button(bill_menu_frame,text="Generete/Save Bill",cursor="hand2",font=('Georgia',11,"bold"),bg='chartreuse',command=self.generate_bill)
        bill_generete_btn.place(x=246,y=80,width=160,height=50)

        #footer

        footer=Label(self.window,text='Any Technical Issue Contact us \n Contact:Ritesh(9067467472),Omkar(8788077104)',
                    font=('Times New Roman',15),bg='Gray14',fg='White')
        footer.pack(side=BOTTOM,fill=X)
        self.show()
        self.update_date_time()


        
if __name__=="__main__":
    window=Tk()
    obj=Billing(window)
    window.state('zoomed')
    window.mainloop()