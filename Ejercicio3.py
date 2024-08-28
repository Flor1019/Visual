class Auto:
    def __init__(self, precio_compra, nacional, caracteristicas):
        self._precio_compra = precio_compra
        self._nacional = nacional
        self._caracteristicas = caracteristicas

    def obtener_precio_venta(self):
        return round(self._precio_compra * 1.4, 2)

    def mostrar_informacion(self):
        tipo = "Nacional" if self._nacional else "Importado"
        return f"Tipo: {tipo}, Precio de Venta: {self.obtener_precio_venta()}, Características: {', '.join(self._caracteristicas)}"

# Ejemplo de uso:
auto1 = Auto(precio_compra=20000, nacional=True, caracteristicas=["4 ruedas", "5 pasajeros", "Aire acondicionado", "GPS", "Bluetooth"])
auto2 = Auto(precio_compra=30000, nacional=False, caracteristicas=["4 ruedas", "5 pasajeros", "Asientos de cuero", "Sunroof", "Sistema de sonido premium"])

print(auto1.mostrar_informacion())
print(auto2.mostrar_informacion())
