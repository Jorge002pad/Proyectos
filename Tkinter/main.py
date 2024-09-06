import tkinter as tk
from tkinter import messagebox, ttk

def saludo():
    """Función que imprime un saludo en la consola."""
    print("¡Hola!")

def mostrar_mensaje():
    """Función que muestra un cuadro de mensaje con información."""
    messagebox.showinfo("Información", "Esto es un mensaje informativo.")

def abrir_ventana():
    """Función que abre una nueva ventana secundaria."""
    ventana_nueva = tk.Toplevel(root)
    ventana_nueva.title("Ventana secundaria")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Widgets en Tkinter")
root.geometry("800x700")  # Tamaño de la ventana principal

# Crear un Canvas para contener todos los widgets
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear una barra de desplazamiento vertical asociada al Canvas
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Crear un Frame dentro del Canvas donde se colocarán los widgets
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

# Función para actualizar el área de desplazamiento del Canvas cuando el Frame cambia de tamaño
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Asociar la función de actualización con el evento de cambio de tamaño del Frame
frame.bind("<Configure>", on_frame_configure)

# Agregar widgets al Frame

# Etiqueta que muestra texto con formato
tk.Label(frame, text="Hola, Tkinter!", font=("Arial", 16), fg="blue", bg="yellow").pack(pady=10)

# Entrada de texto para ingresar datos
tk.Entry(frame, width=50).pack(pady=10)

# Botón que ejecuta la función saludo cuando se hace clic
tk.Button(frame, text="Saludar", command=saludo, fg="white", bg="green").pack(pady=10)

# Casilla de verificación que utiliza una variable para almacenar su estado
var_check = tk.IntVar()
tk.Checkbutton(frame, text="Acepto los términos", variable=var_check).pack(pady=10)

# Botones de opción que permiten seleccionar una opción
var_radio = tk.IntVar()
tk.Radiobutton(frame, text="Opción 1", variable=var_radio, value=1).pack(pady=5)
tk.Radiobutton(frame, text="Opción 2", variable=var_radio, value=2).pack(pady=5)

# Lista desplegable que permite seleccionar una opción
lista = tk.Listbox(frame, height=3)
lista.insert(1, "Opción 1")
lista.insert(2, "Opción 2")
lista.insert(3, "Opción 3")
lista.pack(pady=10)

# Barra deslizante horizontal que permite seleccionar un valor entre 0 y 100
tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL).pack(pady=10)

# Área de texto para mostrar y editar texto multi-línea
texto = tk.Text(frame, height=5, width=50)
texto.insert(tk.END, "Este es un área de texto.")
texto.pack(pady=10)

# Dibuja líneas y rectángulos en el Canvas (lienzo)
canvas.create_line(0, 0, 200, 100, fill="blue", width=3)
canvas.create_rectangle(50, 25, 150, 75, outline="red", width=3)
canvas.pack(pady=10)

# Frame adicional para mostrar una etiqueta con un fondo de color
frame_sub = tk.Frame(frame, bg="lightblue", bd=5)
tk.Label(frame_sub, text="Soy un Frame").pack()
frame_sub.pack(pady=10, fill="both", expand=True)

# Crear un menú en la ventana principal
menu = tk.Menu(root)
root.config(menu=menu)

# Crear un menú desplegable "Archivo" en el menú principal
archivo_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.quit)

# Botón que muestra un cuadro de mensaje informativo cuando se hace clic
tk.Button(frame, text="Mostrar mensaje", command=mostrar_mensaje).pack(pady=10)

# Botón que abre una nueva ventana secundaria
tk.Button(frame, text="Abrir ventana secundaria", command=abrir_ventana).pack(pady=10)

# Barra de progreso que muestra el progreso de una operación
progress = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
