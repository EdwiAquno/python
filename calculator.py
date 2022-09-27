from email import message


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2
def multi(num1, num2):

 def dvide(num1, num2):
     return num1/ num2   



if __name__=='__main__':
    message = F"calculadora: \n Elige una opcon\n, 1 - resta\n, 3 - multiplicasion\n, 4 - divicion"
    
    while True:
        opcion = int(input(message))
        if  opcion == 5:
            print('Bye')
            break

