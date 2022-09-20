# scrip que juega piedra papel o tijera con el usuario

import random
 # leer elecion del usuario
user = input("elige pidra,papel o tijera")
 #generar elecion maquina 
aleatorio = random.randint(1, 3)
if aleatorio == 1:
    machine = "piedra"
elif aleatorio == 2:
    machine ="papel" 
else:
    machine ="tijera"       


 #compárar para determinar quien gana 
print(f"El usuario eligiop{user}y la maquina eligio {machine}")

if machine == "piedra" and user== "tijera":
    print("la maquina gana")
elif machine == "piedra" and user== "papel":
    print("el usuario gana")
elif machine == "piedra" and user== "piedra":
    print("empate")
elif machine == "papel" and user== "tijera":
    print("la maquina pierde")
elif machine == "papel" and user== "piedra":
    print("la maquina gana")
elif machine == "papel" and user== "papel":
    print("empate")
elif machine == "tijera" and user== "tijera":
    print("empate")
elif machine == "tijera" and user== "piedra":
    print("la maquina pirde")
elif machine == "tijera" and user== "papel":
    print("la maquina gana")    

