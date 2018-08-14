from tkinter import *
import tkinter as tk
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk


# CONEXÃO COM O BANCO
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

root = Tk()
# CONFIGURAÇÕES DA JANELA
root.geometry("433x390+0+0")
root.configure(background='#00B2EE')

class Cadastro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Compras")

        Label(self.master,text="Cadastrar Compra", background='#00B2EE', font=('Windings', 14)).place(x=130, y=15)
        # RECEBE O CPF
        Label(self.master, text="CPF", background='#00B2EE', font=('Windings', 11)).place(x=50, y=70)
        self.cpf = tkinter.Entry(self.master)
        self.cpf.place(x=90, y=70, width=150, height=22)
        # RECEBE O PRODUTO
        Label(self.master, text="Produto", background='#00B2EE', font=('Windings', 11)).place(x=30, y=110)
        self.produto = Entry(self.master)
        self.produto.place(x=90, y=110, width=150, height=22)
        # RECEBE O VALOR
        Label(self.master, text="Valor R$", background='#00B2EE', font=('Windings', 11)).place(x=27, y=150)
        self.valor = Entry(self.master)
        self.valor.place(x=90, y=150, width=80, height=22)

        # CALCULO DO TOTAL
        Label(self.master, text="Total R$", background='#00B2EE', font=('Windings',12)).place(x=225, y=348)

        self.total = Entry(self.master)
        self.total.place(x=289, y=348, width=90, height=22)

        # POSICIONA O CURSOR
        self.cpf.focus_force()


        # RETORNO TELA DE LOGIN
        def voltar():
            self.master.destroy()
            from Pimeira_Tela import Login
            callable('Primeira_Tela.py python')

        # LIMPA OS CAMPOS PARA NOVA INSERÇÃO
        def limpar():
            self.produto.delete(0, END)
            self.valor.delete(0, END)

        # ADICIONA O PRODUTO E O VALOR NA LISTA
        def add_lista():
            # METODO DE INSERÇÃO
            self.treeview.insert('', 'end', text="Item_" + str(self.i),
                                 values=(self.produto.get(), self.valor.get()))
            self.i = self.i + 1
            # BLOQUEIA O CAMPO CPF APOS A PRIMEIRA INSERÇÃO
            self.cpf.configure(state="readonly")
            # INSERE OS VALORES DIGITADOS NA TABELA
            cursor.execute("""INSERT INTO vendas (cpf, produto, valor) VALUES (?,?,?)""",
                           (self.cpf.get(), self.produto.get(), self.valor.get()))
            conn.commit()


        # ENVIA OS DADOS PARA O BANCO
        def enviar_bd():
            cursor.execute("""INSERT INTO registro (operador, cpf, valorTotal, data, hora) VALUES
                           (?,?,?,strftime('%d-%m-%Y','now','localtime'),strftime('%H:%M','now','localtime'))""",
                            (self.produto.get(), self.cpf.get(),self.valor.get()))
            conn.commit()
            # LIMPA TODOS OS CAMPOS
            self.cpf.configure(state='normal')
            self.cpf.delete(0, END)
            self.produto.delete(0, END)
            self.valor.delete(0, END)
            self.total.delete(0, END)
            self.tree.delete(*self.tree.get_children())

        # BOTAO Q ENVIA PARA O BANCO DE DADOS
        self.enviar = tkinter.Button(self.master, text="Salvar", font=('Widings', 10),command=enviar_bd)
        self.enviar.place(x=30 ,y=348, width= 65, height=26)
        # BOTAO Q ENVIA PARA A LISTA
        self.add = tkinter.Button(self.master, text="Adicionar", font=('Windings',10), command=add_lista)
        self.add.place(x=255, y=150, width=65, height=26)
        self.limpar = tkinter.Button(self.master, width=7, text="Limpar", command=limpar)
        self.limpar.place(x=330, y=150, width=65, height=26)
        # RETORNO TELA DE LOGIN
        self.add = tkinter.Button(self.master, text="<", font=('Windings', 10), command=voltar)
        self.add.place(x=5, y=5, width=25, height=20)


        # TABELA DE INSERÇÃO DOS PRODUTOS
        self.tree = ttk.Treeview(self.master, columns=('Nº', 'Produto', 'Valor R$'))
        self.tree.heading('#0', text='Nº')
        self.tree.heading('#1', text='Produto')
        self.tree.heading('#2', text='Valor R$')
        self.tree.column('#0', stretch=tkinter.YES, width=12)
        self.tree.column('#1', stretch=tkinter.YES, width=274)
        self.tree.column('#2', stretch=tkinter.YES, width=55)
        self.tree.place(x=30, y=190, width=350, height=150)
        # BARRA DE SCROLL DA TABELA
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        ysb.place(x=380, y=191, width=20, height=148)
        self.tree['yscroll'] = ysb.set
        self.treeview = self.tree
        # INICIALIZA O CONTADOR
        self.i = 1

Cadastro(root)
root.mainloop()