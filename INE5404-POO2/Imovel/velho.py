from imovel import Imovel

class Velho(Imovel):
    def __init__(self, endereco, preco):
        super().__init__(endereco, preco)

    def preco_velho(self):
        return self.preco * 0.85
        