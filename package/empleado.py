from .persona import Persona
from .usuario import Usuario

class Empleado(Persona, Usuario):
    
    def __init__(self, nombre, apellido, fecha_nacimiento, dni, direccion, email, clave, activo, salario, horario, departamento):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.salario = salario
        self.horario = horario
        self.departamento = departamento

    def __str__(self):
        return f'Empleado: {self.nombre} {self.apellido}\n\tDepartamento: {self.departamento}\n\tSalario: {self.salario}\n'