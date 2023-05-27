from tkinter import *
from produtos import Produtos

produtos = []
carrinho = []
codigos = []


def main():
	def cadastro():
		def cadastrar():
			codigo = caixa_codigo.get()
			tipo = caixa_tipo.get()
			marca = caixa_marca.get()
			quantidade = int(caixa_estoque.get())
			preco = float(caixa_preco.get())

			if codigo in codigos:
				texto_confirmacao['text'] = 'Código já cadastrado'
			
			else:
				codigos.append(codigo)

				produto1 = Produtos('','','','','')
				produto1.set_codigo(codigo)
				produto1.set_tipo(tipo)
				produto1.set_marca(marca)
				produto1.set_preco(preco)
				produto1.set_quantidade(quantidade)

				produtos.append(produto1)

				texto_confirmacao['text'] = 'Produto cadastrado com sucesso!'

		
		def voltar():
			janela2.destroy()
			main()

		
		janela.destroy()


		janela2 = Tk()
		janela2.title('Supermercado')
		#janela2.geometry("600x600")
		
		menu = Label(janela2, text='Cadastro de Produto')
		menu.grid(column = 2, row = 0)

		
		label_codigo = Label(janela2, text='Digite o código do produto:')
		label_codigo.grid(column = 1, row = 1)

		label_produto = Label(janela2, text='Informe o tipo de produto:')
		label_produto.grid(column = 1, row = 2)

		label_marca = Label(janela2, text='Informe a marca do produto:')
		label_marca.grid(column = 1, row = 3)

		label_estoque = Label(janela2, text='Informe a quantidade em estoque:')
		label_estoque.grid(column = 1, row = 4)

		label_preco = Label(janela2, text='Informe o preço unitário:')
		label_preco.grid(column = 1, row = 5)


		caixa_codigo = Entry(janela2)
		caixa_codigo.grid(column = 2, row = 1)

		caixa_tipo = Entry(janela2)
		caixa_tipo.grid(column = 2, row = 2)

		caixa_marca = Entry(janela2)
		caixa_marca.grid(column = 2, row = 3)

		caixa_estoque = Entry(janela2)
		caixa_estoque.grid(column = 2, row = 4)

		caixa_preco = Entry(janela2)
		caixa_preco.grid(column = 2, row = 5)


		botao_cadastrar = Button(janela2, text='Cadastrar', command = cadastrar)
		botao_cadastrar.grid(column = 2, row = 7)

		botao_voltar = Button(janela2, text='Voltar', command = voltar)
		botao_voltar.grid(column = 2, row = 8)

		texto_confirmacao = Label(janela2, text='')
		texto_confirmacao.grid(column = 2, row = 6)


	def remover():
		def remocao():
			codigo = caixa_codigo.get()

			if codigo not in codigos:
				texto_confirmacao['text'] = 'Produto não está cadastrado'

			else:
				codigos.remove(codigo)
				texto_confirmacao['text'] = 'Produto removido com sucesso'



		def voltar():
			janela2.destroy()
			main()

		
		janela.destroy()


		janela2 = Tk()
		janela2.title('Supermercado')
		#janela2.geometry("600x600")
		
		menu = Label(janela2, text='Remoção de Produto')
		menu.grid(column = 2, row = 0)

		
		label_codigo = Label(janela2, text='Digite o código do produto:')
		label_codigo.grid(column = 1, row = 1)


		caixa_codigo = Entry(janela2)
		caixa_codigo.grid(column = 2, row = 1)


		botao_cadastrar = Button(janela2, text='Remover', command = remocao)
		botao_cadastrar.grid(column = 2, row = 7)

		botao_voltar = Button(janela2, text='Voltar', command = voltar)
		botao_voltar.grid(column = 2, row = 8)

		texto_confirmacao = Label(janela2, text='')
		texto_confirmacao.grid(column = 2, row = 6)


	def alterar():
		def att_codigo():
			codigo_produto = caixa_cod_original.get()
			if codigo_produto in codigos:
				codigo = caixa_codigo.get()
				if codigo not in codigos:
					for i in range(len(produtos)):
						if codigo_produto == produtos[i].get_codigo():
							produtos[i].set_codigo(codigo)
							codigos.append(codigo)
							codigos.remove(codigo_produto)
					texto_confirmacao['text'] = 'Código atualizado com sucesso'
				else:
					texto_confirmacao['text'] = 'Código já cadastrado'
			else:
				texto_aux['text'] = 'Código não existe'

		def att_tipo():
			codigo_produto = caixa_cod_original.get()
			if codigo_produto in codigos:
				tipo = caixa_tipo.get()
				for i in range(len(produtos)):
					if codigo_produto == produtos[i].get_codigo():
						produtos[i].set_tipo(tipo)
				texto_confirmacao['text'] = 'Tipo atualizado com sucesso'
			else:
				texto_aux['text'] = 'Código não existe'

		def att_marca():
			codigo_produto = caixa_cod_original.get()
			if codigo_produto in codigos:
				marca = caixa_marca.get()
				for i in range(len(produtos)):
					if codigo_produto == produtos[i].get_codigo():
						produtos[i].set_marca(marca)

				texto_confirmacao['text'] = 'Marca atualizado com sucesso'
			else:
				texto_aux['text'] = 'Código não existe'

		def att_quantidade():
			codigo_produto = caixa_cod_original.get()
			if codigo_produto in codigos:
				quantidade = caixa_estoque.get()

				if quantidade == int:
					for i in range(len(produtos)):
						if codigo_produto == produtos[i].get_codigo():
							produtos[i].set_quantidade(quantidade)
					texto_confirmacao['text'] = 'Quantidade atualizada com sucesso'
				else:
					texto_confirmacao['text'] = 'Nova quantidade não é um número'
			else:
				texto_aux['text'] = 'Código não existe'
		
		def att_preco():
			codigo_produto = caixa_cod_original.get()
			if codigo_produto in codigos:
				preco = caixa_preco.get()

				if preco == float or preco == int:
					for i in range(len(produtos)):
						if codigo_produto == produtos[i].get_codigo():
							produtos[i].set_preco(preco)
					texto_confirmacao['text'] = 'Preço atualizado com sucesso'
				else:
					texto_confirmacao['text'] = 'Novo preço não é válido'
			else:
				texto_aux['text'] = 'Código não existe'
			

		def voltar():
			janela2.destroy()
			main()

		janela.destroy()

		janela2 = Tk()
		janela2.title('Supermercado')
		#janela2.geometry("600x600")
		
		menu = Label(janela2, text='Menu de Alteração')
		menu.grid(column = 2, row = 0)

		
		label_codigo = Label(janela2, text='Atualize o código do produto:')
		label_codigo.grid(column = 1, row = 3)

		label_produto = Label(janela2, text='Atualize o tipo de produto:')
		label_produto.grid(column = 1, row = 4)

		label_marca = Label(janela2, text='Atualize a marca do produto:')
		label_marca.grid(column = 1, row = 5)

		label_estoque = Label(janela2, text='Atualize a quantidade em estoque:')
		label_estoque.grid(column = 1, row = 6)

		label_preco = Label(janela2, text='Atualize o preço unitário:')
		label_preco.grid(column = 1, row = 7)


		caixa_codigo = Entry(janela2)
		caixa_codigo.grid(column = 2, row = 3)

		caixa_tipo = Entry(janela2)
		caixa_tipo.grid(column = 2, row = 4)

		caixa_marca = Entry(janela2)
		caixa_marca.grid(column = 2, row = 5)

		caixa_estoque = Entry(janela2)
		caixa_estoque.grid(column = 2, row = 6)

		caixa_preco = Entry(janela2)
		caixa_preco.grid(column = 2, row = 7)


		botao_att_codigo = Button(janela2, text='Atualizar', command = att_codigo)
		botao_att_codigo.grid(column = 3, row = 3)

		botao_att_tipo = Button(janela2, text='Atualizar', command = att_tipo)
		botao_att_tipo.grid(column = 3, row = 4)

		botao_att_marca = Button(janela2, text='Atualizar', command = att_marca)
		botao_att_marca.grid(column = 3, row = 5)

		botao_att_quantidade = Button(janela2, text='Atualizar', command = att_quantidade)
		botao_att_quantidade.grid(column = 3, row = 6)

		botao_att_preco = Button(janela2, text='Atualizar', command = att_preco)
		botao_att_preco.grid(column = 3, row = 7)

		botao_voltar = Button(janela2, text='Voltar', command = voltar)
		botao_voltar.grid(column = 2, row = 9)


		texto_confirmacao = Label(janela2, text='')
		texto_confirmacao.grid(column = 2, row = 8)
		
		texto_aux = Label(janela2, text='')
		texto_aux.grid(column = 2, row = 1)

		texto_codigo = Label(janela2, text='Digite o código original do produto')
		texto_codigo.grid(column = 1, row = 2)

		caixa_cod_original = Entry(janela2)
		caixa_cod_original.grid(column = 2, row = 2)


	def visualizar():
		def ver():
			codigo = caixa_codigo.get()

			if codigo not in codigos:
				texto_confirmacao['text'] = 'Produto não está cadastrado'

			else:
				for i in range(len(produtos)):
					if codigo == produtos[i].get_codigo():
						tipo = produtos[i].get_tipo()
						marca = produtos[i].get_marca()
						preco = produtos[i].get_preco()
						quantidade = produtos[i].get_quantidade()

						texto = f'''
						Tipo: {tipo}
						Marca: {marca}
						Preço: {preco}
						Quantidade: {quantidade} '''

						texto_info['text'] = texto



		def voltar():
			janela2.destroy()
			main()

		
		janela.destroy()


		janela2 = Tk()
		janela2.title('Supermercado')
		#janela2.geometry("600x600")
		
		menu = Label(janela2, text='Vizualizar Produto')
		menu.grid(column = 2, row = 0)

		
		label_codigo = Label(janela2, text='Digite o código do produto:')
		label_codigo.grid(column = 1, row = 1)


		caixa_codigo = Entry(janela2)
		caixa_codigo.grid(column = 2, row = 1)


		botao_cadastrar = Button(janela2, text='Vizualizar', command = ver)
		botao_cadastrar.grid(column = 2, row = 7)

		botao_voltar = Button(janela2, text='Voltar', command = voltar)
		botao_voltar.grid(column = 2, row = 8)

		texto_confirmacao = Label(janela2, text='')
		texto_confirmacao.grid(column = 2, row = 6)

		texto_info = Label(janela2, text='')
		texto_info.grid(column = 1, row = 3)


	def venda():
		def vender():
			codigo = caixa_codigo.get() 
			quantidade_venda = int(caixa_quantidade.get())

			if codigo in codigos:
				for i in range(len(produtos)):
					if codigo == produtos[i].get_codigo():
						if quantidade_venda > produtos[i].get_quantidade():
							texto_confirmacao['text'] = 'Quantidade desejada indisponível'
						else:
							n_quant = produtos[i].get_quantidade() - quantidade_venda
							produtos[i].set_quantidade(n_quant)
							valor_total = produtos[i].get_preco() * quantidade_venda
							texto_confirmacao['text'] = f'Venda confirmada no valor de R${valor_total}'

			else:
				texto_confirmacao['text'] = 'Código inválido'

		def voltar():
			janela2.destroy()
			main()

		
		janela.destroy()


		janela2 = Tk()
		janela2.title('Supermercado')
		#janela2.geometry("600x600")
		
		menu = Label(janela2, text='Vender Produto')
		menu.grid(column = 2, row = 0)

		
		label_codigo = Label(janela2, text='Digite o código do produto:')
		label_codigo.grid(column = 1, row = 1)


		caixa_codigo = Entry(janela2)
		caixa_codigo.grid(column = 2, row = 1)
		
		label_quantidade = Label(janela2, text='Digite a quantidade:')
		label_quantidade.grid(column = 1, row = 2)


		caixa_quantidade = Entry(janela2)
		caixa_quantidade.grid(column = 2, row = 2)


		botao_cadastrar = Button(janela2, text='Vender', command = vender)
		botao_cadastrar.grid(column = 2, row = 7)

		botao_voltar = Button(janela2, text='Voltar', command = voltar)
		botao_voltar.grid(column = 2, row = 8)

		texto_confirmacao = Label(janela2, text='')
		texto_confirmacao.grid(column = 2, row = 6)

		texto_info = Label(janela2, text='')
		texto_info.grid(column = 1, row = 3)

	def sair():
		janela.destroy()
	

	janela = Tk()
	janela.title('Supermercado')
	#janela.geometry("600x600")

	menu = Label(janela, text='Menu Supermercado')
	menu.grid(column = 2, row = 0)

	botao_cadastro = Button(janela, text='Cadastrar um produto', command = cadastro)
	botao_cadastro.grid(column = 2, row = 1)

	botao_remover = Button(janela, text='Remover um produto', command = remover)
	botao_remover.grid(column = 2, row = 2)

	botao_alterar = Button(janela, text='Alterar as informações', command = alterar)
	botao_alterar.grid(column = 2, row = 3)

	botao_visualizar = Button(janela, text='Visualizar produto', command = visualizar)
	botao_visualizar.grid(column = 2, row = 4)

	botao_venda = Button(janela, text='Realizar venda', command = venda)
	botao_venda.grid(column = 2, row = 5)

	botao_sair = Button(janela, text='Sair', command = sair)
	botao_sair.grid(column = 2, row = 6)

	janela.mainloop()

main()