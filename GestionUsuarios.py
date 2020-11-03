from Usuarios import Usuarios

class Gestor:
    def __init__(self):
        self.usuarios=[]
    
    def insertar(self,nombre,apellido,username,password):
        newuser = Usuarios(nombre,apellido,username,password)
        if self.existeuser(username):
            return False
        else:
            self.usuarios.append(newuser)
            return True

    def existeuser(self,username):
        for x in self.usuarios:
            if x.username==username:
                return True
        return False

    def getusuarios(self):
        texto="[\n"
        for x in self.usuarios:
            texto+="{\"nombre\":\""+x.nombre+"\", \"apellido\": \""+x.apellido+"\", \"username\": \""+x.username+"\"}\n"
        texto+='\n]'
        return texto

    def getusuario(self,username):
        for x in self.usuarios:
            if x.username==username:
                return "{\"nombre\":\""+x.nombre+"\", \"apellido\": \""+x.apellido+"\", \"username\": \""+x.username+"\"}\n"
        return ""

    def iniciarsesion(self,username,password):
        for x in self.usuarios:
            if x.username==username and x.password==password:
                return True
        return False

