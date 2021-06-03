import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS clientes(
    id_cliente integer  PRIMARY KEY AUTOINCREMENT,
    nome text,
    telefone text,
    endereco text,
    segmento text,
    created_at text,
    updated_at text
    )""")
    
c.execute("""CREATE TABLE IF NOT EXISTS fornecedores(
    id_fornecedor integer PRIMARY KEY AUTOINCREMENT,
    nome text,
    nome_contato text,
    telefone text,
    endereco text,
    segmento text,
    created_at text,
    updated_at text
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS produtos(
    id_produto integer PRIMARY KEY AUTOINCREMENT,
    id_fornecedor integer,
    codigo_item text,
    descricao text,
    linha text,
    categoria text,
    created_at text,
    updated_at text
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS estoque(
    id_estoque integer PRIMARY KEY AUTOINCREMENT,
    id_produto integer,
    id_fatura integer,
    quantidade integer,
    valor_custo_unit real,
    valor_venda_unit real,
    created_at text,
    updated_at text
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS faturas(
    id_fatura integer PRIMARY KEY AUTOINCREMENT,
    id_cliente integer,
    id_produto integer,
    parcelas integer,
    data_venda text,
    desconto real,
    valor real,
    created_at text,
    updated_at text
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS contas_receber(
    id_contas_receber integer PRIMARY KEY AUTOINCREMENT,
    id_fatura integer,
    id_cliente integer,
    parcela integer,
    parcela_qnt integer,
    situacao text,
    vencimento text,
    forma_de_pagamento text,
    valor real,
    created_at text,
    updated_at text
    )""")



