import tkinter as tk

def crear_planilla(ventana):
    # Crear una matriz de 30x30 entradas
    celdas = []
    for i in range(30):
        fila = []
        for j in range(30):
            # Crear una entrada por cada celda
            celda = tk.Entry(ventana, width=5)
            celda.grid(row=i, column=j)
            fila.append(celda)
        celdas.append(fila)
    return celdas
