import tkinter as tk
from tkinter import simpledialog, messagebox
from mostrar_planilla import mostrar_planilla  # Importar la función correcta
from database import agregar_producto as db_agregar_producto

def agregar_producto():
    nombre = simpledialog.askstring("Agregar Producto", "Ingrese el nombre del producto:")
    if nombre:
        db_agregar_producto(nombre)
        mostrar_planilla()  # Actualizar la planilla directamente
    else:
        messagebox.showwarning("Advertencia", "El nombre del producto no puede estar vacío.")
