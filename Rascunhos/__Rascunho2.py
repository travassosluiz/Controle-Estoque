import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()



#CRIA A LISTA 'lista_table_columns' COM AS COLUNAS NA TABELA
def picklist_table_columns(table):
    #Retorna as colunas da tabela definida no parâmetro 'table'    
    c.execute("SELECT name FROM PRAGMA_TABLE_INFO('"+table+"')")
    lista_table_columns = c.fetchall()
    pos=0
    final=len(lista_table_columns)
    while pos < final:
        elemento = lista_table_columns[pos]
        lista_table_columns[pos] = elemento[0]
        pos += 1
    return lista_table_columns






