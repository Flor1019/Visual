class ArticuloPapeleria:
    def __init__(self, precio_compra):
        self._precio_compra = precio_compra

    def obtener_precio_venta(self):
        return  self._precio_compra * 1.30

class Cuaderno(ArticuloPapeleria):
    def __init__(self, precio_compra, numero_hojas):
        super().__init__(precio_compra)
        self._numero_hojas = numero_hojas
        self._marca = "HOJITAS"

class Lapiz(ArticuloPapeleria):
    def __init__(self, precio_compra, color):
        super().__init__(precio_compra)
        self._color = color
        self._marca = "RAYAS"

# uso
cuaderno_50 = Cuaderno(precio_compra=0.70, numero_hojas=50)
cuaderno_100 = Cuaderno(precio_compra=0.80, numero_hojas=100)
lapiz_rojo = Lapiz(precio_compra=0.30, color="rojo")

print(f"Precio de venta del cuaderno de 50 hojas: {cuaderno_50.obtener_precio_venta()}")
print(f"Precio de venta del cuaderno de 100 hojas: {cuaderno_100.obtener_precio_venta()}")
print(f"Precio de venta del lápiz rojo: {lapiz_rojo.obtener_precio_venta()}")
