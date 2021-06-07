import sqlite3
from databaseCreate import *


def insert_clientes(nome, telefone, endereco, segmento):
    """ Inclui um cliente na tabela, com as variaveis: nome, telefone, endereco, segmento"""
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""INSERT INTO clientes ( nome, telefone, endereco, segmento, created_at, updated_at) VALUES (?, ?, ?, ?, (SELECT datetime ('now', 'localtime')), (SELECT datetime ('now', 'localtime')) )""", (nome, telefone, endereco, segmento))
        conn.commit()
        print("Os dados foram adicionados")
    except sqlite3.Error as erro:
        print("ERRO: ",erro)   

# insert_clientes('', '', '', '', '', '')

def insert_fornecedores(nome, nome_contato, telefone, endereco, segmento):
    """ Inclui um fornecedor na tabela, com as variaveis: nome, nome_contato, telefone, endereco, segmento"""
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""INSERT INTO fornecedores (nome, nome_contato, telefone, endereco, segmento, created_at, updated_at) VALUES (?, ?, ?, ?, ?, (SELECT datetime ('now', 'localtime')), (SELECT datetime ('now', 'localtime')) )""", (nome, nome_contato, telefone, endereco, segmento))
        conn.commit()
        print("Os dados foram adicionados")
    except sqlite3.Error as erro:
        print("ERRO: ",erro)  

#insert_fornecedores('nome', '', '', '', '', '', '')

def insert_produtos(id_fornecedor, codigo_item, descricao, linha, categoria):
    """ Inclui um produto na tabela, com as variaveis: id_fornecedor, codigo_item, descricao, linha, categoria"""
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""INSERT INTO produtos (id_fornecedor, codigo_item, descricao, linha, categoria, created_at, updated_at) VALUES (?, ?, ?, ?, ?, (SELECT datetime ('now', 'localtime')), (SELECT datetime ('now', 'localtime')) )""", (id_fornecedor, codigo_item, descricao, linha, categoria))
        conn.commit()
        print("Os dados foram adicionados")
    except sqlite3.Error as erro:
        print("ERRO: ",erro)

#insert_produtos('', '', '', '', '', '', '')

def insert_estoque(id_produto, id_fatura, quantidade, valor_custo_unit, valor_venda_unit):
    """ Inclui um produto na tabela, com as variaveis: id_produto, id_fatura, quantidade, valor_custo_unit, valor_venda_unit"""
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""INSERT INTO estoque (id_produto, id_fatura, quantidade, valor_custo_unit, valor_venda_unit, created_at, updated_at) VALUES (?, ?, ?, ?, ?, (SELECT datetime ('now', 'localtime')), (SELECT datetime ('now', 'localtime')) )""", (id_produto, id_fatura, quantidade, valor_custo_unit, valor_venda_unit))
        conn.commit()
        print("Os dados foram adicionados")
    except sqlite3.Error as erro:
        print("ERRO: ",erro)

#insert_estoque('', '', '', '', '', '', '')

def number_reg(table):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT 'id' FROM "+table+"  ")
    a = c.fetchall()
    return len(a)


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


def picklist_fornecedores():
    c.execute("SELECT nome FROM fornecedores")
    lista_table_columns = c.fetchall()
    pos=0
    final=len(lista_table_columns)
    while pos < final:
        elemento = lista_table_columns[pos]
        lista_table_columns[pos] = elemento[0]
        pos += 1
    return lista_table_columns


def table_contents(table):
    #Retorna o conteúdo da tabela definida no parâmetro 'table'
    c.execute("SELECT * FROM '"+table+"'")
    contents = c.fetchall()
    return contents


def consulta_tabela(number, table, coluna):
    #Consulta nome cliente ou fornecedor pelo número
    c.execute("SELECT "+coluna+" FROM "+table+" WHERE oid = " +number)
    lista_table_columns = c.fetchall()
    pos=0
    final=len(lista_table_columns)
    while pos < final:
        elemento = lista_table_columns[pos]
        lista_table_columns[pos] = elemento[0]
        pos += 1
    return lista_table_columns

    

#Testes
#insert_clientes('nome', 'telefone', 'endereco', 'segmento')
#insert_fornecedores('nome', 'nome_contato', 'telefone', 'endereco', 'segmento')
#insert_produtos('id_fornecedor', 'codigo_item', 'descricao', 'linha', 'categoria')
#insert_estoque('id_produto', 'id_fatura', 'quantidade', 'valor_custo_unit', 'valor_venda_unit')
#print(table_contents("Clientes"))
#print(consulta_tabela('1', 'clientes', 'segmento'))