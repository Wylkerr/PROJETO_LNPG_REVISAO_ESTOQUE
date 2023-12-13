from tkinter import *

window = Tk()
window.title('Controle de Estoque')
window.geometry('600x400+350+250')

label_nome = Label(window, text= 'Nome do produto')
label_nome.grid(column=0, row=0)

input_nome = Entry(window)
input_nome.grid(column=1, row=0)

label_qtd = Label(window, text= 'Quantidade em estoque')
label_qtd.grid(column=0, row=1)

input_qtd = Entry(window)
input_qtd.grid(column=1, row=1)


label_preco_uni = Label(window, text= 'Preço Unitário')
label_preco_uni.grid(column=0, row=2)

input_preco_uni = Entry(window)
input_preco_uni.grid(column=1, row=2)

buttom = IntVar()
r1 = Radiobutton(window, text='Sim', variable=buttom, value=True)
r2 = Radiobutton(window, text='Não', va)


window.mainloop()
