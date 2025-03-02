from datetime import datetime

def validacion():
    print(" Bienvenidos ")
    
    try:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        datetime.strptime( fecha, "%Y-%m-%d")
        
        nombre_pedido = input("Ingrese el nombre del pedido")
        while len(nombre_pedido) <= 0:
            nombre_pedido = input(" Error Ingrese un nombre del pedido")
            
        estado_impresion = input("Ingrese el estado de impresion(en impresion o esperando diseño)")
        
        while estado_impresion != "en impresion" and estado_impresion != "esperando diseño":
            estado_impresion = input("Error ingrese el estado de impresion(en impresion o esperando diseño)")
        
        estado_corte = input("Ingrese el estado de corte(en espero o cortando)")
        
        while estado_corte != "en espera" and estado_corte != "cortando":
            estado_corte = input("Error ingrese el estado de corte(en espera o cortando)")
            
        estado_entrega = input("Ingrese el estado de entrega(en espera de retiro o entregado)")
        
        while estado_entrega != "en espera de retiro" and estado_entrega != "entregado":
            estado_entrega = input("Error ingrese el estado de entrega(en espera de retiro o entregado)")
        
            
    except ValueError:
     print("La fecha no es valida. Ingresa una fecha en formato correcto")

    return fecha,nombre_pedido,estado_impresion,estado_corte,estado_entrega
    