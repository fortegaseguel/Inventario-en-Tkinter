import tkinter as tk
from tkinter import ttk, messagebox
from models.model import crear_tabla, borrar_tabla, guardar, listar, editar, eliminar
from models.model import Table



# BARRA DE MENUS
def barra_menu(root):
# Barra de Menu
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=600, height=300)

# Menu Inicio
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label='Crear registro en DB', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

# Menu Consultas
    menu_consultas= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
    menu_consultas.add_command(label='1')
    menu_consultas.add_command(label='2')
    menu_consultas.add_command(label='3')

# Menu Configuracion
    menu_configuracion= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuracion', menu=menu_configuracion)
    menu_configuracion.add_command(label='1')
    menu_configuracion.add_command(label='2')
    menu_configuracion.add_command(label='3')

# Menu Ayuda
    menu_ayuda= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)
    menu_ayuda.add_command(label='1')
    menu_ayuda.add_command(label='2')
    menu_ayuda.add_command(label='3')



# FRAMES
class Frame1(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id = None

        self.labels()
        self.deshabilitar_campos()
        self.tabla_data()

# Etiquetas 
    def labels(self):
    # Label 1
        self.label_1 = tk.Label(self, text='Nombre: ')
        self.label_1.config(font=('Arial', 10, 'bold'))
        self.label_1.grid(row=0, column=0, padx=5, pady=5)

    # Label 2
        self.label_2 = tk.Label(self, text='Cantidad: ')
        self.label_2.config(font=('Arial', 10, 'bold'))
        self.label_2.grid(row=1, column=0, padx=5, pady=5)

    # Label 3
        self.label_3 = tk.Label(self, text='Categoria: ')
        self.label_3.config(font=('Arial', 10, 'bold'))
        self.label_3.grid(row=2, column=0, padx=5, pady=5)


# Entradas de Texto / Entrys

    # Entry 1
        self.campo_nombre = tk.StringVar() #Asigna una variable al campo

        self.entry_1 = tk.Entry(self, textvariable=self.campo_nombre)
        self.entry_1.config(
            width=50, 
        )
        self.entry_1.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

    # Entry 2
        self.campo_cantidad = tk.StringVar() #Asigna una variable al campo

        self.entry_2 = tk.Entry(self, textvariable=self.campo_cantidad)
        self.entry_2.config(
            width=50, 
        )
        self.entry_2.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

    # Entry 3
        self.campo_categoria = tk.StringVar() #Asigna una variable al campo

        self.entry_3 = tk.Entry(self, textvariable=self.campo_categoria)
        self.entry_3.config(
            width=50,
        )
        self.entry_3.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

# BOTONES

    #Boton 1
        self.boton_1 = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.boton_1.config(
            width=20,
            font=('Arial', 10, 'bold'),
            bg='#0000ff',
            fg='#dad5d6',
            cursor='hand2',
            activebackground='#35bd6f'
        )
        self.boton_1.grid(row=3, column=0, padx=5, pady=5)

    #Boton 2
        self.boton_2 = tk.Button(self, text='Guardar', command=self.guardar_data)
        self.boton_2.config(
            width=20,
            font=('Arial', 10, 'bold'),
            bg='#0000ff',
            fg='#dad5d6',
            cursor='hand2',
            activebackground='#35bd6f'
        )
        self.boton_2.grid(row=3, column=1, padx=5, pady=5)

    #Boton 3
        self.boton_3 = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_3.config(
            width=20,
            font=('Arial', 10, 'bold'),
            bg='#0000ff',
            fg='#dad5d6',
            cursor='hand2',
            activebackground='#35bd6f'
        )
        self.boton_3.grid(row=3, column=2, padx=5, pady=5)


# ACCIONES
    def habilitar_campos(self):
    # DESBLOQUEAR CAMPOS PARA INGRESAR DATOS

        self.campo_nombre.set('') #Limpia el campo 1 al ejecutar la funcion
        self.campo_cantidad.set('') #Limpia el campo 2 al ejecutar la funcion
        self.campo_categoria.set('') #Limpia el campo 3 al ejecutar la funcion
        self.entry_1.config(state='normal')
        self.entry_2.config(state='normal')
        self.entry_3.config(state='normal')

        self.boton_2.config(state='normal')
        self.boton_3.config(state='normal')


    def deshabilitar_campos(self):
    # BLOQUEAR CAMPOS PARA INGRESAR DATOS
        self.id == None
        self.campo_nombre.set('') #Limpia el campo 1 al ejecutar la funcion
        self.campo_cantidad.set('') #Limpia el campo 2 al ejecutar la funcion
        self.campo_categoria.set('') #Limpia el campo 3 al ejecutar la funcion

        self.entry_1.config(state='disabled')
        self.entry_2.config(state='disabled')
        self.entry_3.config(state='disabled')

        self.boton_2.config(state='disabled')
        self.boton_3.config(state='disabled')


    def guardar_data(self):
    # GUARDAR EN LA BASE DE DATOS
        registro = Table(
            self.campo_nombre.get(),
            self.campo_cantidad.get(),
            self.campo_categoria.get(),
        )
        if self.id == None:
            guardar(registro)
        else:
            editar(registro, self.id)
            self.deshabilitar_campos()


        self.deshabilitar_campos()
        self.tabla_data()


# TABLAS DE LA BASE DE DATOS
    def tabla_data(self):
    # Recupera los datos de la BD
        self.lista = listar()
        self.lista.reverse()

    #Crea el espacio de visualizacion de los datos de la BD
        self.tabla_1 = ttk.Treeview(self, 
        column=('nombre', 'duracion', 'genero'))
        self.tabla_1.grid(row=4, column=0, columnspan=4, sticky='NSE')

    #Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tabla_1.yview)
        self.scrollbar.grid(row=4, column=4, sticky='NSE')
        self.tabla_1.config(yscrollcommand= self.scrollbar.set)

    #Encabezados
        self.tabla_1.heading('#0', text='ID')
        self.tabla_1.heading('#1', text='NOMBRE')
        self.tabla_1.heading('#2', text='CANTIDAD')
        self.tabla_1.heading('#3', text='CATEGORIA')

    #Visualizando toda la lista de la base de datos
        for item in self.lista:
            self.tabla_1.insert('', 0, text=item[0],
                values=(item[1], item[2], item[3]))


# Botones para manipular registros
    #Boton Editar registros
        self.boton_4 = tk.Button(self, text='Editar', command=self.editar_data)
        self.boton_4.config(
            width=20,
            font=('Arial', 10, 'bold'),
            bg='#0000ff',
            fg='#dad5d6',
            cursor='hand2',
            activebackground='#35bd6f'
        )
        self.boton_4.grid(row=5, column=0, padx=5, pady=5)

    #Boton Eliminar registros
        self.boton_5 = tk.Button(self, text='Eliminar', command=self.eliminar_data)
        self.boton_5.config(
            width=20,
            font=('Arial', 10, 'bold'),
            bg='#0000ff',
            fg='#dad5d6',
            cursor='hand2',
            activebackground='#35bd6f'
        )
        self.boton_5.grid(row=5, column=3, padx=5, pady=5)


# EDITAR DATOS DESDE LA APLICACION
    def editar_data(self):
        try:
        #Recupera el item de los datos de la seleccion y los guarda en variable
            self.id = self.tabla_1.item(self.tabla_1.selection())['text']
            self.nombre = self.tabla_1.item(self.tabla_1.selection())['values'][0]
            self.cantidad = self.tabla_1.item(self.tabla_1.selection())['values'][1]
            self.categoria = self.tabla_1.item(self.tabla_1.selection())['values'][2]

        # Desbloquea los campos
            self.habilitar_campos()

        # Inserta el valor de las variables en su respectivo campo
            self.entry_1.insert(0, self.nombre)
            self.entry_2.insert(0, self.cantidad)
            self.entry_3.insert(0, self.categoria)



        except:
        #Mensaje de error
            titulo = 'Edicion de Registros'
            msg = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, msg)


