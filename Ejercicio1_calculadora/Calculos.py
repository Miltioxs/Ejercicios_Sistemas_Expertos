import math

class calculos:
    
    def suma(self, numero1, numero2):
         print('La suma de',numero1, '+',numero2, 'es: ', numero1 + numero2)

    def resta(self, numero1, numero2):
         print('La resta de',numero1, '-',numero2, 'es: ', numero1 - numero2)
    
    def multiplicacion(self, numero1, numero2):
         print('La multiplicacion de',numero1, '*',numero2, 'es: ', numero1 * numero2)

    def division(self, numero1, numero2):
         print('La division de',numero1, '*',numero2, 'es: ', numero1 / numero2)

    def exponenciacion(self, numero1, numero2):
        print('La base es',numero1, 'elevado a la',numero2, 'es: ', numero1 ** numero2)

    def divison_entera(self, numero1, numero2):
        print('La division entera entre',numero1, 'y',numero2, 'es: ', numero1 // numero2)
        
    def raiz(self, numero1):
        print('La raiz cuadrada es:', math.sqrt(numero1))