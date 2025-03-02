from validacion import validacion

pedidos = [
    {"fecha_pedido":"2025-02-20",
     "nombre_pedido":"hola",
     "impresion": "si",
     "corte": "No",
     "pelado":"no",
     "entregado":"no"},
]

def agregar_nuevo_pedido(pedidos):
    nuevo_pedido = validacion()

