#Importación de librería que nos va a permitir la extracción de datos de la API
import requests as req

#Función que obtiene valores de la API
def getOneUser(id):
    # VARIABLE QUE ALMACENA EL ENLACE DE LA API
    url = "https://jsonplaceholder.typicode.com/users/"
    #VARIABLE QUE EXTRAE LOS VALORES DE API O USUARIOS
    response = req.get(url)
    #VARIABLE PARA ACCEDER A LOS VALORES DE ACUERDO AL ID
    valor= response.json()[id]
    #VARIABLE PARA ACCEDER A LOS NOMBRES DEL DICCIONARIO
    nombre = valor.get("name")
    return nombre



    




 

