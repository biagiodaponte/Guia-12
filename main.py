# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from os import system
from package.empleado import Empleado
from package.departamento import Departamento


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

def opcion_2():
    print('opcion 2 - Departameno - Read')
    pausa()

def opcion_3():
    print('opcion 3 - Departameno - Update')
    pausa()

def opcion_4():
    print('opcion 4 - Departameno - Delete')
    pausa()

def opcion_5():
    print('opcion 5 - Empleado - Create')
    objeto_empleado = Empleado('Biagio', 'Daponte', '30-09-1999', 'Y8333427N', 'Gral Diaz Porlier 24', 'biagio', 'bvdm1999', True, 1500,'15:00-23:00')
    print(objeto_empleado)
    nombre_departamento = input('Agregue Departamento: ')
    pausa()

def opcion_6():
    print('opcion 6')
    pausa()

def opcion_7():
    print('opcion 7')
    pausa()

def opcion_8():
    print('opcion 8')
    pausa()



def main():

    lista_departamentos = list()
    dict_departamentos = dict()

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
        elif opcion == '2': opcion_2() #Departamento - Read  
        elif opcion == '3': opcion_3() #Departamento - Update
        elif opcion == '4': opcion_4() #Departamento - Delete
        elif opcion == '5': opcion_5(dict_empleados) #Empleado - Create
        elif opcion == '6': opcion_6() #Empleado - Read
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
