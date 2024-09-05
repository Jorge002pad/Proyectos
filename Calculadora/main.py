import tkinter as tk
from tkinter import colorchooser
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
    window1.config(bg="#0000a0")
    Centrar_ventana(window1, 400, 300)
    label = tk.Label(window1, text="Suma")
    label.pack(padx=20, pady=20)
    
    # Crear un cuadro de texto
    entry1 = ttk.Entry(window1)
    entry1.pack(padx=20, pady=10)
    
    # Crear un cuadro de texto
    entry2 = ttk.Entry(window1)
    entry2.pack(padx=20, pady=10)
    
    def Obtener_resultado():
        numero1 = entry1.get()
        numero2 = entry2.get()
        
        try:
            # Intenta convertir la entrada a un número
            sumita=suma(int(numero1),int(numero2))
            print("Es un número válido.")
            print(f'Esta es la sumita {sumita}')
            print(f"Texto del cuadro de texto: {numero1} y {numero2}")
            label.config(text=f"Resultado: {sumita}")
        except ValueError:
            print("No es un número.")
            label.config(text=f"Verificar los valores de entrada")
        
    
    # Crear un botón
    button = ttk.Button(window1, text="Obtener texto", command=Obtener_resultado)
    button.pack(padx=20, pady=10)
    
    label = tk.Label(window1, text=f"Resultado:")
    label.pack(padx=20, pady=20)

def resta():
    window2 = tk.Toplevel()
    window2.title("Resta")
    Centrar_ventana(window2, 400, 300)
    label = tk.Label(window2, text="Resta")
    label.pack(padx=20, pady=20)

def Ventana_prueba():
    window1 = tk.Toplevel()
    window1.title("Ventana 1")
    #window1.geometry("300x200")  # Definir el tamaño de la ventana principal
    Centrar_ventana(window1, 400, 300)
    window1.resizable(True, True)  # Permitir redimensionar la ventana principal
    
    # Cargar la imagen de fondo
    '''try:
        bg_image = Image.open("fondo1.jpg")
        bg_image = ImageTk.PhotoImage(bg_image)
        canvas = tk.Canvas(window1, width=800, height=600)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
    except Exception as e:
        print(f"Error al cargar la imagen de fondo: {e}")
    '''
    # Crear un cuadro de texto
    entry1 = ttk.Entry(window1)
    entry1.pack(padx=20, pady=10)
    
    # Crear un cuadro de texto
    entry2 = ttk.Entry(window1)
    entry2.pack(padx=20, pady=10)
    
    # Función que se llama al presionar el botón
    def Obtener_resultado():
        numero1 = entry1.get()
        numero2 = entry2.get()
        print(f"Texto del cuadro de texto: {numero1} y {numero2}")
        label.config(text=f"Resultado: {numero1}  {numero2}")
    
    # Crear un botón
    button = ttk.Button(window1, text="Obtener texto", command=Obtener_resultado)
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

# Crear el marco principal
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Añadir botones al marco principal
button1 = ttk.Button(frame, text="Abrir Suma", command=Suma)
button1.pack(padx=10, pady=10)

button2 = ttk.Button(frame, text="Abrir Resta", command=resta)
button2.pack(padx=10, pady=10)

button3 = ttk.Button(frame, text="Abrir prueba", command=Ventana_prueba)
button3.pack(padx=10, pady=10)

# Añadir botón para cerrar la ventana principal
button_close = ttk.Button(frame, text="Cerrar Ventana Principal", command=close_main_window)
button_close.pack(padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
