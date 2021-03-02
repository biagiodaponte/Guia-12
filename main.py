# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from os import system
from package.empleado import Empleado
from package.departamento import Departamento
from package.gerencia import Gerencia

dict_departamentos = dict()

def pausa():
    input('Presione enter para continuar...') 

def opcion_1(dict_departamentos):
    print('opcion 1 - Departameno - Create')
    nombre = input('Ingrese Nombre del Departamento: ')
    telefono = input('Ingrese Telefono del Departamento: ')
    obj_dep = Departamento(nombre, telefono)
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

def opcion_3(dict_departamentos):
    print('opcion 3 - Departameno - Update')
    if len(dict_departamentos) == 0:
        print('No existen departamentos.')
    else:
        nombre_departamento = input('Ingrese nombre del departamento a Editar: ')
        if nombre_departamento  in dict_departamentos.keys():
            atributo = input('Ingrese el atributo a Editar: ')
            if atributo in ['nombre', 'telefono']:
                valor = input(f'Ingrese el nuevo valor para {atributo}: ')
                if atributo == 'nombre':
                    dep_eliminado = dict_departamentos.pop(nombre_departamento)
                    dict_departamentos[valor] = dep_eliminado
                    setattr(dict_departamentos[valor], atributo, valor)
                elif atributo == 'telefono':
                    setattr(dict_departamentos[nombre_departamento], atributo, valor)
                print(f'El {atributo} fue modificado correctamente.')
            else:
                print('El atributo no existe.')
        else:
            print('El departamento no existe.')
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

def opcion_7(dict_departamentos):
    print('opcion 7')
    emple_dni = input('Ingrese DNI de Empleado a Modificar: ')
    atributo = input('Ingrese atributo a modificar: ')
    if atributo == 'dni':
        print('El atributo DNI no se puede modificar.')
    else:
        valor = input(f'Ingrese nuevo valor para el atributo {atributo}: ')
    if atributo in ['nombre', 'apellido', 'fecha_de_nacimiento', 'direccion', 'usuario', 'clave', 'activo', 'salario', 'horario']:
        if atributo == 'salario':
            valor = float(valor)
        
        for depa in dict_departamentos.values():
            if emple_dni in depa.empleados.keys():
                setattr(depa.empleados[emple_dni], atributo, valor)
                print(f'Empleado modificado correctamente en el departamento {depa.nombre}')
    pausa()

def opcion_8(dict_departamentos):
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

    gerencia = Gerencia('Dentosmed')

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

        if   opcion == '1': opcion_1(gerencia.departamentos) #Departamento - Create
        elif opcion == '2': opcion_2(gerencia.departamentos) #Departamento - Read  
        elif opcion == '3': opcion_3(gerencia.departamentos) #Departamento - Update
        elif opcion == '4': opcion_4(gerencia.departamentos) #Departamento - Delete
        elif opcion == '5': opcion_5(gerencia.departamentos) #Empleado - Create
        elif opcion == '6': opcion_6(gerencia.departamentos) #Empleado - Read
        elif opcion == '7': opcion_7(gerencia.departamentos) #Empleado - Update
        elif opcion == '8': opcion_8(gerencia.departamentos) #Empleado - Delete
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()


main()
