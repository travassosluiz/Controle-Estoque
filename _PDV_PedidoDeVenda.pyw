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


        #BOX SELEÇÃO CLIENTE
            #Linha 1
        self.clienteCodLb = Label(text="Cód. Cliente", font=self.fontePadraoBold)
        self.clienteCodLb.grid(row=1, column=1, sticky=W)
        
        self.clienteCod = Entry(textvariable=sv0, validate="focusout", validatecommand=self.consultaCliente)
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


        #BOX ITENS 
            #Linha7
        self.itenslabel = Label(text="Itens", font=("Arial", "8", "bold"), padx=5)
        self.itenslabel.grid(row=7, column=1, sticky=W)        


            #Linha8
        table = ['#', 'Código do Item', 'Descrição do Item', 'Linha', 'Categoria', 'Fornecedor', 'Quantidade', 'Qnt Disponível', 'Preço Unitário', '% do desconto', 'Preço Promocional', 'Preço Final']
        colunas = len(table)
        for x in range(colunas):
            self.tableLabel = Label(text=table[x], font=("Arial", "8", "bold"), background='gray80', padx=5)
            self.tableLabel.grid(row= 8, column=x, sticky='NSWE')

            #Especial linhas 9 a 28

        for x in range(20):
            self.tableLabel = Label(text=[x+1], font=("Arial", "8", "bold"), background='gray80')
            self.tableLabel.grid(row= 9+x, column=0, sticky='WE')
            
        #Texts:
        self.itemDesc1 = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao, width=30, state=DISABLED)
        self.itemDesc1.grid(row=9, column=2, sticky='NSWE')

        self.itemLinha1 = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao, width=10, state=DISABLED)
        self.itemLinha1.grid(row=9, column=3, sticky='NSWE')

        self.itemCateg1 = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao, width=10, state=DISABLED)
        self.itemCateg1.grid(row=9, column=4, sticky='NSWE')

        self.itemForn1 = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao, width=10, state=DISABLED)
        self.itemForn1.grid(row=9, column=5, sticky='NSWE')

        self.itemQntDisp1 = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao, width=10, state=DISABLED)
        self.itemQntDisp1.grid(row=9, column=7, sticky='NSWE')

        self.precoUnit1 = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao, width=10, state=DISABLED)
        self.precoUnit1.grid(row=9, column=8, sticky='NSWE')

        self.desconto1 = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao, width=10, state=DISABLED)
        self.desconto1.grid(row=9, column=9, sticky='NSWE')

        self.precoTotal1 = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao, width=10, state=DISABLED)
        self.precoTotal1.grid(row=9, column=11, sticky='NSWE')

        #Entrys:
        self.itemCod1 = Entry(textvariable=sic1, validate="focusout", validatecommand=self.itemDesc1f, width=15, font=self.fontePadrao)
        self.itemCod1.grid(row=9, column=1, sticky='NSWE')

        self.itemQnt1 = Entry(textvariable=siq1, validate="focusout", validatecommand=self.itemQnt1f, width=10, font=self.fontePadrao)
        self.itemQnt1.grid(row=9, column=6, sticky='NSWE')

        self.precoPromoc1 = Entry(textvariable=spp1, validate="focusout", validatecommand=self.precoPromoc1f, width=10, font=self.fontePadrao)
        self.precoPromoc1.grid(row=9, column=10, sticky='NSWE')



    #FUNÇÕES:

    #Função consulta
    def consultaTabelaCliente(self):
        startfile("_consultaTabela_Clientes.pyw")

    def consultaCliente(self):
        try:
            valorCliente = databaseConnect.consulta_tabela(sv0.get(), "Clientes", "nome")
            self.nomeCliente["state"] = NORMAL
            self.nomeCliente.delete('1.0', END)
            self.nomeCliente.insert('insert', valorCliente)
            self.nomeCliente["state"] = DISABLED
            valorSegmento = databaseConnect.consulta_tabela(sv0.get(), "Clientes", "segmento")
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

    def itemDesc1f(self):
        try:
            itemdesc = databaseConnect.consulta_tabela(sic1.get(), "produtos", "descricao")[0]
            itemLinha = databaseConnect.consulta_tabela(sic1.get(), "produtos", "linha")[0]
            itemCateg = databaseConnect.consulta_tabela(sic1.get(), "produtos", "categoria")[0]
            itemForn  = databaseConnect.consulta_tabela(sic1.get(), "produtos", "id_fornecedor")[0]
        except:
            itemdesc = ""
            itemLinha = ""
            itemCateg = ""
            itemForn = ""
        self.itemDesc1["state"] = NORMAL
        self.itemDesc1.delete('1.0', END)        
        self.itemDesc1.insert('insert', itemdesc)
        self.itemDesc1["state"] = DISABLED
        self.itemLinha1["state"] = NORMAL
        self.itemLinha1.delete('1.0', END)        
        self.itemLinha1.insert('insert', itemLinha)
        self.itemLinha1["state"] = DISABLED       
        self.itemCateg1["state"] = NORMAL
        self.itemCateg1.delete('1.0', END)        
        self.itemCateg1.insert('insert', itemCateg)
        self.itemCateg1["state"] = DISABLED
        self.itemForn1["state"] = NORMAL
        self.itemForn1.delete('1.0', END)        
        self.itemForn1.insert('insert', itemForn)
        self.itemForn1["state"] = DISABLED  
        
        return True


    def itemQnt1f(self):
        return True


    def precoPromoc1f(self):
        return True



root = Tk()

sv0 = StringVar()

sic1 = StringVar()

siq1 = StringVar()

spp1 = StringVar()


Application(root)
root.title('PDV - Pedido de Venda')
#root.geometry('400x300')
root.mainloop()