from carta import Carta
from jogador import Jogador
from baralho import Baralho

deck = Baralho()
deck.criar()
jogadores = []

for r in range(1,10):
    player = Jogador(f'Jogador {r}')
    jogadores.append(player)

while True:
    valid_op = ['0', '1', '2', '3']

    print('========================================================')
    print('Menu')
    print('Escolha uma operação: ')
    print('1 - Ver cartas do baralho')
    print('2 - Embaralhar o baralho')
    print('3 - Comprar cartas para os jogadores')
    print('0 - Sair')
    print('========================================================')
    op = input('Escolha uma operação: ')
    print()
    print()

    if op not in valid_op:
        print('***********************************')
        print('Operação invalida. Digite Novamente')
        print('***********************************')

    else:
        if op == '1':
            deck.ver_baralho()

        if op == '2':
            deck.embaralhar()

        if op == '3':
        
            x = 52
            while x > 0:
                for r in jogadores:
                    if x == 0:
                        break
                    else:
                        r.comprar(deck)
                        x -= 1
            
            for o in jogadores:
                o.ver_mao()


        if op == '0':
            break