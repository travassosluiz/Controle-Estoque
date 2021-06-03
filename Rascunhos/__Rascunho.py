from os import replace
import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

#CRIA A LISTA 'TABELAS' COM AS TABELAS NO DATABASE
c.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'")
tabelas = c.fetchall()
pos=0
final=len(tabelas)
while pos < final:
    elemento = tabelas[pos]
    tabelas[pos] = elemento[0]
    pos += 1

#CRIA A LISTA 'CLIENTES_COLUMNS' COM AS COLUNAS NA TABELA CLIENTES
c.execute("SELECT name FROM PRAGMA_TABLE_INFO('clientes')")
clientes_columns = c.fetchall()
pos=0
final=len(clientes_columns)
while pos < final:
    elemento = clientes_columns[pos]
    clientes_columns[pos] = elemento[0]
    pos += 1

#print(clientes_columns[1:])
#print("?," * (len(clientes_columns)-1))
#print(str(clientes_columns[1:]).replace( "'", "").replace("[","").replace("]",""))

#Define a tabela
tabela='clientes'

#Indaga os valores a preencher
lista=[]
pos=1
final=len(clientes_columns)
while pos < final:
    lista.append(input("Digite o "+clientes_columns[pos]+":"))
    pos += 1




#Preenche
vsql="INSERT INTO "+tabela+" ("+str(clientes_columns[1:]).replace( "'", "").replace("[","").replace("]","")+") VALUES(?, ?, ?, ?, ?, ?)"
def inserir(sql):
    try:
        c.execute(sql, (lista))
        conn.commit()
        print("Os dados foram adicionados")
    except sqlite3.Error as erro:
        print("ERRO: ",erro)

#inserir(vsql)
#print(clientes_columns[1:])
#print(""" '"+nome+"', '"+telefone+"', '"+endereco+"', '"+segmento+"', '"+created_at+"', '"+updated_at+"' """)
#print(len(clientes_columns[1:]))







