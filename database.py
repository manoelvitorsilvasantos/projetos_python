import sqlite3

def Database():
    return sqlite3.connect("dados.db").cursor()
        
