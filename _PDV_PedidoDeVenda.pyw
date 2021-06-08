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
            
            self.itemCod = Entry(textvariable=exec('sic'+str(x+1)), validate="focusout", validatecommand=self.consultaCliente)
            self.itemCod["width"] = 15
            self.itemCod["font"] = self.fontePadrao
            self.itemCod.grid(row=9+x, column=1, sticky='NSWE')
    
            self.itemDesc = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao)
            self.itemDesc["width"] = 30
            self.itemDesc.insert('insert', "Teste")
            self.itemDesc.grid(row=9+x, column=2, sticky='NSWE')
            self.itemDesc["state"] = DISABLED

            self.itemLinha = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao)
            self.itemLinha["width"] = 15
            self.itemLinha.insert('insert', "Teste")
            self.itemLinha.grid(row=9+x, column=3, sticky='NSWE')
            self.itemLinha["state"] = DISABLED

            self.itemCateg = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao)
            self.itemCateg["width"] = 15
            self.itemCateg.insert('insert', "Teste")
            self.itemCateg.grid(row=9+x, column=4, sticky='NSWE')
            self.itemCateg["state"] = DISABLED

            self.itemForn = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao)
            self.itemForn["width"] = 15
            self.itemForn.insert('insert', "Teste")
            self.itemForn.grid(row=9+x, column=5, sticky='NSWE')
            self.itemForn["state"] = DISABLED

            self.itemQnt = Entry(textvariable=exec('siq'+str(x+1)), validate="focusout", validatecommand=self.funcaoteste)
            self.itemQnt["width"] = 10
            self.itemQnt["font"] = self.fontePadrao
            self.itemQnt.grid(row=9+x, column=6, sticky='NSWE')

            self.itemQntDisp = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao)
            self.itemQntDisp["width"] = 15
            self.itemQntDisp.insert('insert', "Teste")
            self.itemQntDisp.grid(row=9+x, column=7, sticky='NSWE')
            self.itemQntDisp["state"] = DISABLED

            self.precoUnit = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao)
            self.precoUnit["width"] = 15
            self.precoUnit.insert('insert', "Teste")
            self.precoUnit.grid(row=9+x, column=8, sticky='NSWE')
            self.precoUnit["state"] = DISABLED            

            self.desconto = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao)
            self.desconto["width"] = 15
            self.desconto.insert('insert', "Teste")
            self.desconto.grid(row=9+x, column=9, sticky='NSWE')
            self.desconto["state"] = DISABLED                

            self.precoPromoc = Entry(textvariable=exec('spp'+str(x+1)), validate="focusout", validatecommand=self.funcaoteste)
            self.precoPromoc["width"] = 10
            self.precoPromoc["font"] = self.fontePadrao
            self.precoPromoc.grid(row=9+x, column=10, sticky='NSWE')

            self.precoTotal = Text(height=1 ,background='gray80', foreground='grey25', relief=FLAT, font=self.fontePadrao)
            self.precoTotal["width"] = 15
            self.precoTotal.insert('insert', "Teste")
            self.precoTotal.grid(row=9+x, column=11, sticky='NSWE')
            self.precoTotal["state"] = DISABLED 

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

    def funcaoteste(self):
        return True





root = Tk()
[sv0, sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8, sv9, sv10, sv11, sv12, sv13, sv14, sv15, sv16, sv17, sv18, sv19, sv20] = (StringVar(),)*21
[sic1, sic2, sic3, sic4, sic5, sic6, sic7, sic8, sic9, sic10, sic11, sic12, sic13, sic14, sic15, sic16, sic17, sic18, sic19, sic20] = (StringVar(),)*20
[siq1, siq2, siq3, siq4, siq5, siq6, siq7, siq8, siq9, siq10, siq11, siq12, siq13, siq14, siq15, siq16, siq17, siq18, siq19, siq20] = (StringVar(),)*20
[spp1, spp2, spp3, spp4, spp5, spp6, spp7, spp8, spp9, spp10, spp11, spp12, spp13, spp14, spp15, spp16, spp17, spp18, spp19, spp20] = (StringVar(),)*20
Application(root)
root.title('PDV - Pedido de Venda')
#root.geometry('400x300')
root.mainloop()