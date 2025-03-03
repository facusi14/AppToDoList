from datetime import datetime

def validacion():
    print(" Bienvenidos ")
    
    try:
        fecha = input(" Ingrese la fecha (YYYY-MM-DD): ")
        datetime.strptime( fecha, "%Y-%m-%d")
        
        nombre_pedido = input(" Ingrese el nombre del pedido ")
        while len(nombre_pedido) <= 0:
            nombre_pedido = input(" Error Ingrese un nombre del pedido")
        
        #Valores predeterminados a los estados
        
        impresion = "en espera"
        corte = "en espera"
        finalizacion = "en espera"
        entrega = "en espera"
        pago = "en espera"
        
    except ValueError:
     print("La fecha no es valida. Ingresa una fecha en formato correcto")

    return{
        "Fecha_pedido": fecha,
        "Nombre_pedido": nombre_pedido,
        "Impresion": impresion,
        "Corte": corte,
        "Finalizacion": finalizacion,
        "Entregado": entrega,
        "Pagado": pago
        }