import tkinter as tk
from tkinter import ttk
from operaciones import *

def Suma():
    window1 = tk.Toplevel()
    window1.title("Suma")
    label = tk.Label(window1, text="Suma")
    label.pack(padx=20, pady=20)

def resta():
    window2 = tk.Toplevel()
    window2.title("Resta")
    label = tk.Label(window2, text="Resta")
    label.pack(padx=20, pady=20)

def open_window1():
    window1 = tk.Toplevel()
    window1.title("Ventana 1")
    
    # Crear un cuadro de texto
    entry = ttk.Entry(window1)
    entry.pack(padx=20, pady=10)
    
    # Función que se llama al presionar el botón
    def on_button_click():
        text = entry.get()
        print(f"Texto del cuadro de texto: {text}")
    
    # Crear un botón
    button = ttk.Button(window1, text="Obtener texto", command=on_button_click)
    button.pack(padx=20, pady=10)
    
    label = tk.Label(window1, text="Esta es la Ventana 1")
    label.pack(padx=20, pady=20)


def close_main_window():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x200")  # Definir el tamaño de la ventana principal
root.resizable(True, True)  # Permitir redimensionar la ventana principal

# Crear el menú
menubar = tk.Menu(root)
root.config(menu=menubar)

# Crear el menú Archivo
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Suma", command=Suma)
file_menu.add_command(label="Resta", command=resta)
file_menu.add_command(label="prueba", command=open_window1)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

# Crear el marco principal
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Añadir botones al marco principal
button1 = ttk.Button(frame, text="Abrir Suma", command=Suma)
button1.pack(padx=10, pady=10)

button2 = ttk.Button(frame, text="Abrir Resta", command=resta)
button2.pack(padx=10, pady=10)

button3 = ttk.Button(frame, text="Abrir prueba", command=open_window1)
button3.pack(padx=10, pady=10)

# Añadir botón para cerrar la ventana principal
button_close = ttk.Button(frame, text="Cerrar Ventana Principal", command=close_main_window)
button_close.pack(padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
