#IMPORTACIÓN DE LIBRERÍAS PARA PODER USAR CONCURRENCIA. IMPORTACIÓN DE TIME PARA MEDIR EL TIEMPO
#IMPORTACIÓN DE FUNCIÓN Y LISTA DE OTROS ARCHIVOS
import time
import requests
import requests as req
import api
import aiohttp
from ids import ids
import aiohttp
import asyncio
import concurrent.futures
import multiprocessing

#lISTA DE LOS IDs
lista = ids


########################################################################################

#NORMAL

#Variable que cuenta el tiempo del proceso. El inicio del proceso
inicio = time.time()


#Cuenta la duración del proceso
time.sleep(1)
#vARIABLE DE ITERADOR DEL CICLO QUE RECORRE CADA VALOR DE LA LISTA PARA DARLE UN VALOR A LA FUNCIÓN PARA QUE MUESTRE USUARIO.
num = 0

#CICLO FOR QUE RECORRE TODOS LOS VALORES DE LA LISTA PARA DARLE EL PARAMETRO A LA FUNCIÓN PARA QUE MUESTRE USUARIOS
for num in lista:
    api.getOneUser(num)
    res = api.getOneUser(num)
    print("El nombre del usuario es= ", res, "\n" )
#REGISTRA EL TIEMPO EN EL QUE CONCLUYE EL PROCESO.
fin = time.time()

print("Este el tiempo que dura la operación sin concurrencia: ", fin-inicio, "\n")

############################################################################################

# 1) ASYNCIO
#FUNCIÓN PARA USAR CONCURRENCIA ASYNCIO
async def mostrar(num):
    async with aiohttp.ClientSession() as session:
        for num in lista:
            api.getOneUser(num)
            res = api.getOneUser(num)
            #print("El nombre del usuario es= ", res, "\n" )
#VARIABLES QUE REGISTRAN EL TIEMPO DEL PROCESO.           
start_time = time.time()
asyncio.get_event_loop().run_until_complete(mostrar(num))
duration = time.time() - start_time
print("Este es tiempo que dura con asyncio  " , duration, "\n")


##########################################################################################

# 2) REQUEST

#FUNCIÓN PARA USAR CONCURRENCIA REQUEST

def mostrar(num):
    with requests.Session() as session:
        for num in lista:
            api.getOneUser(num)
            res = api.getOneUser(num)
            #print("El nombre del usuario es= ", res, "\n" )
#VARIABLES QUE REGISTRAN EL TIEMPO DEL PROCESO.
start_time = time.time()
mostrar(num)
duration = time.time() - start_time
print("Este es tiempo que dura con request " , duration, "\n")


##############################################################################################

# 3) THREAD

#FUNCIÓN PARA USAR CONCURRENCIA THREAD

def mostrar(num):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for num in lista:
            api.getOneUser(num)
            res = api.getOneUser(num)
            #print("El nombre del usuario es= ", res, "\n" )

#VARIABLES QUE REGISTRAN EL TIEMPO DEL PROCESO.
start_time = time.time()
mostrar(num)
duration = time.time() - start_time
print("Este es tiempo que dura con thread " , duration, "\n")


###################################################################################

# 4) MULTIPROCESS

##FUNCIÓN PARA USAR CONCURRENCIA MULTIPROCESS
def mostrar(num):
    with multiprocessing.Pool() as pool:
        
        for num in lista:
            api.getOneUser(num)
            res = api.getOneUser(num)
            #print("El nombre del usuario es= ", res, "\n" )

#VARIABLES QUE REGISTRAN EL TIEMPO DEL PROCESO.
start_time = time.time()
mostrar(num)
duration = time.time() - start_time
print("Este es tiempo que dura con multiprocess " , duration, "\n")
    

print("De acuerdo a los resultados, Multiprocess es el más efectivo")
