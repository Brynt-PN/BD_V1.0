import tkinter as tk

# Crea una ventana
ventana = tk.Tk()
ventana.title("Ejemplo Tkinter")

# Crea una etiqueta
etiqueta = tk.Label(ventana, text="Hola, Tkinter!")
etiqueta.pack()

# Inicia el bucle principal de la ventana
ventana.mainloop()