from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql
import os
 
class salesClass:

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bills'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    
    def get_data(self,ev):
        index=self.sales_list.curselection()
        file_name=self.sales_list.get(index)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bills/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)

        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("ERROR","Invoice No Requered",parent=self.window)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bills/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("ERROR","Invalid Invoice No",parent=self.window)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)


#--------------------------------------------------------------------------------
    def __init__(self,window):

        self.window=window
        self.window.title("SALES")
        self.window.geometry("1100x500+220+130")
        self.window.config(bg='white')
        self.window.focus_force()
        #variable
        self.bill_list=[]
        self.var_invoice=StringVar()

        #title
        title_lbl=Label(self.window,text="View Customer Bills",font=('Georgia',30),bg='Gray14',fg='White',bd=3,relief=RIDGE)
        title_lbl.pack(side=TOP,fill=X,padx=10,pady=20)

        invoice_lbl=Label(self.window,text="Invoice No.",font=("times new romen",15),bg="white")
        invoice_lbl.place(x=50,y=100)
        invoice_entry=Entry(self.window,textvariable=self.var_invoice,font=("times new romen",15),bg="lightyellow")
        invoice_entry.place(x=160,y=100,width=180,height=28)

        search_btn=Button(self.window,text="Search",font=('Georgia',12),bg='green',fg="white",cursor="hand2",command=self.search)
        search_btn.place(x=360,y=100,width=120,height=28)

        clear_btn=Button(self.window,text="Clear/Refresh",font=('Georgia',12),bg="gray",fg="white",cursor="hand2",command=self.clear)
        clear_btn.place(x=490,y=100,width=150,height=30)
        #bill list
        sales_frame=Frame(self.window,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)

        scroll_y=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)
        #bill area
        bill_frame=Frame(self.window,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)

        title_lbl2=Label(bill_frame,text="Bill Area",font=('Georgia',20),bg='orange')
        title_lbl2.pack(side=TOP,fill=X)

        scroll_y2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,bg="lightyellow",yscrollcommand=scroll_y2.set)
        scroll_y2.pack(side=RIGHT,fill=Y)
        scroll_y2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        #image

        self.img1=Image.open("image/sales.jpg").resize((380,320))
        self.photo1=ImageTk.PhotoImage(self.img1)

        self.img_lbl1=Label(self.window,image=self.photo1,bd=2,relief=RAISED)
        self.img_lbl1.place(x=700,y=140)
        self.show()

if __name__=="__main__":
    window=Tk()
    obj=salesClass(window)
    window.mainloop()