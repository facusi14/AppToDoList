import tkinter as tk
from tkinter import messagebox
from validacion import validacion

def agregar_pedido():
    fecha = entrada_fecha.get()
    nombre_pedido = entrada_nombre_pedido.get()
    
    resultado = validacion(fecha, nombre_pedido)
    
    if resultado:
        # Logica para futura base de datos
        print(resultado)
        
        # mostrar un mensaje de confirmación
        messagebox.showinfo("Pedido Agregado", "El pedido ha sido agregado con éxito")
    else:
        messagebox.showerror("Error", "La fecha o el nombre del pedido no son válidos")

# Crea la ventana
ventana = tk.Tk()
ventana.title("Agregar Pedido")

# Crea un widget etiqueta y entrada para la fecha del pedido
etiqueta_fecha = tk.Label(ventana, text="Fecha del Pedido (YYYY-MM-DD):")
etiqueta_fecha.grid(column=0, row=0)
entrada_fecha = tk.Entry(ventana)
entrada_fecha.grid(column=1, row=0)

# Crea un widget etiqueta y entrada para el nombre del pedido
etiqueta_nombre_pedido = tk.Label(ventana, text="Nombre del Pedido:")
etiqueta_nombre_pedido.grid(column=0, row=1)
entrada_nombre_pedido = tk.Entry(ventana)
entrada_nombre_pedido.grid(column=1, row=1)

# Crea un widget botón para agregar el pedido
boton_agregar_pedido = tk.Button(ventana, text="Agregar Pedido", command=agregar_pedido)
boton_agregar_pedido.grid(column=1, row=2)

# Inicia el bucle principal
ventana.mainloop()