from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

from Ajenda import Ajenda
from Contacto import Contacto


class Ventana(tk.Tk):

    def __init__(self):

        super().__init__()
        self.ajenda = Ajenda()  # Creacion de un objeto de tipo ajenda

        self.title('Agenda')  # Titulo de la ventana
        self.geometry('650x500')  # Tamaño de la ventana (ancho - alto)
        colorFondo = '#006'  # Color en hexademimal
        colorLetra = '#FFF'  # Color en hexademimal
        self.config(background=colorFondo)  # Asignacion del color para la ventana
        self.resizable(0, 0)  # Para que el tamaño de la ventana no pueda ser modificado

        # varibles para almacenar las entradas del usuario
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.telefono = StringVar()
        self.correo = StringVar()

        # Creacion de caracteristicas de la ventana
        self.crearEtiquetas(colorFondo, colorLetra)
        self.crearEntradas()
        self.crearBotones()
        self.tabla = self.crearTabla()

        self.ajenda.iniciarArchivo()  # Creacion del archivo
        self.ajenda.cargar()  # Carga los contactos registrados

        self.mostrarContactos(self.ajenda.listaContactos)  # Muestra en la tabla los contactos registrados

        self.contactoSeleccionado = []  # Almacena los datos del contacto seleccionado
        self.banModificar = False  # Bandera para saber si el boton modificar esta activo o no

    def crearEtiquetas(self, colorFondo, colorLetra):

        lbTitulo = Label(self, text='Mi Aplicacion', bg=colorFondo, fg=colorLetra)  # Creacion del Label
        lbTitulo.place(x=270, y=10)  # Ubicacion del Label

        lbNombre = Label(self, text='Nombre', bg=colorFondo, fg=colorLetra)
        lbNombre.place(x=50, y=50)

        lbApellido = Label(self, text='Apellido', bg=colorFondo, fg=colorLetra)
        lbApellido.place(x=50, y=80)

        lbCorreo = Label(self, text='Correo', bg=colorFondo, fg=colorLetra)
        lbCorreo.place(x=50, y=140)

        lbTelefono = Label(self, text='Telefono', bg=colorFondo, fg=colorLetra)
        lbTelefono.place(x=50, y=190)

    def crearEntradas(self):

        self.etNombre = Entry(self, textvariable=self.nombre)  # Creacion de una entrada "Entry"
        self.etNombre.place(x=150, y=50)  # Ubicacion de la entrada
        self.etNombre.focus_set()  # Autofocus

        etApellido = Entry(self, textvariable=self.apellido)
        etApellido.place(x=150, y=80)

        etCorreo = Entry(self, textvariable=self.correo)
        etCorreo.place(x=150, y=140)

        etTelefono = Entry(self, textvariable=self.telefono)
        etTelefono.place(x=150, y=190)

    def crearBotones(self):

        btnGuardar = Button(self, text='Guardar', command=lambda: self.crearContacto(1))  # Creacion de un boton
        btnGuardar.place(x=330, y=190)  # Ubicacion del boton

        btnModificar = Button(self, text='Modificar', command=lambda: self.crearContacto(2))
        btnModificar.place(x=410, y=190)

        btnEliminar = Button(self, text='Eliminar', command=self.eliminarContacto)
        btnEliminar.place(x=500, y=190)

        btnLimpiar = Button(self, text="Limpiar", command=self.limpiarVentana)
        btnLimpiar.place(x=580, y=190)

    def crearTabla(self):

        frame = Frame(self, width=120)  # Creacion de un frame
        frame.place(x=20, y=230)  # Ubicacion del frame

        columnas = ('Nombre', 'Apellido', 'Correo', 'Telefono')  # Definicion de las columnas para la tabla

        tabla = ttk.Treeview(frame, columns=columnas, show='headings', height=11)
        tabla.grid(row=0, column=0, sticky='nsew')
        tabla.heading('Nombre', text='Nombre')
        tabla.column('Nombre', width=150)
        tabla.heading('Apellido', text='Apellido')
        tabla.column('Apellido', width=150)
        tabla.heading('Correo', text='Correo')
        tabla.heading('Telefono', text='Telefono')
        tabla.column('Telefono', width=100)

        # agregar scroll
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
        tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        tabla.bind('<<TreeviewSelect>>', self.seleccionarContacto)  # evento al seleccionar un contacto en la tabla
        return tabla

    def seleccionarContacto(self, event):

        for selccion_item in self.tabla.selection():
            item = self.tabla.item(selccion_item)  # captura el contacto seleccionado
            self.contactoSeleccionado = item['values']  # asigna los valores del contacto seleccionado

    def crearContacto(self, boton):

        if boton == 1:  # Si el boton oprimido es el de guardar
            # Si todos las entradas tienen algun valor
            if self.nombre.get() and self.apellido.get() and self.correo.get() and self.telefono.get():
                if self.banModificar:  # Si la bandera del boton modificar esta activa
                    try:
                        self.modificarContacto()  # Modifica el cotacto
                        messagebox.showinfo("Modificar", "Contacto Modificado")
                    except:
                        messagebox.showerror("Modificar", "Erro al Modificar")

                    self.limpiarVentana()
                    self.contactoSeleccionado = []  # Limpia los datos de la variable contactoSeleccionado
                    self.banModificar = False  # Apaga la bandera de el boton modificar
                else:  # Si la bandera del boton modificar esta apagada

                    contacto = Contacto(self.nombre.get(), self.apellido.get(), self.telefono.get(), self.correo.get())
                    try:
                        self.ajenda.guardar(contacto)  # guarda el contacto
                        messagebox.showinfo("Guardar", "Se guardo correctamente")
                    except:
                        messagebox.showerror("Guardar", "Error al guardar")

                    self.mostrarContactos(self.ajenda.listaContactos)  # Actualiza los datos de la tabla
                    self.limpiarVentana()
                    self.contactoSeleccionado = []  # Limpia los datos de la variable contactoSeleccionado
            else:
                messagebox.showinfo("Vacio", "Algunas entradas estan vacias")

        if boton == 2:  # Si el boton modificar es oprimido
            if len(self.contactoSeleccionado) > 0:  # Si se selecciona un contacto
                # Establecer en las entradas los datos del contacto seleccionado
                self.nombre.set(self.contactoSeleccionado[0])
                self.apellido.set(self.contactoSeleccionado[1])
                self.correo.set(self.contactoSeleccionado[2])
                self.telefono.set(self.contactoSeleccionado[3])
                self.banModificar = True  # Enciende la bandera de el boton modificar
            else:
                messagebox.showerror("Eliminar", "Ningun contacto seleccionado")

    def eliminarContacto(self):

        contacto = []  # Guarda los datos del contacto seleccionado
        for dato in self.contactoSeleccionado:
            contacto.append(str(dato))  # Convierte cada uno de los datos del contacto en string

        if len(self.contactoSeleccionado) > 0:  # Si se selecciona un contacto
            try:
                self.ajenda.eliminar(contacto)  # Elimina el contacto
                messagebox.showinfo("Eliminar", "Contacto " + str(self.contactoSeleccionado[0]) + " eliminado")
            except:
                messagebox.showerror("Eliminar", "Contacto no eliminado")
        else:
            messagebox.showerror("Eliminar", "Ningun contacto seleccionado")

        self.contactoSeleccionado = []  # Limpia los datos de la variable contactoSeleccionado

        self.mostrarContactos(self.ajenda.listaContactos)  # Actualiza los datos de la tabla

    def modificarContacto(self):

        contacto = []  # Guarda los datos actuales del contacto seleccionado
        for dato in self.contactoSeleccionado:
            contacto.append(str(dato))  # Convierte cada uno de los datos del contacto en string

        # Si todas las entradas tienen un valor
        if self.nombre.get() and self.apellido.get() and self.correo.get() and self.telefono.get():
            contactoModificado = []  # Garda los datos modificados del contacto seleccionado
            contactoModificado.append(self.nombre.get())
            contactoModificado.append(self.apellido.get())
            contactoModificado.append(self.correo.get())
            contactoModificado.append(self.telefono.get())

            self.ajenda.guardar(contacto, contactoModificado)  # Modifica el contacto
            self.mostrarContactos(self.ajenda.listaContactos)  # Actualiza los datos de la tabla
        else:
            messagebox.showinfo("vacio", "algunas entradas estan vacias")

    def mostrarContactos(self, contactos):

        self.tabla.delete(*self.tabla.get_children())  # Elimina todos los datos de la tabla, menos los encabezados

        for i in range(len(contactos)):
            data = (contactos[i].split("$"))
            self.tabla.insert('', END, values=data)  # Inserta los contactos en la tabla

    def limpiarVentana(self):

        self.nombre.set("")
        self.apellido.set("")
        self.telefono.set("")
        self.correo.set("")
        self.etNombre.focus_set()
