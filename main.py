import tkinter as tk
from tkinter import ttk

def open_window1():
    window1 = tk.Toplevel()
    window1.title("Ventana 1")
    label = tk.Label(window1, text="Esta es la Ventana 1")
    label.pack(padx=20, pady=20)

def open_window2():
    window2 = tk.Toplevel()
    window2.title("Ventana 2")
    label = tk.Label(window2, text="Esta es la Ventana 2")
    label.pack(padx=20, pady=20)

def close_main_window():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.resizable(True, True)  # Permitir redimensionar la ventana principal

# Crear el menú
menubar = tk.Menu(root)
root.config(menu=menubar)

# Crear el menú Archivo
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir Ventana 1", command=open_window1)
file_menu.add_command(label="Abrir Ventana 2", command=open_window2)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

# Crear el marco principal
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Añadir botones al marco principal
button1 = ttk.Button(frame, text="Abrir Ventana 1", command=open_window1)
button1.pack(padx=10, pady=10)

button2 = ttk.Button(frame, text="Abrir Ventana 2", command=open_window2)
button2.pack(padx=10, pady=10)

# Añadir botón para cerrar la ventana principal
button_close = ttk.Button(frame, text="Cerrar Ventana Principal", command=close_main_window)
button_close.pack(padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
