
numeros_1 = 10
numeros_2 = 5

string_1 = "Texto1"
string_2 = "Texto2"

lista_1 = ["Valor1", "Valor2", "Valor3"]
lista_2 = ["Valor4", "Valor5", "Valor6"]

dic_1 = {"Clave1": "valor1", "Clave2": "valor2"}
dic_2 = {"Clave3": "valor3", "Clave4": "valor4"}

# Operadores Aritmeticos
print(numeros_1 + numeros_2)
print(numeros_1 - numeros_2)
print(numeros_1 * numeros_2)
print(numeros_1 ** numeros_2)

# Operadores de pertenencia   IN

# valor5 se encuentra en la lista_1 ?
print('valor5' in lista_1) 

# Valor 45 no esta en lista_2 ?
print('valor 45' not in lista_2)

# Clave1 se encuentra en el diccionario_1 ?
print("Clave1" in dic_1)



## Operadores Logicos   AND, OR, NOT
print( numeros_1 < numeros_2 or "Valor1" in lista_1)
print( numeros_1 < numeros_2 and "Valor1" in lista_1)
print( not(numeros_1 > numeros_2))


## Operadores de Identidad   IS, IS NOT
print(type(string_1) is str)  # El tipo string_1 es de tipo string ?
print(type(lista_1) is list)  # El tipo lista_1 es de tipo lista ?
print(type(numeros_1) is int)  # El tipo numeros_1 es de tipo entero ?