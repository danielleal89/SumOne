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
root.geometry("588x390+0+0")
root.configure(background='#00B2EE')

class Loginss:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Compras")
        Label(self.master,text="Compras Cadastradas", background='#00B2EE', font=('Windings', 14)).place(x=180, y=10)

        # FILTRO POR DATA
        def filtro_data():
            self.tree.delete(*self.tree.get_children())
            sql = "select * from registro ORDER BY data"
            try:
                cursor.execute(sql)
                compras = cursor.fetchall()
                linha = 0
                for dados in compras:
                    operador = dados[0]
                    cpf = dados[1]
                    valorTotal = dados[2]
                    data = dados[3]
                    hora = dados[4]
                    self.treeview.insert('', 'end', text="" + str(self.i), values=(operador, cpf, valorTotal, data, hora))
                    linha += 1
            except sql as erro:
                print('Problema ao se conectar com o BD')

        # FILTRO POR VALOR
        def filtro_valor():
            self.tree.delete(*self.tree.get_children())
            sql = "select * from registro ORDER BY valorTotal"
            try:
                cursor.execute(sql)
                compras = cursor.fetchall()
                linha = 0
                for dados in compras:
                    operador = dados[0]
                    cpf = dados[1]
                    valorTotal = dados[2]
                    data = dados[3]
                    hora = dados[4]
                    self.treeview.insert('', 'end', text="" + str(self.i), values=(operador, cpf, valorTotal, data, hora))
                    linha += 1
            except sql as erro:
                print('Problema ao se conectar com o BD')

        # FILTRO POR OPERADOR
        def filtro_operador():
            self.tree.delete(*self.tree.get_children())
            sql = "select * from registro ORDER BY operador"
            try:
                cursor.execute(sql)
                compras = cursor.fetchall()
                linha = 0
                for dados in compras:
                    operador = dados[0]
                    cpf = dados[1]
                    valorTotal = dados[2]
                    data = dados[3]
                    hora = dados[4]
                    self.treeview.insert('', 'end', text="" + str(self.i),
                                         values=(operador, cpf, valorTotal, data, hora))
                    linha += 1
            except sql as erro:
                print('Problema ao se conectar com o BD')

        def voltar():
            self.master.destroy()
            from OKsegundaTela import Cadastro
            callable('Segunda_Tela.py python')

        # TABELA DE INSERÇÃO DOS PRODUTOS
        self.tree = ttk.Treeview(self.master, columns=('Nº','Operador','CPF','Valor R$','Data','Hora'))
        self.tree.heading('#0', text='')
        self.tree.heading('#1', text='Operador')
        self.tree.heading('#2', text='CPF')
        self.tree.heading('#3', text='Total R$')
        self.tree.heading('#4', text='Data')
        self.tree.heading('#5', text='Hora')
        # TAMANHO DAS COLUNAS
        self.tree.column('#0', stretch=tkinter.YES, width=0)
        self.tree.column('#1', stretch=tkinter.YES, width=150)
        self.tree.column('#2', stretch=tkinter.YES, width=150)
        self.tree.column('#3', stretch=tkinter.YES, width=70)
        self.tree.column('#4', stretch=tkinter.YES, width=100)
        self.tree.column('#5', stretch=tkinter.YES, width=70)
        # TAMANHO DA TABELA
        self.tree.place(x=0, y=140, width=570, height=250)
        # BARRAS DE SCROLL
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        ysb.place(x=570, y=140, width=20, height=250)
        self.tree['yscroll'] = ysb.set
        xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=self.tree.xview)
        xsb.place(x=0, y=370, width=570, height=20)
        self.tree['xscroll'] = xsb.set
        self.treeview = self.tree
        # INICIALIZA O CONTADOR
        self.i = 1

        # BOTAO - PESQUISA FILTRA POR MENOR VALOR
        self.add = tkinter.Button(self.master, text="Valor", font=('Windings',10), command=filtro_valor)
        self.add.place(x=130, y=70, width=85, height=32)
        # BOTAO - PESQUISA FILTRA POR OPERADOR
        self.add = tkinter.Button(self.master, text="Operador", font=('Windings', 10), command=filtro_operador)
        self.add.place(x=235, y=70, width=85, height=32)
        # BOTAO - PESQUISA FILTRA POR DATA
        self.add = tkinter.Button(self.master, text="Data", font=('Windings', 10), command=filtro_data)
        self.add.place(x=338, y=70, width=85, height=32)

        # RETORNO TELA DE CADASTRO
        self.add = tkinter.Button(self.master, text="<", font=('Windings', 10), command=voltar)
        self.add.place(x=5, y=5, width=25, height=20)

Loginss(root)
root.mainloop()