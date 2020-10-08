# Resolucion del lab de segundo registro de SE
 
Explicacion de la asignacion para el laboratorio 2 sistemas expertos

1. GENERALIDADES:
● Inicio de Evaluación: 07/10/2020
● Entrega de laboratorio: 08/10/2020 a más tardar a las 23:55
● entrega parcial: 09/10/2020 a más tardar a las 23:55
2. ESCENARIO LABORATORIO:
Se solicita que codifique una solución que cumpla con las siguientes características:
1. Generar una estructura de datos que almacene 10 millones de puntos en una distribución
normal con una media de 500 y una escala de 30
2. Iterarla exclusivamente con estructuras de control
3. Calcular la sumatoria de los puntos que son menores a 500,000
4. Devolver el valor de la sumatoria y el tiempo en que la lógica de negocios del problema
tardo en ejecutarse
5. Subir la solución a su repositorio en una rama “desarrollo1”, el nombre del archivo debe ser
lab2_<carnet>.<extension>
6. Es importante que el último commit de esta rama no sea después de la fecha y hora de
entrega del laboratorio.
7. Suba al aula virtual un archivo ZIP que contenga: a) una captura de pantalla con la fecha y
hora del último commit, b) un TXT con la direccion de su repositorio.

## Explicacion del codigo

lo primero se importan las librerias de t numpy y time, time para hacer el calculo del tiempo y determinar el tiempo el que lleva ejecutar el codigo, y numpy para hacer una lista de datos ramdon con parametros de una media de 500, escala 30, y la cantidad de datos 10000000

inicio =time.time() #lo utilizo para poder alamacenar el tiempo de ejecucion 

data_menor=[] #en data_menor es una lista donde se estara alamacenando cada uno de los datos que sean menores a 500000.

for datos in random_data: #aqui se recorren los datos anteriormente creados con la funcion de numpy random.normal en la variable datos.

if (datos < 500000):#Este condicional esta evaluando cada uno de los datos, si estos datos son menores a 500000, son alamacenados en la variable data_menor, utilizando la funcion append.
	data_menor.append(datos)

print ('Sumatoria de datos menores a 500000: ',sum(data_menor))#Aqui se imprime el valor de la sumatoria de todo los datos menores a 500000, que se encuentran almacenados en la variable data_menor.

print ('Duracion: {} segundos'.format(time.time() - inicio))# esta linea se ocupa para hacer el calculo del tiempo de ejecucion, que lleva desde el inicio hasta el final.


