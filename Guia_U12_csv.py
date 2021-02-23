
# Guia U12 ( U6-U12 ) - CONTINUACION

#? 1) EJERCICIO 
#? escriba y lea un archivo CSV 
#? con el formato siguiente:

import csv

path = 'C:/Users/biagi/Desktop/Master Python/EJERCICIOS'

    #* fichero.csv ( recuerde separado por comas ',' y sin espacios )
    #* nombre,apellido,fecha_de_nacimiento,dni,direccion,email,clave,activo,salario,horario
    #? Patricia,Herresanchez,15-09-71,223233444T,iglesia2,patricia@gmail.com,jfjfur123∑,True,40000,partido

# Parte II - LECTURA
fichero = open( path+'/empleados.csv', 'r', encoding='utf-8')
lectura = csv.reader(fichero) 
for fila in lectura:
    print(fila)
fichero.close()

    #* fichero.csv ( recuerde separado por comas ',' y sin espacios )
    #* nombre,apellido,fecha_de_nacimiento,dni,direccion,email,clave,activo,salario,horario
    #? ['Patricia', 'Herresanchez', '15-09-71', '223233444T', 'iglesia2', 'patricia@gmail.com', 'jfjfur123∑', 'True', '40000', 'partido']

#? 2) EJERCICIO
# agrege una clase al paquete que permita manejar una lista del departamento 
# llamada Gerencia y posea el nombre de la empresa

#? 3) EJERCICIO
# partiendo del ejercicio anterior, cree una carga de datos desde un fichero.csv
# que permita carga 3 departamentos que tengan al menos 4 empleados cada uno

#? 4) EJERCICIO
# Cree un menu que le permita manejar (CRUD) de la empresa: 
# a)los departamentos 
# b)los empleado
#* C - Create - Crear un Objeto
#* R - Read   - Consultar Exitencia 
#* U - Update - Editar Datos
#* D - Delete - Eliminar Objeto
# serian en total 8 opciones

#? 5) EJERCICIO
# partiendo del ejercicio 3, en la creacion de empleado,
# a) validar que cuando introduzca un correo sea un correo correcto con el 
# uso de expresiones regulares
# b) tambien debera validar que el salario es un numero y posteriormente convertirlo 
# c) validar que cuando introduzca una fecha pueda convertirla en un Datetime
# NOTA: si considera manejar algun error manejelo con el uso de 
# try try:
#     pass
# except expression as identifier:
#     pass


#? 6) EJERCICIO
# para cada departamento se manejara un supervisor de empleados,
# recuerde que un supervidor tambien es un empleado que pertenece al departamento
# ayuda
# empleado -> empleado.supervidor siempre sera diferente de None ( Nulo )
# supervisor -> empleado.supervisor siempre sera None (Nulo)


#? 8) EJERCICIO
# partiendo del ejercicio anterior, maneje los errores de existencia de fichero
# y si existe, validar que si esta vacio para manejar los posibles errores



