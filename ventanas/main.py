import tkinter as tk
from PIL import Image, ImageTk

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Ventana con imagen de fondo")
    root.geometry("300x200")

    # Cargar la imagen de fondo
    image_path = "fondo1.jpg"  # Cambia esto por la ruta de tu imagen
    image = Image.open(image_path)
    background_image = ImageTk.PhotoImage(image)

    # Crear un widget Label para mostrar la imagen
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Expande la imagen a toda la ventana

    # Añadir otros widgets encima de la imagen de fondo si es necesario
    frame = tk.Frame(root, bg='white', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)

    button = tk.Button(frame, text="Buscar", font=40, command=lambda: print("Buscando..."))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    # Iniciar el bucle principal de tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
