class Funcionario():
    def __init__ (self, senha):
        self.senha = senha
        self.senhacorreta = "1234"


    def verificacao(self):
        if self.senha == self.senhacorreta:
            return True

        elif self.senha == "0000":
            return "sair"

        elif self.senha != self.senhacorreta: 
            return False

    