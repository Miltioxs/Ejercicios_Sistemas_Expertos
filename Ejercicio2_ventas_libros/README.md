# Otro enfoque para optimizar el codigo ventaslibros por Milton Mejia
#IDE utilizado JuppyterNoteBook

#archivos a utilizar libros_24_meses.txt y catalogo_libros.txt

## Primeros pasos
importar las librerias a utilizar: 
#import time
#import numpy as np

Regla de negocio: Basicamente dentro de libros_24_meses.txt se encuentra un listado de libros vendidos en un periodo de 24 meses, y dentro de catalogo_libros.txt se encuentra como su nombre lo describe un catalago de libros, entonces, lo que se realizara es un codigo que me devuelva la cantidad de libros vendidos durante todo ese periodo, para ello se tiene que consultar los dos archivos antes mencionados.

# Otro enfoque para optimizar el codigo,  mi propuesta es la siguiente: 

inicio = time.time() #Aqui se usa el modulo time para calcular el tiempo de ejecucion del codigo

libros_vendidos = list (set(historial_vendidos).intersection(set(catalogo_libros))) #basicamente este es mi algoritmo que me esta comparando los datos de ambos archivos y los que son iguales tanto  en libros_24_meses.txt y catalogo_libros.txt, los estamos alamacenando en la variable libros_vendidos, set(historial_vendidos) y (set(catalogo_libros), lo que hace es transformar mi lista de datos en conjuntos con la instruccion set para poder utilizar la funcion intersection que es la que me devolvera los libros vendidos en el perido de 24 meses, luego este consulta la estoy tranformando en una lista nuevamente.

print(len(libros_vendidos)) #Aqui con la instruccion len lo que estamos haciendo es nada mas que contar la longitud de elementos que hay dentro de nuestra lista libros_vendidos.

print('Duracion: {} segundos'.format(time.time() - inicio)) #Aqui solamente se realiza el calculo del tiempo total que llevo el codigo en ejecutarse. 
