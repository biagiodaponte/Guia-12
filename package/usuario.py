class Usuario(object):

    def __init__(self, email, clave, activo:bool):
        self.email = email
        self.clave = clave
        self.activo = activo

    def validacion(self, param_email, param_clave):
        if self.activo == True:
            if param_email == self.email and param_clave == self.clave:
                return True
            else:
                return False
        else:
            return False

# biagio = Usuario('bdaponte@gmail.com', '12345', True)
# print(biagio.validacion('bdaponte@gmail.com', '12345'))