from validacion import validacion
from cambiar_estado_de_tarea import cambiar_estado
pedidos = []

def agregar_nuevo_pedido():
    nuevo_pedido = validacion()
    pedidos.append(nuevo_pedido)

def mostrar_estados():
    
    pedido_a_mostrar = input("Ingrese que pedido debe mostrar")
    
    while pedido_a_mostrar not in [pedido["Nombre_pedido"] for pedido in pedidos]:
        pedido_a_mostrar = input("No se encontro el pedido Reingrese un nombre de pedido correcto")
    
    for pedido in pedidos:
        print(pedido)
def modificar_estados():
    seleccione_pedido = input("Seleccione el nombre del pedido que desea modificar: ")
    cambios = {}
    
    cambiar_impresion = input("Desea cambiar el estado de impresión? (s/n): ")
    if cambiar_impresion.lower() == "s":
        cambios["impresion"] = input("Ingrese el nuevo estado de impresión: ")
    
    cambiar_corte = input("Desea cambiar el estado de corte? (s/n): ")
    if cambiar_corte.lower() == "s":
        cambios["corte"] = input("Ingrese el nuevo estado de corte: ")
    
    cambiar_finalizacion = input("Desea cambiar el estado de finalización? (s/n): ")
    if cambiar_finalizacion.lower() == "s":
        cambios["finalizacion"] = input("Ingrese el nuevo estado de finalización: ")
    
    cambiar_entrega = input("Desea cambiar el estado de entrega? (s/n): ")
    if cambiar_entrega.lower() == "s":
        cambios["entrega"] = input("Ingrese el nuevo estado de entrega: ")
    
    cambiar_pago = input("Desea cambiar el estado de pago? (s/n): ")
    if cambiar_pago.lower() == "s":
        cambios["pago"] = input("Ingrese el nuevo estado de pago: ")
    
    cambiar_estado(pedidos, cambios, seleccione_pedido)
    
def impresion_completada():
    print(pedidos)
    seleccione_pedido = input("Seleccione el nombre del pedido que desea marcar como terminado. ")
    cambiar_estado(pedidos,"impresion",seleccione_pedido)
        

def corte_completado():
    print(pedidos)
    seleccione_pedido = input("Seleccione el nombre del pedido que desea marcar como terminado. ")
    cambiar_estado(pedidos,"corte",seleccione_pedido)

def finalizacion_completada():
    print(pedidos)
    seleccione_pedido = input("Seleccione el nombre del pedido que desea marcar como terminado. ")
    cambiar_estado(pedidos,"finalizacion",seleccione_pedido)

def entrega_completada():
    print(pedidos)
    seleccione_pedido = input("Seleccione el nombre del pedido que desea marcar como terminado. ")
    cambiar_estado(pedidos,"entrega",seleccione_pedido)

def  pago_completado():
    print(pedidos)
    seleccione_pedido = input("Seleccione el nombre del pedido que desea marcar como pagado. ")
    cambiar_estado(pedidos,"pago",seleccione_pedido)