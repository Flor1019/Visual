
#El programa permite a una escuela de música gestionar su inventario de instrumentos musicales. Los usuarios pueden agregar nuevos instrumentos al inventario, ver la información de todos los instrumentos y calcular el precio de alquiler de cada instrumento. Esto facilita la organización 
# y el seguimiento de los instrumentos disponibles en la escuela.

# Definición de la clase InstrumentoMusical
class InstrumentoMusical:
    # Método constructor para inicializar los atributos del instrumento
    def __init__(self, nombre, precio_compra, caracteristicas):
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.caracteristicas = caracteristicas

    # Método para calcular el precio de alquiler basado en el precio de compra
    def obtener_precio_alquiler(self):
        return round(self.precio_compra * 0.05, 2)

    # Método para mostrar la información del instrumento
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Precio de Alquiler: {self.obtener_precio_alquiler()}, Características: {', '.join(self.caracteristicas)}"

# Función para agregar un nuevo instrumento al inventario
def agregar_instrumento():
    # Solicita al usuario ingresar el nombre del instrumento
    nombre = input("Ingrese el nombre del instrumento: ")
    # Solicita al usuario ingresar el precio de compra del instrumento
    precio_compra = float(input("Ingrese el precio de compra: "))
    # Solicita al usuario ingresar las características del instrumento, separadas por comas
    caracteristicas = input("Ingrese las características (separadas por comas): ").split(", ")
    # Crea una instancia de InstrumentoMusical con los datos ingresados y la retorna
    return InstrumentoMusical(nombre, precio_compra, caracteristicas)

# Función para mostrar la información de todos los instrumentos en el inventario
def mostrar_inventario(inventario):
    # Recorre cada instrumento en el inventario y muestra su información
    for instrumento in inventario:
        print(instrumento.mostrar_informacion())

# Lista para almacenar los instrumentos en el inventario
inventario = []

# Bucle principal del programa
while True:
    # Muestra el menú de opciones al usuario
    print("\n1. Agregar instrumento")
    print("2. Mostrar inventario")
    print("3. Salir")
    # Solicita al usuario seleccionar una opción del menú
    opcion = input("Seleccione una opción: ")

    # Si el usuario selecciona la opción 1, agrega un nuevo instrumento al inventario
    if opcion == "1":
        inventario.append(agregar_instrumento())
    # Si el usuario selecciona la opción 2, muestra el inventario
    elif opcion == "2":
        mostrar_inventario(inventario)
    # Si el usuario selecciona la opción 3, sale del programa
    elif opcion == "3":
        break
    # Si el usuario ingresa una opción no válida, muestra un mensaje de error
    else:
        print("Opción no válida. Intente de nuevo.")
