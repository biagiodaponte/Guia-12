from os import system
import csv
from package.empleado import Empleado
from package.departamento import Departamento
from package.gerencia import Gerencia

def main():

    gerencia = Gerencia('Dentosmed')

    path = 'C:/Users/biagi/Desktop/Master Python/GUIA12-REPO/Guia-12/'
    # Apertura del Archivo
    fichero = open(path + 'departamentos.csv', 'r', encoding='utf-8')

    # Transformación del archivo csv a lineas de listas
    lectura_departamentos = csv.reader(fichero)
    #% CREACION DE DEPARTAMENTOS
    for fila in lectura_departamentos:
        obj_departamento = Departamento(fila[0].upper(), fila[1])
        if not obj_departamento.nombre in gerencia.departamentos.keys():
            gerencia.departamentos[obj_departamento.nombre] = obj_departamento
    print(gerencia.departamentos)

    # Cierre del fichero (debe ser luego de la transormacion del archivo).
    fichero.close()

main()