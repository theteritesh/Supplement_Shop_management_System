from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
import os

#database

def login_user():
    if Uname_entry.get()=='' or Password_entry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()

        except:
            messagebox.showerror('Error','Problem to Connect Database ')
            return
        
        query='use sup_shop'
        mycursor.execute(query)

        query='select * from userinfo where emp_id=%s and password=%s'
        mycursor.execute(query,(Uname_entry.get(),Password_entry.get()))
        row=mycursor.fetchone()

        if row==None:
            messagebox.showerror('Error','Invalid Username Or Password')
        else:
            if row[4]=="Admin":
                signin_win.destroy()
                os.system("python dashbord.py")
            else:
                signin_win.destroy()
                os.system("python billing.py")
            



        

#functions
def hide():
    Password_entry.config(show='*')
    eyeButton.config(command=show)

def show():
    Password_entry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if Uname_entry.get()=='User ID':
        Uname_entry.delete(0,END)

def password_enter(event):
    if Password_entry.get()=='Password':
        Password_entry.delete(0,END)

#GUI Part
signin_win=Tk()
signin_win.title("Login Page")
signin_win.geometry("1300x670+20+20")


image=Image.open("image/bg1.jpg")
rs=image.resize((1400, 720))
photo=ImageTk.PhotoImage(rs)


bg=Label(image=photo)
bg.place(x=0,y=0)



userlogin=Label(signin_win,text="USER LOGIN",font=('Microsoft YaHei UI Light',24,'bold'),bg='white',fg='red')
userlogin.place(x=580,y=180)

Uname_entry=Entry(signin_win,width=25,font=('Microsoft YaHei UI Light',12,'bold'),bd='0',fg='red')
Uname_entry.place(x=560,y=250)
Uname_entry.insert(0,'User ID')

Uname_entry.bind('<FocusIn>',user_enter)

Frame(signin_win,width=250,height=2,bg='red').place(x=560,y=280)


Password_entry=Entry(signin_win,width=25,font=('Microsoft YaHei UI Light',12,'bold'),bd='0',fg='red')
Password_entry.place(x=560,y=315)
Password_entry.insert(0,'Password')

Password_entry.bind('<FocusIn>',password_enter)

Frame(signin_win,width=250,height=2,bg='red').place(x=560,y=345)


closedEye=Image.open("image/closedEye.jpg").resize((20,18))
closedEYE=ImageTk.PhotoImage(closedEye)
eyeButton=Button(signin_win,image=closedEYE,bd=0,bg='white',
                    activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=780,y=315)

loginButton=Button(signin_win,text='Login',font=('Open Sans',16,'bold')
                ,fg='white',bg='red',activebackground='white',activeforeground='red'
                ,cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=560,y=400)

designLabel=Label(signin_win,text='-------------------------------',font=('Seagull',28,'bold')
                ,fg='red',bg='white')
designLabel.place(x=510,y=450)


signin_win.state('zoomed')
signin_win.mainloop()
