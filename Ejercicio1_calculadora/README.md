# Calculadora en Python, Primer Ejercicio Sistemas Expertos, por Milton Mejia

## Primer paso, estar en el fichero  donde se encuentra la solucion

El archivo principal para utilizar la Calculadora es Menu_Principal.py
para ejecutarlo tienes que estar dentro de la ruta de ese fichero por Ej. 
C:\user\nombre_usuario\ficheros si se esta desde una distribucion de Windows
nombre_usuario@nombre_equipo:~/Ficheros$ si se esta desde una distribucion de Linux

## Segundo paso, Ejecutar el archivo principal [Menu_Principal.py]

C:\user\nombre_usuario\ficheros\python Menu_Principal.py para usuarios que esten utilizando Windows

nombre_usuario@nombre_equipo:~/Ficheros$python3 Menu_Principal.py 

## Tercer paso, Utilizar la Calculadora

Al ejecutar el Menu_Principal lo primero que aparecera desde la consula es un menu con diferentes opciones a elegir, 
para operar como suma, resta, multiplicacion, division, etc. y una opcion de terminar el programa, por que al iniciarlo
este va a estarse ejecutando una y otra vez hasta que el usurio decida dejar de realizar operaciones.

Con este codigo lo que se busca es poner en practica la programacion en python, tanto la estructurada como la orientada a objetos

## Explicacion codigo

ya como mencione anteriormente se encuentran 2 archivos que son los fundamentales para hacer  funcionar el proyecto de la calculadora Menu_Principal.py y Calculos.py. 

Dentro de Menu_Principal.py vamos a importar la clase calculos que es la que me permite hacer las distintas operaciones de suma, resta, multiplicacion, etc. de la siguiente manera
from Calculos import calculos # Calculos con C Mayuscula hace referencia al archivo mientras que calculos con c minuscula hace referencia a la clase de ese archivo.

luego de eso crearemos una variable que llame a la clase calculos,
operacion = calculos()

Lo siguiente es una funcion que he llamado menu, que tiene un print que muestra direntes opciones, lo importante es el return por que aqui se indica al usuario que escoja una opcion y este numero que indique lo retornara.
def menu():
    print("""Que operacion desea hacer:\n
        Opcion 1: Suma\n
        Opcion 2: Resta\n
        Opcion 3: Multiplicacion\n
        Opcion 4: Division\n
        Opcion 5: Exponenciacion\n
        Opcion 6: Division Entera\n
        Opcion 7: Raiz cuadrada\n
        Opcion 0: Salir
        """)
    return int(input('elige una opcion: '))

Lo siguiente viene siendo la logica, si la opcion que se escoja siempre entrara en ciclo While y si el usuario no escoje la opcion salir, hasta eso momento no podra salir del codigo, 
lo importante son las condicionales por ejemplo: si yo he escugido la operacion raiz, al usuario se le pedira que ingrese un valor al que desee sacarle la raiz, y luego se creara un objeto de tipo operacion que hara referencia al metodo raiz que se encuentra en el archivo Calculos.

while (True):
    opcion = menu()
    if (opcion ==0):
        break

elif (opcion ==7):
    numero1 = int(input('Elija el numero al que le quiera sacar raiz cuadrada: '))
   	operacion.raiz(numero1)

Como su archivo ya lo menciona con su nombre en Calculos es donde se realizan estos.
Dentro de este archivo se encuentra una clase llamada calculos y varios metodos como suma, resta, multplicacion, division, etc. 

solo que estaba vez en este achivo se importa una libreria que es math para poder utilizar un metodo para sacar la raiz cuadrada de un numero. 

Siguiendo con el ejemplo anterior: 
def raiz(self, numero1):
        print('La raiz cuadrada es:', math.sqrt(numero1))

Aqui se puede observar el metodo de raiz, que recibe dos parametros self y numero1, el self hace referencia a el objeto que se crea, y el numero al valor que sera enviado por ese objeto, por ultimo hay un print que imprime un mensaje y la operacion de sacar la raiz a un numero que esta enviando.

y asi con todas las demas operaciones, practicamente siguen la misma logica, usurio eligio un operacion, entra a buscar el numero al que se le ha asigando esa operacion, el usurio recibe un mensaje de ingresar numeros para realizar la operacion, se crea la instancia, que hace refencia al metodo, el metodo recibe esos datos y realiza la operacion he imprime por pantalla y se repite el ciclo hasta que usuario, escoja la opcion de salir en el menu, que es la que cierra el ciclo. 


## Conclusion
La calculadora en python es un ejercicio que nos introduce a este lenguaje multiparadigma que es de alto nivel, para comenzar a programar en este lenguaje considero que es importante hacer este tipo de ejercicio, sobre todo la parte de POO, por que es la supone un mayor desafio, por todo terminos, abstracciones, estructura, etc. considero que se puede mejorar, incluyendo validaciones, y talvez para ver la parte estetica un poco mejor, utilizar la libreria de python tinker para crear una interfaz grafica. 
