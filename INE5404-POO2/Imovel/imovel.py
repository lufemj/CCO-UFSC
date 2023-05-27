class Imovel():
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def get_endereco(self):
        return self.endereco
    def get_preco(self):
        return self.preco

    def set_endereco(self, endereco):
        self.endereco = endereco
    def set_preco(self, preco):
        self.preco = preco

        