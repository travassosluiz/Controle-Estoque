from os import startfile
from tkinter import *




class Application:
    #Layout
    def __init__(self, parent):

        self.espacamentoantes = Label(text="", padx=10)
        self.espacamentoantes.grid(row=10, column=0)

        self.espacamentodepois = Label(text="", padx=5)
        self.espacamentodepois.grid(row=10, column=2)

        #Button1
        self.cadastrar = Button()
        self.cadastrar["text"] = "Cadastro Clientes"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 20
        self.cadastrar["command"] = self.open_cadastroClientes
        self.cadastrar.grid(row=3, column=1, pady=10, sticky=W)

        #Button2
        self.cadastrar = Button()
        self.cadastrar["text"] = "Cadastro Fornecedores"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 20
        self.cadastrar["command"] = self.open_cadastroFornecedores
        self.cadastrar.grid(row=5, column=1, pady=10, sticky=W)

        #Button3
        self.cadastrar = Button()
        self.cadastrar["text"] = "Cadastro Produtos"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 20
        self.cadastrar["command"] = self.open_cadastroProdutos
        self.cadastrar.grid(row=7, column=1, pady=10, sticky=W)

        #Button4
        self.cadastrar = Button()
        self.cadastrar["text"] = "Consulta Cadastro Clientes"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 20
        self.cadastrar["command"] = self.consulta_tabela_clientes
        self.cadastrar.grid(row=8, column=1, pady=10, sticky=W)


    def open_cadastroClientes(new):
        startfile("_cadastroClientes.pyw")

    def open_cadastroFornecedores(new):
        startfile("_cadastroFornecedores.pyw")

    def open_cadastroProdutos(new):
        startfile("_cadastroProdutos.pyw")        

    def consulta_tabela_clientes(new):
        startfile("_consultaTabela.pyw")
        




root = Tk()
Application(root)
root.title('Interface')
root.geometry('400x300')
root.mainloop()