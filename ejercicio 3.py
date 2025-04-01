from abc import ABC, abstractmethod

class Factura(ABC):
    def _init_(self):
        self.productos = [] 

    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))  (nombre, precio)

    @abstractmethod
    def calcular_total(self):
        pass

class FacturaTienda(Factura):
    def calcular_total(self):
        return round(sum(precio for _, precio in self.productos), 2)


factura = FacturaTienda()
factura.agregar_producto("Pan", 2.50)
factura.agregar_producto("Leche", 5.75)
factura.agregar_producto("Huevos", 10.30)

print(f"Total de la compra: {factura.calcular_total()}")
