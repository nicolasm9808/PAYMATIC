import sys

sys.path.append("..")

from MODULO_MENÚ.menu_usuario import menu_usuario
from MODULO_MENÚ.menu_entrada_salida import *
from MODULO_MENÚ.menu_nómina import *
from MODULO_DATOS.datos import *

def menu_principal():
    print("Bienvenid@ a ServiPro")
    print("")
    while True:
        print("")
        print("1- Modulo Usuarios")
        print("2- Modulo de Nómina")
        print("3- Modulo de Entradas/Salidas")
        print("4- Cerrar Programa")
        print("")

        opcion = input("Selecciona una opcion: ")
        print("")

        if opcion == "1":
            menu_usuario();
        elif opcion == "2":
            menu_nómina();
        elif opcion == "3":
            menu_entrada_salida();
        elif opcion == "4":
            print("")
            print("Programa Finalizado")
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")