#Tarea 1 Roney Rivera C

import requests as req

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1: Lista de Ligas', accion1),
        '2': ('Opción 2: Lista de temporadas en una liga', accion2),
        '3': ('Opción 3: Datos de jugadores por ID', accion3),
        '4': ('Opción 4: Tabla por Liga y Temporada', accion4),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def accion1():
    def Lista_de_Ligas():
        urlGet1 = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"
        getResponse1 = req.get(urlGet1)
        if getResponse1.status_code == 200:
            data1 = getResponse1.json()
            print("Respuesta del servidor:")
            print(data1)
        else:
            print("Error al realizar la solicitud.")
    if __name__ == "__main__":
        Lista_de_Ligas()


def accion2():
    def Lista_temporadas_en_una_liga():
  
        urlGet2 = "https://www.thesportsdb.com/api/v1/json/3/search_all_seasons.php?id=4328"
        getResponse2 = req.get(urlGet2)
        if getResponse2.status_code == 200:
            data2 = getResponse2.json()
            print("Respuesta del servidor:")
            print(data2)
        else:
            print("Error al realizar la solicitud.")
    if __name__ == "__main__":
        Lista_temporadas_en_una_liga()


def accion3():
    def Datos_de_jugadores_por_ID():
        urlGet3 = "https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php?id=34145937"
    
        getResponse3 = req.get(urlGet3)
        if getResponse3.status_code == 200:
            data3 = getResponse3.json()
            print("Respuesta del servidor:")
            print(data3)
        else:
            print("Error al realizar la solicitud.")
    if __name__ == "__main__":
        Datos_de_jugadores_por_ID()

def accion4():
    def Tabla_por_liga_y_temporada():
    
        urlGet4 = "https://www.thesportsdb.com/api/v1/json/3/lookuptable.php?l=4328&s=2020-2021"
        getResponse4 = req.get(urlGet4)
        if getResponse4.status_code == 200:
            data4 = getResponse4.json()
            print("Respuesta del servidor:")
            print(data4)
        else:
            print("Error al realizar la solicitud.")
    if __name__ == "__main__":
        Tabla_por_liga_y_temporada()




def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()


