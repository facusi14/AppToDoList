import tkinter as tk
from tkinter import messagebox
from validacion import validacion
from cambiar_estado_de_tarea import cambiar_estado
from main import agregar_nuevo_pedido, mostrar_estados, modificar_estados

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Pedidos")
        self.geometry("400x300")

        # Menu principal
        
        self.menu_principal = tk.Frame(self)
        self.menu_principal.pack()

        self.label_menu = tk.Label(self.menu_principal, text="Menú principal")
        self.label_menu.pack()

        self.button_agregar_pedido = tk.Button(self.menu_principal, text="Agregar nuevo pedido", command=self.agregar_nuevo_pedido)
        self.button_agregar_pedido.pack()

        self.button_mostrar_estados = tk.Button(self.menu_principal, text="Mostrar estados de pedidos", command=self.mostrar_estados)
        self.button_mostrar_estados.pack()

        self.button_modificar_estados = tk.Button(self.menu_principal, text="Modificar estados de pedidos", command=self.modificar_estados)
        self.button_modificar_estados.pack()

        self.button_salir = tk.Button(self.menu_principal, text="Salir", command=self.destroy)
        self.button_salir.pack()

    def agregar_nuevo_pedido(self):
        
        # Llamada a la función para agregar un nuevo pedido
        agregar_nuevo_pedido()
        messagebox.showinfo("Mensaje", "Pedido agregado correctamente")

    def mostrar_estados(self):
        
        # Llamada a la función para mostrar los estados de los pedidos
        mostrar_estados()
        messagebox.showinfo("Mensaje", "Estados de pedidos mostrados correctamente")

    def modificar_estados(self):
        
        # Llamada a la función para modificar los estados de los pedidos
        modificar_estados()
        messagebox.showinfo("Mensaje", "Estados de pedidos modificados correctamente")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()