from tkinter import *

def mid() :
    resultado = float(celcios.get()) * 1.8 + 32
    Fahrenheit['text']=str(resultado)
top=Tk()

celcios=Entry(top,font='arial 24')
Fahrenheit=Label(top,font='arial 24',)
calcular=Button(top,font='arial 24',command=mid, text=X)

celcios.grid(row=0,column=0,sticky=EW)
Fahrenheit.grid(row=1,column=0,sticky=EW)
calcular.grid(row=2,column=0,sticky=EW)
top.mainloop()