from produtos import Produtos


produtos = []
carrinho = []
codigos = []

op1 = True

while True:
    print()
    print('------------------- MENU -------------------')
    print()
    print('1 - Entrar como funcionário.')
    print('2 - Entrar como cliente.')
    print('0 - Sair.')
    print()
    print('--------------------------------------------')

    valid_op = ['0', '1', '2']

    if op1 == True:
        op = input('Selecione uma operação: ')

    if op1 == False:
        op = input('Operação inválida. Tente novamente: ')

    if op not in valid_op:
        op1 = False
        print()

    elif op == '0':
        break

    if op == '1':
        op1 = True
        op2 = True
        while True:
            senha = ['123']
            print()
            print('Digite "0000" para sair')
            if op2 == True:
                op = input('Digite sua senha: ')
                print()
            else:
                op = input('Senha inválida. Tente novamente: ')
                print()


            if op in senha:
                break

            elif op not in senha:
                op2 = False

            if op == '0000':
                break

        op2 = True
        if op in senha:
            while True:
                valid_op = ['0', '1', '2', '3', '4']
                print('------------------- MENU -------------------')
                print()
                print('1 - Cadastrar um produto.')
                print('2 - Remover um produto.')
                print('3 - Alterar as informações de um produto.')
                print('4 - Visualizar catálogo.')
                print('0 - Voltar.')
                print()
                print('--------------------------------------------')

                if op1 == True:
                    op = input('Selecione uma operação: ')

                if op1 == False:
                    op = input('Operação inválida. Tente novamente: ')

                if op not in valid_op:
                    op1 = False

                if op == '0':
                    break
                
                if op == '1':
                    print('------------ CADASTRO DE PRODUTO -----------')
                    print()
                    op1 = True
                    while True:
                        if op1 == True:
                            print()
                            print('Digite "0000" para voltar')
                            print()
                            codigo = int(input('Digite o código do produto: '))
                        
                        else:
                            print()
                            print('Digite "0000" para voltar')
                            print()
                            codigo = int(input('Código já cadastrado. Digite outro código: '))

                        if codigo == 0000:
                            break

                        if codigo in codigos:
                            op1 = False
                            
                        if codigo not in codigos:
                            break

                    if codigo == 0000:
                        break

                    op1 = True           
                    codigos.append(codigo)

                    tipo = input('Informe o tipo de produto: ')
                    marca = input('Informe a marca do produto: ')
                    quantidade = int(input('Informe a quantidade em estoque: '))
                    preco = float(input('Informe o preço unitário: '))

                    produto1 = Produtos('','','','','')
                    produto1.set_codigo(codigo)
                    produto1.set_tipo(tipo)
                    produto1.set_marca(marca)
                    produto1.set_preco(preco)
                    produto1.set_quantidade(quantidade)

                    produtos.append(produto1)

                    print()
                    print('Produto cadastrado com sucesso!')
                    print()
                
                if op == '2':
                    op1 = True
                    while True:
                        if op1 == True:
                            print()
                            print('Digite "0000" para voltar')
                            print()
                            op = int(input('Digite o código do produto que será removido: '))
                            print()
                        
                        else:
                            print()
                            print('Digite "0000" para voltar')
                            print()
                            op = int(input('Produto não cadastrado no sistema. Tente novamente: '))
                            print()
                        
                        if op == 0000:
                            break

                        if op not in codigos:
                            op1 = False
                        
                        if op in codigos:
                            codigos.remove(op)
                            break

                    for i in range(len(produtos)):
                        if op == produtos[i].get_codigo():
                            produtos.remove(produtos[i])
                            print()
                            print('Produto removido com sucesso!')
                            print()
                            break
                        
                if op == '3':
                    op1 = True
                    while True:
                        if op1 == True:
                            cod1 = int(input('Digite o código do produto a ser alterado: '))

                        elif op1 == False:
                            cod1 = int(input('Produto não cadastrado no sistema. Tente novamente: '))

                        if cod1 not in codigos:
                            op1 = False
                        
                        else:
                            codigo_produto = cod1
                            break
                    
                    valid_op = ['0', '1', '2', '3', '4', '5']
                    op1 = True

                    while True:
                        print('--------------- MENU DE ALTERAÇÃO ---------------')
                        print()
                        print('1 - Alterar código')
                        print('2 - Alterar tipo')
                        print('3 - Alterar marca')
                        print('4 - Alterar preço')
                        print('5 - Alterar quantidade')
                        print('0 - Voltar')
                        print()

                        if op1 == True:
                            op = input('Selecione uma operação: ')
                        
                        elif op1 == False:
                            op = input('Operação inválida. Tente novamente: ')
                        
                        if op not in valid_op:
                            op1 = False
                        
                        if op == '0':
                            break

                        if op == '1':
                            op1 = True
                            for i in range(len(produtos)):
                                if codigo_produto == produtos[i].get_codigo():
                                    
                                    while True:
                                        if op1 == True:
                                            novo_codigo = int(input('Digite o novo código do produto: '))
                                        else:
                                            novo_codigo = int(input('Código já cadastrado. Digite outro código: '))

                                        if novo_codigo in codigos:
                                            op1 = False
                                            
                                        else:
                                            produtos[i].set_codigo(novo_codigo)
                                            codigos.append(novo_codigo)
                                            codigos.remove(codigo_produto)
                                            print()
                                            print('Código alterado com sucesso!')
                                            print()
                                            op1 = True
                                            break
                                        

                        if op == '2':
                            for i in range(len(produtos)):
                                if codigo_produto == produtos[i].get_codigo():
                                    novo_tipo = input('Digite o novo tipo de produto: ')
                                    produtos[i].set_tipo(novo_tipo)
                                    print()
                                    print('Tipo alterado com sucesso!')
                                    print()
                            break

                        if op == '3':
                            for i in range(len(produtos)):
                                if codigo_produto == produtos[i].get_codigo():
                                    nova_marca = input('Digite a nova marca do produto: ')
                                    produtos[i].set_marca(nova_marca)
                                    print()
                                    print('Marca alterada com sucesso!')
                                    print()
                            break

                        if op == '4':
                            for i in range(len(produtos)):
                                if codigo_produto == produtos[i].get_codigo():
                                    novo_preco = float(input('Digite o novo preço do produto: '))
                                    produtos[i].set_preco(novo_preco)
                                    print()
                                    print('Preço alterado com sucesso!')
                                    print()
                            break

                        if op == '5':
                            for i in range(len(produtos)):
                                if codigo_produto == produtos[i].get_codigo():
                                    nova_quant = int(input('Digite a nova quantidade do produto: '))
                                    produtos[i].set_quantidade(nova_quant)
                                    print()
                                    print('Quantidade alterada com sucesso!')
                                    print()
                            break

                if op == '4':
                    print('------------------- CATÁLOGO -------------------')
                    print()
                    for i in range(len(produtos)):
                        indice = i + 1
                        codigo1 = produtos[i].get_codigo()
                        tipo1 = produtos[i].get_tipo()
                        marca1 = produtos[i].get_marca()
                        preco1 = produtos[i].get_preco()
                        quantidade1 = produtos[i].get_quantidade()
                        print('%d - Código: %d, Tipo: %s, Marca: %s, Preço: R$ %.2f, Quantidade: %d' % (indice ,codigo1, tipo1, marca1, preco1, quantidade1))
                        print()
                               
    if op == '2':
        valid_op = ['0', '1', '2']
        op1 = True
        while True:
            print('------------------- MENU -------------------')
            print()
            print('1 - Realizar compras.')
            print('0 - Voltar.')
            print()
            print('--------------------------------------------')

            if op1 == True:
                op = input('Selecione uma operação: ')
            
            else:
                op = input('Operação inválida. Tente novamente: ')

            if op not in valid_op:
                op1 = False
            
            elif op in valid_op:
                break
        
            if op == '0':
                break

        if op == '1':
            valor_total = 0
            op1 = True
            while True:
                print('------------------- CATÁLOGO -------------------')
                print()
                for i in range(len(produtos)):
                    indice = i + 1
                    codigo1 = produtos[i].get_codigo()
                    tipo1 = produtos[i].get_tipo()
                    marca1 = produtos[i].get_marca()
                    preco1 = produtos[i].get_preco()
                    quantidade1 = produtos[i].get_quantidade()
                    print('%d - Código: %d, Tipo: %s, Marca: %s, Preço: R$ %.2f, Quantidade: %d' % (indice ,codigo1, tipo1, marca1, preco1, quantidade1))
                    print()
                
                if op1 == True:
                    print('----------------------------------------------')
                    print('Digite "0000" para voltar')
                    print('Digite "9999" para finalizar a compra')
                    print()
                    prod = int(input('Selecione o código do produto para adicioná-lo ao carrinho: '))
                    print()
                
                if op1 == False:
                    print('Digite "0000" para voltar')
                    print('Digite "9999" para finalizar a compra')
                    print()
                    prod = int(input('Código inválido. Tente novamente: '))
                    print()

                if prod == 9999:
                    print('Valor total do carrinho: R$ %.2f' % (valor_total))
                    print()
                    break

                if prod == 0000:
                    break

                if prod not in codigos:
                    op1 = False
                
                elif prod in codigos:
                    op1 = True
                    for i in range(len(produtos)):
                        if prod == produtos[i].get_codigo():
                            while True:
                                if op1 == True:
                                    op = int(input('Digite a quantidade desejada: '))
                                    print()
                                else:
                                    print('Quantidade desejada indisponível. Há %d itens em estoque.' % (produtos[i].get_quantidade()))
                                    op = int(input('Digite uma quantidade válida: '))
                                    print()

                                if op > produtos[i].get_quantidade():
                                    op1 = False
                                else:
                                    print('Produto(s) adicionados ao carrinho com sucesso!')
                                    print()
                                    n_quant = produtos[i].get_quantidade() - op
                                    produtos[i].set_quantidade(n_quant)
                                    valor_total += produtos[i].get_preco() * op
                                    break