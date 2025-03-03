def cambiar_estado(pedidos, cambios, nombre_pedido):
    for pedido in pedidos:
        if pedido["Nombre_pedido"] == nombre_pedido:
            for clave, valor in cambios.items():
                clave_original = clave.capitalize()  # Convierte la primera letra a mayúscula
                pedido[clave_original] = valor
            return
    print("Pedido no encontrado")