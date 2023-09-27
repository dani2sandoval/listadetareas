import json
import os

def cargar(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as archivo:
            return json.load(archivo)
    else:
        return []

def guardar(tareas, nombre):
    with open(nombre, 'w') as archivo:
        json.dump(tareas, archivo)

def agregar(tareas):
    tarea = {"titulo": input("Ingresa el nombre de la tarea: "),
             "descripcion": input("Ingresa de que trata la tarea: "),
             "completada": False}
    tareas.append(tarea)
    print("La tarea fue agregada correctamente")

def listar(tareas):
    for i, tarea in enumerate(tareas):
        print(f"Tarea {i+1}:")
        print(f"Título: {tarea['titulo']}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Completada: {'Sí' if tarea['completada'] else 'No'}\n")

def completar(tareas):
    listar(tareas)
    numero = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
    if 0 <= numero < len(tareas):
        tareas[numero]['completada'] = True
        print("La tarea fue marcada como completada correctamente")
    else:
        print("Número de tarea inválido")

pendientes = cargar("pendientes.json")

while True:
    print("1. Agregar tarea")
    print("2. Mostrar tareas pendientes")
    print("3. Marcar como completada")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar(pendientes)
    elif opcion == '2':
        listar(pendientes)
    elif opcion == '3':
        completar(pendientes)
    elif opcion == '4':
        break
    else:
        print("Seleccione una de las opciones")

guardar(pendientes, "pendientes.json")
