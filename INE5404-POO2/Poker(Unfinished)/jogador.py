from carta import Carta

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.fichas = 10.0
        self.fold = False
        self.poder = 0
        self.blind = False

    def get_nome(self):
        return self.nome
    def get_mao(self):
        return self.mao
    def get_fichas(self):
        return self.fichas
    def get_fold(self):
        return self.fold
    def get_poder(self):
        return self.poder
    def get_blind(self):
        return self.blind


    def set_fichas (self, fichas):
            self.fichas = fichas
    def set_fold (self, fold):
            self.fold = fold
    def set_poder (self, poder):
            self.poder = poder
    def set_blind (self, blind):
            self.blind = blind

    def comprar(self, baralho):
        self.mao.append(baralho.comprar_baralho())
        return self

    def ver_mao(self):
        print(f'Cartas {self.nome}:')
        print()
        for j in self.mao:
            j.ver_cartas()
        print()

    def ver_fichas(self):
        print(f'Fichas {self.nome}: {self.fichas}')
        if self.fold == True:
            print('Fold')
        else:
            if self.blind == True:
                print("BLIND: 2 Fichas")
        print()

    def limpar_mao(self):
        self.mao = []


    

    