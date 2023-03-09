#tkinter練習
from tkinter import *

window = Tk()                   #創建Tk object
window.title('MyWindow')        #設定視窗名稱
window.geometry('400x300')      #設定視窗大小為400*300
window.config(bg = 'light yellow')  #背景設定為 light yellow

window.mainloop()  #顯示視窗