import tkinter as tk
from tkinter import scrolledtext, Menu, messagebox, filedialog
import os
from analizadorLexico import analizador_sintactico

class interfaz:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación de Análisis")
        self.ventana.geometry("1080x700")
        
        # Fondo azul marino
        self.ventana.configure(bg="#0B3954")
        
        self.agregar_menu()
        
        # Frame para botones y menú
        self.frame_menu = tk.Frame(self.ventana, bg="#0B3954")  # Fondo azul marino para el frame
        self.frame_menu.pack(side=tk.TOP, fill=tk.X)
        
        # Menú
        menubar = Menu(self.frame_menu, bg="#0B3954", fg="white")  # Fondo azul marino y texto blanco para el menú
        self.ventana.config(menu=menubar)
        opciones = Menu(menubar, tearoff=0)
        opciones.add_command(label="Nuevo", command=self.nuevo)
        opciones.add_command(label="Abrir archivo", command=self.abrir_archivo)
        opciones.add_command(label="Guardar")
        opciones.add_command(label="Guardar como", command=self.guardar_como)
        opciones.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Menu", menu=opciones)
        
        # Botones en el frame
        btn_analisis = tk.Button(self.frame_menu, text='Análisis', width=15, height=2, command=self.analizar, bg="#1B4F72", fg="white")  # Fondo azul oscuro y texto blanco para el botón
        btn_analisis.pack(side=tk.LEFT, padx=10, pady=10)
        btn_analisis.configure(font=('Arial', 12, 'bold'))
        
        btn_tokens = tk.Button(self.frame_menu, text='Tabla Tokens', width=15, height=2, command=self.tabla_tokens, bg="#1B4F72", fg="white")  # Fondo azul oscuro y texto blanco para el botón
        btn_tokens.pack(side=tk.LEFT, padx=10, pady=10)
        btn_tokens.configure(font=('Arial', 12, 'bold'))
        
        btn_errores = tk.Button(self.frame_menu, text='Tabla Errores', width=15, height=2, command=self.tabla_errores, bg="#1B4F72", fg="white")  # Fondo azul oscuro y texto blanco para el botón
        btn_errores.pack(side=tk.LEFT, padx=10, pady=10)
        btn_errores.configure(font=('Arial', 12, 'bold'))
        
        # Elementos de texto
        self.scrolledtext = scrolledtext.ScrolledText(self.ventana, width=80, height=20, bg="#154360", fg="white")  # Fondo azul marino oscuro y texto blanco para el área de texto
        self.scrolledtext.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
        
        self.scrolledtext1 = scrolledtext.ScrolledText(self.ventana, width=80, height=10, bg="#154360", fg="white")  # Fondo azul marino oscuro y texto blanco para el área de texto
        self.scrolledtext1.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
        
        # Centrar la ventana
        self.centrar_ventana()
        
        self.ventana.mainloop()

    def agregar_menu(self):
        menubar = Menu(self.ventana)
        self.ventana.config(menu=menubar)
        opciones = Menu(menubar, tearoff=0)
        opciones.add_command(label="Nuevo", command=self.nuevo)
        opciones.add_command(label="Abrir archivo", command=self.abrir_archivo)
        opciones.add_command(label="Guardar")
        opciones.add_command(label="Guardar como", command=self.guardar_como)
        opciones.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Menu", menu=opciones)

    def nuevo(self):
        self.scrolledtext.delete("1.0", tk.END)
        self.scrolledtext1.delete("1.0", tk.END)

    def abrir_archivo(self):
        nombre_archivo = filedialog.askopenfilename(initialdir="c:/pythonya", title="Seleccione archivo",
                                                    filetypes=(("todos los archivos", "*.*"),))
        if nombre_archivo != '':
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                self.scrolledtext.delete("1.0", tk.END)
                self.scrolledtext.insert("1.0", contenido)
                self.texto = contenido

    def guardar_como(self):
        nombre_archivo = filedialog.asksaveasfilename(initialdir="c:/pythonya", title="Guardar como",filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombre_archivo != '':
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(self.scrolledtext.get("1.0", tk.END))
            messagebox.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def salir(self):
        self.ventana.quit()

    def analizar(self):
        respuestas = []
        self.texto = self.scrolledtext.get("1.0", tk.END)
        respuestas = analizador_sintactico(self.texto)
        self.scrolledtext1.delete('1.0', tk.END)
        for respuesta in respuestas:
            self.scrolledtext1.insert(tk.END, f'\n {respuesta}')

    def tabla_errores(self):
        path = 'TablaErrores.html'
        os.system(path)

    def tabla_tokens(self):
        path = 'TablaTokens.html'
        os.system(path)

    def centrar_ventana(self):
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)
        self.ventana.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))

# Crear la aplicación
aplicacion = interfaz()
