import tkinter as tk
from tkinter import ttk
from operaciones import *
from PIL import Image, ImageTk

def Centrar_ventana(window, width, height):
    # Obtener el ancho y alto de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calcular la posición del centro
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Establecer la geometría de la ventana
    window.geometry(f'{width}x{height}+{x}+{y}')

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
    #window1.geometry("300x200")  # Definir el tamaño de la ventana principal
    Centrar_ventana(window1, 400, 300)
    window1.resizable(True, True)  # Permitir redimensionar la ventana principal
    
    # Cargar la imagen de fondo
    try:
        bg_image = Image.open("fondo1.jpg")
        bg_image = ImageTk.PhotoImage(bg_image)
        canvas = tk.Canvas(window1, width=800, height=600)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
    except Exception as e:
        print(f"Error al cargar la imagen de fondo: {e}")
    
    # Crear un cuadro de texto
    entry1 = ttk.Entry(window1)
    entry1.pack(padx=20, pady=10)
    
    # Crear un cuadro de texto
    entry2 = ttk.Entry(window1)
    entry2.pack(padx=20, pady=10)
    
    # Función que se llama al presionar el botón
    def on_button_click():
        numero1 = entry1.get()
        numero2 = entry2.get()
        print(f"Texto del cuadro de texto: {numero1} y {numero2}")
        label.config(text=f"Resultado: {numero1}  {numero2}")
    
    # Crear un botón
    button = ttk.Button(window1, text="Obtener texto", command=on_button_click)
    button.pack(padx=20, pady=10)
    
    label = tk.Label(window1, text=f"Resultado:")
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
