import tkinter as tk
from tkinter import simpledialog, messagebox
from database import eliminar_producto as db_eliminar_producto
from mostrar_planilla import mostrar_planilla  # Importa la función correcta para actualizar la vista

def eliminar_producto():
    id_producto = simpledialog.askinteger("Eliminar Producto", "Ingrese el ID del producto a eliminar:")
    if id_producto is not None:
        if db_eliminar_producto(id_producto):
            mostrar_planilla()  # Actualiza la planilla después de eliminar el producto
        else:
            messagebox.showwarning("Advertencia", "El producto con el ID proporcionado no existe.")
