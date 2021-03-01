# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from os import system
from package.empleado import Empleado
from package.departamento import Departamento

dict_departamentos = dict()

def pausa():
    input('Presione enter para continuar...') 

def opcion_1(dict_departamentos):
    print('opcion 1 - Departameno - Create')
    obj_dep = Departamento('RRHH', '633522411')
    print(obj_dep)
    # DICCIONARIO
    if not obj_dep.nombre in dict_departamentos.keys():
        dict_departamentos[obj_dep.nombre] = obj_dep
    else:
        print('Departamento ya Existe')
    pausa()

def opcion_2(dict_departamentos):
    print('opcion 2 - Departameno - Read')
    for dep in dict_departamentos.values():
        print(dep)
        for emple in dep.empleados.values():
            print(emple)
    pausa()

def opcion_3():
    print('opcion 3 - Departameno - Update')
    pausa()

def opcion_4(dict_departamentos):
    print('opcion 4 - Departameno - Delete')
    nombre_departamento = input('Ingrese nombre del Departamento a ELIMINAR: ')
    if nombre_departamento in dict_departamentos.keys():
        dict_departamentos.pop(nombre_departamento)
        print(f'Departamento {nombre_departamento} eliminado correctamente.')
    else:
        print('Departamento no Existe.')
    pausa()

def opcion_5(dict_departamentos):
    print('opcion 5 - Empleado - Create')
    objeto_empleado = Empleado('Biagio', 'Daponte', '30-09-1999', 'Y8333427N', 'Gral Diaz Porlier 24', 'biagio', 'bvdm1999', True, 1500,'15:00-23:00')
    print(objeto_empleado)
    nombre_departamento = input('Agregue Departamento: ')
    if nombre_departamento in dict_departamentos.keys():
        if not objeto_empleado.dni in dict_departamentos[nombre_departamento].empleados.keys():
            dict_departamentos[nombre_departamento].empleados[objeto_empleado.dni] = objeto_empleado
            print(f'Empleado agregado correctamente al departamento {dict_departamentos[nombre_departamento].nombre}')
        else:
            print('Empleado ya existe en el Departamento')
    else:
        print('Empleado no Agregado. No existe el Departamento')
    pausa()

def opcion_6(dict_departamentos):
    print('opcion 6')
    # nombre_departamento = input('Agregue el Departamento del Empleado: ')
    # if nombre_departamento in dict_departamentos.keys():
    #     dni_empleado = input('Ingrese el DNI del Empleado: ')
    #     if dni_empleado in dict_departamentos[nombre_departamento].empleados.keys():
    #         print(dict_departamentos[nombre_departamento].empleados[dni_empleado])
    #     else:
    #         print('El empleado no existe en el Departamento')
    # else:
    #     print('El departamento no Existe')
    
    dni_empleado = input('Ingrese el DNI del Empleado: ')
    for depa in dict_departamentos.values():
        if dni_empleado in depa.empleados.keys():
            print(f'{depa.nombre}: {depa.empleados[dni_empleado]}')
        else:
            print('El empleado no existe en la empresa.')

    pausa()

def opcion_7():
    print('opcion 7')
    pausa()

def opcion_8():
    print('opcion 8')
    dni_empleado = input('Ingrese el DNI del Empleado a ELIMINAR: ')
    for depa in dict_departamentos.values():
        if dni_empleado in depa.empleados.keys():
            emple_eliminado = depa.empleados.pop(dni_empleado)
            print(f'Empleado {emple_eliminado.nombre} eliminado del departamento {depa.nombre}')
        else:
            print('El empleado no existe en la empresa.')
    pausa()



def main():

    salida = True
    while salida == True:
        system('clear') # system('cls') 

        print('--- TITULO MENU ---')
        print('1. opcion - Departamento - Create ')
        print('2. opcion - Departamento - Read ')
        print('3. opcion - Departamento - Update ')
        print('4. opcion - Departamento - Delete ')
        print('5. opcion - Empleado - Create')
        print('6. opcion - Empleado - Read')
        print('7. opcion - Empleado - Update')
        print('8. opcion - Empleado - Delete')

        opcion = input('selecione una:')

        if   opcion == '1': opcion_1(dict_departamentos) #Departamento - Create
        elif opcion == '2': opcion_2(dict_departamentos) #Departamento - Read  
        elif opcion == '3': opcion_3() #Departamento - Update
        elif opcion == '4': opcion_4(dict_departamentos) #Departamento - Delete
        elif opcion == '5': opcion_5(dict_departamentos) #Empleado - Create
        elif opcion == '6': opcion_6(dict_departamentos) #Empleado - Read
        elif opcion == '7': opcion_7() #Empleado - Update
        elif opcion == '8': opcion_8() #Empleado - Delete
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()


main()
