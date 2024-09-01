
# Lista de tareas
lista_tareas = ["tarea1", "tarea2", "tarea3", "tarea4", "tarea5"]

# Tuploa de tareas
tupla_tareas = ("tarea1", "tarea2", "tarea3", "tarea4", "tarea5")

#Diccionario de tareas
dic_tareas = {
  "tarea1": "pendiente",
  "tarea2": "en proceso" ,
  "tarea3": "pendiente" ,
  "tarea4": "terminada" ,
  "tarea5": "en proceso"
}

# Indexing - Acceder por indice
print(lista_tareas[2])
print(lista_tareas[-1]) # Accede al ultimo elemento
print(lista_tareas[2][3]) # Acceder al tercer elemento y a la posicion de la letra

# Indexing - Diccionario. Toca acceder por nombre de la clave
print(dic_tareas["tarea2"])



# Slicing - Nos permite seleccionar un rango.
print(lista_tareas[1:3])

cadena_texto = "cadena de texto"
print(cadena_texto[2:6])


# Stride - Numero Inicial : Numero Final : Cantidad de Saltos
print(tupla_tareas[0::2])

lista_tareas[2] = "Tarea Especial"  # Modificamos la lista de tareas
print(lista_tareas)