import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def mostrar_contenido_pdf(pdf_path):
    try:
        # Abrir el archivo PDF en modo binario
        print(pdf_path)
        with open(pdf_path, 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)
            numero_paginas = len(lector_pdf.pages)
            print(f"El PDF tiene {numero_paginas} páginas.\n")

            # Iterar a través de cada página y extraer el texto
            for pagina_numero in range(numero_paginas):
                pagina = lector_pdf.pages[pagina_numero]
                texto = pagina.extract_text()
                
                print(f"Página {pagina_numero + 1}:\n")
                print(texto)
                print("\n" + "-"*50 + "\n")
    except FileNotFoundError:
        print(f"El archivo '{pdf_path}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el PDF: {e}")

def seleccionar_pdf():
    # Abrir un cuadro de diálogo para seleccionar el archivo PDF
    archivo_pdf = filedialog.askopenfilename(
        title="Seleccionar archivo PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    
    if archivo_pdf:
        # Mostrar el contenido del archivo PDF seleccionado
        mostrar_contenido_pdf(archivo_pdf)
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lector de PDF")

# Crear un botón para abrir el cuadro de diálogo de selección de archivo
boton_seleccionar_pdf = tk.Button(ventana, text="Seleccionar archivo PDF", command=seleccionar_pdf)
boton_seleccionar_pdf.pack(pady=20)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
