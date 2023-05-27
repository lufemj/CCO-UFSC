from carta import Carta
import random

class Baralho:
    def __init__(self):
        self.cartas = []

    def criar(self):
        for naipe in ['Ouros','Espadas','Copas', 'Paus']:
            for valor in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A']:
                self.cartas.append(Carta(valor, naipe))
        return self.cartas

    def embaralhar(self):
        random.shuffle(self.cartas)

    def comprar_baralho(self):
        if self.cartas == []:
            pass

        else:
            self.cartas.reverse()
            carta = self.cartas.pop()
            self.cartas.reverse()
            return carta

    def novo_deck(self):
        self.cartas = []
        self.criar()
        self.embaralhar()
