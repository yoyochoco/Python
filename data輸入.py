#輸入視窗
from tkinter import *
def printInfo():
    print("Account: %s\nPassword: %s"%(e1.get(),e2.get()))

win =Tk()
win.title("MyWindow")
win.geometry('250x100')
lab1 = Label(win,text='帳號').grid(row=0)
lab2 = Label(win,text='密碼').grid(row=1)

e1= Entry(win) #文字方塊1
e2= Entry(win,show='*')

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

btn1=Button(win,text='登入',command=printInfo)
btn1.grid(row=2,column=0)
btn2 = Button(win,text='離開',command=win.destroy)
btn2.grid(row=2,column=1)

win.mainloop()