from carta import Carta
import random

class Baralho:
    def __init__(self):
        self.cartas = []

    def criar(self):
        for naipe in ['Paus', 'Copas', 'Espadas', 'Ouros']:
            for valor in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cartas.append(Carta(valor, naipe))

    def ver_baralho(self):
        if self.cartas == []:
            print('***********************************')
            print('Não há cartas no baralho.')
            print('***********************************')
            print()

        else:
            print('Cartas do baralho:')
            print()
            for i in self.cartas:
                i.ver_cartas()

    def embaralhar(self):
        if self.cartas == []:
            print('***********************************')
            print('Não há cartas no baralho.')
            print('***********************************')
            print()

        else:
            random.shuffle(self.cartas)
            print('***********************************')
            print('Deck embaralhado com sucesso.')
            print('***********************************')
            print()

    def comprar_baralho(self):
        if self.cartas == []:
            pass

        else:
            self.cartas.reverse()
            carta = self.cartas.pop()
            self.cartas.reverse()
            return carta