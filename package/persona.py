class Persona(object):
    
    def __init__(self, nombre, apellido, fecha_nacimiento, dni, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
        self.direccion = direccion

    def getNombreCompleto(self):
        return f'{self.nombre} {self.apellido}'

    def getDia(self):
        return self.fecha_nacimiento[0:2]

    def getMes(self):
        return self.fecha_nacimiento[3:5]

    def getAño(self):
        return self.fecha_nacimiento[6::]

    def setDia(self, nuevo_dia):
        fecha_list = self.fecha_nacimiento.split('-')
        fecha_list[0] = str(nuevo_dia)
        self.fecha_nacimiento = f'{fecha_list[0]}-{fecha_list[1]}-{fecha_list[2]}'
        return self.fecha_nacimiento

    def setMes(self, nuevo_mes):
        fecha_list = self.fecha_nacimiento.split('-')
        fecha_list[1] = str(nuevo_mes)
        self.fecha_nacimiento = f'{fecha_list[0]}-{fecha_list[1]}-{fecha_list[2]}'
        return self.fecha_nacimiento

    def setAño(self, nuevo_año):
        fecha_list = self.fecha_nacimiento.split('-')
        fecha_list[2] = str(nuevo_año)
        self.fecha_nacimiento = f'{fecha_list[0]}-{fecha_list[1]}-{fecha_list[2]}'
        return self.fecha_nacimiento

# biagio = Persona('Biagio', 'Daponte', '30-09-1999', 'Y8279557P', 'Gral Díaz Porlier 24')

# print(biagio.getNombreCompleto())
# print(biagio.getDia())
# print(biagio.getMes())
# print(biagio.getAño())
