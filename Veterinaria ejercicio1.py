class perro :
    def __init__(self, nombre, edad, raza,peso):
        self .__Nombre=nombre
        self.__Edad=edad
        self.__Raza=raza
        self.__Peso=peso
        self.__Estado='No atendido'
        
        def obtener_estado(self):
            return self._estado
        
        def cambiar_estado(self,estado):
            if estado in  ['No atendido','Atendido']:
                self.__estado=estado
        
        def tamañoporpeso(self):
            if self.__peso<10:
                return 'Perro pequeño'
            else :
                return 'Perro grande'
            
            # Ejemplo de uso:
            perro1=perro('Loki', 3, 'Pastor aleman',8)
            print(perro1.tamañoporpeso())
            perro1.cambiar_estado('ATENDIDO')
            print(perro1.obtener_estado())  
            