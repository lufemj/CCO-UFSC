from velho import Velho
from novo import Novo

while True:
    
    endereco = input('Digite o endereço do do imóvel: ')
    print()
    preco = float(input('Digite o preço do imóvel: R$'))

    while True:
        op_valida = ['1','2','3']

        print()
        print('Selecione a condição do imóvel:')
        print('1 - Imóvel Novo')
        print('2 - Imóvel Velho')
        print('3 - Sair')
        print()

        op = input('Digite uma opção: ')

        if op not in op_valida:
            print('Opção inválida. Digite Novamente.')

        elif op == '1':
            valor = Novo(endereco, preco)
            print(f'O valor do imóvel é R${valor.preco_novo()}')
            break

        elif op == '2':
            valor = Velho(endereco, preco)
            print(f'O valor do imóvel é R${valor.preco_velho()}')
            break

        else:
            break
    