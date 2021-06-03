from tkinter import *
import databaseConnect


#id_fornecedor, codigo_item, descricao, linha, categoria


class Application:
    #Layout
    def __init__(self, parent):
        self.fontePadrao = ("Arial", "10", "bold")
        
        self.espacamentodepois = Label(text="", padx=5)
        self.espacamentodepois.grid(row=10, column=2)

        #TITULO
        self.titulo = Label(text="Dados do Produto", pady=10)
        self.titulo["font"] = ("Arial", "10")
        self.titulo.grid(row=0, column=1)
             
        #ID_PRODUTO
        self.codigoLabel = Label(text="id", font=self.fontePadrao) 
        self.codigoLabel.grid(row=1, sticky=E)

        self.codigo = Text(height=1, background='snow2', foreground='gray')
        self.codigo["width"] = 30
        self.codigo["font"] = ("Arial", "10")
        self.codigo.tag_config('justified',justify='right')
        self.codigo.grid(row=1, column=1)
        
        self.nValorAtual = databaseConnect.number_reg('produtos') + 1
        self.codigo.insert('insert', self.nValorAtual, 'justified')
        self.codigo["state"] = DISABLED

        #ID_FORNECEDOR picklist
        self.id_fornecedor_label = Label(text="Código Fornecedor", font=self.fontePadrao)
        self.id_fornecedor_label.grid(row=2, sticky=E)

        try:
            self.lista_fornecedores = databaseConnect.picklist_fornecedores()
            self.option_var = StringVar(root)
            self.option_var.set(self.lista_fornecedores[0])
        except:
            self.option_var.set('')
            self.lista_fornecedores = ['']

        self.id_fornecedor_pick = OptionMenu(root, self.option_var, *self.lista_fornecedores)
        self.id_fornecedor_pick["width"] = 29
        self.id_fornecedor_pick["font"] = ("Arial", "8")
        self.id_fornecedor_pick.grid(row=2, column=1, sticky=W)
        
        #CODIGO_ITEM
        self.codigo_item_label = Label(text="Código Item", font=self.fontePadrao) 
        self.codigo_item_label.grid(row=3, sticky=E)

        self.codigo_item = Entry()
        self.codigo_item["width"] = 30
        self.codigo_item["font"] = self.fontePadrao
        self.codigo_item.grid(row=3, column=1, sticky=W)        

        #DESCRIÇÃO
        self.descricao_label = Label(text="Descrição", font=self.fontePadrao)
        self.descricao_label.grid(row=4, sticky=E)

        self.descricao = Entry()
        self.descricao["width"] = 30
        self.descricao["font"] = self.fontePadrao
        self.descricao.grid(row=4, column=1, sticky=W)
        
        # linha
        self.linha_label = Label(text="Linha", font=self.fontePadrao)
        self.linha_label.grid(row=5, sticky=E)

        self.linha = Entry()
        self.linha["width"] = 30
        self.linha["font"] = self.fontePadrao
        self.linha.grid(row=5, column=1, sticky=W)

        # categoria 
        self.categoria_label = Label(text="Categoria", font=self.fontePadrao)
        self.categoria_label.grid(row=6, sticky=E)

        self.categoria = Entry()
        self.categoria["width"] = 30
        self.categoria["font"] = self.fontePadrao
        self.categoria.grid(row=6, column=1, sticky=W)        

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

            id_fornecedor = databaseConnect.picklist_fornecedores().index(self.option_var.get())+1
            codigo_item = self.codigo_item.get()
            descricao = self.descricao.get()
            linha = self.linha.get()
            categoria = self.categoria.get()
            databaseConnect.insert_produtos(id_fornecedor, codigo_item, descricao, linha, categoria)
            self.mensagem["text"] = "Cadastrado"
            #Limpar campos
            self.option_var.set(self.lista_fornecedores[0])
            self.codigo_item.delete(0, END)
            self.descricao.delete(0, END)
            self.linha.delete(0, END)
            self.categoria.delete(0, END)
            #Atualizar próx código
            self.nValorAtual = databaseConnect.number_reg('produtos') + 1
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
root.title('Cadastro de Produtos')
#root.geometry('400x300')
root.mainloop()