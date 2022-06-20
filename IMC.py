from tkinter import *

def zed():
    resultado = float(peso.get())/(float(altura.get()) * float(altura.get()))

    IMC["text"] = str(resultado)

    if resultado < 18.5:
        print('baixo peso')
        classificacao['text'] = 'baixo peso'
    elif resultado >= 18.5 and resultado <= 24.9:
        print('eutrofia')
        classificacao['text'] = 'eutrofia'
    elif resultado >= 25.0 and resultado <=29.9:
        print('sobrepeso')
        classificacao['text'] = 'sobrepeso'
    else:
        print('obesidade')
        classificacao['text'] = 'obesidade'


p1=Tk()

altura=Entry(p1,font='arial 23')
peso=Entry(p1,font='arial 23')
A3=Button(p1,text="calcular",font='arial 23',command=zed)
IMC=Label(p1,font='arial 23')
classificacao=Label(p1,font='arial 23')

altura.grid(row=0,column=0,sticky=EW)
peso.grid(row=0,column=1,sticky=EW)
A3.grid(row=1,column=0,sticky=EW)
IMC.grid(row=1,column=1,sticky=EW)
classificacao.grid(row=2,column=0,sticky=EW)
p1.mainloop()