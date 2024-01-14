from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntery.delete(0,END)
    usernameEntery.delete(0,END)
    passwordEntery.delete(0,END)
    confirmEntery.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntery.get()=='' or usernameEntery.get()=='' or passwordEntery.get()=='' or confirmEntery.get()=='':
        messagebox.showerror('Error',"All Fields Are Requried")
    elif passwordEntery.get()!=confirmEntery.get():
        messagebox.showerror('Error',"Password Mismatch")
    elif check.get()==0:
        messagebox.showerror('Error',"Please accept Terms and Conditions")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Amar@1998')
            mycursur=con.cursor()
        except:
            messagebox.showerror('Error',"Database Connectivity Issue,Please Try Again")
            return
        try:
            query='create database userdata'
            mycursur.execute(query)
            query='use userdata'
            mycursur.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursur.execute(query)
        except:
            mycursur.execute("use userdata")
        query='select * from data where username=%s'
        mycursur.execute(query,(usernameEntery.get()))

        row=mycursur.fetchone()
        if row !=None:
           messagebox.showerror('Error',"Username already exist")
        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursur.execute(query,(emailEntery.get(),usernameEntery.get(),passwordEntery.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success",'Registration is successful')
            clear()
            signup_window.destroy()
            import signin
    

def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.title("SighUp Page")
signup_window.resizable(0,0)
background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading= Label(frame,text="CREATE AN ACCOUNT",font=("Microsoft Yahei UI Light",18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=("Microsoft Yahei UI Light",10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
 
emailEntery=Entry(frame,width=30,font=("Microsoft Yahei UI Light",10,'bold'),bg='firebrick1',fg='white')
emailEntery.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=("Microsoft Yahei UI Light",10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
 
usernameEntery=Entry(frame,width=30,font=("Microsoft Yahei UI Light",10,'bold'),bg='firebrick1',fg='white')
usernameEntery.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=("Microsoft Yahei UI Light",10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
 
passwordEntery=Entry(frame,width=30,font=("Microsoft Yahei UI Light",10,'bold'),bg='firebrick1',fg='white')
passwordEntery.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=("Microsoft Yahei UI Light",10,'bold'),bg='white',fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
 
confirmEntery=Entry(frame,width=30,font=("Microsoft Yahei UI Light",10,'bold'),bg='firebrick1',fg='white')
confirmEntery.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms and Conditions',font=("Microsoft Yahei UI Light",9,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=("Open Sans",16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground="firebrick1",activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text="Don't have an account",font=("Open Sans",9,'bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=login_page)
loginButton.place(x=170,y=404)

signup_window.mainloop()