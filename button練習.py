#button
from tkinter import *
def msgShow():
    label["text"] = "I love CCE"
    label["bg"] = 'lightyellow'
    label['fg'] = 'blue'
    
win= Tk()
win.title("MyButton")
label = Label(win)

btn = Button(win,text='Message',width=15,command = msgShow)
btn2 = Button(win,text = 'Exit',width =15,command = win.destroy)

label.pack()
btn.pack(side=LEFT)
btn2.pack(side=LEFT)

win.mainloop()