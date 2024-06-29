import sys

sys.path.append("..")

from MODULO_MENÚ.menu_principal import *

def menu_usuario():
    print("Módulo Usuarios")
    print("")
    while True:
        print("")
        print("1- Agregar usuario")
        print("2- Modificar usuario")
        print("3- Eliminar usuario")
        print("4- Listar usuarios")
        print("5- Cerrar Programa")
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
            menu_entrada_salida();
        elif opcion == "5":
            print("")
            print("Regreseando...")
            menu_principal();
            break
        else:
            print("")
            print("Opción Incorrecta")
            print("")