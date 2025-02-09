tareas = []

def agregar_tarea():
    nombre_tarea = input("Ingrese el nombre de la tarea")
    while nombre_tarea == "":
        print("El nombre de la tarea no puede estar vacio")
        nombre_tarea = input("Ingrese nuevamente el nombre de la tarea")
        
    tareas.append({"nombre": nombre_tarea, "completada":False})
    print(f"Tarea '{nombre_tarea}' agregada correctamente.")    
        
def mostrar_tareas():
    contador = 0
    for i in tareas:
        contador += 1
        print(f"La tarea {contador} es {i}")

def marca_completada():
    indice = int(input("Ingrese el indice de la tarea que quiere marcar como completada"))
    indice = indice - 1
    while indice < 0 or indice >= len(tareas):
        print(f"Ingrese un indice correcto")
        indice = int(input("Ingrese el indice de la tarea que quiere marcar como completada"))
        
    tarea_marcada = tareas[indice]
    tarea_marcada["completada"] = True
    print(f"La tarea {tarea_marcada} ha sido marcada como completada")
            
        
    
    while indice > len(tareas):
        print("Error el indice no esta disponible, reingrese nuevamente un indice valido")
        indice = int(input("Ingrese el indice de la tarea que quiere marcar como completada"))
    
    

def eliminar_tarea():
    indice = int(input("Ingrese el indice de la tarea que quiere eliminar"))
    indice = indice - 1
    
    while indice < 0 or indice >= len(tareas):
        print(f"Ingrese un indice correcto")
        indice = int(input("Ingrese el indice de la tarea que quiere eliminar"))
    
    tarea_eliminada = tareas.pop(indice)
    
    nombre_tarea_eliminada = tarea_eliminada["nombre"]
    
    print(f"La tarea {nombre_tarea_eliminada} ha sido borrada")

