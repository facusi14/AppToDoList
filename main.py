from funciones import *


while True:
    print("MENU:")
    print("1.Agregar nuevo pedido")
    print("2.Mostrar tareas")
    print("3.Marcar tarea como completada")
    print("4.Eliminar tarea")
    print("5.Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        agregar_nuevo_pedido()
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    else:
        print("Saliendo del programa... ")
        break