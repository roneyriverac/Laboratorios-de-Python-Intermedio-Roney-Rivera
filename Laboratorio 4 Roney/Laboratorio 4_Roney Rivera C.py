#LABORATORIO 4 RONEY RIVERA C MANEJO DE DATOS BASICO

#IMPORTACIÓN DE LIBRERÍAS PANDAS, MATPLOTLIB, Y NUMPY
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#CARGA DEL ARCHIVO VENTAS EN UN DATAFRAME DE PANDAS
ventas = pd.read_csv('ventas.csv')
#CALCULO DEL BENEFICIO MENSUAL Y AGREGACIÓN DE NUEVA COLUMNA CON RESULTADOS
ventas['Ganancia'] = ventas['Ventas'] - ventas['Gastos']

#VARIABLES QUE ALMACENAN DATOS DE COLUMNAS
mes = ventas['Mes']
ganancias = ventas['Ganancia']
ventas2 = ventas['Ventas']
gastos = ventas['Gastos']

#MOSTRAR DATOS DE DATAFRAME
print(ventas)

#VARIABLE QUE MIDE LA LONGITUD DE MES
n = len(ventas.Mes)
x = np.arange(n)

#MUESTRA DATOS DE VENTAS EN EJE Y
plt.plot(x , ventas.Ventas,  label='Ventas')
#MUESTRA DATOS DE GASTOS EN EJE Y
plt.plot(x, ventas.Gastos,  label='Gastos')

#fig, ax = plt.subplots()
#AGREGA PUNTOS A GRAFICO
plt.plot(ventas.Ventas,  "--")
plt.plot(ventas.Gastos,  "--")
plt.plot(ventas.Ventas, "o", markersize=10)
plt.plot(ventas.Gastos, "o", markersize=10)
#AGREGAR LEYENDA Y ETIQUETAS AL GRAFICO
plt.xticks(x, ventas.Mes)
plt.legend(loc='best')
plt.xlabel("Meses")
#TITULO DEL GRÁFICO
plt.ylabel("evolución Mensual de las Ventas y los Gastos")
#MUESTRA EL GRÁFICO
plt.show()



