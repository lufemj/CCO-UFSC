
class Historico():
    def __init__ (self):
        self.alugueis = []


    def listagem(self, alugado):
        if alugado == True:
            print()
            print("Este veículo está alugado no momento.")
            print()
        print('Histórico de alugueis do veiculo:')
        if len(self.alugueis) < 1:
            print("Este veículo nunca foi alugado anteriormente.")
            print()
        
        else:
            for i in range (len(self.alugueis)):
                print("...............")
                print("Locacação: ", i+1)
                print("Alugado por", self.alugueis[i][3])
                print("Nome:",self.alugueis[i][0])
                print("Dias alugados:", self.alugueis[i][1])
                print("Quilometros percorridos:",self.alugueis[i][2])
                print()

 