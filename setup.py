from cx_Freeze import setup, Executable

# Define la configuración del ejecutable
setup(
    name="MiAplicacion",
    version="1.0",
    description="Descripción de la Aplicación",
    executables=[Executable("main.py", base="Win32GUI")],
)
