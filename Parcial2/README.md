# Resolucion del parcial segundo registro de SE

 ESCENARIO PARCIAL:
1. Codificar una solución que optimice la ejecución del planteamiento del laboratorio.
2. La solución debe optimizar el tiempo de ejecución al menos en un 300%.
3. subir la solución a una rama denominada “desarrollo2”, el nombre del archivo debe ser
parcial2_<carnet>.<extension>
4. Si la meta de optimización se cumple consolide en la rama master la nueva solución.
5. Documente el proceso de ejecución de laboratorio y parcial en un video tutorial no menos
de 5 minutos.
6. Suba al aula virtual una captura de pantalla con la fecha y hora del último commit.
7. En el README.md del repo publique el link de su video.

## explicacion del codigo

lo primero se importan las librerias de t numpy y time, time para hacer el calculo del tiempo y determinar el tiempo el que lleva ejecutar el codigo, y numpy para hacer una lista de datos ramdon con parametros de una media de 500, escala 30, y la cantidad de datos 10000000

inicio =time.time() #lo utilizo para poder alamacenar el tiempo de ejecucion

valores_menores = random_data[random_data <= 500000]#Aqui estamos creado la lista donde se almacenaran todos los datos que sean menores a 500000, utilizando una lista de tipo numpy.ndarray

Se realiza la sumatoria de los datos menores a 500000 y se imprimira
print ('Sumatoria de datos menores a 500000: ',sum(valores_menores))

Se imprime el tiempo de duracion que ha tardo el codigo en ejecutarse
print ('Duracion: {} segundos'.format(time.time() - inicio))