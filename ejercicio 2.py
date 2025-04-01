from abc import ABC, abstractmethod

class Estudiante(ABC):
    def _init_(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas  

    @abstractmethod
    def calcular_promedio(self):
        pass

class EstudianteRegular(Estudiante):
    def calcular_promedio(self):
        return round(sum(self.notas) / len(self.notas), 1)  

estudiante1 = EstudianteRegular("Juan", [4.0, 4.5, 5.0])
print(f"Promedio de {estudiante1.nombre}: {estudiante1.calcular_promedio()}")
