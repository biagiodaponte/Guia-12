class Gerencia():
    
    def __init__(self, nombre_empresa, departamentos):
        self.nombre_empresa = nombre_empresa
        self.departamentos = dict()

    def getDepartamentos(self):
        for departamento in departamentos.keys():
            print(departamento)