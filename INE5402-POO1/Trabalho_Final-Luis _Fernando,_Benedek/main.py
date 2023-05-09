from cliente import Cliente
from automovel import Automovel
from empresa import Empresa
from funcionario import Funcionario
from pessoa import Pessoa
from historico import Historico

frota = {}
clientes = {}
alugados = []



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
            print('Menu da Locadora')
            print('Escolha uma operação para realizar: ')
            print('1 - Cadastrar veículo para a frota')
            print('2 - Cadastrar clientes no sistema')
            print('3 - Orçamento de aluguel')
            print('4 - Devolução')
            print('5 - Consultar históricos de aluguéis')
            print('6 - Consultar dados')
            print('7 - Atualizar dados')
            print('0 - Encerrar execução')
            print('========================================================')
            op = int(input('Escolha uma operação: '))
        

            if op < 0 or op > 7:
                        print('Operação invalida. Digite Novamente')
                        print()

            elif op == 1:
                while True:
                    print('========================================================')
                    print('Veículo')
                    print('1 - Cadastrar')
                    print('2 - Apagar')
                    print('3 - Voltar')
                    print('========================================================')
                    op1 = int(input('Escolha uma operação: '))
                    
                    
                    if op1 < 1 or op1 > 3:
                        print('Operação invalida. Digite Novamente')
                        print()
                    
                    elif op1 == 1:
                        print('========================================================')
                        print('Cadastro de veículo')
                        print()
                        placa = str(input('Placa: '))
                        marca = str(input('Marca: '))
                        tipo = str(input('Tipo: '))
                        preco = float(input('Preço da diária: '))
                        quilometragem = int(input('Quilometragem atual: '))

                        auto = Automovel('', '', '', '', '')
                        auto.set_placa(placa)
                        auto.set_marca(marca)
                        auto.set_tipo(tipo)
                        auto.set_preco(preco)
                        auto.set_quilometragem(quilometragem)

                        frota[placa] = auto


                    elif op1 == 2:
                        print('========================================================')
                        print('Apagar veículo cadastrado')
                        print()
                        auto_placa = str(input('Placa do veículo a ser apagado da frota:  '))
                        
                        if auto_placa in frota.keys():
        
                            frota.pop(auto_placa)
                        
                            print(f"Veiculo com placa {auto_placa} foi removido da frota")
                            print()
                            
                        else:
                            print(f"A placa {auto_placa} nao esta cadastrado na frota!")
                            print()

                    else:
                        break

            elif op == 2:
                print('========================================================')
                print("Cadastro de cliente")
                print('1 - Cadastrar Pessoa Física')
                print('2 - Cadastrar Pessoa Jurídica')
                print('3 - Voltar')
                print('========================================================')
                opcliente = int(input('Escolha uma operação: '))
                print("Informe os seguintes dados")
                print()

                if opcliente < 1 or opcliente > 3:
                        print('Operação invalida. Digite Novamente')
                        print()
                
                elif opcliente == 1:
                    while True:
                        cpf = input('CPF: ')
                        if cpf in clientes.keys():
                            print('ERRO: CPF já está cadastrado.')
                            print()
                        elif len(cpf) > 14:
                            print('ERRO: CPF é invalido.')
                            print()
                        else:
                            break

                    nome = str(input('Nome completo: '))
                    tel = str(input('Telefone ou Celular: '))
                    endereco = str(input('Endereço: '))
                
                    pessoa = Pessoa( '', '', '', '', '')

                    pessoa.set_nome(nome)
                    pessoa.set_tipo("Pessoa Física")
                    pessoa.set_cpf(cpf)
                    pessoa.set_tel(tel)
                    pessoa.set_endereco(endereco)
                    clientes[cpf] = pessoa
                    
                    print('Cliente cadastrado com sucesso.')
                    print()

                elif opcliente == 2:
                    while True:
                        cnpj = input('CNPJ: ')
                        if cnpj in clientes.keys():
                            print('ERRO: CNPJ já está cadastrado.')
                            print()
                        elif len(cnpj) < 15:
                            print('ERRO: CNPJ é invalido.')
                            print()
                        else:
                            break

                    nome = str(input('Nome da empresa: '))
                    tel = str(input('Telefone ou Celular: '))
                    endereco = str(input('Endereço: '))

                    empresa = Empresa( '', '', '', '', '')

                    empresa.set_nome(nome)
                    empresa.set_tipo("Empresa")
                    empresa.set_cnpj(cnpj)
                    empresa.set_tel(tel)
                    empresa.set_endereco(endereco)
                    clientes[cnpj] = empresa
                    
                    print('Cliente cadastrado com sucesso.')
                    print()

                else:
                    break

            elif op == 3:

                while True:
                    print('========================================================')
                    print('Orçamento de aluguel')
                    print()
                    print('1 - Aluguel para Pessoa Física (1 Veículo)')
                    print('2 - Aluguel para Pessoa Jurídica (1+ Veículos)')
                    print('3 - Voltar')
                    print('========================================================')
                    op3 = int(input('Escolha uma operação: '))

                    if op3 < 1 or op3 > 3:
                        print('Operação invalida. Digite Novamente')
                        print()

                    elif op3 == 3:
                            break

                    print('========================================================')
                    while True:
                        cadastro = input("Informe o CPF/CNPJ do cliente: ")
                        print()
                        if cadastro == "0":
                            break

                        if len(cadastro) < 15 and op3 == 2:
                            print('CNPJ inválido. Digite Novamente, Tecle 0 para voltar')
                            print()

                        elif len(cadastro) > 14 and op3 == 1:
                            print('CPF inválido. Digite Novamente, Tecle 0 para voltar')
                            print()

                        else:
                            break

                    if cadastro in clientes.keys():
                        print('========================================================')
                        print('Veículos disponíveis na frota: ')
                        for placa in frota:
                            auto=frota[placa]
                            if placa not in alugados:

                                print("...............")
                                print("Marca:", auto.get_marca())
                                print("Modelo:", auto.get_tipo())
                                print("Placa:", auto.get_placa())
                                print()
                            
                        

                        if op3 == 1:
                            print('========================================================')
                            placa = str(input('Placa do veículo a ser alugado:  '))
                            if placa in frota.keys() and placa not in alugados:
                                orcamento = frota[placa]
                                print('========================================================')
                                print("Veículo selecionado")
                                print("Marca: ",orcamento.get_marca())
                                print("Modelo: ",orcamento.get_tipo())
                                print("Quilometragem: ",orcamento.get_quilometragem())
                                print()
                                print("Valor diário do aluguel: ")
                                print(f"R${orcamento.get_preco()} + R$1,50 por Km excedido.")
                                print("Incluso: 200Km(s) diários")
                                print('========================================================')


                                if (input("Deseja confirmar o aluguel do veículo?(S/N) ").upper()) == "S":          
                                    print()
                                    alugados.append(placa)
                                    print("Veículo foi alugado com sucesso")
                                    print()

                                else:
                                    print("Orçamento cancelado.")
                                    print()
                    
                            else:
                                print (f"A placa {placa} não esta cadastrado na frota! ")      
                                print()      
                                break
                                

                        elif op3 == 2:
                            print('========================================================')
                            num_veic = int(input("Número de veículos a serem alugados pela empresa: "))
                            print()
                            for carro in range (num_veic):
                                porc = str(input(f'Placa do veículo ({carro+1}) a ser alugado:  '))
                                if porc in frota.keys():
                                    orca = frota[porc]
                                    print("Veículo selecionado: ")
                                    print(orca.get_marca())
                                    print(orca.get_tipo())
                                    print()
                                    print("Valor diário do aluguel: ")
                                    print(f"R$:{orca.get_preco()}")
                                    print("incluso: 200Km(s) diários")
                                    print(f"Desconto para empresa: -15% do valor final")
                                    print()


                                    if (input("Deseja confirmar o aluguel do veículo?(S/N) ").upper()) == "S":          
                                        print()
                                        alugados.append(placa)
                                        print("-.-.-.-.-.-.-.-.-")
                                        print()
                                        print("Veículo foi alugado com sucesso")
                                        print()
                                        print("-.-.-.-.-.-.-.-.-")


                                    else:
                                        print()
                                        print("Orçamento cancelado.")

                                else:
                                    print (f"A placa {porc} nao esta cadastrado na frota! ")            
                                    break
                                
                    else:
                        print("O cliente informado não está cadastrado.")
                    

            elif op == 4:
                print('========================================================')
                print('Devolução de veículo')
                
                placa_devolvido = str(input('Placa do veículo a ser devolvido:  '))
                print()

                if placa_devolvido in alugados:

                    carro_devolvido = frota[placa_devolvido]
                    
                    while True:
                        devolvedor = str(input('CPF/CNPJ do cliente que devolveu o automóvel:  '))
                        print()
                        

                        if devolvedor in clientes.keys():
                            break
                            
                        else:
                            print('ERRO: CPF/CNPJ não está. Digite novamente.')
                            print()

                    while True:
                        quilometragem_nova = int(input("Quilometragem atual do veículo: "))
                        quilometragem_antiga = carro_devolvido.get_quilometragem()

                        if quilometragem_nova < quilometragem_antiga:
                            print('ERRO: A nova quilometragem é menor que a antiga. Digite novamente.')
                            print()
                        else:
                            break

                    while True:
                        dias_alugados = int(input('Dias decorridos desde a retirada:  '))

                        if dias_alugados < 1:
                            print('ERRO: O veículo tem que ter sido alugado por pelo menos um dia. Digite novamente.')
                            print()
                        else:
                            break

                    
                    alugados = [value for value in alugados if value != placa_devolvido]
                    
                    cliente_devolveu = clientes[devolvedor]
                    km_rodado = carro_devolvido.km_rodado(quilometragem_nova)
                    carro_devolvido.set_quilometragem(quilometragem_nova)
                    diaria_atual = carro_devolvido.get_preco()
                    valor_total = cliente_devolveu.calcular_locacao(km_rodado, dias_alugados, diaria_atual)

                    print('========================================================')
                    
                    print(f"Km(s) rodados: {km_rodado}")
                    print("incluso: 200Km(s) diários")
                    print()

                    nome = cliente_devolveu.get_nome()
                    tipo = cliente_devolveu.get_tipo()
                    
                    carro_devolvido.registrar_historico(nome, dias_alugados, km_rodado, tipo)


                    print("-.-.-.-.-.-.-.-.-")
                    print()
                    print(f"Valor total : {valor_total} ")
                    print()
                    print("-.-.-.-.-.-.-.-.-")
                
                else:
                    if placa_devolvido in frota.keys():
                        print( "ERRO : Veiculo não foi alugado")
                        print()
                    else:
                        print (f"A placa {placa_devolvido} não esta cadastrada na frota! ")
                        print()

            elif op == 5:

                placa = str(input('Placa do veículo a ser consultado:  '))

                if placa in frota.keys():
                    auto = frota[placa]
                    alugado_momento = placa in alugados
                    auto.historico.listagem(alugado_momento)
                else:
                    print('Placa não está registrada na frota! ')
            


            elif op == 6:
                while True:
                    print('========================================================')
                    print('Consultar dados cadastrais')
                    print()
                    print('1 - Consultar dados de veículo')
                    print('2 - Consultar dados de clientes')
                    print('3 - Voltar')
                    print('========================================================')
                    op6 = int(input('Escolha uma operação: '))


                    if op6 < 1 or op6 > 3:
                        print('Operação invalida. Digite Novamente')
                        print()

                    elif op6 == 3:
                        break

                    elif op6 == 1:
                        print('========================================================')
                        placa = input("Informe a placa do veículo que deseja consultar: ")
                        print()
                        if placa not in frota:
                            print("Placa não está registrada.")
                            print()
                            break

                        auto = frota[placa]

                        print("...............")
                        print("Placa:", auto.get_placa())
                        print("Marca:", auto.get_marca())
                        print("Tipo", auto.get_tipo())
                        print("Preço:", auto.get_preco())
                        print("Quilometragem:", auto.get_quilometragem())
                        print()

                    elif op6 == 2:
                        print('========================================================')
                        codigo = input("Informe o CPF/CNPJ do cliente que deseja consultar: ")
                        print()
                        
                        if codigo not in clientes:
                            print("Cliente não está registrado.")
                            print()
                            break

                        cliente = clientes[codigo]

                        print("...............")
                        print("Nome:", cliente.get_nome())
                        print("Tipo:", cliente.get_tipo())
                        if len(codigo) > 14:
                            print("CNPJ:", cliente.get_cnpj())
                        else:
                            print("CPF:", cliente.get_cpf())
                        print("Telefone:", cliente.get_tel())
                        print("Endereço:", cliente.get_endereco())
                        print()


            elif op == 7:

                while True:
                    print('========================================================')
                    print('Atualizar dados cadastrais')
                    print()
                    print('1 - Atualizar dados de veículo')
                    print('2 - Atualizar dados de clientes')
                    print('3 - Voltar')
                    print('========================================================')
                    op7 = int(input('Escolha uma operação: '))


                    if op7 < 1 or op7 > 3:
                        print('Operação invalida. Digite Novamente')
                        print()

                    elif op7 == 3:
                        break

                    elif op7 == 1:
                        print('========================================================')
                        placa = input("Informe a placa do veículo que terá seus dados alterados: ")
                        print()
                        if placa not in frota:
                            print("Placa não está registrada.")
                            print()
                            break

                        auto = frota[placa]

                        print('========================================================')
                        print('Qual dado deseja alterar: ')
                        print()
                        print('1 - Placa')
                        print('2 - Marca')
                        print('3 - Tipo')
                        print('4 - Preço')
                        print('5 - Quilometragem')
                        print('6 - Cancelar')
                        print('========================================================')
                        op7_2 = int(input('Escolha uma operação: '))

                        if op7_2 < 1 or op7_2 > 6:
                            print('Operação invalida. Digite Novamente')
                            print()

                        elif op7_2 == 1:
                            alteracao = input('Novo dado da placa: ')
                            auto.set_placa(alteracao)
                        
                        elif op7_2 == 2:
                            alteracao = input('Novo dado da marca: ')
                            auto.set_marca(alteracao)

                        elif op7_2 == 3:
                            alteracao = input('Novo dado do tipo: ')
                            auto.set_tipo(alteracao)
                        
                        elif op7_2 == 4:
                            alteracao = input('Novo dado do preço: ')
                            auto.set_preco(alteracao)

                        elif op7_2 == 5:
                            alteracao = input('Novo dado da quilometragem: ')
                            auto.set_quilometragem(alteracao)
                        
                        else:
                            break
                        
                        print()
                        print('Dado Alterado com sucesso.')
                        print()


                    elif op7 == 2:
                        print('========================================================')
                        codigo = input("Informe o CPF/CNPJ do cliente que terá seus dados alterados: ")
                        print()

                        if codigo not in clientes:
                            print("Cliente não está registrado.")
                            print()
                            break

                        cliente = clientes[codigo]

                        print('========================================================')
                        print('Qual dado deseja alterar: ')
                        print()
                        print('1 - Nome')
                        print('2 - Tipo')
                        if len(codigo) > 14:
                            print('3 - CNPJ')
                        else:
                            print('3 - CPF')
                        print('4 - Telefone')
                        print('5 - Endereço')
                        print('6 - Cancelar')
                        print('========================================================')
                        op7_1 = int(input('Escolha uma operação: '))

                        if op7_1 < 1 or op7_1 > 6:
                            print('Operação invalida. Digite Novamente')
                            print()

                        elif op7_1 == 1:
                            alteracao = input('Novo dado do nome: ')
                            cliente.set_nome(alteracao)
                        
                        elif op7_1 == 2:
                            alteracao = input('Novo dado do tipo: ')
                            cliente.set_tipo(alteracao)

                        elif op7_1 == 3:
                            if len(codigo) > 14:
                                alteracao = input('Novo dado do CNPJ: ')
                                cliente.set_cnpj(alteracao)
                            else:
                                alteracao = input('Novo dado do CPF: ')
                                cliente.set_cpf(alteracao)
                        elif op7_1 == 4:
                            alteracao = input('Novo dado do telefone: ')
                            cliente.set_tel(alteracao)

                        elif op7_1 == 5:
                            alteracao = input('Novo dado do endereço: ')
                            cliente.set_endereco(alteracao)
                        
                        else:
                            break
                        
                        print()
                        print('Dado Alterado com sucesso.')
                        print()



            else:
                break

    else:
        print ("=/==")
        print ("Senha Incorreta. Digite Novamente.")
        print ("=/==")


