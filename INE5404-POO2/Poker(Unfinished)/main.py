from carta import Carta
from jogador import Jogador
from baralho import Baralho

deck = Baralho()
cartas_aux = deck.criar()
jogadores = []
jogadores_validos = []
blind = -50


def novo_round(blind):
    for i in jogadores:
        i.limpar_mao()
        i.set_fold(False)

    for o in jogadores:
        if (o.get_fichas() > 0):
            o.get_fold() == False
            jogadores_validos.append(o)

    if blind != -50:
        if (blind + 1 >= len(jogadores_validos)):
            if blind < len(jogadores_validos):
                jogadores_validos[blind].set_blind(False)
            blind = 0
        else:
            jogadores_validos[blind].set_blind(False)
            blind += 1

    else:
        blind = 0

    jogadores_validos[blind].set_blind(True)
    

    mesa.limpar_mao()
    mesa.set_fichas(0)
    deck.novo_deck()

    for i in jogadores_validos:
        while True:
            if len(i.get_mao()) < 2:
                i.comprar(deck)
            else:
                break

    for j in jogadores_validos:
            if j.get_blind() == True:
                j.set_fichas(j.get_fichas() - 2)
                mesa.set_fichas(mesa.get_fichas()+2)
    

    return blind

def calc_aumento(aumento,x):
    pot = 0
    if x == 1:
        for k in jogadores_validos:
            if k.get_blind() == False:
                if (2+aumento) > k.get_fichas():
                    novas_fichas = 0
                    pot += k.get_fichas()
                    k.set_fichas(0)

                else:    
                    novas_fichas = k.get_fichas() - (2 + aumento)
                    pot += (2 + aumento)
                    k.set_fichas(novas_fichas)

            else:
                novas_fichas = k.get_fichas() - aumento
                pot += aumento
                k.set_fichas(novas_fichas)

    elif x == 2:
        for p in jogadores_validos:
            if (aumento) > p.get_fichas():
                novas_fichas = 0
                pot += p.get_fichas()
                k.set_fichas(0)

            else:    
                novas_fichas = p.get_fichas() - (aumento)
                pot += (aumento)
                p.set_fichas(novas_fichas)

        
    mesa.set_fichas(mesa.get_fichas()+pot)

def menu():
    print('========================================================')
    for j in jogadores:
        j.ver_fichas()
    print('========================================================')
    mesa.ver_fichas()
    print()
    mesa.ver_mao()


    print()
    jogadores[0].ver_mao()


    while True:
        valid_op = ['1', '2', '3']

        print('========================================================')
        print('Escolha uma operação: ')
        print('1 - Check')
        print('2 - Aumentar')
        print('3 - Fold')
        print('========================================================')
        op = input('Escolha uma operação: ')
        print()
        print()

        if op not in valid_op:
            print('***********************************')
            print('Operação invalida. Digite Novamente')
            print('***********************************')

        else: return op

def menu_aumento():
    while True:
        print('========================================================')
        print('Aumentar Aposta')
        
        aumento = float(input('Quantas fichas deseja aumentar: '))

        if aumento < 1:
            print('Quantidade Inválida. Digite novamente')
        elif aumento > jogadores[0].get_fichas():
            print('Quantidade de Fichas insuficiente.')
        else: break
    return aumento

def comparar():
    def definir_valores(valor):
        num = valor
        poder = 0
        if num == 'A':
            poder = 14
        elif num == 'K':
            poder = 13
        elif num == 'Q':
            poder == 12
        elif num == 'J':
            poder == 11
        else:
            poder = int(num)
        
        return poder

    for t in jogadores:
        t.set_poder(0)
        if t.get_fold() == True and t != jogadores[0]:
            if t in jogadores_validos:
                jogadores_validos.remove(t)

    for player in jogadores_validos:
        aux = 0
        cards_mao = player.get_mao()
        for card in cards_mao:
            valor = card.get_valor()
            valor_mao = definir_valores(valor)
            if aux == 0:
                carta2 = cards_mao[1]
                valor2 = carta2.get_valor()
                valor2_mao = definir_valores(valor2)
                if valor_mao == valor2_mao:
                    x = player.get_poder()
                    player.set_poder(x+30)
                aux = 1
                    
            cards_mesa = mesa.get_mao()
            for table in cards_mesa:
                valor = table.get_valor()
                valor_mesa = definir_valores(valor)

                x = player.get_poder()
                if valor_mao == valor_mesa:
                    player.set_poder(x+30)
            
            x = player.get_poder()
            player.set_poder(valor_mao+x)
                        

for r in range(5):
	player = Jogador(f'Jogador {r+1}')
	jogadores.append(player)

mesa = Jogador('Mesa')

blind = novo_round(blind)

op = 0

while True:
    if len(mesa.get_mao()) == 3:
        comparar()

        for y in jogadores_validos:
            if y != jogadores[0]:
                if y.get_poder() < 30:
                    y.set_fold(True)

    if op != '3':
        op = menu()

    if op == '3' and len(mesa.get_mao()) != 5:
        while len(mesa.get_mao()) < 3:
            mesa.comprar(deck)
        comparar()

        while len(mesa.get_mao()) < 5:
            mesa.comprar(deck)

        comparar()

        print()
        mesa.ver_mao()

    if len(mesa.get_mao()) == 0:

        if op == '1':
            calc_aumento(0,1)
        
        if op == '2':
            
            aumento = menu_aumento()

            calc_aumento(aumento, 1)


    if len(mesa.get_mao()) == 3:
        if op == '1':
            for i in range(2):
                mesa.comprar(deck)

        if op == '2':
            aumento = menu_aumento()
            calc_aumento(aumento, 2)

        while len(mesa.get_mao()) < 5:
            mesa.comprar(deck)

    if len(mesa.get_mao()) == 0:
        for i in range(3):
            mesa.comprar(deck)

    if len(mesa.get_mao()) == 5:
        print('========================================================')
        mesa.ver_mao()
        print()
        print('========================================================')
        comparar()
        #MUDAR ABAIXO
        maior = 0
        for final in jogadores_validos:
            if final.get_poder() > maior:
                ganhador = final
                ganhador_nome = final.get_nome()
                maior = final.get_poder()

        print()
        print(f'Mão mais forte: {ganhador_nome}')
        ganhador.ver_mao()
        print('========================================================')
        print()

        ganhador.set_fichas(ganhador.get_fichas()+mesa.get_fichas())
        mesa.set_fichas(0)
        op = 0
###MUDAR ACIMA
        if jogadores[0].get_fichas() == 50: 
            print('Parabéns!')
            print('Você Venceu')
            break

        if jogadores[0].get_fichas() == 0:
            print('Banca Zerada.')
            print('Você Perdeu')
            break

        jogadores_validos = []
        blind = novo_round(blind)

    

            