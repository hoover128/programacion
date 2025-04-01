from abc import ABC, abstractmethod

class MenuBase(ABC):
    @abstractmethod
    def mostrar_opciones(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass

class Menu(MenuBase):
    def mostrar_opciones(self):
        print("1. Saludar")
        print("2. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_opciones()
            opcion = input("Elige una opción: ")
            if opcion == "1":
                print("¡Hola!")
            elif opcion == "2":
                print("Saliendo...")
                break
            else:
                print("Opción no válida")

 
menu = Menu()
menu.ejecutar()