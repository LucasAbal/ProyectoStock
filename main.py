import tkinter as tk
from agregar_producto import agregar_producto
from eliminar_producto import eliminar_producto
from mostrar_planilla import mostrar_planilla
from mostrar_grafica import mostrar_grafica

def main_ventana():
    ventana = tk.Tk()
    ventana.title("Pantalla Principal")
    ventana.geometry("300x250")

    # Botón para agregar producto
    boton_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto)
    boton_agregar.pack(pady=10)

    # Botón para eliminar producto
    boton_eliminar = tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto)
    boton_eliminar.pack(pady=10)

    # Botón para mostrar planilla
    boton_planilla = tk.Button(ventana, text="Mostrar Planilla", command=mostrar_planilla)
    boton_planilla.pack(pady=10)

    # Botón para mostrar gráfica
    boton_grafica = tk.Button(ventana, text="Mostrar Gráfica", command=mostrar_grafica)
    boton_grafica.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    import database
    database.crear_tablas()  # Crear tablas si no existen
    main_ventana()
