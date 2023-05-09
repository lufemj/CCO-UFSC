class Cliente():
    def __init__ (self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def get_nome(self):
        return self.nome
    def get_tipo(self):
        return self.tipo

    def set_nome (self, nome):
        self.nome = nome
    def set_tipo (self, tipo):
        self.tipo = tipo

    
    
    def calcular_locacao(self, kmrodado, dias_alugados, diaria_atual):
        precodias = (diaria_atual*dias_alugados)
        valor_excesso = 0
        if kmrodado > (dias_alugados*200):
            print("Quilometragem diária excedida")
            print()
            excesso = kmrodado - (dias_alugados*200)
            valor_excesso = excesso* 1.50
            print("Taxa de excesso: R$1,50 por Km excedido!")
            print(f"Valor do excesso a ser cobrado: {valor_excesso} ")
        locacao = precodias + valor_excesso
       
        return locacao
