from funciones import *


while True:
    print("MENU:")
    print("1.Agregar tarea")
    print("2.Mostrar tareas")
    print("3.Marcar tarea como completada")
    print("4.Eliminar tarea")
    print("5.Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        marca_completada()
    elif opcion == "4":
        eliminar_tarea()
    else:
        print("Saliendo del programa... ")
        break