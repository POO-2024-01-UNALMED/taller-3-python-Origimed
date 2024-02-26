class TV:
    
    numTV = 0
    def __init__(self, marca, estado:bool):
        self.estado = estado
        self.marca = marca
        

    canal = 1
    volumen = 1
    precio = 500

    def getMarca(self):
        return self.marca
    
    def getCanal(self):
        return self.canal
    
    def getPrecio(self):
        return self.precio
    
    def getVolumen(self):
        return self.volumen
    
    def getControl(self):
        return self.control
    
    def getNumTV(self):
        return self.numTV
    
    def getEstado(self):
        return self.estado

##########################################################
    

    def setMarca(self, marca):
        self.marca = marca
    
    def setCanal(self, canal:int):
        if self.estado == True and canal > 1 and canal < 120:
            self.canal = canal
    
    def setPrecio(self, precio:int):
        self.precio = precio
    
    def setVolumen(self, volumen:int):
        if self.estado == True and volumen  > 0 and volumen < 7:
            self.volumen = volumen
    
    def setControl(self, control):
        self.control = control

    def setNumTV(self, num:int):
        self.numTV = num

###########################################
        
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado == True and self.canal  < 120:
            self.canal += 1

    def canalDown(self):
        if self.estado == True and self.canal  > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.estado == True and self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.estado == True and self.volumen > 0:
            self.volumen -= 1




        
    

    
    

        