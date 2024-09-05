import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def convert_image(format):
    file_path = entry_path.get()
    if not file_path:
        messagebox.showerror("Error", "Por favor, selecciona un archivo de imagen.")
        return
    
    try:
        image = Image.open(file_path)
        save_path = filedialog.asksaveasfilename(defaultextension=f".{format}", filetypes=[(f"{format.upper()} files", f"*.{format}")])
        if save_path:
            image.save(save_path)
            messagebox.showinfo("Éxito", f"Imagen convertida y guardada como {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo convertir la imagen: {e}")

def Cerrar_Ventana():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de Imágenes")
root.geometry("400x250")
root.resizable(False, False)

# Crear el marco principal
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Campo de entrada para la ruta del archivo
entry_path = ttk.Entry(frame, width=40)
entry_path.pack(side=tk.LEFT, padx=(0, 10), pady=10)

# Botón para seleccionar el archivo
button_browse = ttk.Button(frame, text="Seleccionar Archivo", command=select_file)
button_browse.pack(side=tk.LEFT, pady=10)

# Marco para los botones de formato
format_frame = ttk.LabelFrame(root, text="Selecciona el Formato de Conversión", padding="10")
format_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Botones para los formatos de imagen
formats = ["png", "jpg", "bmp", "gif"]
for fmt in formats:
    button = ttk.Button(format_frame, text=fmt.upper(), command=lambda f=fmt: convert_image(f))
    button.pack(side=tk.LEFT, padx=10, pady=5)

# Crear el marco principal
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

close_button = ttk.Button(frame, text="Cerrar Ventana", command=Cerrar_Ventana)
close_button.pack( padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
