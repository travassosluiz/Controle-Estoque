from os import startfile
from tkinter import *
import databaseConnect




class Application:
    #Layout
    def __init__(self, parent):

        self.fontePadrao = ("Arial", "8")
        self.fontePadraoBold = ("Arial", "8", "bold")

        self.espacamentoantes = Label(text="", padx=10)
        self.espacamentoantes.grid(row=0, column=0)

        self.espacamentomeio = Label(text="", padx=10)
        self.espacamentomeio.grid(row=0, column=3)

        self.espacamentodepois = Label(text="", padx=5)
        self.espacamentodepois.grid(row=100, column=100)

        #Box Seleção Cliente
            #Linha 1
        self.clienteCodLb = Label(text="Cód. Cliente", font=self.fontePadraoBold)
        self.clienteCodLb.grid(row=1, column=1, sticky=W)
        
        self.clienteCod = Entry(validatecommand= self.consultaCliente)
        self.clienteCod["width"] = 30
        self.clienteCod["font"] = self.fontePadrao
        #self.clienteCod["command"] = self.consultaCliente
        self.clienteCod.grid(row=1, column=2, sticky=W)

        self.clienteBusca = Button(text="Pesquisar", font=self.fontePadrao)
        self.clienteBusca["command"] = self.consultaTabelaCliente
        self.clienteBusca.grid(row=1, column=4)

            #Linha 2
        self.nomeClienteLb = Label(text="Nome", font=self.fontePadraoBold)
        self.nomeClienteLb.grid(row=2,column=1, sticky=W)
        
        self.nomeCliente = Label(height=1 ,background='snow2', foreground='gray', relief=SUNKEN)
        #self.nomeCliente["width"] = 26
        self.nomeCliente["font"] = self.fontePadrao
        self.nomeCliente.grid(row=2, column=2, sticky='WE')

        
        


        """#Codigo
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
        """
        
        
        #Linha3
        self.segmentoClienteLb = Label(text="Segmento", font=self.fontePadraoBold)
        self.segmentoClienteLb.grid(row=3, column=1, sticky=W)

        self.segmentoCliente = Label(height=1 ,background='snow2', foreground='gray', relief=SUNKEN)
        #self.nomeCliente["width"] = 26
        self.segmentoCliente["font"] = self.fontePadrao
        self.segmentoCliente.grid(row=3, column=2, sticky='WE')

        #Linha4,5,6
        self.espacamentomeio = Label(text="", padx=10)
        self.espacamentomeio.grid(row=4, column=0)
        self.espacamentomeio = Label(text="", padx=10)
        self.espacamentomeio.grid(row=5, column=0)
        self.espacamentomeio = Label(text="", padx=10)
        self.espacamentomeio.grid(row=6, column=0)

        #Linha7
        self.itenslabel = Label(text="Itens", font=self.fontePadraoBold)
        self.itenslabel.grid(row=7, column=1, sticky=W)        


        #Linha8
        table = ['#', 'Código do Item', 'Descrição do Item', 'Linha', 'Categoria', 'Fornecedor', 'Quantidade', 'Qnt Disponível', 'Preço Unitário', '% do desconto', 'Preço Promocional', 'Preço Final']
        colunas = len(table)
        for x in range(colunas):
            self.tableLabel = Label(text=table[x], font=("Arial", "8", "bold"), background='gray80')
            self.tableLabel.grid(row= 8, column=x, sticky='WE')

        #Especial linhas 9 a 28
        table = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
        colunas = len(table)
        for x in range(colunas):
            self.tableLabel = Label(text=table[x], font=("Arial", "8", "bold"), background='gray80')
            self.tableLabel.grid(row= 9+x, column=0, sticky='WE')


    #Função consulta
    def consultaTabelaCliente(self):
        startfile("_consultaTabela_Clientes.pyw")

    def consultaCliente(self):
        try:
            valorCliente = databaseConnect.consulta_tabela(self.clienteCod.get(), "Clientes")
            self.nomeCliente["text"] = valorCliente
        except:
            self.nomeCliente["text"] = ""

    


root = Tk()
Application(root)
root.title('PDV - Pedido de Venda')
#root.geometry('800x300')
root.mainloop()

'''        if self.clienteCod.get() == "":
            return ""
        else: 
            valorCliente = databaseConnect.consulta_tabela(self.clienteCod.get(), "Clientes")
            return valorCliente
'''