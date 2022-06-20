from tkinter import *

def show():
    a1["text"]=a3.get()+a4.get()
    a1["foreground"]="red"


f1 = Tk()

a1=Label(f1,text="hello World",font='Arial 23',foreground='blue')
a2=Button(f1,text="alterar",command=show)
a3=Entry(f1,font='Arial 23')
a4=Entry(f1,font='Arial 24')
a1.pack()
a2.pack()
a3.pack()
a4.pack()
f1.mainloop()