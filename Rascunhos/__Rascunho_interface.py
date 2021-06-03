from tkinter import *
import sqlite3
import databaseConnect

root = Tk()

fontePadrao = ("Arial", "10", "bold")


id_fornecedor_label = Label(text="Código Fornecedor", font=fontePadrao) 
id_fornecedor_label.grid(row=2, sticky=E)

OPTIONS = databaseConnect.lista_fornecedor()
variable = StringVar(root)
variable.set(OPTIONS[0])
        
id_fornecedor = OptionMenu(root, variable, *OPTIONS)
id_fornecedor["width"] = 30
id_fornecedor["font"] = ("Arial", "9")
id_fornecedor.grid(row=2, column=1, sticky=W)

print(variable.get())



root.title('Cadastro de Produtos')
root.geometry('400x200')
root.mainloop()

