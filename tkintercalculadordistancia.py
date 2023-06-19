import tkinter
import tkinter.messagebox

janela = tkinter.Tk() #comando para criar guia
janela.configure (background="#000000") #cor da guia
janela.title('template') #titulo da guia
janela.geometry('300x300') #tamanho da guia

rotulotexto = tkinter.Label (janela, text='Calculador distância km:', bg="#000000", fg="white")
rotulotexto.pack()

rotulotexto = tkinter.Label (janela, text='200 km: R$0,50/km | >200km: R$0,45/km', bg="#000000", fg="white")
rotulotexto.pack()

rotulodistancia = tkinter.Label(janela, text='Digite a distância: ')
rotulodistancia.pack()
distancia = tkinter.Entry(janela)
distancia.pack()

def preco():
    if float(distancia.get()) <= 200:
        preco = float(distancia.get()) * 0.50
        tkinter.messagebox.showinfo ('Valor final: R$', preco)
        
    else:
        preco = float(distancia.get()) * 0.45
        tkinter.messagebox.showinfo ('Valor final: R$', preco)

botao = tkinter.Button(janela, text='Calcular', command=preco)
botao.pack()
