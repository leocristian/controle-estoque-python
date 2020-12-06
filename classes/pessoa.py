class Pessoa():

    __slots__ = ['_nome','_cpf','_endereco','_telefone','_idade','_email']

    def __init__(self,nome,cpf,endereco,telefone,idade,email):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._idade = idade
        self._telefone = telefone
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
    
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade
    
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email