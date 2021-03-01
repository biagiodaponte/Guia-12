
from package.persona import Persona
from package.usuario import Usuario
from package.empleado import Empleado
from package.departamento import Departamento
from package.gerencia import Gerencia

import csv

path = 'C:/Users/biagi/Desktop/Master Python/EJERCICIOS'

csv_empleados = open( path+'/empleados.csv', 'r', encoding='utf-8')
csv_departamentos = open (path+'/departamentos.csv', 'r', encoding='utf-8')

empleados = dict()
departamentos = dict()
def cargaTodo():
    lectura_empleados = csv.reader(csv_empleados)
    def crearEmpleados():
        #% Creacion de Todos los Empleados
        for fila in lectura_empleados:
            empleados[fila[4]]= Empleado(fila[0], fila[1], fila[2], fila[4], fila[3], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10])
        #% FIN Creacion de Todos los Empleados
    crearEmpleados()

    
    def crearDepartamentos():
        #% CREACION DE TODOS LOS DEPARTAMENTOS CON SUS EMPLEADOS
        lectura_departamentos = csv.reader(csv_departamentos)
        for fila in lectura_departamentos:
            departamentos[fila[0]] = Departamento(fila[0], fila[1])
        for emple in empleados.values():
            departamentos[emple.departamento].lista_empleados.append(emple)
        #% FIN CREACION DE TODOS LOS DEPARTAMENTOS CON SUS EMPLEADOS
    crearDepartamentos()
    csv_empleados.close()
cargaTodo()

# #% IMPRESION DE TODOS LOS EMPLEADOS
def imprimeEmpleados():
    for emple in empleados.values():
        print(f'{emple}\n')
# imprimeEmpleados()

#! IMPRESION DE DETALLE DE EMPLEADOS POR DEPARTAMENTO
# print(departamentos['Soporte'])


opcion1 = 0
opcion2 = 0

print('Seleccione qué tipo desea trabajar...')
print('1.Empleados')
print('2.')















# def menu():
#     def menu1():
#         print(f'''Seleccione con qué opción desea Trabajar:
# a) Departamentos
# b) Empleados''')
#         global opcion1
#         opcion1 = input('Escriba Opción: ').lower()
#         while not (opcion1 == 'a' or opcion1 == 'b'):
#             opcion1 = input('Opción Incorrecta. Escriba Opción: ')
#         else:
#             pass

#         if opcion1 == 'a':
#             opcion1 = 'Departamentos'
#         else:
#             opcion1 = 'Empleados'
#     menu1()

#     #% MENÚ PARTE 2
#     def menu2():
#         print(f'''\nSeleccione una acción para manejar los {opcion1}:
# C) Crear un Objeto
# R) Consultar Existencia
# U) Editar Datos
# D) Eliminar Objeto''')
#         global opcion2
#         opcion2 = input('Escriba Opción: ').lower()
#         while not (opcion2 == 'c' or opcion2 == 'r' or opcion2 == 'u' or opcion2 == 'd'):
#             opcion2 = input('Opción Incorrecta. Escriba Opción: ')
#         else:
#             pass

#         #% CREAR OBJETO
#         if opcion2 == 'c':
#             if opcion1 == 'Departamentos':
#                 csv_empleados = open(path+'/departamentos.csv', 'r', encoding='utf-8')
#                 lectura_empleados = csv.reader(csv_empleados)
#                 departamentos_exist = list()
#                 for fila in lectura_empleados:
#                     departamentos_exist.append(fila[0])
#                 print(departamentos_exist)

#                 nuevo_departamento = input('Ingrese Nombre del nuevo Departamento: ')
#                 while nuevo_departamento in departamentos_exist:
#                     nuevo_departamento = input('Ingrese Nombre del nuevo Departamento: ')
#                 else:
#                     pass
#                 telefono = input('Ingrese Telefono del nuevo Departamento: ')
#                 with open(path+'/departamentos.csv', 'w') as dep_writer:
#                     writer = csv.writer(dep_writer)
#                     writer.writerow(nuevo_departamento, telefono)
#                 dep_writer.close()
#     menu2()
# menu()


# # # print(depto_1.mediaSalarial())

# # print(depto_1.mediaSalarial())
# # print(depto_1.reporteDepto())