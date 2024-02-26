class Marca:
    def __init__(self, _nombre:str):

        self._nombre = _nombre


    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre:str):
        self._nombre = nombre
    