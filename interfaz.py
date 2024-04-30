from tkinter import *
from tkinter import ttk, scrolledtext, filedialog, messagebox
import os
from analizadorLexico import instruccion, analizador_sintactico

class Aplicacion:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1050x400")
        self.agregar_menu()
        self.scrolledtext = scrolledtext.ScrolledText(self.ventana, width=60, height=20)
        self.scrolledtext.grid(column=0, row=0, padx=10, pady=10)
        self.scrolledtext1 = scrolledtext.ScrolledText(self.ventana, width=60, height=20)
        self.scrolledtext1.grid(column=1, row=0, padx=10, pady=10)
        Button(self.ventana, text='Análisis', width=15, height=2, command=self.analizar).place(x=100, y=350)
        Button(self.ventana, text='Tabla Tokens', width=15, height=2, command=self.tabla_tokens).place(x=300, y=350)
        Button(self.ventana, text='Tabla Errores', width=15, height=2, command=self.tabla_errores).place(x=500, y=350)
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
        self.scrolledtext.delete("1.0", END)
        self.scrolledtext1.delete("1.0", END)

    def abrir_archivo(self):
        nombre_archivo = filedialog.askopenfilename(initialdir="c:/pythonya", title="Seleccione archivo",
                                                    filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombre_archivo != '':
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                self.scrolledtext.delete("1.0", END)
                self.scrolledtext.insert("1.0", contenido)
                self.texto = contenido

    def guardar_como(self):
        nombre_archivo = filedialog.asksaveasfilename(initialdir="c:/pythonya", title="Guardar como",filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombre_archivo != '':
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(self.scrolledtext.get("1.0", END))
            messagebox.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def salir(self):
        self.ventana.quit()

    def analizar(self):
        respuestas = []
        self.texto = self.scrolledtext.get("1.0", END)
        respuestas = analizador_sintactico(self.texto)
        self.scrolledtext1.delete('1.0', END)
        for respuesta in respuestas:
            self.scrolledtext1.insert(END, f'\n {respuesta}')

    def tabla_errores(self):
        path = 'TablaErrores.html'
        os.system(path)

    def tabla_tokens(self):
        path = 'TablaTokens.html'
        os.system(path)

aplicacion = Aplicacion()
