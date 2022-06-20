from tkinter import *
z9=Tk()


def somar():
    c1["text"]= int(c6.get()) + int(c7.get())
def  subtrair():
    c1["text"]= int(c6.get()) - int(c7.get())
def dividir():
    c1["text"]= int(c6.get()) / int(c7.get())
def  multiplicar():
    c1["text"]= int(c6.get()) * int(c7.get())


c1=Label(z9,font='Arial 23')
c2=Button(z9,text="+",font='Arial 23',command=somar)
c3=Button(z9,text="-",font='Arial 23',command=subtrair)
c4=Button(z9,text="/",font='Arial 23',command=dividir)
c5=Button(z9,text="*",font='Arial 23',command=multiplicar)
c6=Entry(z9,font='Arial 23')
c7=Entry(z9,font='Arial 23')


c1.grid(column=0,row=0,columnspan=5)
c6.grid(column=0,row=1,columnspan=5)
c7.grid(column=0,row=2,columnspan=5)
c2.grid(column=0,row=3,sticky=EW)
c3.grid(column=1,row=3,sticky=EW)
c4.grid(column=2,row=3,sticky=EW)
c5.grid(column=3,row=3,sticky=EW)



z9.mainloop()