#condicionales if elif else 
#nos permite evaluar expreciones boleanas que al cumplirse 
#una accion y en caso d eque no realizar otra 

#evaluar si una poersona es mayor de edad
# nos diga si es joven , niño,bebe ,muy mayor 

genero = input("ingrasa tu genero M o F:")
age =int(input('ingresa tu edad:' ))

if genero == "M":
    
  if age < 2:
    print("Eres un  bebe")
  elif age <12:
    print("eres un niño")
  elif age < 18:
    print("eres un joven") 
  elif age < 50:
    print("eres un adulto") 



#if age > 18:
    #print("Eres mayor de edad!")
  else:
    print("Eres muy mayor!")  
else:
  if age < 2:
    print("Eres una  bebe")
  elif age <12:
    print("eres una niña")
  elif age < 18:
    print("eres una joven") 
  elif age < 50:
    print("eres una adulta") 



#if age > 18:
    #print("Eres mayor de edad!")
  else:
    print("Eres muy mayor!")     

