

lista = ["tarea1", "tarea2", "tarea3"]

for tarea in lista:
  print("Estoy trabajando en la tarea: ", tarea)

print("\n##########\n")

lista_tareas = {
  "tarea1": "completada",
  "tarea2": "pendiente",
  "tarea3": "en progreso",
  "tarea4": "completada",
}

for tarea in lista_tareas:
  print("Estoy trabajando en la tarea:", tarea)
  print("El estado de la tarea es:",lista_tareas[tarea])

print("\n##########\n")

  ##### WHILE ####

num = 10

while num > 0:
  num -= 1
  print(num)

print("\n##########\n")

for i in range(21):
  print(i)