#Laboratorio 3 hecho por Roney Rivera C
#Chistes de Chuck Norris
condición = "si";
import requests as req

while condición == "si":

    pregunta = int(input("Digite 1) Para ver chiste aleatorio, 2) lista de categorías de chistes, 3) Ver chiste con categoria especifica. ")); 
    if pregunta == 1:
        
        def Elegir_chiste_aleatorio():
            urlGet = "https://api.chucknorris.io/jokes/random"
            getResponse = req.get(urlGet)
            if getResponse.status_code == 200:
                data = getResponse.json()
                print("Respuesta del servidor:")
                print(data)
            else:
                print("Error al realizar la solicitud.")
            
    elif pregunta == 2:
        
        def Mostrar_categorias_chistes():
            urlGet2 = "https://api.chucknorris.io/jokes/categories"
            getResponse2 = req.get(urlGet2)
            if getResponse2.status_code == 200:
                data2 = getResponse2.json()
                print("Respuesta del servidor:")
                print(data2)
            else:
                print("Error al realizar la solicitud.")
    else:
        
        def Chiste_de_una_categoria_especifica():
            urlGet3 = "https://api.chucknorris.io/jokes/random?category={category}"
            getResponse3 = req.get(urlGet3)
            if getResponse3.status_code == 200:
                data3 = getResponse3.json()
                print("Respuesta del servidor:")
                print(data3)
            else:
                print("Error al realizar la solicitud.")
    condición = str(input("Quiere seguir viendo chistes, digite si/no: "));
    
    
    if __name__ == "__main__":
        Elegir_chiste_aleatorio()
        Mostrar_categorias_chistes()
        Chiste_de_una_categoria_especifica()
       
        
    
