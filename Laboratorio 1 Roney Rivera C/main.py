#IMPORTACIÓN DE LIBRERÍAS
import Trig
from datetime import datetime

#DEFINICÓN DE VARIABLES Y CREACIÓN DE ARCHIVO DE TEXTO
date = (datetime.now())
instancia = Trig.Trig()
archivo = open("log.txt","x")


#VARIABLE DE CONDICIONAL PARA INICIAR CICLO

Continuar = "si"

#CICLO WHILE QUE REPITE CODIGO HASTA QUE USUARIO DECIDA TERMINAR
while Continuar == "si":
    
    #VARIABLE QUE PREGUNTA CUAL OPCIÓN QUIERE VER
    pregunta = int(input("Tiene tres opciones para consultar, digite 1) Seno, 2) Coseno y 3) Tangente: "))

    #CONDICIONALES QUE MUESTRAN EL VALOR DEPENDIENDO LA OPCIÓN ELEGIDA
    if pregunta == 1:

        #VARIABLE QUE GUARDA RESULTADO
        res1 = instancia.seno()
    
        #ESCRITURA DE LA FECHA Y RESULTADO EN DOCUMENTO DE TEXTO
        text = f" La fecha es {date}. La operación es seno, el resultado es {res1} \n"
        archivo.write(text)
        
        print(res1)
        
        
        

    elif pregunta == 2:
        #VARIABLE QUE GUARDA RESULTADO
        res2 = instancia.coseno()

        #ESCRITURA DE LA FECHA Y RESULTADO EN DOCUMENTO DE TEXTO
        text2 = f" La fecha es {date}. La operación es coseno, el resultado es {res2} \n"
        archivo.write(text2)
        
        print(res2)
        

    elif pregunta == 3:
        #VARIABLE QUE GUARDA RESULTADO
        res3 = instancia.tangente()

        #ESCRITURA DE LA FECHA Y RESULTADO EN DOCUMENTO DE TEXTO
        text3 = f" La fecha es {date}. La operación es tangente, el resultado es {res3} \n"
        archivo.write(text3)
        
        print(res3)
        
    else:
        print("Por favor introduzca un número válido")

        #VARIABLE QUE PREGUNTA AL USUARIO SI DESEA CONTINUAR

    Continuar = str(input("Desea continuar, digite si / no : "))

archivo.close()
    
    
    

    
        

