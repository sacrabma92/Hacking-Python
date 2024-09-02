 

edad = int(input("Introduce tu edad: "))

if edad >= 18 and edad < 21: 
  print("El usuario es mayor de 18 y menor a 21")
elif edad >= 21:
  print("El usuario es mayor de 21") 

if edad in [18, 20, 25, 4]:
  print("El usuario tiene 18 o 20 o 25 o 4")