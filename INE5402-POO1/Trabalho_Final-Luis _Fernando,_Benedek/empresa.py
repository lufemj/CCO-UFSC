from cliente import Cliente

class Empresa(Cliente):
    def __init__ (self, nome, tipo, cnpj, tel, endereco):
        super().__init__(nome, tipo)
        self.cnpj = cnpj
        self.tel = tel
        self.endereco = endereco
    
    def get_cnpj(self):
        return self.cnpj
    def get_tel(self):
        return self.tel
    def get_endereco(self):
        return self.endereco

    def set_cnpj (self, cnpj):
        self.cnpj = cnpj
    def set_tel (self, tel):
        self.tel = tel
    def set_endereco (self, endereco):
        self.edereco = endereco


    def calcular_locacao(self, km_rodado, dias_alugados, diaria_atual):
        precodias = (diaria_atual*dias_alugados)
        vexcesso = 0
        if km_rodado > (dias_alugados*200):
            print("Quilometragem diária excedida")
            print()
            excesso = km_rodado - (dias_alugados*200)
            vexcesso = excesso * 1.50
            print("Taxa de excesso: R$1,50 por Km excedido!")
            print(f"Valor do excesso a ser cobrado: {vexcesso} ")
        valortotal = precodias + vexcesso
        locacao = (precodias + vexcesso)*0.85

        print()
        print(f"Desconto para empresas: -15% de {valortotal}")
        print()

        return locacao