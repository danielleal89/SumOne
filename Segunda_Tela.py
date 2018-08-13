from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk
from datetime import datetime

# HORARIO E DATA - APAGAR --------------------------------------------
now = datetime.now()
print(now)
print(f'{now.hour}:{now.minute}')
print(now.minute)

# MUDAR PARA BANCO.DB ------------------------------------------------
conn = sqlite3.connect('logs.db')
cursor = conn.cursor()


root = Tk()
# CONFIGURAÇÕES DA JANELA
root.geometry("433x390+0+0")
root.configure(background='#00B2EE')

class Cadastro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Compras")

        Label(self.master,text="OPERADOR:", background='#00B2EE', font=('Windings', 12)).place(x=80, y=10)
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


        # LIMPA OS CAMPOS PARA NOVA INSERÇÃO
        def limpar():
            self.produto.delete(0, END)
            self.valor.delete(0, END)

        # ADICIONA O PRODUTO E O VALOR NA LISTA
        def insert_data():
            """
            Insertion method.
            """
            self.treeview.insert('', 'end', text="Item_" + str(self.i),
                                 values=(self.produto.get(), self.valor.get()))
            # Increment counter
            self.i = self.i + 1
            # BLOQUEIA O CAMPO CPF APOS A PRIMEIRA INSERÇÃO
            self.cpf.configure(state="readonly")
            #cursor.execute("""insert into completa (cpf, produto, valor, hora, data) values (?,?,?,datetime('now'),?)""", (self.cpf.get(), self.produto.get(), self.valor.get(), self.produto.get()))
            cursor.execute(
                """insert into completa (cpf, produto, valor, hora, data) values (?,?,?,strftime('%d-%m-%Y'), strftime('%H:%M'))""",
                (self.cpf.get(), self.produto.get(), self.valor.get()))
            conn.commit()

        # ENVIA OS DADOS PARA O BANCO E LIMPA TODOS OS CAMPOS
        def enviar_bd():

            self.cpf.configure(state='normal')
            self.cpf.delete(0, END)
            self.produto.delete(0, END)
            self.valor.delete(0, END)
            self.total.delete(0, END)


        # BOTAO Q ENVIA PARA O BANCO DE DADOS
        self.enviar = tkinter.Button(self.master, text="Salvar", font=('Widings', 10),command=enviar_bd)
        self.enviar.place(x=30 ,y=348, width= 65, height=26)


        # BOTAO Q ENVIA PARA A LISTA
        self.add = tkinter.Button(self.master, text="Adicionar", font=('Windings',10), command=insert_data)
        self.add.place(x=255, y=150, width=65, height=26)
        self.limpar = tkinter.Button(self.master, width=7, text="Limpar", command=limpar)
        self.limpar.place(x=330, y=150, width=65, height=26)


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





        """# GRAVA NO BD AS COMPRAS
        def salvar():
            if int(self.qtd.get()) <= 1:
                self.lista.insert(-0, self.valor.get())
                self.lista2.insert(-0, self.produto.get())
            else:
                soma = (int(self.valor.get()) * int(self.qtd.get()))
                self.lista.insert(0, soma, self.produto.get())
            # cpf1 = self.cpf.get()
            # sql = "insert into teste (id) values ('"+cpf1+"')"
            # tkinter.messagebox._show(title="novo", message="Compra Cadastrada!")
            # cursor.execute(sql)
            # conn.commit()
"""
Cadastro(root)
root.mainloop()