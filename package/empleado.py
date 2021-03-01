from .persona import Persona
from .usuario import Usuario

class Empleado(Persona, Usuario):
    
    def __init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion, usuario, clave, activo, salario, horario):
        Persona.__init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion)
        Usuario.__init__(self, usuario, clave, activo)
        self.salario = salario
        self.horario = horario

    def __str__(self):
        return f'Empleado: {self.nombre} {self.apellido}\nSalario: {self.salario}'