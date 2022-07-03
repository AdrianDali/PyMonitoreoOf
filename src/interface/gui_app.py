import tkinter as tk
from tkinter import ttk
# env\Scripts\activate

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu ,width =300, height =300)
    menu_inicio = tk.Menu(barra_menu ,tearoff= 0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Agregar Pelicula')
    menu_inicio.add_command(label='Eliminar Registro e db')
    menu_inicio.add_command(label='Salir', command=root.destroy)
    barra_menu.add_cascade(label='Inicio',  menu=menu_inicio) 
    barra_menu.add_cascade(label='Configuracion', )
    barra_menu.add_cascade(label='Ayuda', )

def listar():
    lista_peliculas = [{1,'pelio',1, 'accion'}]
    return lista_peliculas


class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root, width = 600 , height = 400)
        self.root = root 
        self.pack()
        self.config( bg = '#ffffff')
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()

    def campos_pelicula(self):
        #labels de cada campo
        self.label_nombre = tk.Label(self, text = 'Nombre de  operador: ' , bg = '#ffffff')
        self.label_nombre.config(font=('Arial', 12, "bold"))
        self.label_nombre.grid(row = 0, column = 0,padx=10, pady=10)

        self.label_duracion = tk.Label(self, text = 'Nombre de proceso: ' , bg = '#ffffff')
        self.label_duracion.config(font=('Arial', 12, "bold"))
        self.label_duracion.grid(row = 1, column = 0, padx=10, pady=10)  

        self.label_genero = tk.Label(self, text = 'Fecha: ' , bg = '#ffffff')
        self.label_genero.config(font=('Arial', 12, "bold"))
        self.label_genero.grid(row = 2, column = 0, padx=10, pady=10)     
        

        #Entrys de cada campo 
        #self.mi_nombre = tk.StringVar()
        #self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        #self.entry_nombre.config(width= 50,font=('Arial', 12) )
        #self.entry_nombre.grid(row = 0, column = 1, padx=10, pady=10, columnspan= 2)
        self.combo_nombre = ttk.Combobox(self, values = ('Pelicula 1', 'Pelicula 2', 'Pelicula 3'))
        self.combo_nombre.config(width= 50,font=('Arial', 12) )
        self.combo_nombre.grid(row = 0, column = 1, padx=10, pady=10, columnspan= 2)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable = self.mi_duracion)
        self.entry_duracion.config(width= 50,font=('Arial', 12) )
        self.entry_duracion.grid(row = 1, column = 1, padx=10, pady=10 , columnspan= 2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable = self.mi_genero)
        self.entry_genero.config(width= 50,font=('Arial', 12) )
        self.entry_genero.grid(row = 2, column = 1, padx=10, pady=10    , columnspan= 2)

        #Botones
        self.boton_nuevo = tk.Button(self, text = 'Nuevo', state = 'normal', command = self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, "bold"), fg = '#dad5d6', bg = '#158645',
        cursor='hand2', activebackground= "#35bd6f")
        self.boton_nuevo.grid(row = 3, column = 0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text = 'Guardar', state = 'normal', command = self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, "bold"), fg = '#dad5d6', bg = '#1658a2',
        cursor='hand2', activebackground= "#3586df")
        self.boton_guardar.grid(row = 3, column = 1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text = 'Cancelar', state = 'normal', command = self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, "bold"), fg = '#dad5d6', bg = '#bd152e',
        cursor='hand2', activebackground= "#e15370")
        self.boton_cancelar.grid(row = 3, column = 2, padx=10, pady=10)

        #Boton eliminar 
        self.boton_eliminar = tk.Button(self, text = 'Eliminar', state = 'normal', command = self.deshabilitar_campos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, "bold"), fg = '#dad5d6', bg = '#bd152e',
        cursor='hand2', activebackground= "#e15370")
        self.boton_eliminar.grid(row = 5, column = 1, padx=10, pady=10)

        #Botones
        self.boton_editar = tk.Button(self, text = 'Editar', state = 'normal', command = self.habilitar_campos)
        self.boton_editar.config(width=20, font=('Arial', 12, "bold"), fg = '#dad5d6', bg = '#158645',
        cursor='hand2', activebackground= "#35bd6f")
        self.boton_editar.grid(row = 5, column = 0, padx=10, pady=10)

    def habilitar_campos(self):
        #self.entry_nombre.config(state = 'normal')
        self.entry_duracion.config(state = 'normal')
        self.entry_genero.config(state = 'normal')
        self.boton_guardar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')
        self.boton_nuevo.config(state = 'disabled')

    def deshabilitar_campos(self):
        #borrar los campos
        #self.mi_nombre.set('')
        self.mi_genero.set('')
        self.mi_duracion.set('')
        #deshabilitar los campos
        #self.entry_nombre.config(state = 'disabled')
        self.entry_duracion.config(state = 'disabled')
        self.entry_genero.config(state = 'disabled')
        self.boton_guardar.config(state = 'disabled')
        self.boton_cancelar.config(state = 'disabled')
        self.boton_nuevo.config(state = 'normal')
    
    def guardar_datos(self):
        self.deshabilitar_campos()

    def tabla_peliculas(self):
        self.lista_peliculas = listar()
        self.tablar = ttk.Treeview(self,
        column= ('nombre', 'duracion', 'genero'))
        self.tablar.grid(row = 4, column = 0, columnspan= 4)

        self.tablar.heading('#0', text = 'ID')
        self.tablar.heading('#1', text = 'NOMBRE')
        self.tablar.heading('#2', text = 'DURACION')
        self.tablar.heading('#3', text = 'GENERO')
        self.tablar.insert('',0, text = '1', values = ( 'Pelicula 1', '1', 'Accion'))

        #iterar lista peliculas 
        for p in range(4):
            self.tablar.insert('', 0, text = '2', values = ('peli', '4', 'Accion'))
