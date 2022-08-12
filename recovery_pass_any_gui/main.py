import sqlite3
import pandas as pd
import numpy as np
from tabulate import tabulate
import os
import platform

def clear():
    sistema_operacional = platform.system()

    if sistema_operacional == 'Windows':
        os.system('cls') or None
    else :
        os.system('clear') or None
        

def init():
    clear()
    conn = sqlite3.connect("dados.db")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS backup(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            redeSocial TEXT NOT NULL,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            mail TEXT NOT NULL,
            dt TEXT NOT NULL
            )""")
    conn.close()
            
def lista():
    clear()
    conn = sqlite3.connect("dados.db")
    cur = conn.cursor()
    minha_lista = cur.execute("""
    SELECT * FROM backup ORDER BY redeSocial;
    """)

    codigo = []
    redeSocial = []
    login = []
    senha = []
    mail = []
    dn = []
    
    
    
    for row in minha_lista:
        codigo.append(row[0])
        redeSocial.append(row[1])
        login.append(row[2])
        senha.append(row[3])
        mail.append(row[4])
        dn.append(row[5])
    clear()

    #print(tabulate([redeSocial, login, senha, mail], headers=["Platform", "User", "Pass", "Email"]))

 
    d = {
        "id":codigo,
        "Rede Social" : redeSocial,
        "Login": login,
        "Senha":senha,
        "E-mail":mail,
        "DtNasc":dn
    }

    d1 = {
        "id":codigo,
        "Rede Social":redeSocial,
        "Login":login
    }

    df = pd.DataFrame(d)

    html = df.to_html()
    text_file = open("page/index.html", "w")
    text_file.write(html)
    text_file.close()

    df2 = pd.DataFrame(d1)
    print(df2)
    
    conn.close()


def update(codigo, redeSocial, login, senha, mail, dt):
    clear()

    conn = sqlite3.connect("dados.db")
    cur = conn.cursor()

    lista = [(redeSocial, login, senha, mail, dt)]
    
    cur.execute("""
    UPDATE backup
    SET redeSocial = ?, login = ?, senha = ?, mail = ?, dt = ?
    WHERE id = ?
    """, (redeSocial, login, senha, mail, dt, codigo))
    print("Informações atualizadas com sucesso...")
    conn.commit()
    conn.close()

def save(redeSocial, login, senha, mail, dt):
    clear()
    lista = [(redeSocial, login, senha, mail, dt)]
    conn = sqlite3.connect("dados.db")
    cur = conn.cursor()
    cur.executemany("""
            INSERT INTO backup(redeSocial, login, senha, mail, dt)
            VALUES(?,?,?,?, ?)
            """, lista)
    conn.commit()
    print("Informações salvas com sucesso...")
    conn.close()
    
def delete(codigo):
    clear()
    conn = sqlite3.connect("dados.db")
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM backup
    WHERE id = ?
    """, (codigo,))
    print("Registro removido com sucesso...")
    conn.commit()
    conn.close()

while True:
    opc = int(input("1 - Save, 2 - Lista , 3 - Update, 4 - Deletar , 0 - fechar >> "))
    if opc == 1:
        redeSocial = input('Nome da Rede Social >> ')
        login = input('Login >> ')
        senha = input('Senha >> ')
        mail = input('E-mail >> ')
        dt = input('Data de Nascimento (dd-mm-aaaa) >> ') 
        choice = int(input("Você realmente salvar esse registro ? 1 [SIM] ou 2 [NÃO]"))
        if choice == 1:
            save(redeSocial, login, senha, mail, dt)
    elif opc == 2:
        lista()
    elif opc == 3:
        
        codigo = int(input("Id da lista >> "))

        conn = sqlite3.connect("dados.db")
        cur = conn.cursor()
    
        redeSocial_save = ''
        login_save = ''
        senha_save = ''
        mail_save = ''
        dt_save = ''

        minha_lista = cur.execute("""
            SELECT * FROM backup
            WHERE id = ?
        """, (codigo,))

        for item in minha_lista:
            redeSocial_save = item[1]
            login_save = item[2]
            senha_save = item[3]
            mail_save = item[4]
            dt_save = item[5]
        
        
        redeSocial = input('Nome da Rede Social >> ')
        login = input('Login >> ')
        senha = input('Senha >> ')
        mail = input('E-mail >> ')
        dt = input('Data de Nascimento (dd-mm-aaaa) >> ')

        if not redeSocial:
            redeSocial = redeSocial_save
        if not login:
            login = login_save
        if not senha:
            senha = senha_save
        if not mail:
            mail = mail_save
        if not dt:
            dt = dt_save
            

        choice = int(input("Você realmente salvar esse registro ? 1 [SIM] ou 2 [NÃO]"))
        if choice == 1:
            update(codigo, redeSocial, login, senha, mail, dt)
            print("Informações foram atualizadas com sucesso...")
    elif opc == 4:
        codigo = int(input("Id da lista >> "))
        choice = int(input("Você realmente que remover esse registro ? 1 [SIM] ou 2 [NÃO]"))
        if choice == 1:
            delete(codigo)
    elif opc == 0:
        exit(0)
        
