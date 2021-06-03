from tkinter import *
import databaseConnect

table = "Clientes"

#def _consultaTabela(table):
class Application:
    #Layout
    def __init__(self, parent):
        

        
        self.fontePadrao = ("Arial", "10")
        
        self.espacamentodepois = Label(text="", padx=5)
        self.espacamentodepois.grid(row=0, column=100)

        #TITULO "Dados de 'table'"
        self.titulo = Label(text="Dados "+table , pady=10)
        self.titulo["font"] = ("Arial", "10")
        self.titulo.grid(row=0, column=1)

        
        #NOME DAS COLUNAS DA TABELA
        col = 0
        for x in databaseConnect.picklist_table_columns(table):
            self.tableLabel = Label(text= x, font= ("Arial", "10", "bold"))
            self.tableLabel.grid(row=1, column=col)
            col = col + 1
        

        #CONTEÚDO DA TABELA
        linhas = len(databaseConnect.table_contents(table))
        colunas = len(databaseConnect.table_contents(table)[0])

        for y in range(linhas):
            for x in range(colunas):
                self.tableLabel = Label(text=databaseConnect.table_contents(table)[y][x], font=self.fontePadrao)
                self.tableLabel.grid(row= 2 + y, column=x)

    

root = Tk()
Application(root)
root.title('Consulta Cadastro de ' + table)
#root.geometry('400x300')
root.mainloop()


#Teste
#_consultaTabela("Clientes")