from abc import ABC, abstractmethod

class Autenticable(ABC):
    @abstractmethod
    def autenticar(self, contraseña_introducida):
        pass

class Usuario(Autenticable):
    def _init_(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def autenticar(self, contraseña_introducida):
        return self.contraseña == contraseña_introducida


usuario1 = Usuario("Juan", "hola123")
print("Autenticación:", usuario1.autenticar("hola123"))  
print("Autenticación:", usuario1.autenticar("clave123"))    