import tkinter as tk
from tkinter import simpledialog, messagebox
from datos import obtener_datos_productos
from database import actualizar_producto

# Inicializar la variable global
planilla_ventana = None

def mostrar_planilla():
    global planilla_ventana  # Declarar que vamos a usar la variable global
    
    if planilla_ventana:
        planilla_ventana.destroy()

    planilla_ventana = tk.Toplevel()
    planilla_ventana.title("Planilla de Productos")

    # Crear encabezados
    tk.Label(planilla_ventana, text="ID").grid(row=0, column=0)
    tk.Label(planilla_ventana, text="Nombre").grid(row=0, column=1)
    tk.Label(planilla_ventana, text="Cant. Comprado").grid(row=0, column=2)
    tk.Label(planilla_ventana, text="Cant. Usado").grid(row=0, column=3)
    tk.Label(planilla_ventana, text="Acción").grid(row=0, column=4)

    # Obtener y mostrar productos
    productos = obtener_datos_productos()
    for idx, (id_producto, nombre, comprado, usado) in enumerate(productos):
        tk.Label(planilla_ventana, text=id_producto).grid(row=idx+1, column=0)
        tk.Label(planilla_ventana, text=nombre).grid(row=idx+1, column=1)
        
        # Campos de entrada para los valores
        comprado_entry = tk.Entry(planilla_ventana)
        comprado_entry.insert(0, comprado)
        comprado_entry.grid(row=idx+1, column=2)
        
        usado_entry = tk.Entry(planilla_ventana)
        usado_entry.insert(0, usado)
        usado_entry.grid(row=idx+1, column=3)
        
        # Botón para guardar cambios
        boton_guardar = tk.Button(planilla_ventana, text="Guardar", command=lambda id=id_producto, c=comprado_entry, u=usado_entry: guardar_cambios(id, c.get(), u.get()))
        boton_guardar.grid(row=idx+1, column=4)

def guardar_cambios(id_producto, nuevo_comprado, nuevo_usado):
    try:
        nuevo_comprado = int(nuevo_comprado)
        nuevo_usado = int(nuevo_usado)
        if nuevo_usado > nuevo_comprado:
            respuesta = messagebox.askyesno("Advertencia", "El Cant. Usado es mayor que el Cant. Comprado. ¿Ha comprado más? Si no, es imposible tener más usado que comprado.")
            if respuesta:
                cantidad_adicional = simpledialog.askinteger("Cantidad Adicional", "¿Cuánto más ha comprado?")
                if cantidad_adicional is not None:
                    nuevo_comprado += cantidad_adicional
                else:
                    messagebox.showerror("Error", "Debe ingresar una cantidad adicional válida.")
                    return

            # Verificar si después de agregar la cantidad adicional, la cantidad comprada sigue siendo menor que la cantidad usada
            if nuevo_usado > nuevo_comprado:
                messagebox.showerror("Error", "La cantidad comprada sigue siendo menor que la cantidad usada. No se pueden guardar los cambios.")
                return
                
        actualizar_producto(id_producto, nuevo_comprado, nuevo_usado)
        mostrar_planilla()  # Actualizar la planilla después de guardar los cambios
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")
