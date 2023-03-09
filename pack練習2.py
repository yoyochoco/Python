#pack練習2
from tkinter import *

win = Tk()
win.title("MyWindow")
win.geometry('300x150')
lab1 = Label(win,text = "銘傳大學",bg ='lightyellow',width=10)
lab2 = Label(win,text ="資訊學院",bg = 'lightgreen',width=10)
lab3 = Label(win,text = '資工系',bg = 'orange',width=10)
lab4 = Label(win,text='資傳系',bg = 'cyan',width=10)
lab5 = Label(win,text='資管系',bg='lightblue',width=10)
lab1.pack(side=TOP,pady=5)
lab2.pack()

lab3.pack(side=LEFT,padx=10)
lab4.pack(side=LEFT,padx=15)
lab5.pack(side=LEFT)

win.mainloop()


