from os import startfile
from sqlite3.dbapi2 import enable_shared_cache
from tkinter import *
import databaseConnect




class Application:
    #Layout
    def __init__(self, parent):


        #FONTES PADRÃO
        self.fontePadrao = ("Arial", "8")
        self.fontePadraoBold = ("Arial", "8", "bold")

        #ESPAÇAMENTOS
        linhas = ['0', '4', '5', '6', '100']
        for x in linhas:
            self.espacamento = Label(text="", padx=10)
            self.espacamento.grid(row= x, column=0)

        colunas = ['3', '100']
        for x in colunas:
            self.espacamento = Label(text="", padx=10)
            self.espacamento.grid(row= 0, column=x)


        #Box Seleção Cliente
            #Linha 1
        self.clienteCodLb = Label(text="Cód. Cliente", font=self.fontePadraoBold)
        self.clienteCodLb.grid(row=1, column=1, sticky=W)
        
        self.clienteCod = Entry(textvariable=sv, validate="focusout", validatecommand=self.consultaCliente)
        self.clienteCod["width"] = 30
        self.clienteCod["font"] = self.fontePadrao
        self.clienteCod.grid(row=1, column=2, sticky=W)

        self.clienteBusca = Button(text="Pesquisar", font=self.fontePadrao)
        self.clienteBusca["command"] = self.consultaTabelaCliente
        self.clienteBusca.grid(row=1, column=4)

            #Linha 2
        self.nomeClienteLb = Label(text="Nome", font=self.fontePadraoBold)
        self.nomeClienteLb.grid(row=2,column=1, sticky=W)
        
        self.nomeCliente = Text(height=1 ,background='snow2', foreground='gray', relief=SUNKEN)
        self.nomeCliente["width"] = 30
        self.nomeCliente["font"] = self.fontePadrao
        self.nomeCliente.grid(row=2, column=2)
        self.nomeCliente["state"] = DISABLED

        
            #Linha3
        self.segmentoClienteLb = Label(text="Segmento", font=self.fontePadraoBold)
        self.segmentoClienteLb.grid(row=3, column=1, sticky=W)

        self.segmentoCliente = Text(height=1 ,background='snow2', foreground='gray', relief=SUNKEN)
        self.segmentoCliente["width"] = 30
        self.segmentoCliente["font"] = self.fontePadrao
        self.segmentoCliente.grid(row=3, column=2)
        self.segmentoCliente["state"] = DISABLED



        #Linha7
        self.itenslabel = Label(text="Itens", font=self.fontePadraoBold)
        self.itenslabel.grid(row=7, column=1, sticky=W)        


        #Linha8
        table = ['#', 'Código do Item', 'Descrição do Item', 'Linha', 'Categoria', 'Fornecedor', 'Quantidade', 'Qnt Disponível', 'Preço Unitário', '% do desconto', 'Preço Promocional', 'Preço Final']
        colunas = len(table)
        for x in range(colunas):
            self.tableLabel = Label(text=table[x], font=("Arial", "8", "bold"), background='gray80', padx=5)
            self.tableLabel.grid(row= 8, column=x, sticky='WE')

        #Especial linhas 9 a 28
        table = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
        colunas = len(table)
        for x in range(colunas):
            self.tableLabel = Label(text=table[x], font=("Arial", "8", "bold"), background='gray80')
            self.tableLabel.grid(row= 9+x, column=0, sticky='WE')


    #FUNÇÕES:

    #Função consulta
    def consultaTabelaCliente(self):
        startfile("_consultaTabela_Clientes.pyw")

    def consultaCliente(self):
        try:
            valorCliente = databaseConnect.consulta_tabela(sv.get(), "Clientes", "nome")
            self.nomeCliente["state"] = NORMAL
            self.nomeCliente.delete('1.0', END)
            self.nomeCliente.insert('insert', valorCliente)
            self.nomeCliente["state"] = DISABLED
            valorSegmento = databaseConnect.consulta_tabela(sv.get(), "Clientes", "segmento")
            valorSegmento = valorSegmento[0]
            self.segmentoCliente["state"] = NORMAL
            self.segmentoCliente.delete('1.0', END)
            self.segmentoCliente.insert('insert', valorSegmento)
            self.segmentoCliente["state"] = DISABLED            
        except:
            valorCliente = ""
            self.nomeCliente["state"] = NORMAL
            self.nomeCliente.delete('1.0', END)
            self.nomeCliente.insert('insert', valorCliente)
            self.nomeCliente["state"] = DISABLED
            valorSegmento = ""
            self.segmentoCliente["state"] = NORMAL
            self.segmentoCliente.delete('1.0', END)
            self.segmentoCliente.insert('insert', valorSegmento)
            self.segmentoCliente["state"] = DISABLED                
        return True

    


root = Tk()
sv = StringVar()
Application(root)
root.title('PDV - Pedido de Venda')
#root.geometry('400x300')
root.mainloop()