# ELIMINAR REGISTROS 
    def eliminar_data(self):
        try:
            self.id = self.tabla_1.item(self.tabla_1.selection())['text']
            eliminar(self.id)

            self.tabla_data()
            self.id = None

        except:
        #Mensaje de error
            titulo = 'Eliminar un Registro'
            msg = 'No ha seleccionado podido eliminar el registro'
            messagebox.showerror(titulo, msg)

######################################################################

##### FRAME 2 ###############

class Frame2(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.id = None

        self.labels()
        #self.deshabilitar_campos()
        self.tabla_data()

# Etiquetas 
    def labels(self):
    # Label 1
        self.label_1 = tk.Label(self, text='Nombre: ')
        self.label_1.config(font=('Arial', 10, 'bold'))
        self.label_1.grid(row=0, column=0, padx=5, pady=5)


# TABLAS DE LA BASE DE DATOS
    def tabla_data(self):
    # Recupera los datos de la BD
        self.lista = listar()
        self.lista.reverse()

    #Crea el espacio de visualizacion de los datos de la BD
        self.tabla_1 = ttk.Treeview(self, 
        column=('', 'duracion', 'genero'))
        self.tabla_1.grid(row=1, column=0, columnspan=1, rowspan=3, sticky='N')

    #Crea el espacio de visualizacion de los datos seleccionados de la BD
        self.tabla_2 = ttk.Treeview(self, 
        column=('', 'duracion', 'genero'))
        self.tabla_2.grid(row=1, column=1, columnspan=1, rowspan=3, sticky='S')

    #Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tabla_1.yview)
        self.scrollbar.grid(row=1, column=1, sticky='NSE')
        self.tabla_1.config(yscrollcommand= self.scrollbar.set)

    #Scrollbar 2
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tabla_2.yview)
        self.scrollbar.grid(row=4, column=2, sticky='NSE')
        self.tabla_2.config(yscrollcommand= self.scrollbar.set)


    #Encabezados
        self.tabla_1.heading('#0', text='ID')
        self.tabla_1.heading('#1', text='NOMBRE')
        self.tabla_1.heading('#2', text='CANTIDAD')
        self.tabla_1.heading('#3', text='CATEGORIA')

    #Encabezados 2
        self.tabla_2.heading('#0', text='ID')
        self.tabla_2.heading('#1', text='NOMBRE')
        self.tabla_2.heading('#2', text='CANTIDAD')
        self.tabla_2.heading('#3', text='CATEGORIA')

    #Visualizando toda la lista de la base de datos
        for item in self.lista:
            self.tabla_1.insert('', 0, text=item[0],
                values=(item[1], item[2], item[3]))


# Botones para manipular registros
    #Boton Editar registros
        self.boton_4 = tk.Button(self, text='Editar')
        self.boton_4.config(
            width=20,
            font=('Arial', 10, 'bold'),
            bg='#0000ff',
            fg='#dad5d6',
            cursor='hand2',
            activebackground='#35bd6f'
        )
        self.boton_4.grid(row=5, column=0, padx=5, pady=5)

    #Boton Eliminar registros
        self.boton_5 = tk.Button(self, text='Eliminar')
        self.boton_5.config(
            width=20,
            font=('Arial', 10, 'bold'),
            bg='#0000ff',
            fg='#dad5d6',
            cursor='hand2',
            activebackground='#35bd6f'
        )
        self.boton_5.grid(row=5, column=1, padx=5, pady=5)