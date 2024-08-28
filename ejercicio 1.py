class Perro:
    def __init__(self, nombre, edad, raza, peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza
        self.__peso = peso
        self.__estado = "NO ATENDIDO"

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def obtener_raza(self):
        return self.__raza

    def obtener_peso(self):
        return self.__peso

    def obtener_estado(self):
        return self.__estado

    def cambiar_estado(self, estado):
        if estado in ['NO ATENDIDO', 'ATENDIDO']:
            self.__estado = estado

    def tamaño_por_peso(self):
        if self.__peso < 10:
            return 'Perro Pequeño'
        else:
            return 'Perro Grande'

# Uso
perro1 = Perro('Loki', 3, 'Pastor Aleman', 8)
print("Nombre=",perro1.obtener_nombre())  
print("Edad=",perro1.obtener_edad())    
print("Raza=",perro1.obtener_raza())   
print("Peso=",perro1.obtener_peso())   
print("Tamaño=",perro1.tamaño_por_peso()) 
perro1.cambiar_estado('ATENDIDO')
print("Estado=",perro1.obtener_estado())  

print("-----------------------------------")

perro2 = Perro('Cansancio', 1, 'Basenji', 19)
print("Nombre=",perro2.obtener_nombre())  
print("Edad=",perro2.obtener_edad())    
print("Raza=",perro2.obtener_raza())   
print("Peso=",perro2.obtener_peso())   
print("Tamaño=",perro2.tamaño_por_peso()) 
perro1.cambiar_estado('NO ATENDIDO')
print("Estado=",perro2.obtener_estado())  


