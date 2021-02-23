
#? UNIDAD 6
#? GUIA DE CLASES


#! NOTA: 
#* para todas las clases deberan manejar: 
#* un constructor : __init__ 
#* una funcion de impresion del objeto  : __str__ 

# 1.- Cree una clase Persona con los siguientes atributos: 
#     nombre:str 
#     apellido:str 
#     fecha de nacimiento:str -> 'dia-mes-año' 
#     dni:str
#     direccion:list

# 2.- Edite la clase Persona y agrege un metodo que permita concatenar 
#     el nombre completo (nombre y apellido):
#     def getNombreCompleto(self):
#         pass
    
# 3.- Edite la clase Persona y 3 metodos que permita adquirir(getter) el dia , el mes y el año
#     nota: el atributo fecha_nacimiento es un str ( String )
#     def getDia(self):
#         pass
#     def getMes(self):
#         pass
#     def getAño(self):
#         pass

# 4.- Edite la clase Persona y 3 metodos que permita editar(setter) el dia , el mes y el año
#     nota: el atributo fecha_nacimiento es un str ( String )
#     def setDia(self, dia):
#         pass
#     def setMes(self, mes):
#         pass
#     def setAño(self, año):
#         pass

# 5.- Cree una clase Usuario con los siguientes atributos:
#     email:str
#     clave:str
#     activo:bool

# 6.- Edite la clase Usuario y agregele un metodo:
#     def validacion(self, param_email, param_clave):
#         pass
#     la funcion validacion recibe 2 parametros externos -> param_email y param_clave  
#     y revisa si son iguales con los de la clase -> self.email y self.clave
#     tambien debera verificar si ese encuentra activo o no self.activo -> ( True o False )
#     y por ultimo devuelve True en caso de que sean iguales y False en caso de que no
    
    
# 6.- Cree una clase Departamento con los siguientes atributos:
#     nombre:str
#     telefono:str

# 7.- Cree una clase Empleado que herede de Persona y Usuario, adicionalmente posea el atributo:
#     salario:float
#     horario:str

# 8.- Edite la clase Departamento y agrege una lista de Empleados para poder manejar los empleados 
#     de cada Departamento

# 9.- Edite la clase Departamento y agregele metodos para el calculo de la media salarial 
#     del Departamento, tambien un metodo que imprima un reporte de los empledos y sus salarios,
#     ordenados de mayor a menor en funcion de sus salarios

# 10.- Cree 1 Departamento y 10 empleados ( datos inventados por usted ), luego agregele los empleados
#     al Departamento, y muestre los dos reportes de Departamento, calculo de media salarial del 
#     Departamento y el reporte de los empleados y sus salarios 

# 11.- Separe el archivo de las clases en un paquete como se reviso en el 'ejemplo5_clase' y 
#     luego cree un archivo main.py donde ubicara la 
#     pregunta 10 y todas las funcionalidadesde que no pertenezcan a ninguna clase
