import sqlite3

def conectar_db():
    return sqlite3.connect('productos.db')

def crear_tablas():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            comprado INTEGER,
            usado INTEGER
        )
        ''')
        conn.commit()

def obtener_productos():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos')
        return cursor.fetchall()

def agregar_producto(nombre, comprado=0, usado=0):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO productos (nombre, comprado, usado) VALUES (?, ?, ?)', (nombre, comprado, usado))
        conn.commit()

def eliminar_producto(id_producto):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
        conn.commit()
        return cursor.rowcount > 0  # Retorna True si se eliminó al menos una fila

def actualizar_producto(id_producto, nuevo_comprado, nuevo_usado):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE productos SET comprado = ?, usado = ? WHERE id = ?', (nuevo_comprado, nuevo_usado, id_producto))
        conn.commit()
