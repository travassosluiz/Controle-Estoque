from tkinter import *
import databaseConnect


#nome, telefone, endereco, segmento


class Application:
    #Layout
    def __init__(self, parent):
        self.fontePadrao = ("Arial", "10", "bold")
        
        self.espacamentodepois = Label(text="", padx=5)
        self.espacamentodepois.grid(row=10, column=2)

        #TITULO
        self.titulo = Label(text="Dados do Cliente", pady=10)
        self.titulo["font"] = ("Arial", "10")
        self.titulo.grid(row=0, column=1)
        
        
        #Codigo
        self.codigoLabel = Label(text="Código", font=self.fontePadrao) 
        self.codigoLabel.grid(row=1, sticky=E)


        self.codigo = Text(height=1, background='snow2', foreground='gray')
        self.codigo["width"] = 30
        self.codigo["font"] = ("Arial", "10")
        self.codigo.tag_config('justified',justify='right')
        self.codigo.grid(row=1, column=1)
        
        self.nValorAtual = databaseConnect.number_reg('clientes') + 1
        self.codigo.insert('insert', self.nValorAtual, 'justified')
        self.codigo["state"] = DISABLED



        #NOME
        self.nomeLabel = Label(text="Nome", font=self.fontePadrao) 
        self.nomeLabel.grid(row=2, sticky=E)

        self.nome = Entry()
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.grid(row=2, column=1, sticky=W)


        #TELEFONE
        self.telefoneLabel = Label(text="Telefone", font=self.fontePadrao)
        self.telefoneLabel.grid(row=3, sticky=E)

        self.telefone = Entry()
        self.telefone["width"] = 30
        self.telefone["font"] = self.fontePadrao
        self.telefone.grid(row=3, column=1, sticky=W)
        
        # endereco
        self.enderecoLabel = Label(text="Endereco", font=self.fontePadrao)
        self.enderecoLabel.grid(row=4, sticky=E)

        self.endereco = Entry()
        self.endereco["width"] = 30
        self.endereco["font"] = self.fontePadrao
        self.endereco.grid(row=4, column=1, sticky=W)


        # segmento 
        self.segmentoLabel = Label(text="Segmento", font=self.fontePadrao)
        self.segmentoLabel.grid(row=5, sticky=E)

        self.segmento = Entry()
        self.segmento["width"] = 30
        self.segmento["font"] = self.fontePadrao
        self.segmento.grid(row=5, column=1, sticky=W)        



        #BOTÃO1
        self.cadastrar = Button()
        self.cadastrar["text"] = "Cadastrar"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 12
        self.cadastrar["command"] = self.insert
        self.cadastrar.grid(row=8, column=1, pady=10, sticky=W)

        #BOTÃO2
        self.cancelar = Button()
        self.cancelar["text"] = "Cancelar"
        self.cancelar["font"] = ("Calibri", "8")
        self.cancelar["width"] = 12
        self.cancelar["command"] = self.close_program
        self.cancelar.grid(row=8, column=1, pady=10, padx=(38,0))        

        self.mensagem = Label(text="", font=self.fontePadrao)
        self.mensagem.grid(row=9, column=1)
    
    #Função do botão cadastrar
    def insert(self):
        try:
            nome = self.nome.get()
            telefone = self.telefone.get()
            endereco = self.endereco.get()
            segmento = self.segmento.get()
            databaseConnect.insert_clientes(nome, telefone, endereco, segmento)
            self.mensagem["text"] = "Cadastrado"
            #Limpar campos
            self.nome.delete(0, END)
            self.telefone.delete(0, END)
            self.endereco.delete(0, END)
            self.segmento.delete(0, END)
            #Atualizar próx código
            self.nValorAtual = databaseConnect.number_reg('clientes') + 1
            self.codigo["state"] = NORMAL
            self.codigo.delete('1.0', END)
            self.codigo.insert('insert', self.nValorAtual, 'justified')
            self.codigo["state"] = DISABLED

        except ValueError as erro:
            self.mensagem["text"] = "ERRO:",erro

    #Função do botão cancelar        
    def close_program(self):
        root.destroy()


root = Tk()
Application(root)
root.title('Cadastro de Clientes')
#root.geometry('400x300')
root.mainloop()