from tkinter import * #Importamos todas las funcionalidades
# de esta forma para no tener que escribir 'tkinter' antes de
# cada función.

raiz = Tk()# Instancia de la ventana (En adelante referida como Instancia)
raiz.title('Ventana de Prueba')# Titulo de la instancia
raiz.resizable(True,False)# Permiso de Redimencion (Ancho,Alto)
raiz.iconbitmap('Img/b.ico')# Icono de la instancia
raiz.geometry('1080x920')# Tamaño por defecto (Ancho x Alto)
raiz.config(bg='black')# bg Color de fondo (back graund)
raiz.mainloop()# Loop infinito para ejecución permanente