from historico import Historico

class Automovel():
    def __init__ (self, placa, marca, tipo, preco, quilometragem):
        self.placa = placa
        self.marca = marca
        self.tipo = tipo
        self.preco = preco
        self.quilometragem = quilometragem
        self.historico = Historico()

    def get_placa(self):
        return self.placa
    def get_marca(self):
        return self.marca
    def get_tipo(self):
        return self.tipo
    def get_preco(self):
        return self.preco
    def get_quilometragem(self):
        return self.quilometragem
    

    def set_placa(self, placa):
        self.placa = placa
    def set_marca (self, marca):
        self.marca = marca
    def set_tipo (self, tipo):
        self.tipo = tipo
    def set_preco (self, preco):
        self.preco = preco
    def set_quilometragem (self, quilometragem):
        self.quilometragem = quilometragem


    def km_rodado(self, quilometragem_nova):
        km_rodado = quilometragem_nova - self.get_quilometragem()
        return km_rodado

    def registrar_historico (self, cliente_devolveu, dias_alugados, km_rodados, tipo_cliente):
        nome = cliente_devolveu
        dias = dias_alugados
        km = km_rodados
        tipo = tipo_cliente

        dados = [nome, dias, km, tipo]
        self.historico.alugueis.append(dados)
