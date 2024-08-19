import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datos import obtener_datos_productos

def mostrar_grafica():
    datos = obtener_datos_productos()
    
    if not datos:
        messagebox.showinfo("Información", "No hay datos para mostrar en la gráfica.")
        return

    # Separar los datos
    ids = [producto[0] for producto in datos]
    nombres = [producto[1] for producto in datos]
    comprados = [producto[2] for producto in datos]
    usados = [producto[3] for producto in datos]

    # Crear la figura y el eje para la gráfica
    fig, ax = plt.subplots()
    index = range(len(nombres))
    
    bar_width = 0.35
    opacity = 0.8

    bars1 = ax.bar(index, comprados, bar_width, alpha=opacity, color='b', label='Cant. Comprado')
    bars2 = ax.bar([i + bar_width for i in index], usados, bar_width, alpha=opacity, color='r', label='Cant. Usado')

    ax.set_xlabel('Productos')
    ax.set_ylabel('Cantidad')
    ax.set_title('Cantidad Comprada vs Usada por Producto')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(nombres, rotation=45, ha='right')
    ax.legend()

    # Insertar la gráfica en la ventana de Tkinter
    ventana_grafica = tk.Toplevel()
    ventana_grafica.title("Gráfica de Productos")
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Botón para cerrar la ventana de la gráfica
    boton_cerrar = tk.Button(ventana_grafica, text="Cerrar", command=ventana_grafica.destroy)
    boton_cerrar.pack(pady=10)

