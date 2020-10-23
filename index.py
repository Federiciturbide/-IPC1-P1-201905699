# Aca realizamos las importaciones
from flask import Flask,request
from flask_cors import CORS
import json
from GestionUsuarios import Gestor

# En esta parte creamos nuestra aplicacion 
app = Flask(__name__)

# Aca realizamos configuracion de cors
CORS(app)



#En este espacio puedo declarar alguna variable global
gestor = Gestor()


#Aca iniciamos con el manejo de nuestras rutas
@app.route('/')
def index():
    return 'Hola :)'
    

#Obtener todos los usuarios
@app.route('/obtenerusuarios')
def usuarios():
    return gestor.getusuarios()

#Insertar un usuario
@app.route('/insertar',methods=['POST'])
def insertar():
    dato=request.json
    if gestor.insertar(dato['nombre'],dato['apellido'],dato['username'],dato['password']):
        return '{\"data\":\"Se ha insertado correctamente\"}'
    else:
        return '{\"data\": \"Usuario ya existe\"}'

#Carga masiva
@app.route('/masiva',methods=['POST'])
def insertar2():
    dato=request.json
    for x in dato:
        gestor.insertar(x['nombre'],x['apellido'],x['username'],x['password'])
    return 'Se ha insertado correctamente'

#Ejemplo de misma ruta pero difente tipo  de metodo
@app.route('/masiva')
def insertarget():
    return 'ESTA ES MASIVA PERO CON GET'

#Obtener  usuario con username en especifico
@app.route('/obteneruser/<username>')
def obtenerid(username):
    return gestor.getusuario(username)

@app.route('/iniciarsesion',methods=['POST'])
def iniciarsesion():
    dato=request.json
    if dato['username'] =='admin' and dato['password'] == "admin":
        return "{\"data\":\"admin\"}"
    elif gestor.iniciarsesion(dato['username'],dato['password']):
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}"
    

if __name__ == "__main__":
    app.run(port="5001",host="0.0.0.0",debug=True)  