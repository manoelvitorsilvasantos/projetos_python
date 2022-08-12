import sqlite3 as lite

# criando conexao
con = lite.connect('data/dados.db')

# cursor

with con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS birth(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    dt TEXT NOT NULL,
    descricao TEXT NOT NULL)
    """)
    
    
