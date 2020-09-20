#Creador Milton Mejia
#Calculadora utilizando Python y POO

from Calculos import calculos

print('Bienvenido a la Calculadora\n')

operacion = calculos()

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
            
    


while (True):
    opcion = menu()
    if (opcion ==0):
        break

    elif (opcion == 5):
        numero1 = int(input('Elige la base: '))
        numero2 = int(input('La base elevada a: '))  
        operacion.exponenciacion(numero1,numero2)
        
    
    elif (opcion ==7):
        numero1 = int(input('Elija el numero al que le quiera sacar raiz cuadrada: '))
        operacion.raiz(numero1)

    else: 
        numero1 = int(input('Escribe tu primer numero: '))
        numero2 = int(input('Escribe tu segundo numero: '))

        if(opcion == 1):
            operacion.suma(numero1,numero2)
            
        elif(opcion == 2):
             operacion.resta(numero1,numero2)

        elif(opcion == 3):
            operacion.multiplicacion(numero1,numero2)
        
        elif(opcion == 4):
            operacion.division(numero1,numero2)

        elif(opcion == 6):
            operacion.divison_entera(numero1,numero2)
        
        else: 
            print('opcion invalida')
