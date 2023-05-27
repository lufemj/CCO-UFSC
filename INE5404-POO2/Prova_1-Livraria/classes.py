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


class Livro():
    def __init__ (self, codigo, nome, genero, paginas):
        self.codigo = codigo
        self.nome = nome
        self.genero = genero
        self.paginas = paginas

    def get_codigo(self):
        return self.codigo
    def get_nome(self):
        return self.nome
    def get_genero(self):
        return self.genero
    def get_paginas(self):
        return self.paginas


    def set_codigo(self, codigo):
        self.codigo = codigo
    def set_nome (self, nome):
        self.nome = nome
    def set_genero (self, genero):
        self.genero = genero
    def set_paginas (self, paginas):
        self.paginas = paginas

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

class Pessoa(Cliente):
    def __init__ (self, nome, tipo, cpf, celular, endereco):
        super().__init__(nome, tipo)
        self.cpf = cpf
        self.tel = celular
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


class Empresa(Cliente):
    def __init__ (self, nome, tipo, cnpj, telefone, endereco):
        super().__init__(nome, tipo)
        self.cnpj = cnpj
        self.tel = telefone
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
