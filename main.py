from funciones import *
def menu_principal():
    while True:
        print("Menú principal")
        print("1. Agregar nuevo pedido")
        print("2. Mostrar estados de pedidos")
        print("3. Modificar estados de pedidos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_nuevo_pedido()
        elif opcion == "2":
            mostrar_estados()
        elif opcion == "3":
            modificar_estados()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu_principal()