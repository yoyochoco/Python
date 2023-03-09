#Label練習
from tkinter import *

window = Tk()
window.title('MyWindow')
window.geometry('400x300')
label = Label(window,text = 'I like CCE',           #設定標籤文字
              bg = 'lightyellow',                   #設定標籤背景顏色
              width = 15,                           #設定標籤寬度
              font = "Helvetical 16 bold italic",   #設定標籤字體和文字大小
              relief = RAISED)

label.pack()                                        #包裝標籤和定位
window.mainloop()