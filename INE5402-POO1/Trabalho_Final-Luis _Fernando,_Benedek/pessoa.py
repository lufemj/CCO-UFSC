from cliente import Cliente

class Pessoa(Cliente):
    def __init__ (self, nome, tipo, cpf, tel, endereco):
        super().__init__(nome, tipo)
        self.cpf = cpf
        self.tel = tel
        self.endereco = endereco
    
    def get_cpf(self):
        return self.cpf
    def get_tel(self):
        return self.tel
    def get_endereco(self):
        return self.endereco

    def set_cpf (self, cpf):
        self.cpf = cpf
    def set_tel (self, tel):
        self.tel = tel
    def set_endereco (self, endereco):
        self.edereco = endereco

