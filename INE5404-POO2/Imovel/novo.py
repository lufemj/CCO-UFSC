from imovel import Imovel

class Novo(Imovel):
    def __init__(self, endereco, preco):
        super().__init__(endereco, preco)

    def preco_novo(self):
        return self.preco * 1.15