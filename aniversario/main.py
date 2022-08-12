# importando o Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import font
from PIL import Image, ImageTk
from view import *



######## cores #########

co0 = "#f0f3f5" # preta
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#ef5350" # vermelha
co8 = "#263238" # + verde
co9 = "#e9edf5" # sky blue
co10 = "#f7fe2e" # amarelo
preto = "#000000" #black
branco = "#ffffff"
azul_celestre = "#00BFFF"
incolor = "-transparentcolor"



######## criando janela #########

janela = Tk()
janela.title("Formulário")
janela.geometry('1023x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


######## dividindo a Janela #########


# frame cima

frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)




# frame baixo


frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0,pady=1)


# frame direita


frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1,pady=0, sticky=NSEW)



######## Label Cima #########

app_nome = Label(frame_cima, text='Cadastro de Aniversário', anchor=NW, font=('Arial 13 bold'), bg=co2, fg=branco, relief='flat')
app_nome.place(x=10, y=20)

######## Configurando Frame baixo #########

# Nome

lb_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
lb_nome.place(x=10, y=10)
edit_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
edit_nome.place(x=15, y=40)

# Sobrenome

lb_sobrenome = Label(frame_baixo, text='Sobrenome *', anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
lb_sobrenome.place(x=10, y=70)
edit_sobrenome = Entry(frame_baixo, width=45, justify='left', relief='solid')
edit_sobrenome.place(x=15, y=100)


# Dt

lb_dtNasc = Label(frame_baixo, text='Data Nascimento *', anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
lb_dtNasc.place(x=10, y=130)
edit_dtNasc = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
edit_dtNasc.place(x=15, y=160)

# Informações Extra

lb_extra = Label(frame_baixo, text='Informações Extra *', anchor=NW, font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
lb_extra.place(x=10, y=190)
edit_extra = Entry(frame_baixo, width=45, justify='left', relief='solid')
edit_extra.place(x=15, y=220)

# variavel arvore global
global arvore
global codigo

def mostrar():

	global arvore

	lista = listar()

	"""
	lista = [
		[0, 'Manoel Vitor', 'Pau Ferro', "20/07/1991", 'Meu Aniversário'],
		[1, 'Maria', 'Romana', "08/05/1945", 'Minha mãe (avo)']
	]"""

	list_tag = ['ID', 'Nome', 'Sobrenome', 'DtNasc', 'Descricao']



	# cria a tabela

	arvore = ttk.Treeview(
		frame_direita, 
		selectmode="extended",
		columns=list_tag, 
		show="headings"
	)

	# barra de rolamento vertical
	vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=arvore.yview)

	# barra de rolamento horizontal

	hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=arvore.xview)


	arvore.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
	arvore.grid(column=0, row=0, sticky='nsew')
	vsb.grid(column=1, row=0, sticky='ns')
	hsb.grid(column=0, row=1, sticky='ew')


	frame_direita.grid_rowconfigure(0, weight=12)


	hd=["nw", "nw", "nw", "nw", "nw", "center", "center"]
	h=[60, 170, 170, 100, 170]
	n=0

	for col in list_tag:
		arvore.heading(col, text=col.title(), anchor=CENTER)
		#AJUSTAR A COLUNA LARGURA DE ACORDO COM TITULO 
		arvore.column(col, width=h[n], anchor=hd[n])
		n+=1

	for item in lista:
		arvore.insert('', 'end', values=item)


def remover():

	global codigo

	try:
		arvore_dados = arvore.focus()
		arvore_dicionario = arvore.item(arvore_dados)
		arvore_lista = arvore_dicionario['values']

		codigo = arvore_lista[0]
		#deletar(codigo)
		msgbox = messagebox.askquestion('Alerta', 'Você tem certeza que excluir?', icon='error')

		if msgbox == 'yes':
			deletar(codigo)
			messagebox.showinfo('Sucesso', 'Essa informação foi removida com sucesso!')

			for widget in frame_direita.winfo_children():
				widget.destroy()
			mostrar()

	except IndexError:
		messagebox.showerror('Error', 'Você precisa selecionar um item da tabela.')


def update():

	nome = edit_nome.get()
	sobrenome = edit_sobrenome.get()
	dt = edit_dtNasc.get()
	extra = edit_extra.get()

	lista = [nome, sobrenome, dt, extra, codigo]

	if not nome:
		messagebox.showerror('Error', 'Campo nome vázio!')
	elif not sobrenome:
		messagebox.showerror('Error', 'Campo sobrenome vázio!')
	elif not dt:
		messagebox.showerror('Error', 'Campo data de nascimento vázio!')
	elif not extra:
		messagebox.showerror('Error', 'Campo descricao vázio!')
	else:
		atualizar(lista)
		messagebox.showinfo('Sucesso', 'As informações foram atualizadas com sucesso...')

		edit_nome.delete(0,'end')
		edit_sobrenome.delete(0,'end')
		edit_dtNasc.delete(0,'end')
		edit_extra.delete(0,'end')

		for widget in frame_direita.winfo_children():
			widget.destroy()

		mostrar()


def alterar():
	try:
		arvore_dados = arvore.focus()
		arvore_dicionario = arvore.item(arvore_dados)
		arvore_lista = arvore_dicionario['values']

		valor = arvore_lista[0]

		global codigo

		codigo = valor

		edit_nome.delete(0, 'end')
		edit_sobrenome.delete(0, 'end')
		edit_dtNasc.delete(0, 'end')
		edit_extra.delete(0, 'end')

		edit_nome.insert(0, arvore_lista[1])
		edit_sobrenome.insert(0, arvore_lista[2])
		edit_dtNasc.insert(0, arvore_lista[3])
		edit_extra.insert(0, arvore_lista[4])

		#lista = [arvore_lista[1], arvore_lista[2], arvore_lista[3], arvore_lista[4], arvore_lista[0]]
		#atualizar(lista)
		mostrar()
	except IndexError:
		messagebox.showerror('Error', 'Selecione um item da tabela')


def inserir():

	nome = edit_nome.get()
	sobrenome = edit_sobrenome.get()
	dt = edit_dtNasc.get()
	extra = edit_extra.get()

	lista = [nome, sobrenome, dt, extra]

	if not nome:
		messagebox.showerror('Error', 'Campo nome vázio!')
	elif not sobrenome:
		messagebox.showerror('Error', 'Campo sobrenome vázio!')
	elif not dt:
		messagebox.showerror('Error', 'Campo data de nascimento vázio!')
	elif not extra:
		messagebox.showerror('Error', 'Campo descricao vázio!')
	else:
		salvar(lista)
		messagebox.showinfo('Sucesso', 'As informações foram salvas com sucesso...')

		edit_nome.delete(0,'end')
		edit_sobrenome.delete(0,'end')
		edit_dtNasc.delete(0,'end')
		edit_extra.delete(0,'end')

		for widget in frame_direita.winfo_children():
			widget.destroy()

		mostrar()


mostrar()

# Botão Buscar

#btn_save = Button(frame_baixo, width=38, text='Buscar', justify='left', bg=co10, font=('Arial 8 bold'), fg=preto, relief='raised', overrelief='ridge')
#btn_save.place(x=15, y=255)

# Botão Salvar

btn_save = Button(frame_baixo, width=38, font=('Arial 8 bold'), bg=preto, fg=branco, command=update, activebackground=branco, text='Alterar Informações', justify='left', borderwidth=0,  relief='raised', overrelief='ridge')
btn_save.place(x=15, y=250)


icon_save = PhotoImage(file=r"assets/save_icon.png")
btn_save = Button(frame_baixo, image=icon_save, bg=branco, command=inserir, activebackground=branco, width=48, text='Salvar', justify='left', borderwidth=0,  relief='raised', overrelief='ridge')
btn_save.place(x=20, y=295)

# Botão Atualizar
icon_update = PhotoImage(file=r"assets/update_icon.png")
btn_update = Button(frame_baixo, image=icon_update, bg=branco, command=alterar, activebackground=branco, width=48, text='Atualizar', justify='left', borderwidth=0,  relief='raised', overrelief='ridge')
btn_update.place(x=130, y=295)

# Botão Deletar
icon_delete = PhotoImage(file=r"assets/delete_icon.png")
btn_delete = Button(frame_baixo, image=icon_delete, bg=branco, command=remover, activebackground=branco, width=48, text='Deletar', justify='left', borderwidth=0,  relief='raised', overrelief='ridge')
btn_delete.place(x=230, y=295)



janela.mainloop()

