import tkinter
import tkinter.messagebox

janela = tkinter.Tk() #comando para criar guia
janela.configure (background="#000000") #cor da guia
janela.title('template') #titulo da guia
janela.geometry('300x300') #tamanho da guia

rotulotexto = tkinter.Label (janela, text='Concessor de empréstimo: ', bg="#000000", fg="white")
rotulotexto.pack()

rotulocasa = tkinter.Label(janela, text='Digite o valor da casa: ')
rotulocasa.pack()
casa = tkinter.Entry(janela)
casa.pack()

rotulosalario = tkinter.Label(janela, text='Digite o seu salário: ')
rotulosalario.pack()
salario = tkinter.Entry(janela)
salario.pack()

rotulomeses = tkinter.Label(janela, text='Meses a pagar: ')
rotulomeses.pack()
meses = tkinter.Entry(janela)
meses.pack()

def prestacao():
    emprestimonegado = ("Empréstimo Negado!")
    prestacao = float(casa.get()) / int(meses.get())
        
    if prestacao > float(salario.get()) * 0.3:
        tkinter.messagebox.showinfo ('Empréstimo negado', emprestimonegado)
        return
    
    tkinter.messagebox.showinfo('Valor da Prestação:', prestacao)

botao = tkinter.Button(janela, text='Calcula Prestação', command=prestacao )
botao.pack()
