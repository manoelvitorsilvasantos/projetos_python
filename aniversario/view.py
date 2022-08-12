

# importando sqlite
import sqlite3 as lite

# criando conexao 
conn = lite.connect('data/dados.db')


def salvar(i):
	# inserir informações
	with conn:
		cur = conn.cursor()
		query = """
		INSERT INTO birth(nome, sobrenome, dt, descricao)
		VALUES(?, ?, ?, ?) 
		"""
		cur.execute(query,i)

def listar():

	# listar informações

	minha_lista = []

	with conn:
		cur = conn.cursor()
		query = """
		SELECT * FROM birth
		ORDER BY nome, sobrenome
		"""
		lista = cur.execute(query)

		for item in lista.fetchall():
			minha_lista.append(item)

	return minha_lista

def deletar(codigo):
	# inserir informações
	with conn:
		cur = conn.cursor()
		query = """
		DELETE FROM birth
		WHERE id = ?
		"""
		cur.execute(query, (codigo,))

def atualizar(i):

	# atualizar  informações

	nome_save = ''
	sobrenome_save = ''
	dt_save = ''
	descricao_save = ''

	with conn:
		cur = conn.cursor()
		query = """
		UPDATE birth SET nome = ?, sobrenome = ?, dt = ?, descricao = ?
		WHERE id = ? 
		"""
		cur.execute(query,i)

i = ['raquel','barbosa', "14-04-1997", 'pastora', 2]
atualizar(i)