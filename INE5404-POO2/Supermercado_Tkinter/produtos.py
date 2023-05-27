class Produtos():
    def __init__ (self, codigo, tipo, marca, preco, quantidade):
        self.codigo = codigo
        self.tipo = tipo
        self.marca = marca
        self.preco = preco
        self.quantidade = quantidade

    def get_codigo(self):
        return self.codigo
    def get_tipo(self):
        return self.tipo
    def get_marca(self):
        return self.marca
    def get_preco(self):
        return self.preco
    def get_quantidade(self):
        return self.quantidade

    def set_codigo(self, codigo):
        self.codigo = codigo
    def set_tipo(self, tipo):
        self.tipo = tipo
    def set_marca(self, marca):
        self.marca = marca
    def set_preco(self, preco):
        self.preco = preco
    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
        