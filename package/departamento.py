class Departamento():

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.empleados = dict()

    def mediaSalarial(self):
        salario_depto = 0
        cantidad_empleados = 0
        for emple in self.lista_empleados:
            salario_depto += int(emple.salario)
            cantidad_empleados += 1
        return f'Media Salarial del Departamento {self.nombre} = €{int(salario_depto/cantidad_empleados)}'

    def reporteDepto(self):
        print('--- REPORTE DEPTO', self.nombre, '---')
        lista_empleados_ord = sorted(self.lista_empleados, key=lambda x: x.salario)
        for emple in lista_empleados_ord:
            print(emple)
        return ''

    def __str__(self):
        return f'Departamento {self.nombre} - Telefono: {self.telefono}'