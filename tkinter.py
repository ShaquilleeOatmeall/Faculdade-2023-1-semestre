import tkinter
import tkinter.messagebox

janela = tkinter.Tk() #comando para criar guia
janela.configure (background="#000000") #cor da guia
janela.title('template') #titulo da guia
janela.geometry('300x300') #tamanho da guia
#champions = tkinter.PhotoImage (file = 'ucl.png') ##Para por uma imagem

#rotuloescudo = tkinter.Label(janela, image=champions) ##Para por uma imagem
#rotuloescudo.pack() ##Para por uma imagem

rotulocor = tkinter.Label (janela, text='Ola', bg="#000000", fg="white")
rotulocor.pack()

rotulocaixa = tkinter.Label(janela, text='caixa1') #criar caixa de texto
rotulocaixa.pack()

nome = tkinter.Entry(janela)
nome.pack()

rotulocaixa = tkinter.Label(janela, text='caixa2')
rotulocaixa.pack()

nomesenha = tkinter.Entry(janela)
nomesenha.pack()

def click(): #criar caixa para clicar
    print ('Click!')
    tkinter.messagebox.showinfo('Click!')

botao = tkinter.Button(janela, text='Clicar', command=click) 
#criar botao para clicar
botao.pack()

janela.mainloop()
