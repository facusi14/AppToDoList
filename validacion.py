from datetime import datetime

def validacion(fecha , nombre_pedido):
    try:
        datetime.strptime( fecha, "%Y-%m-%d")
        
        while len(nombre_pedido) <= 0:
           
            return False
        
        #Valores predeterminados a los estados
        
        impresion = "en espera"
        corte = "en espera"
        finalizacion = "en espera"
        entrega = "en espera"
        pago = "en espera"
        
    

        return{
            "Fecha_pedido": fecha,
            "Nombre_pedido": nombre_pedido,
            "Impresion": impresion,
            "Corte": corte,
            "Finalizacion": finalizacion,
            "Entregado": entrega,
            "Pagado": pago
        }
    
    except ValueError:
        return False