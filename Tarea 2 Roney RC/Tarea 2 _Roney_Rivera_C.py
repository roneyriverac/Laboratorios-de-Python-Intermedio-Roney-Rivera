#Tarea 2 Roney Rivera C

#IMPORTACIÓN DE LIBRERÍAS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests as req
global new_val

#FUNCIÓN QUE MUESTRA EL MENU
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

#FUNCION QUE DETERMINA SI LA OPCION INGRESADA ES CORRECTA
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

#FUNCIÓN QUE EJECUTA LAS OPCIONES
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

#FUNCIÓN QUE EJECUTA MENU HASTA USUARIO DECIDA
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

#FUNCIÓN QUE MUESTRA LAS OPCIONES DEL MENU AL USUARIO
def menu_principal():
    opciones = {
        '1': ('Opción 1: Lista de Ligas', accion1),
        '2': ('Opción 2: Lista de temporadas en una liga', accion2),
        '3': ('Opción 3: Datos de jugadores por ID', accion3),
        '4': ('Opción 4: Tabla por Liga y Temporada', accion4),
        '5': ('Opción 5: Gráfico 1', accion5),
        '6': ('Opción 6: Gráfico 2', accion6),
        '7': ('Opción 7: Gráfico 3', accion7),
        '8': ('Salir', salir)
    }

    generar_menu(opciones, '8')

#FUNCIÓN QUE EJECUTA AL ACCIÓN PRIMERA DEL MENU
def accion1():
    #FUNCIÓN QUE CONSUME API LA PROCESA, EXTRAE LISTAS MEDIANTE CICLOS FOR. Y CONVIERTE LISTA DE DATAFRAME
    def Lista_de_Ligas():
        
        urlGet1 = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"
        getResponse1 = req.get(urlGet1)
        if getResponse1.status_code == 200:
            data1 = getResponse1.json()
            df = pd.DataFrame(data1)
            idligue = df['leagues']
            strLeague = df['leagues']
            strSport = df['leagues']
            strLeagueAlternate = df['leagues']
            
            idLeague_lista =[]
            strLeague_lista =[]
            strSport_lista =[]
            strLeagueAlternate_lista =[]
            
            for x in idligue:
                idLeague_lista.append(x['idLeague'])
            #print(idLeague_lista)
            for x in strLeague:
                strLeague_lista.append(x['strLeague'])
            #print(strLeague_lista)
            for x in strSport:
                strSport_lista.append(x['strSport'])
                
            #print(strSport_lista)
            for x in strLeagueAlternate:
                strLeagueAlternate_lista.append(x['strLeagueAlternate'])
            #print(strLeagueAlternate_lista)

            data = {
                "Idliga": idLeague_lista,
                "Liga": strLeague_lista,
                "Deporte": strSport_lista,
                "LigaAlterna": strLeagueAlternate_lista,
            }
            global dff
            dff = pd.DataFrame(data)
            
            new_val = dff.head(10)
            print(new_val)
            
                
            
            
            #print("Respuesta del servidor:")
            #print(df)
            #print(idligue)
        
            
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
            df2 = pd.DataFrame(data2)

            strSeason = df2['seasons']
            
            
            strSeason_lista =[]
            
            
            for x in strSeason:
                strSeason_lista.append(x['strSeason'])
            print(strSeason_lista)
            

            data22 = {
                "Temporada": strSeason_lista
                
            }
            dff2 = pd.DataFrame(data22)
            new_val2 = dff2.head(10)
            print(new_val2)
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
            df3 = pd.DataFrame(data3)
            print("Respuesta del servidor:")
            print(df3)
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
            df4 = pd.DataFrame(data4)

            
            tabla = df4['table']
            
            
            idStanding_lista =[]
            intRank_lista =[]
            idTeam_lista =[]
            strTeam_lista =[]
            strTeamBadge_lista =[]
            idLeague_lista =[]
            strSeason_lista =[]
            strForm_lista =[]
            strDescription_lista =[]
            intPlayed_lista =[]
            intWin_lista =[]
            intLoss_lista =[]
            intDraw_lista =[]
            intGoalsFor_lista =[]
            intGoalsAgainst_lista =[]
            intGoalDifference_lista =[]
            intPoints_lista =[]
            dateUpdated_lista =[]

            
            
            

            
            
            for x in tabla:
                idStanding_lista.append(x['idStanding'])
            #print(idStanding_lista)
            for x in tabla:
                intRank_lista.append(x['intRank'])
            #print(intRank_lista)
            for x in tabla:
                idTeam_lista.append(x['idTeam'])
            #print(idTeam_lista)
            for x in tabla:
                strTeam_lista.append(x['strTeam'])
            #print(strTeam_lista)

            for x in tabla:
                strTeamBadge_lista.append(x['strTeamBadge'])
            #print(strTeamBadge_lista)
            for x in tabla:
                idLeague_lista.append(x['idLeague'])
            #print(idLeague_lista)
            for x in tabla:
                strSeason_lista.append(x['strSeason'])
            #print(strSeason_lista)
            for x in tabla:
                strForm_lista.append(x['strForm'])
            #print(strForm_lista)

            for x in tabla:
                strDescription_lista.append(x['strDescription'])
            #print(strDescription_lista)
            for x in tabla:
                intPlayed_lista.append(x['intPlayed'])
            #print(intPlayed_lista)
            for x in tabla:
                intWin_lista.append(x['intWin'])
            #print(intWin_lista)
            for x in tabla:
                intLoss_lista.append(x['intLoss'])
            #print(intLoss_lista)

            for x in tabla:
                intDraw_lista.append(x['intDraw'])
            #print(intDraw_lista)
            for x in tabla:
                intGoalsFor_lista.append(x['intGoalsFor'])
            #print(intGoalsFor_lista)
            for x in tabla:
                intGoalsAgainst_lista.append(x['intGoalsAgainst'])
            #print(intGoalsAgainst_lista)
            for x in tabla:
                intGoalDifference_lista.append(x['intGoalDifference'])
            #print(intGoalDifference_lista)

            for x in tabla:
                intPoints_lista.append(x['intPoints'])
            #print(intPoints_lista)
            for x in tabla:
                dateUpdated_lista.append(x['dateUpdated'])
            #print(dateUpdated_lista)

            data5 = {
                "idStanding": idStanding_lista,
                "intRank": intRank_lista,
                "idTeam": idTeam_lista,
                "strTeam": strTeam_lista,
                "strTeamBadge": strTeamBadge_lista,
                "idLeague": idLeague_lista,
                "strSeason": strSeason_lista,
                "strForm": strForm_lista,
                "strDescription": strDescription_lista,
                "intPlayed": intPlayed_lista,
                "intWin": intWin_lista,
                "intLoss": intLoss_lista,
                "intDraw": intDraw_lista,
                "intGoalsFor": intGoalsFor_lista,
                "intGoalsAgainst": intGoalsAgainst_lista,
                "intGoalDifference": intGoalDifference_lista,
                "intPoints": intPoints_lista,
                "dateUpdated": dateUpdated_lista,
                
                
            }

            global dff5
            dff5 = pd.DataFrame(data5)

            pd.options.display.max_columns = 18
            print(dff5)
            new_val5 = dff5.head(10)
            print(new_val5)

            print(dff5.columns.values)
            type(dff5.columns.values)
            
            #print("Respuesta del servidor:")
            #print(df4)
            #print(data4)
            
        else:
            print("Error al realizar la solicitud.")
    if __name__ == "__main__":
        Tabla_por_liga_y_temporada()
