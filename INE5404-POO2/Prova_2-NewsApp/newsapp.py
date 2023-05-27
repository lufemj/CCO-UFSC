import io, webbrowser, requests, json
from tkinter import *
import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
from PIL import ImageTk,Image


class Usuario():
	def __init__(self, login, senha):
		self.login = login
		self.senha = senha

	def get_login(self):
		return self.login
	def get_senha(self):
		return self.senha

class Login():
	def __init__(self):
		self.cadastros = []
		self.janela_login()

	def janela_login(self):
		def fechar():
			self.login.destroy()

		def cadastrar_usuario():
			if caixa_usuario.get() == '':
				label_aux['text'] = 'Informe um usuário!'
			elif caixa_senha.get() == '':
				label_aux['text'] = 'Informe uma senha!'
			else:

				aux = 0
				for o in self.cadastros:
					if caixa_usuario.get() == o.get_login():
						label_aux['text'] = 'Usuário já cadastrado'
						aux = 1
						break
				if aux == 0:
					login = caixa_usuario.get()
					senha = caixa_senha.get()

					x = Usuario(login, senha)

					self.cadastros.append(x)

					label_aux['text'] = 'Usuário cadastrado com sucesso!'


		def verificar_login():
			aux1 = 0
			ver_login = caixa_usuario.get()
			ver_senha = caixa_senha.get()

			if ver_login == '':
				label_aux['text'] = 'Informe um usuário!'
			elif ver_senha == '':
				label_aux['text'] = 'Informe uma senha!'
			else:
				
				for y in self.cadastros:
					if y.get_login() == caixa_usuario.get() and y.get_senha() == caixa_senha.get():
						fechar()
						x = NewsApp()

					if y.get_login() == caixa_usuario.get():
						aux1 = 1
				
				if aux1 == 0:
					label_aux['text'] = 'Usuário não está cadastrado!'
				elif aux1 == 1:
					label_aux['text'] = 'Senha está incorreta!'
				

			
		
		self.login = tk.Tk()
		self.login.title('News App')
		self.login.configure(background='bisque')


		label = Label(self.login, text='NEWS APP',bg='bisque',fg='grey11')
		label.grid(column = 1, row = 1)


		label_usuario = Label(self.login, text='Usuário:',bg='bisque',fg='grey11')
		label_usuario.grid(column = 1, row = 2)
		caixa_usuario = Entry(self.login)
		caixa_usuario.grid(column = 1, row = 3)


		label_senha = Label(self.login, text='Senha:',bg='bisque',fg='grey11')
		label_senha.grid(column = 1, row = 4)
		caixa_senha = Entry(self.login)
		caixa_senha.grid(column = 1, row = 5)


		label_aux = Label(self.login, text='',bg='bisque',fg='grey11')
		label_aux.grid(column = 1, row = 6)

		
		botao_login = Button(self.login, text='Login', command = verificar_login)
		botao_login.grid(column = 1, row = 7)


		botao_cadastrar = Button(self.login, text='Cadastrar', command = cadastrar_usuario)
		botao_cadastrar.grid(column = 1, row = 8)


		botao_sair = Button(self.login, text='Sair', command = fechar)
		botao_sair.grid(column = 1, row = 9)


		self.login.mainloop()


