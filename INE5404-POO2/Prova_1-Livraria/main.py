from classes import *


livros = []
clientes = []
vendidos = []

#Aluno: Luis Fernando Mendonça Junior 22103512
#Usado para testar com mais eficiencia
'''
livro = Livro('1', 'Narnia', 'Aventura', 364)
cliente = Pessoa('Luis','Pessoa','123','(48)9234','Rua Laranja')
livros.append(livro)
clientes.append(cliente)

cliente = Empresa('Apple','Empresa','456','9234','Rua Uva')
clientes.append(cliente)
'''


while True:
    print('========================================================')
    print('Login de funcionário')
    print()
    print('Digite 0000 para sair.')
    print('========================================================')
    senha = Funcionario(str(input("Digite a senha do sistema: ")))
    senha.verificacao()


    if senha.verificacao() == "sair":
        break
        
    elif senha.verificacao():
        while True:
            print('========================================================')
            print('Menu da Livraria')
            print('Escolha uma operação para realizar: ')
            print('1 - Cadastrar um livro')
            print('2 - Cadastrar clientes no sistema')
            print('3 - Orçamento da venda')
            print('4 - Consultar vendas')
            print('0 - Encerrar execução')
            print('========================================================')
            
            valid_op = ['0','1','2','3','4']

            op = input('Escolha uma operação: ')

            if op not in valid_op:
                print("Operação inválida. Digite Novamente.")
                print()
            
            elif op == '0':
                break

            elif op == '1':
                print('========================================================')
                print('Cadastro de livro')
                print()
                codigo = input('Código: ')
                nome = input('Nome: ')
                genero = input('Gênero: ')
                paginas = int(input('Número de páginas: '))

                livro = Livro('', '', '', '')
                livro.set_codigo(codigo)
                livro.set_nome(nome)
                livro.set_genero(genero)
                livro.set_paginas(paginas)


                livros.append(livro)


            elif op == '2':
                print('========================================================')
                print("Cadastro de cliente")
                print('1 - Cadastrar Pessoa Física')
                print('2 - Cadastrar Pessoa Jurídica')
                print('3 - Voltar')
                print('========================================================')
                opcliente = input('Escolha uma operação: ')
                
                valid_opc = ['1','2','3']

                if opcliente not in valid_opc:
                        print('Operação invalida. Digite Novamente')
                        print()
                
                elif opcliente == '1':
                    
                    cpf = input('CPF: ')
                    nome = input('Nome completo: ')
                    tel = input('Celular: ')
                    endereco = input('Endereço: ')
                
                    pessoa = Pessoa( '', '', '', '', '')

                    pessoa.set_nome(nome)
                    pessoa.set_tipo('Pessoa')
                    pessoa.set_cpf(cpf)
                    pessoa.set_tel(tel)
                    pessoa.set_endereco(endereco)
                    clientes.append(pessoa)
                    
                    print('Cliente cadastrado com sucesso.')
                    print()

                elif opcliente == '2':
                
                    cnpj = input('CNPJ: ')
                    nome = input('Nome da empresa: ')
                    tel = input('Telefone: ')
                    endereco = input('Endereço: ')

                    empresa = Empresa( '', '', '', '', '')

                    empresa.set_nome(nome)
                    empresa.set_tipo('Empresa')
                    empresa.set_cnpj(cnpj)
                    empresa.set_tel(tel)
                    empresa.set_endereco(endereco)
                    clientes.append(empresa)
                    
                    print('Cliente cadastrado com sucesso.')
                    print()

                else:
                    break


            elif op == '3':
                
                while True:
                    print('========================================================')
                    cod_livro = input('Digite o código do livro que será alugado. (Pressione 0 para sair) ')
                    print()

                    if cod_livro == '0':
                        break
                    
                    valido = False

                    for i in livros:
                        if i.get_codigo() == cod_livro:
                            valido = True
                            break

                    if valido == False:
                        print('Código invalido. Digite Novamente')
                        print()

                    else:
                        dado_cliente = input('Digite o CPF/CNPJ que será alugado. (Pressione 0 para sair) ')
                        print()

                        cliente_valido = False

                        for j in clientes:
                            tipo = j.get_tipo()

                            if tipo == 'Empresa':
                                if j.get_cnpj() == dado_cliente:
                                    tipo_cliente = j.get_tipo()
                                    cliente_valido = True
                                    break
                            elif tipo == 'Pessoa':
                                if j.get_cpf() == dado_cliente:
                                    tipo_cliente = j.get_tipo()
                                    cliente_valido = True
                                    break
                        
                        if cliente_valido == False:
                            print('CPF/CNPJ invalido. Digite Novamente')
                            print()
                        
                        else:
                            

                            valor = 0.25

                            if tipo_cliente == 'Empresa':
                                print('Desconto de 60% para Empresas')
                                print()
                                valor = 0.15

                            paginas = i.get_paginas()

                            preco_final = valor * paginas
            


                            print('Livro selecionado:')
                            print('Nome:', i.get_nome())
                            print('Gênero:', i.get_genero())
                            print('Páginas:', i.get_paginas())
                            print('Preço final: R$', preco_final)
                            print()

                            opf = input('Deseja completar a operação? S/N ')

                            opf = opf.upper()

                            if opf == 'S':
                                venda = [i, j, preco_final]
                                vendidos.append(venda)


                            else: break

            elif op == '4': 
                while True:
                    print('========================================================')
                    cod_livro = input('Digite o código do livro que será consultado. (Pressione 0 para sair) ')
                    print()

                    if cod_livro == '0':
                        break
                    
                    valido == False

                    for i in livros:
                        if i.get_codigo() == cod_livro:
                            valido == True
                            break

                    for venda in vendidos:
                        if i in venda:
                            livro = i
                            print('Dados da venda:')
                            print('Livro: ',livro.get_nome())
                            print('Gênero: ',livro.get_genero())
                            print('Vendido para: ')
                            for k in vendidos:
                                cliente = k[1]
                                print()
                                print('Nome',cliente.get_nome())
                                print('Valor: R$', k[2])
                                print()
                            print()
                            break






