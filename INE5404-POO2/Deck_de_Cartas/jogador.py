from carta import Carta

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def comprar(self, baralho):
        self.mao.append(baralho.comprar_baralho())
        return self

    def ver_mao(self):
        print(f'Cartas de {self.nome}:')
        print()
        for j in self.mao:
            j.ver_cartas()
        print()

    