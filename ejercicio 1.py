from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        return self.salario_por_hora * self.horas_trabajadas


empleado1 = EmpleadoTiempoCompleto("Juan", 10, 40)
print(f"Salario de {empleado1.nombre}: {empleado1.calcular_salario()}")
