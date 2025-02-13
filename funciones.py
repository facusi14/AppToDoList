tareas = []

def agregar_tarea():
    nombre_tarea = input(" \nIngrese el nombre de la tarea:  ")
    while nombre_tarea == "":
        print("El nombre de la tarea no puede estar vacio")
        nombre_tarea = input("Ingrese nuevamente el nombre de la tarea")
        
    tareas.append({"nombre": nombre_tarea, "completada":False})
    print( "\n--------------")
    print(f" \n La Tarea \n {nombre_tarea} fue agregada correctamente ")    
    print( "\n")
        
def mostrar_tareas():   
    contador = 0
    
    for i in tareas:
        contador_tareas_pendientes = 0
        if i["completada"] == False:
            contador_tareas_pendientes += 1
            print(f"Las tareas que estan pendientes  son {i["nombre"]}")
        elif i["completada"]  == True:
            print(f"Las tareas que estan completadas son {i["nombre"]}")
        
            
        
        

def marca_completada():
    
    try:
        indice = int(input("Ingrese el indice de la tarea que quiere marcar como completada"))
        indice = indice - 1
        while indice < 0 or indice >= len(tareas):
            print(f"Ingrese un indice correcto")
            indice = int(input("Ingrese el indice de la tarea que quiere marcar como completada"))
        
        tarea_marcada = tareas[indice]
        tarea_marcada["completada"] = True
        
        print(f"La tarea {tarea_marcada} ha sido marcada como completada")
        
    except ValueError:
        print("Error debe ingresar un indice numero entero valido")
    
            
        
    
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

