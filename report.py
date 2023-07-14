from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql

class reportClass:


    def show(self):
        
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        

        try:
            query='select * from report'
            mycursor.execute(query)
            rows=mycursor.fetchall()
            self.reportTable.delete(*self.reportTable.get_children())
            for row in rows:
                self.reportTable.insert('',END,values=row)



        except:
            messagebox.showerror('Error','Problem to show info',parent=self.window)
            return
        
    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='')
        mycursor=con.cursor()
        mycursor.execute('use sup_shop')
        try:
            
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Bill no. should be required",parent=self.window)
            else:               
                query='select * from report  where bill_no=%s'
                mycursor.execute(query,(self.var_searchtxt.get()))
                row=mycursor.fetchone()
                if row !=None:
                    self.reportTable.delete(*self.reportTable.get_children())
                    self.reportTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.window)

        except:
            messagebox.showerror("Error","Problem to Search Info",parent=self.window)


    #======================================================================
    def __init__(self,window):

        self.window=window
        self.window.title("REPORT")
        self.window.geometry("1100x500+220+130")
        self.window.config(bg='white')
        self.window.focus_force()

        #All variable
        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()

        #title

        title=Label(self.window,text='Reports',font=('Georgia',30),bg='Gray14',fg='White')
        title.pack(side=TOP,fill=X,padx=10,pady=20)

        #search

        searchframe=LabelFrame(self.window,text="Search Bills",font=("goudy old style",12,"bold"),bg='white')
        searchframe.place(x=250,y=80,width=600,height=70)

        #option

        search_lbl=Label(searchframe,text="Search By Bill No.",font=('goudy old style',14),bg="white")
        search_lbl.place(x=10,y=10)

        text_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",13),bg="lightyellow")
        text_search.place(x=200,y=10)

        btn_search=Button(searchframe,text="Search",font=("goudy old style",12),bg="green",fg="white",command=self.search)
        btn_search.place(x=400,y=8,width=150,height=25)

        #details

        report_frame=Frame(self.window,bd=3,relief=RIDGE)
        report_frame.place(x=0,y=160,relwidth=1,height=340)

        scroll_y=Scrollbar(report_frame,orient=VERTICAL)
        scroll_x=Scrollbar(report_frame,orient=HORIZONTAL)

        self.reportTable=ttk.Treeview(report_frame,columns=("bill_no","date","cname","contact","bill_amt","bill_dics","net_pay"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.reportTable.xview)
        scroll_y.config(command=self.reportTable.yview)

        self.reportTable.heading("bill_no",text="Bill No.")
        self.reportTable.heading("date",text="Date")
        self.reportTable.heading("cname",text="NAME")
        self.reportTable.heading("contact",text="Contact")
        self.reportTable.heading("bill_amt",text="Amount")
        self.reportTable.heading("bill_dics",text="Discount")
        self.reportTable.heading("net_pay",text="Net_Pay")

        self.reportTable.column("bill_no",width=90)
        self.reportTable.column("date",width=100)
        self.reportTable.column("cname",width=100)
        self.reportTable.column("contact",width=100)
        self.reportTable.column("bill_amt",width=100)
        self.reportTable.column("bill_dics",width=100)
        self.reportTable.column("net_pay",width=100)
        
        self.reportTable["show"]="headings"
        self.reportTable.pack(fill=BOTH,expand=1)
        self.show()


if __name__=="__main__":
    window=Tk()
    obj=reportClass(window)
    window.mainloop()