#FUNCIÓN QUE FILTA VALORES POR DEPORTE Y MUESTRA RESULTADOS CON GRÁFICO DE PASTEL MEDIANTE PORCENTAJES
def accion5():
    
    #cont = (dff['Deporte'] == "Rugby").count()
    #freq = dff.groupby(['Deporte']).count()
    freq = dff['Deporte'].value_counts()
    print(freq)

    valores = freq.values
    deportes = freq.index
    plt.pie(valores, labels=deportes, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Porcentaje de deportes practicados en ligas")
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=5)
    plt.show()

    
#FUNCIÓN QUE FILTRA DATOS Y MUESTRA GRÁFICO DE BARRAS  
def accion6():
    print(dff5)
    goles_por_equipo = dff5.groupby("strTeam")["intWin"].sum()
    
   
    plt.bar(goles_por_equipo.index, goles_por_equipo.values)
    plt.xlabel("Equipo de futbol", fontsize=20)
    plt.ylabel("Cantidad de victorias", fontsize=20)
    plt.title("Cantidad de victorias por equipo")
    plt.xticks(fontsize=1)
    plt.yticks(fontsize=10)
    
    
    plt.show()

def accion7():
    print(dff5)
    Cantidad_de_puntos = dff5.groupby("strTeam")["intPoints"].sum()
    top = Cantidad_de_puntos.head(19)
    fig, ax = plt.subplots()
    top.inplace=True
    grafica = dict(sorted(top.items(), key=lambda x: x[0]))
    y = list(grafica.values())
    x = list(grafica.keys())
    plt.title("Cantidad de puntos por equipo")
    ax.barh(x,y)
    plt.show()


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()


