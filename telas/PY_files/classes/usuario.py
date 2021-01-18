__author__ = "Lucas Vinicius, Rubenilson de Sousa, Leonardo Cristian"
__licence__= "GPL"
__email__= "vinicius.lucas@ufpi.edu.br"
__version__= "1.0.0.1"

'''
    A Classe Usuario cria um objeto do tipo Usuario
'''

class Usuario():

    __slots__ = ['_id','_usuario','_tipo']

    def __init__(self,ID,pessoa,tipo):
        self._id = ID
        self._usuario = pessoa
        self._tipo = tipo
        '''
           Atributos
           ____
           _id: variavel do tipo Inteiro
           _usuario: objeto do tipo Pessoa
           _tipo: variavel do tipo String
        ''' 

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, ID):
        self._id = ID
    
    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    
    
    
