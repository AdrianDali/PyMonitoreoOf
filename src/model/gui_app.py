import tkinter as tk
from tkinter import ttk
import datetime

#from tomlkit import value
from usuario import select_name_usuario_enabled
from pieza import select_name_piezas, select_id_pieza
from maquina import select_name_maquinas_enabled , select_id_maquina
from proceso import DBProceso, select_procesos_unfinish



# env\Scripts\activate
print(select_name_usuario_enabled())
lista_usuarios = select_name_usuario_enabled()
lista_piezas = select_name_piezas()
lista_maquina = select_name_maquinas_enabled()
fecha_inicio = datetime.datetime.now()
fecha  = str(fecha_inicio.strftime("%Y-%m-%d"))
fecha_completa = str(fecha_inicio.strftime("%Y-%m-%d %H:%M:%S"))
print(fecha)
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu ,width =1200, height =1200)
    menu_inicio = tk.Menu(barra_menu ,tearoff= 0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Agregar Pelicula')
    menu_inicio.add_command(label='Eliminar Registro e db')
    menu_inicio.add_command(label='Salir', command=root.destroy)
    barra_menu.add_cascade(label='Inicio',  menu=menu_inicio) 
    barra_menu.add_cascade(label='Configuracion', )
    barra_menu.add_cascade(label='Ayuda', )

def listar():
    select_procesos_unfinish()
    return select_procesos_unfinish()


class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root, width = 1500 , height = 1200)
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

        self.label_proceso = tk.Label(self, text = 'Nombre de proceso: ' , bg = '#ffffff')
        self.label_proceso.config(font=('Arial', 12, "bold"))
        self.label_proceso.grid(row = 1, column = 0, padx=10, pady=10)  

        self.label_fecha = tk.Label(self, text = 'Fecha: ' , bg = '#ffffff')
        self.label_fecha.config(font=('Arial', 12, "bold"))
        self.label_fecha.grid(row = 2, column = 0, padx=10, pady=10)     

        self.label_pieza = tk.Label(self, text = 'Pieza: ' , bg = '#ffffff')
        self.label_pieza.config(font=('Arial', 12, "bold"))
        self.label_pieza.grid(row = 3, column = 0, padx=10, pady=10)   

        self.label_maquina = tk.Label(self, text = 'Maquina: ' , bg = '#ffffff')
        self.label_maquina.config(font=('Arial', 12, "bold"))
        self.label_maquina.grid(row = 4, column = 0, padx=10, pady=10)   

        self.label_observaciones = tk.Label(self, text = 'Observaciones: ' , bg = '#ffffff')
        self.label_observaciones.config(font=('Arial', 12, "bold"))
        self.label_observaciones.grid(row = 5, column = 0, padx=10, pady=10)   





        #Entrys de cada campo 
        self.mi_nombre = tk.StringVar()
        self.combo_nombre = ttk.Combobox(self, values = lista_usuarios )
        self.combo_nombre.config(width= 50,font=('Arial', 12) )
        self.combo_nombre.grid(row = 0, column = 1, padx=10, pady=10, columnspan= 2)

        self.mi_proceso = tk.StringVar()
        self.entry_proceso = tk.Entry(self, textvariable = self.mi_proceso)
        self.entry_proceso.config(width= 50,font=('Arial', 12),background='#ffffff' )
        self.entry_proceso.grid(row = 1, column = 1, padx=10, pady=10 , columnspan= 2)

        self.mi_fecha = tk.StringVar()
        self.entry_fecha = tk.Entry(self, textvariable = self.mi_fecha )
        self.entry_fecha.config(width= 50,font=('Arial', 12) )
        self.entry_fecha.grid(row = 2, column = 1, padx=10, pady=10    , columnspan= 2)


        self.combo_pieza = ttk.Combobox(self, values = lista_piezas )
        self.combo_pieza.config(width= 50,font=('Arial', 12) )
        self.combo_pieza.grid(row = 3, column = 1, padx=10, pady=10, columnspan= 2)
        
        self.combo_maquina = ttk.Combobox(self, values = lista_maquina)
        self.combo_maquina.config(width= 50,font=('Arial', 12) )
        self.combo_maquina.grid(row = 4, column = 1, padx=10, pady=10, columnspan= 2)

        self.mi_observaciones = tk.StringVar()
        self.text_observaciones = tk.Text(self)
        self.text_observaciones.config(width= 50,height= 5 ,font=('Arial', 12) )
        self.text_observaciones.grid(row = 5, column = 1, padx=10, pady=10    , columnspan= 2)


        

        #Botones
        self.boton_nuevo = tk.Button(self, text = 'Nuevo', state = 'normal', command = self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#158645',
        cursor='hand2', activebackground= "#35bd6f")
        self.boton_nuevo.grid(row = 6, column = 0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text = 'Iniciar Proceso', state = 'normal', command = self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#1658a2',
        cursor='hand2', activebackground= "#3586df")
        self.boton_guardar.grid(row = 6, column = 1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text = 'Cancelar', state = 'normal', command = self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#bd152e',
        cursor='hand2', activebackground= "#e15370")
        self.boton_cancelar.grid(row = 6, column = 2, padx=10, pady=10)

        #Boton eliminar 
        self.boton_eliminar = tk.Button(self, text = 'Eliminar', state = 'normal', command = self.deshabilitar_campos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#bd152e',
        cursor='hand2', activebackground= "#e15370")
        self.boton_eliminar.grid(row =8, column = 1, padx=10, pady=10)

        #Botones
        self.boton_editar = tk.Button(self, text = 'Editar', state = 'normal', command = self.habilitar_campos)
        self.boton_editar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#158645',
        cursor='hand2', activebackground= "#35bd6f")
        self.boton_editar.grid(row = 8, column = 0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text = 'Terminar Proceso', state = 'normal', command = self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, "bold"), fg = '#ffffff', bg = '#1658a2',
        cursor='hand2', activebackground= "#3586df")
        self.boton_guardar.grid(row = 8, column = 2, padx=10, pady=10)

    def habilitar_campos(self):
        self.text_observaciones.config(state = 'normal')
        self.combo_nombre.config(state = 'readonly')
        self.combo_pieza.config(state = 'readonly')
        self.combo_maquina.config(state = 'readonly')
        #self.entry_duracion.config(state = 'normal')
        self.entry_fecha.config(state = 'readonly')
        self.boton_guardar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')
        self.boton_nuevo.config(state = 'disabled')
        self.mi_fecha.set(fecha)

    def deshabilitar_campos(self):
        #borrar los campos
        self.mi_fecha.set('')
        self.mi_proceso.set('')
        self.combo_nombre.set('')
        self.combo_maquina.set('')
        self.combo_pieza.set('')
        self.mi_observaciones.set('')

        #deshabilitar los campos
        self.text_observaciones.config(state = 'disabled')
        self.combo_maquina.config(state = 'disabled')
        self.combo_pieza.config(state = 'disabled')
        self.combo_nombre.config(state = 'disabled')
        #self.entry_duracion.config(state = 'disabled')
        self.entry_fecha.config(state = 'disabled')
        self.boton_guardar.config(state = 'disabled')
        self.boton_cancelar.config(state = 'disabled')
        self.boton_nuevo.config(state = 'normal')
    
    def guardar_datos(self):
        
        nombre = self.combo_nombre.get()
        print(nombre)
        pieza = self.combo_pieza.get()
        print(pieza)
        maquina = self.combo_maquina.get()
        print(maquina)
        observaciones = self.mi_observaciones.get()
        print(observaciones)
        fecha = self.mi_fecha.get()
        print(fecha)
        nombre_proceso = self.mi_proceso.get()
        print(nombre_proceso)
        id_maquina = select_id_maquina(maquina)
        id_pieza = select_id_pieza(pieza)
        DBProceso(id_maquina, id_pieza, nombre_proceso, fecha_completa,  observaciones )
        self.tabla_peliculas();
        self.deshabilitar_campos()




    def tabla_peliculas(self):
        self.lista_peliculas = listar()
        
        self.tabla = ttk.Treeview(self,
        column= ('nombre', 'proceso', 'nombre_maquina', 'nombre_pieza', 'hora_inicio','numero_piezas', 'peso_merma', 'observaciones'))
        self.tabla.grid(row = 7, column = 0, columnspan= 6)

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'NOMBRE')
        self.tabla.heading('#2', text = 'PROCESO')
        self.tabla.heading('#3', text = 'MAQUINA')
        self.tabla.heading('#4', text = 'PIEZA')
        self.tabla.heading('#5', text = 'HORA INICIO')
        self.tabla.heading('#6', text = 'NUMERO PIEZAS')
        self.tabla.heading('#7', text = 'PESO MERMA')
        self.tabla.heading('#8', text = 'OBSERVACIONES')
        #self.tabla_seleccion()
        #self.tabla.insert('',0, text = '1', values = ( 1,'Pelicula 1', '1', 'Accion'))

        #iterar lista peliculas 
        for p in self.lista_peliculas:
            self.tabla.insert('', 0, text = p[0], values = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))

    def tabla_seleccion(self):
        select_procesos_unfinish()
        print("")
        print("PSO")
        self.tabla.insert('', 0, text = '2', values = ('peli', '4', 'Accion'))
        