class NewsApp:
	def __init__(self):
		self.data = requests.get('https://newsapi.org/v2/everything?q=brasil&language=pt&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()
		self.filtros = {}
		self.pagina_noticias()
		self.pagina_filtros()
		self.carregar_noticias(0)

	def pagina_noticias(self):
		self.root = tk.Tk()
		self.root.geometry('600x700')
		self.root.title('News App')
		self.root.configure(background='bisque')
	
	def clear(self):
		for i in self.root.grid_slaves():
			if int(i.grid_info()['column']) > 5: 
				i.destroy()
		
	def pagina_filtros(self):
		def atualizar_filtros():
			self.filtros = {}
			
			filtro_data_inicio = (f'{caixa_datai_ano.get()}-{caixa_datai_mes.get()}-{caixa_datai_dia.get()}')
			filtro_data_fim = (f'{caixa_dataf_ano.get()}-{caixa_dataf_mes.get()}-{caixa_dataf_dia.get()}')
			filtro_assunto = caixa_assunto.get()
			filtro_categorias = caixa_categorias.get()

			if (caixa_datai_ano.get() == '') or (caixa_datai_mes.get() == '') or (caixa_datai_dia.get() == ''): self.filtros['data_inicio'] = ''
			else: self.filtros['data_inicio'] = 'from='+filtro_data_inicio
			
			if (caixa_dataf_ano.get() == '') or (caixa_dataf_mes.get() == '') or (caixa_dataf_dia.get() == ''): self.filtros['data_fim'] = ''
			else: self.filtros['data_fim'] = 'to='+filtro_data_fim
			
			if filtro_assunto == '': self.filtros['assunto'] = ''
			else: self.filtros['assunto'] = 'q='+ filtro_assunto

			if filtro_categorias == '' or filtro_categorias == 'Geral': self.filtros['categorias'] = ''
			else: self.filtros['categorias'] = filtro_categorias

			aux = self.filtros['assunto']
			aux1 = self.filtros['data_inicio']
			aux2 = self.filtros['data_fim']

			if self.filtros['categorias'] == '' or self.filtros['categorias'] == 'Geral':

				
				if aux == '':
					if aux1 == '':
						if aux2 == '':
							self.data = requests.get(f'https://newsapi.org/v2/everything?q=brasil&language=pt&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()
						else:
							self.data = requests.get(f'https://newsapi.org/v2/everything?q=brasil&{aux2}&language=pt&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()
					else:
						if aux2 == '':
							self.data = requests.get(f'https://newsapi.org/v2/everything?q=brasil&{aux1}&language=pt&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()
						else:
							self.data = requests.get(f'https://newsapi.org/v2/everything?q=brasil&{aux1}&{aux2}&language=pt&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()
				else:
					if aux1 == '':
						if aux2 == '':
							self.data = requests.get(f'https://newsapi.org/v2/everything?{aux}&language=pt&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()
						else:
							self.data = requests.get(f'https://newsapi.org/v2/everything?{aux}&{aux2}&language=pt&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()
					else:
						if aux2 == '':
							self.data = requests.get(f'https://newsapi.org/v2/everything?{aux}&{aux1}&language=pt&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()
						else:
							self.data = requests.get(f'https://newsapi.org/v2/everything?{aux}&{aux1}&{aux2}&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()

			else:
				if self.filtros['categorias'] == 'Saúde':
					aux0 = 'health'
				elif self.filtros['categorias'] == 'Esportes':
					aux0 = 'sports'
				elif self.filtros['categorias'] == 'Tecnologia':
					aux0 = 'technology'
				self.data = requests.get(f'https://newsapi.org/v2/top-headlines?country=br&category={aux0}&apiKey=481d4bbaa4fd4d199e8b311e92c8601f').json()

			self.clear()
			self.carregar_noticias(0)

		self.clear()



		valorbtn = StringVar()
		
		
		label_datai = Label(self.root, text='Data Início:',bg='bisque',fg='grey11')
		label_datai.grid(column = 1, row = 1)

		label_dataf = Label(self.root, text='Data Fim:',bg='bisque',fg='grey11')
		label_dataf.grid(column = 1, row = 2)

		label_assunto = Label(self.root, text='Assunto:',bg='bisque',fg='grey11')
		label_assunto.grid(column = 1, row = 3)

		label_categorias = Label(self.root, text='Categoria:',bg='bisque',fg='grey11')
		label_categorias.grid(column = 1, row = 4)


		caixa_datai_dia = Entry(self.root,width = 5)
		caixa_datai_dia.grid(column = 2, row = 1)
		
		caixa_datai_mes = Entry(self.root,width = 5)
		caixa_datai_mes.grid(column = 3, row = 1)

		caixa_datai_ano = Entry(self.root,width = 5)
		caixa_datai_ano.grid(column = 4, row = 1)


		caixa_dataf_dia = Entry(self.root,width = 5)
		caixa_dataf_dia.grid(column = 2, row = 2)
		
		caixa_dataf_mes = Entry(self.root,width = 5)
		caixa_dataf_mes.grid(column = 3, row = 2)

		caixa_dataf_ano = Entry(self.root,width = 5)
		caixa_dataf_ano.grid(column = 4, row = 2)

		caixa_assunto = Entry(self.root,width = 10)
		caixa_assunto.grid(column = 3, row = 3)

		categorias = ['Geral','Saúde','Esportes','Tecnologia']
		caixa_categorias = ttk.Combobox(self.root, values= categorias, width=10)
		caixa_categorias.set('Geral')
		caixa_categorias.grid(column = 3, row = 4)

		atualizar = Button(self.root, text='Atualizar', width=10, command = atualizar_filtros)
		atualizar.grid(column = 3, row = 9)


	def carregar_noticias(self, index):
		self.clear()

		try:
			img_url = self.data['articles'][index]['urlToImage']
			raw_data = urlopen(img_url).read()
			im = Image.open(io.BytesIO(raw_data)).resize((350,250))
			photo = ImageTk.PhotoImage(im)
		except:
			img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
			raw_data = urlopen(img_url).read()
			im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
			photo = ImageTk.PhotoImage(im)


		label = Label(self.root,image=photo)
		label.grid(column=6,row=40)


		heading = Label(self.root,text=self.data['articles'][index]['title'],bg='bisque',fg='grey11',wraplength=350,justify='center')
		heading.grid(column=6,row=48)
		heading.config(font=('verdana',15))

		details = Label(self.root, text=self.data['articles'][index]['description'], bg='bisque', fg='grey11', wraplength=350,justify='center')
		details.grid(column=6,row=49)
		details.config(font=('verdana', 12))

		frame = Frame(self.root,bg='black')
		frame.grid(column=6,row=50)

		if index != 0:
			prev = Button(frame,text='Anterior',width=16,height=3,command=lambda :self.carregar_noticias(index-1))
			prev.grid(column=5, row= 100)

		read = Button(frame, text='Ler Mais', width=16, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
		read.grid(column=6, row= 100)

		if index != len(self.data['articles'])-1:
			next = Button(frame, text='Próximo', width=16, height=3,command=lambda :self.carregar_noticias(index+1))
			next.grid(column=7, row= 100)

		self.root.mainloop()

	def open_link(self,url):
		webbrowser.open(url)


y = Login()
