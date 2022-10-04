import os

from cgitb import reset
from email import message

def dvide(num1, num2):
    if num2 == 0:
       print("no  es posible dividir entre 0")
       num2 = 1

    return num1/ num2 

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2
def multi(num1, num2):
    return num1 * num2
def return_values():
    num1 = int(input("introduce un numero"))
    num2 = int(input("introduce otro numero"))
    return [num1,num2]     
  



if __name__=='__main__':
    message = message = f"Calculadora: \n Elige una opcion\n 1 - Suma\n 2 - Resta\n 3 - Multiplicacion\n 4 - Division\n5 - salir\n"
    
    while True:
        opcion = int(input(message))

        if  opcion == 1:

            numeros=return_values()
            
            resultado_suma = suma(numeros[0],numeros[1])
            print("El resultado de la suma es",resultado_suma)
        elif  opcion == 2:
            numeros=return_values()
            resultado_restsa = resta(numeros[0],numeros[1])
            print("El resultado de la resta es",resultado_restsa)
        elif  opcion == 3:
            numeros=return_values()
            resultado_m = multi(numeros[0],numeros[1])
            print("El resultado de la multiplicasion es",resultado_m)
        elif  opcion == 4:
            numeros=return_values()
            resultado_d = dvide(numeros[0],numeros[1])
            print("El resultado de la division es",resultado_d)
        elif  opcion == 5:
            
            print('bye')
            break

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


clearConsole()