class Usuario():

    __slots__ = ['_id','_usuario','_tipo']

    def __init__(self,ID,pessoa,tipo):
        self._id = ID
        self._usuario = pessoa
        self._tipo = tipo

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

    
    
    
