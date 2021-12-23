import tkinter as tk
from client.views import Frame1, Frame2, barra_menu


def main():

    # Ventana base
    root = tk.Tk()
    root.state('zoomed')
    root.title('Mi Negocio')
    root.iconbitmap('img\icon.ico')
    #root.resizable(0,0)


    # Estructura de la ventana
    barra_menu(root)
    app = Frame1(root = root)
    #⌂app = Frame2(root = root)





    app.mainloop()

if __name__ == '__main__':
    main()












'''
PARA CREAR EJECUTABLE CON PYINSTALLER

- pip install pyinstaller

- en terminal : pyi-makespec main.py --windowed


a = Analysis(['main.py'],
             pathex=['E:\\Proyectos Programacion\\Proyecto Negocio\\Negocio'],
             binaries=[],

             AQUI SE AGREGAN LAS CARPETAS DE ARCHIVOS ESTATICOS QUE REQUIERE LA APP
             //DATAS=[(./ORIGEN/*.EXTENSION, CARPETA DE LA APP)]//
             datas=[('./img/*.*', 'img'), ('./database/*.*', 'database')],

             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyinstaller archivo.spec

'''