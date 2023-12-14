from tkinter import *

window = Tk()
window.title('Controle de Estoque')
window.geometry('600x400+350+250')

def adicionar_produto():
    nome = input_nome.get()
    qtd = input_qtd.get()
    preco_uni = input_preco_uni.get()
    temperatura = buttom.get()
    erro = 0


    if nome.strip() == '':
        # Label(window, text='Nome é obrigatorio').grid(column=3, row= 0)
        erro += 1
    if qtd.strip() == '' or qtd.isnumeric or int(qtd) <= 0:
        # Label(window, text='Quantidade é obrigatoria').grid(column=3, row= 1)
        erro += 1
    if preco_uni.strip() == '' or preco_uni.isdecimal or float(preco_uni) <= 0:
        # Label(window, text='O preço deve ser maior que 0').grid(column=3, row= 2)
        erro += 1

    if erro == 0:
        with open('estoque.txt', 'a', encoding= 'utf-8') as estoque:
            estoque.write(f"{nome},{qtd},{preco_uni},{temperatura}\n")
    else:
        Label(window, text='Por favor preencha todos os campos corretamente').grid(column=0, row= 5, columnspan=2)
def mostrar_lista():
    with open('estoque.txt', 'r') as variable_estoque:
        estoque = variable_estoque.read()
        Label(window, text=estoque).grid(row=6)

def limpar_formulario():
    input_qtd.delete(0, END)
    input_nome.delete(0, END)
    input_preco_uni.delete(0, END)

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

label_tempetatura = Label(window, text='Gelado:')
label_tempetatura.grid(column= 0, row= 3)

buttom = IntVar()
r1 = Radiobutton(window, text='Sim', variable=buttom, value=True)
r2 = Radiobutton(window, text='Não', variable=buttom, value = False)

r1.grid(column= 1, row= 3, sticky= W)
r2.grid(column= 1, row= 3, sticky= E)

botao_adiciona = Button(window, text= 'Cadastrar', command=adicionar_produto)
botao_adiciona.grid(column=0, row=4)

botao_limpa = Button(window, text='Limpa', command=limpar_formulario)
botao_limpa.grid(column=1, row=4)

botao_lista = Button(window, text= 'Gerar Lista', command=mostrar_lista)
botao_lista.grid(column= 2, row=4)


window.mainloop()
