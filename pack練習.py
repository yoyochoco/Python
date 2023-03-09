#pack練習
from tkinter import *

win = Tk()

win.title("MyWindow")
win.geometry("300x150")
lab1 = Label(win,text="銘傳大學",
              bg = "lightyellow",
              width=10)

lab2 = Label(win,text="資訊學院",
             bg = "lightgreen",
             width = 10)

lab3= Label(win,text = "資傳系",
            bg = 'lightblue',
            width = 10)

lab1.pack(side =TOP,pady=5)
lab2.pack(side = TOP,pady=5)
lab3.pack(side = TOP,pady = 5)

win.mainloop()