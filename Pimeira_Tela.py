from tkinter import *
import tkinter.messagebox
import sqlite3

# CONEXÂO COM O BANCO
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

root = Tk()
# CONFIGURAÇÕES DA JANELA
root.geometry("300x200+0+0")
root.configure(background='#00B2EE')

# INICIA O SISTEMA
class Login:
    def __init__(self,master):
        self.master = master
        self.master.title("Acesso ao Sistema")
        Label(self.master,text="Acessar o Sistema", background='#00B2EE', font=('Windings', 12)).place(x=80, y=25)

        # CAMPO USUARIO
        Label(self.master, text="Usuário:", background='#00B2EE', font=('Windings')).place(x=50, y=69)
        self.usuario = Entry(self.master, font=('Windings'))
        self.usuario.place(x=120, y=70, width=115)
        # CAMPO SENHA
        Label(self.master, text="Senha:", background='#00B2EE', font=('Windings')).place(x=60, y=100)
        self.senha = Entry(self.master, show="*", fg="darkgrey", font=('Windings'))
        self.senha.place(x=120, y=100, width=115)
        # POSICIONA O CURSOR
        self.usuario.focus_force()

        # LOGAR NO SISTEMA
        def entrar():
            try:
                # BUSCA O USUARIO E A SENHA NO BANCO
                sql = "select * from login where usuario like '"+self.usuario.get()+"' and senha like '"+self.senha.get()+"'"
                cursor.execute(sql)
                valido = cursor.fetchall()
                # FAZ A VALIDAÇÃO
                if len(valido) > 0:
                    tkinter.messagebox._show(title="novo", message="Seja Bem-Vindo!")
                    # FECHA A PRIMEIRA TELA
                    self.master.destroy()
                    # ABRE A SEGUNDA TELA
                    from Segunda_Tela import Cadastro
                    callable('Segunda_Tela.py python')
                else:
                    tkinter.messagebox._show(title="novo", message="Login e/ou Senha Incorreta!")
            except sqlite3 as erro:
                print('problema ao se conectar ccom o bd')

        # FINALIZA O PROGRAMA
        def sair():
            exit()

        # BOTÃO ENTRAR
        self.entrar = Button(self.master, width=7, text="Entrar", command=entrar)
        self.entrar.place(x=55, y=135, width=120)
        # BOTÂO SAIR
        self.sair = Button(self.master, width=7, text="Sair", command=sair)
        self.sair.place(x=175, y=135)

Login(root)
root.mainloop()