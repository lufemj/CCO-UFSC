class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def get_valor(self):
        return self.valor
    def get_naipe(self):
        return self.naipe

    def ver_cartas(self):
        print(f'{self.valor} de {self.naipe}')